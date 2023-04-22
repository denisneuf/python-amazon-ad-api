import abc
import functools
import json
import os
import pprint

from typing import Dict, Iterable, Optional, Type

import confuse
import logging

logger = logging.getLogger(__name__)
required_credentials = [
    'refresh_token',
    'client_id',
    'client_secret',
    'profile_id'
]


class MissingCredentials(Exception):
    """
    Credentials are missing, see the error output to find possible causes
    """
    pass


class BaseCredentialProvider(abc.ABC):

    def __init__(self, credentials: dict or str, *args, **kwargs):
        self.credentials = credentials

    @abc.abstractmethod
    def load_credentials(self):
        pass


    def _get_env(self, key):
        return os.environ.get(f'{key}',
                              os.environ.get(key))

    def check_credentials(self):
        try:
            self.errors = [c for c in required_credentials if
                           c not in self.credentials.keys() or not self.credentials[c]]
        except (AttributeError, TypeError):
            raise MissingCredentials(f'Credentials are missing: {", ".join(required_credentials)}')
        if not len(self.errors):
            return self.credentials
        raise MissingCredentials(f'Credentials are missing: {", ".join(self.errors)}')



class FromEnvCredentialProvider(BaseCredentialProvider):

    def __init__(self, *args, **kwargs):
        pass

    def load_credentials(self):
        account_data = dict(
            refresh_token=self._get_env('AD_API_REFRESH_TOKEN'),
            client_id=self._get_env('AD_API_CLIENT_ID'),
            client_secret=self._get_env('AD_API_CLIENT_SECRET'),
            profile_id=self._get_env('AD_API_PROFILE_ID'),
        )
        self.credentials = account_data
        self.check_credentials()
        return self.credentials

    def _get_env(self, key):
        return os.environ.get(f'{key}',
                              os.environ.get(key))

class FromCodeCredentialProvider(BaseCredentialProvider):

    def __init__(self, credentials: dict, *args, **kwargs):
        super().__init__(credentials)

    def load_credentials(self):
        self.check_credentials()
        return self.credentials


class FromConfigFileCredentialProvider(BaseCredentialProvider):

    file = 'credentials.yml' # Will moved to default confuse config.yaml

    def __init__(self, account: str, *args, **kwargs):
        self.account = account

    def load_credentials(self):
        try:
            config = confuse.Configuration('python-ad-api')
            config_filename = os.path.join(config.config_dir(), self.file)
            config.set_file(config_filename)
            account_data = config[self.account].get()
            super().__init__(account_data)
            self.check_credentials()
            return (account_data)


        except confuse.exceptions.NotFoundError:
            raise MissingCredentials(f'The account {self.account} was not setup in your configuration file.')
        except confuse.exceptions.ConfigReadError:
            raise MissingCredentials(
                f'Neither environment variables nor a config file were found. '
                f'Please set the correct variables, or use a config file (credentials.yml). '
                f'See https://confuse.readthedocs.io/en/latest/usage.html#search-paths for search paths.'
            )


class CredentialProvider():

    def load_credentials(self):
        pass

    def _get_env(self, key):
        return os.environ.get(f'{key}',
                              os.environ.get(key))

    def __init__(
        self,
        account: str = 'default',
        credentials: Optional[Dict[str, str]] = None,
    ):

        client_id_env = self._get_env('AD_API_CLIENT_ID'),
        client_secret_env = self._get_env('AD_API_CLIENT_SECRET')

        if client_id_env is not None and client_secret_env is not None:

            try:
                self.credentials = FromEnvCredentialProvider().load_credentials()
            except MissingCredentials:
                logging.error("MissingCredentials")
                logging.error(MissingCredentials)

        elif isinstance(credentials, dict):
            try:
                self.credentials = FromCodeCredentialProvider(credentials).load_credentials()

            except MissingCredentials:
                logging.error("MissingCredentials")
                logging.error(MissingCredentials)

        else:

            try:
                self.credentials = FromConfigFileCredentialProvider(account).load_credentials()

            except MissingCredentials:
                logging.error("MissingCredentials")
                logging.error(MissingCredentials)

    class Config:
        def __init__(self, **kwargs):
            self.refresh_token = kwargs.get('refresh_token')
            self.client_id = kwargs.get('client_id')
            self.client_secret = kwargs.get('client_secret')
            self.profile_id = kwargs.get('profile_id')