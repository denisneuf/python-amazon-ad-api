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

log = logging.getLogger(__name__)
role_cache = TTLCache(maxsize=10, ttl=3600)

class Client(BaseClient):
    grantless_scope = ''
    def __init__(
            self,
            marketplace: Marketplaces = Marketplaces.ES,
            *,
            refresh_token=None,
            account='default',
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

    def _request(self, path: str, *, data: str = None, params: dict = None, headers=None,
                 add_marketplace=True) -> ApiResponse:
        if params is None:
            params = {}
        if data is None:
            data = {}

        method = params.pop('method')

        if method in ('POST', 'PUT', 'PATCH'):

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
            print(content)
            exception = get_exception_for_content(data)
            raise exception(data)

        if vars(res).get('_content') == b'[]' and vars(res).get('_content_consumed') is True:
            data = json.loads('{"status_code": 200, "msg": "No Data Available"}')

        headers = vars(res).get('headers')
        status_code = vars(res).get('status_code')
        next_token = vars(res).get('_next')
        return ApiResponse(data, next_token, headers=headers)
