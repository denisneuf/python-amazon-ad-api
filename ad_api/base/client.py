import json
from datetime import datetime
import logging
from cachetools import TTLCache
from requests import request
from ad_api.auth import AccessTokenClient, AccessTokenResponse
from .api_response import ApiResponse
from .base_client import BaseClient
from .exceptions import get_exception_for_code, get_exception_for_content, AdvertisingApiBadRequestException
from .marketplaces import Marketplaces
import sys
import os
import requests
from io import BytesIO
import gzip
from zipfile import ZipFile
import zipfile

from urllib.parse import urlparse

log = logging.getLogger(__name__)
role_cache = TTLCache(maxsize=10, ttl=3600)

class Client(BaseClient):
    grantless_scope = ''
    def __init__(
            self,
            account='default',
            marketplace: Marketplaces = Marketplaces.EU,
            refresh_token=None,
            credentials=None
    ):

        super().__init__(account, credentials)
        self.endpoint = marketplace.endpoint
        self._auth = AccessTokenClient(refresh_token=refresh_token, account=account, credentials=credentials)

    @property
    def headers(self):
        return {
            'user-agent': self.user_agent,
            'Amazon-Advertising-API-ClientId': self.credentials.client_id,
            'Authorization': 'Bearer %s' % self.auth.access_token,
            'Amazon-Advertising-API-Scope': self.credentials.profile_id,
            'content-type': 'application/json'
        }

    @property
    def auth(self) -> AccessTokenResponse:
        return self._auth.get_auth()

    @staticmethod
    def _download(self, params: dict = None, headers=None) -> ApiResponse:

        location = params.get("url")

        try:
            r = requests.get(location, headers=self.headers, data=None, allow_redirects=True)

        except requests.exceptions.InvalidSchema as e:
            error = {
                'success': False,
                'code': 400,
                'response': e
            }
            next_token = None
            return ApiResponse(error, next_token, headers=self.headers)
        except requests.exceptions.RequestException as e:
            error = {
                'success': False,
                'code': 503,
                'response': e
            }
            next_token = None
            return ApiResponse(error, next_token, headers=self.headers)
        except requests.exceptions.ConnectionError as e:
            error = {
                'success': False,
                'code': e.status_code,
                'response': e
            }
            next_token = None
            return ApiResponse(error, next_token, headers=self.headers)

        bytes = r.content
        mode = params.get("format")

        if mode is None:
            mode = "url"

        name = params.get("file")

        if name is None:
            o = urlparse(r.url)
            name = o.path[1:o.path.find('.')]


        if mode == "raw":

            next_token = None
            return ApiResponse(bytes, next_token, headers=r.headers)

        elif mode == "url":

            next_token = None
            return ApiResponse(r.url, next_token, headers=r.headers)

        elif mode == "data":

            if bytes[0:2] == b'\x1f\x8b':
                logging.info("Is gzip report")
                buf = BytesIO(bytes)
                f = gzip.GzipFile(fileobj=buf)
                read_data = f.read()
                next_token = None
                return ApiResponse(json.loads(read_data.decode('utf-8')), next_token, headers=r.headers)

            else:
                logging.info("Is bytes snapshot")
                next_token = None
                return ApiResponse(json.loads(r.text), next_token, headers=r.headers)

        elif mode == "json":
            if bytes[0:2] == b'\x1f\x8b':
                buf = BytesIO(bytes)
                f = gzip.GzipFile(fileobj=buf)
                read_data = f.read()
                fo = open(name+".json", 'w')
                fo.write(read_data.decode('utf-8'))
                fo.close()
                next_token = None
                return ApiResponse(name+".json", next_token, headers=r.headers)
            else:
                fo = open(name+".json", 'w')
                fo.write(r.text)
                fo.close()
                next_token = None
                return ApiResponse(name+".json", next_token, headers=r.headers)

        elif mode == "gzip":
            fo = gzip.open(name + ".json.gz", 'wb').write(r.content)
            next_token = None
            return ApiResponse(name + ".json.gz", next_token, headers=r.headers)

        elif mode == "zip":

            if bytes[0:2] == b'\x1f\x8b':
                buf = BytesIO(bytes)
                f = gzip.GzipFile(fileobj=buf)
                read_data = f.read()
                fo = open(name+".json", 'w')
                fo.write(read_data.decode('utf-8'))
                fo.close()

                zipObj = ZipFile(name+'.zip', 'w', zipfile.ZIP_DEFLATED)
                zipObj.write(name + ".json")
                zipObj.close()
            else:
                fo = open(name + ".json", 'w')
                fo.write(r.text)
                fo.close()

                zipObj = ZipFile(name+'.zip', 'w', zipfile.ZIP_DEFLATED)
                zipObj.write(name + ".json")
                zipObj.close()

            if os.path.exists(name + ".json"):
                os.remove(name + ".json")

            next_token = None
            return ApiResponse(name + ".zip", next_token, headers=r.headers)


        else:

            error = {
                'success': False,
                'code': 400,
                'response': 'The mode "%s" is not supported perhaps you could use "data", "raw", "url", "json", "zip" or "gzip"' % (mode)
            }
            next_token = None
            return ApiResponse(error, next_token, headers=self.headers)

        sys.exit()



    def _request(self, path: str, *, data: str = None, params: dict = None, headers=None,
                 add_marketplace=True) -> ApiResponse:
        if params is None:
            params = {}
        if data is None:
            data = {}

        method = params.pop('method')

        if method in ('POST', 'PUT', 'PATCH'):

            if headers is not None:
                headers.update(self.headers)

            res = request(method,
                      self.endpoint + path,
                      params=params,
                      data=data,
                      headers=headers or self.headers)

        else:
            res = request(method,
                      self.endpoint + path,
                      params=params,
                      headers=headers or self.headers)

        return self._check_response(res)

    @staticmethod
    def _check_response(res) -> ApiResponse:

        content = vars(res).get('_content')
        str_content = content.decode('utf8')
        data = json.loads(str_content)

        if type(data) is dict and data.get('code')=='UNAUTHORIZED':
            exception = get_exception_for_content(data)
            raise exception(data)

        if vars(res).get('_content') == b'[]' and vars(res).get('_content_consumed') is True:
            data = json.loads('{"status_code": 200, "msg": "No Data Available"}')

        headers = vars(res).get('headers')
        status_code = vars(res).get('status_code')
        next_token = vars(res).get('_next')
        return ApiResponse(data, next_token, headers=headers)
