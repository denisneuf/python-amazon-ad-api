import json
from json import JSONDecodeError
import logging
from requests import request
from ad_api.auth import AccessTokenClient, AccessTokenResponse
from .api_response import ApiResponse
from ad_api.shared.base_client import BaseClient
from .exceptions import (get_exception_for_code, get_exception_for_content,
                         MissingEndpointHeader, AmbiguousEndpointHeader)
from .marketplaces import Marketplaces
import os
import requests
from io import BytesIO
import gzip
from zipfile import ZipFile
import zipfile
from urllib.parse import urlparse, quote
from ad_api.base.credential_provider import CredentialProvider
import ad_api.version as vd
from typing import Any, Dict, Optional

log = logging.getLogger(__name__)
# The three headers that name which account a call is about. A route may only
# send one of them; which one it sends is decided per route and, when a route
# accepts more than one, per call.
_IDENTITY_HEADERS = (
    'Amazon-Advertising-API-Scope',
    'Amazon-Ads-AccountId',
    'Amazon-Advertising-API-Manager-Account',
)

# selector= value -> header it sends. The keys are the same keys credentials.yml
# takes, so a caller writes the name it already knows.
_SELECTOR_HEADERS = {
    'profile_id': 'Amazon-Advertising-API-Scope',
    'account_id': 'Amazon-Ads-AccountId',
    'manager_account_id': 'Amazon-Advertising-API-Manager-Account',
}

_DEFAULT_MARKETPLACE = Marketplaces[os.environ['AD_API_DEFAULT_MARKETPLACE']] if 'AD_API_DEFAULT_MARKETPLACE' in os.environ else Marketplaces.EU


class Client(BaseClient):
    def __init__(
        self,
        account: str = 'default',
        marketplace: Marketplaces = _DEFAULT_MARKETPLACE,
        credentials: Optional[Dict[str, str]] = None,
        proxies: Optional[Dict[str, str]] = None,
        verify: bool = True,
        timeout: Optional[int] = None,
        debug: bool = False,
        access_token: Optional[str] = None,
        verify_additional_credentials: bool = True,
    ):
        _provider = CredentialProvider(account, credentials, verify_additional_credentials)
        self.credentials = _provider.credentials
        self.account_name = getattr(_provider, 'account', account)
        self.credentials_source = getattr(_provider, 'source', 'yml')
        self._auth = AccessTokenClient(
            credentials=self.credentials,
            proxies=proxies,
            verify=verify,
            timeout=timeout,
        )
        self._access_token = access_token
        self.endpoint = marketplace.endpoint
        self.debug = debug
        self.timeout = timeout
        self.proxies = proxies
        self.verify = verify

        version = vd.__version__
        self.user_agent += f'-{version}'

    @property
    def headers(self) -> Dict[str, str]:
        data = {
            'User-Agent': self.user_agent,
            'Amazon-Advertising-API-ClientId': self.credentials['client_id'],
            'Authorization': 'Bearer %s' % self.auth.access_token,
            'Content-Type': 'application/json',
        }
        if profile_id := self.credentials.get('profile_id'):
            data['Amazon-Advertising-API-Scope'] = profile_id

        if account_id := self.credentials.get('account_id'):
            data['Amazon-Ads-AccountId'] = account_id

        if manager_account_id := self.credentials.get('manager_account_id'):
            data['Amazon-Advertising-API-Manager-Account'] = manager_account_id
        return data

    @property
    def auth(self) -> AccessTokenResponse:
        return self._auth.get_auth() if self._access_token is None else AccessTokenResponse(access_token=self._access_token)

    @staticmethod
    def _download(self: Any, params: Optional[dict] = None, headers: Optional[dict] = None) -> ApiResponse:
        location = params.get("url")

        try:
            r = requests.get(
                location,
                headers=headers or self.headers,
                data=None,
                allow_redirects=True,
                timeout=self.timeout,
                proxies=self.proxies,
                verify=self.verify,
            )

        except requests.exceptions.InvalidSchema as e:
            error = {'success': False, 'code': 400, 'response': e}
            next_token = None
            return ApiResponse(error, next_token, headers=self.headers)
        except requests.exceptions.ConnectionError as e:
            error = {'success': False, 'code': 503, 'response': e}
            next_token = None
            return ApiResponse(error, next_token, headers=self.headers)
        except requests.exceptions.RequestException as e:
            error = {'success': False, 'code': 503, 'response': e}
            next_token = None
            return ApiResponse(error, next_token, headers=self.headers)

        bytes = r.content
        mode = params.get("format")

        if mode is None:
            mode = "url"

        name = params.get("file")

        if name is None:
            o = urlparse(r.url)
            file_name = o.path[1 : o.path.find('.')]
            name = file_name.replace("/", "-")

        if mode == "raw":
            next_token = None
            return ApiResponse(bytes, next_token, headers=r.headers)

        elif mode == "url":
            next_token = None
            return ApiResponse(r.url, next_token, headers=r.headers)

        elif mode == "data":
            if bytes[0:2] == b'\x1f\x8b':
                log.info("Is gzip report")
                buf = BytesIO(bytes)
                f = gzip.GzipFile(fileobj=buf)
                read_data = f.read()
                next_token = None
                return ApiResponse(json.loads(read_data.decode('utf-8')), next_token, headers=r.headers)

            else:
                log.info("Is bytes snapshot")
                next_token = None
                return ApiResponse(json.loads(r.text), next_token, headers=r.headers)

        elif mode == "json":
            if bytes[0:2] == b'\x1f\x8b':
                buf = BytesIO(bytes)
                f = gzip.GzipFile(fileobj=buf)
                read_data = f.read()
                fo = open(name + ".json", 'w')
                fo.write(read_data.decode('utf-8'))
                fo.close()
                next_token = None
                return ApiResponse(name + ".json", next_token, headers=r.headers)
            else:
                fo = open(name + ".json", 'w')
                fo.write(r.text)
                fo.close()
                next_token = None
                return ApiResponse(name + ".json", next_token, headers=r.headers)

        elif mode == "csv":
            if bytes[0:2] == b'\x1f\x8b':
                buf = BytesIO(bytes)
                f = gzip.GzipFile(fileobj=buf)
                read_data = f.read()
                fo = open(name + ".csv", 'w')
                fo.write(read_data.decode('utf-8'))
                fo.close()
                next_token = None
                return ApiResponse(name + ".csv", next_token, headers=r.headers)
            else:
                fo = open(name + ".csv", 'w')
                fo.write(r.text)
                fo.close()
                next_token = None
                return ApiResponse(name + ".csv", next_token, headers=r.headers)

        elif mode == "gzip":
            fo = gzip.open(name + ".json.gz", 'wb').write(r.content)
            next_token = None
            return ApiResponse(name + ".json.gz", next_token, headers=r.headers)

        elif mode == "zip":
            if bytes[0:2] == b'\x1f\x8b':
                buf = BytesIO(bytes)
                f = gzip.GzipFile(fileobj=buf)
                read_data = f.read()
                fo = open(name + ".json", 'w')
                fo.write(read_data.decode('utf-8'))
                fo.close()

                zipObj = ZipFile(name + '.zip', 'w', zipfile.ZIP_DEFLATED)
                zipObj.write(name + ".json")
                zipObj.close()
            else:
                fo = open(name + ".json", 'w')
                fo.write(r.text)
                fo.close()

                zipObj = ZipFile(name + '.zip', 'w', zipfile.ZIP_DEFLATED)
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
                'response': 'The mode "%s" is not supported perhaps you could use "data", "raw", "url", "json", "zip" or "gzip"' % (mode),
            }
            next_token = None
            return ApiResponse(error, next_token, headers=self.headers)

        raise NotImplementedError("Unknown mode")

    def _request(
        self,
        path: str,
        data: Optional[str] = None,
        params: Optional[dict] = None,
        headers: Optional[dict] = None,
    ) -> ApiResponse:
        if params is None:
            params = {}

        method = params.pop('method')
        endpoint_headers = params.pop('endpoint_headers', None)
        selector = params.pop('selector', None)

        if headers is False:
            base_header = self.headers.copy()
            base_header.pop("Content-Type")
            headers = base_header

        elif headers is not None:
            base_header = self.headers.copy()
            base_header.update(headers)
            headers = base_header

        elif endpoint_headers is not None:
            # headers is None: self.headers is used at request time. Copy it so
            # the filter below has something to mutate.
            headers = self.headers.copy()

        # A method that passed its own headers often carries only Accept and
        # Content-Type. Rebuild the layer from the base so the filter sees what
        # the property would have produced. With headers=None the old helper
        # deleted the identity header earlier in _request itself, which is why
        # this has to happen before the branches above.
        if endpoint_headers is not None:
            headers = dict(headers or {})
            for h in _IDENTITY_HEADERS:
                headers.pop(h, None)
            for h, v in self.headers.items():
                if h in _IDENTITY_HEADERS:
                    headers[h] = v

        # Build the identity picture from self.headers, independently of the
        # per-method headers dict (which often carries only Accept/Content-Type).
        identity = {h: v for h, v in self.headers.items() if h in _IDENTITY_HEADERS}

        # A route that declares headers sends only those, and fails loudly when
        # none of them can be supplied: an identity header left out silently
        # turns into a 401 or 400 from the service that names nothing useful.
        if endpoint_headers is not None:
            if endpoint_headers:
                present = [h for h in endpoint_headers if h in identity]
                if not present:
                    raise MissingEndpointHeader(
                        path, method, endpoint_headers,
                        getattr(self, 'account_name', 'default'),
                        list(identity.keys()),
                        getattr(self, 'credentials_source', 'yml'),
                    )
                if selector is not None:
                    chosen = _SELECTOR_HEADERS.get(selector)
                    if chosen is None:
                        raise ValueError(
                            f"unknown selector {selector!r}; valid values are "
                            + ', '.join(repr(k) for k in _SELECTOR_HEADERS)
                        )
                    if chosen in identity and chosen not in endpoint_headers:
                        raise MissingEndpointHeader(
                            path, method, endpoint_headers,
                            getattr(self, 'account_name', 'default'),
                            list(identity.keys()),
                            getattr(self, 'credentials_source', 'yml'),
                            reason='not-accepted',
                        )
                    if chosen not in present:
                        raise MissingEndpointHeader(
                            path, method, [chosen],
                            getattr(self, 'account_name', 'default'),
                            list(identity.keys()),
                            getattr(self, 'credentials_source', 'yml'),
                        )
                    keep = {chosen}
                elif len(present) > 1:
                    raise AmbiguousEndpointHeader(
                        path, method, present,
                        getattr(self, 'account_name', 'default'),
                        getattr(self, 'credentials_source', 'yml'),
                    )
                else:
                    keep = set(present)
            else:
                keep = set()
            # Apply the selection both to the base headers and to the dict
            # the method supplied: the identity header must not survive in
            # either place if this route did not declare it.
            headers = headers or {}
            for h in _IDENTITY_HEADERS:
                headers.pop(h, None)
                if h in keep and h in identity:
                    headers[h] = identity[h]

        request_data = data if method in ('POST', 'PUT', 'PATCH') else None
        res = request(
            method,
            self.endpoint + path,
            params=params,
            data=request_data,
            headers=headers or self.headers,
            timeout=self.timeout,
            proxies=self.proxies,
            verify=self.verify,
        )

        if self.debug:
            log.info(headers or self.headers)

            if params:
                str_query = ""
                for key, value in params.items():
                    str_query += key + "=" + quote(str(value))
                message = method + " " + self.endpoint + path + "?" + str_query
            else:
                message = method + " " + self.endpoint + path

            log.info(message)
            if data is not None:
                log.info(data)

            log.info(vars(res))

        return self._check_response(res)

    @staticmethod
    def _check_response(res: requests.Response) -> ApiResponse:
        headers = vars(res).get('headers')
        status_code = vars(res).get('status_code')

        if 200 <= res.status_code < 300:
            try:
                js = res.json() or {}
            except JSONDecodeError:
                js = {}

            try:
                error = js.get('error', None)  # Dict.get(key, default=None)
            except AttributeError:
                error = None

            if error:
                exception = get_exception_for_content(error[0].get('code'))
                raise exception(error[0].get('code'), error[0], headers)

            next_token = vars(res).get('_next')

            return ApiResponse(js, next_token, headers=headers)

        else:
            exception = get_exception_for_code(res.status_code)

            try:
                js = res.json()
            except JSONDecodeError:
                js = res.content

            raise exception(status_code, js, headers)
