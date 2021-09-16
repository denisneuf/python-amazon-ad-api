import json
import os
import requests
import hashlib
import logging
from cachetools import TTLCache
from ad_api.base import BaseClient

from .credentials import Credentials
from .access_token_response import AccessTokenResponse
from .exceptions import AuthorizationError

cache = TTLCache(maxsize=10, ttl=3600)
grantless_cache = TTLCache(maxsize=10, ttl=3600)

logger = logging.getLogger(__name__)


class AccessTokenClient(BaseClient):
    host = 'api.amazon.com'
    grant_type = 'refresh_token'
    path = '/auth/o2/token'

    def __init__(self, refresh_token=None, account='default', credentials=None):
        super().__init__(account, credentials)
        self.cred = Credentials(refresh_token, self.credentials)

    def _request(self, url, data, headers):
        response = requests.post(url, data=data, headers=headers)
        response_data = response.json()
        if response.status_code != 200:
            error_message = response_data.get('error_description')
            error_code = response_data.get('error')
            raise AuthorizationError(error_code, error_message, response.status_code)
        return response_data

    def get_auth(self) -> AccessTokenResponse:
        """
        Get's the access token
        :return:AccessTokenResponse
        """
        global cache
        cache_key = self._get_cache_key()

        try:
            access_token = cache[cache_key]
        except KeyError:
            cache_ttl = 3600
            access_token = None

            if not access_token:
                request_url = self.scheme + self.host + self.path
                access_token = self._request(request_url, self.data, self.headers)
            else:
                cache_ttl = access_token.get('expires_in')
            cache = TTLCache(maxsize=10, ttl=cache_ttl - 15)
            cache[cache_key] = access_token
        return AccessTokenResponse(**access_token)


    def authorize_auth_code(self, auth_code):
        request_url = self.scheme + self.host + self.path
        res = self._request(
            request_url,
            data=self._auth_code_request_body(auth_code),
            headers=self.headers
        )
        return res

    def _auth_code_request_body(self, auth_code):
        return {
            'grant_type': 'authorization_code',
            'code': auth_code,
            'client_id': self.cred.client_id,
            'client_secret': self.cred.client_secret
        }

    @property
    def data(self):
        return {
            'grant_type': self.grant_type,
            'client_id': self.cred.client_id,
            'refresh_token': self.cred.refresh_token,
            'client_secret': self.cred.client_secret
        }

    @property
    def headers(self):
        return {
            'User-Agent': self.user_agent,
            'content-type': self.content_type
        }

    def _get_cache_key(self, token_flavor=''):
        return 'access_token_' + hashlib.md5(
            (token_flavor + self.cred.refresh_token).encode('utf-8')
        ).hexdigest()
