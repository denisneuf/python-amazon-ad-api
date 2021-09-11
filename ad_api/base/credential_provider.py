import json
import os
import confuse
from cachetools import Cache
import sys

class MissingCredentials(Exception):
    """
    Credentials are missing, see the error output to find possible causes
    """
    pass


class CredentialProvider:
    credentials = None
    cache = Cache(maxsize=10)

    def __init__(self, account='default', credentials=None):
        self.account = account
        self.read_credentials = [
            self.read_config
        ]
        if credentials:
            self.credentials = self.Config(**credentials)
            missing = self.credentials.check_config()
            if len(missing):
                raise MissingCredentials(f'The following configuration parameters are missing: {missing}')
        else:
            self.load_credentials()

    def load_credentials(self):
        for read_method in self.read_credentials:
            if read_method():
                return True

    def read_config(self):
        try:
            config = confuse.Configuration('python-ad-api')
            config_filename = os.path.join(config.config_dir(), 'credentials.yml')
            config.set_file(config_filename)
            account_data = config[self.account].get()
            self.credentials = self.Config(**account_data)
            missing = self.credentials.check_config()
            if len(missing):
                raise MissingCredentials(f'The following configuration parameters are missing: {missing}')
        except confuse.exceptions.NotFoundError:
            raise MissingCredentials(f'The account {self.account} was not setup in your configuration file.')
        except confuse.exceptions.ConfigReadError:
            raise MissingCredentials(
                f'Neither environment variables nor a config file were found. '
                f'Please set the correct variables, or use a config file (credentials.yml). '
                f'See https://confuse.readthedocs.io/en/latest/usage.html#search-paths for search paths.'
            )
        else:
            return True

    class Config:
        def __init__(self,
                     refresh_token,
                     client_id,
                     client_secret,
                     profile_id
                     ):
            self.refresh_token = refresh_token
            self.client_id = client_id
            self.client_secret = client_secret
            self.profile_id = profile_id

        def check_config(self):
            errors = []
            for k, v in self.__dict__.items():
                if not v and k != 'refresh_token':
                    errors.append(k)
            return errors
