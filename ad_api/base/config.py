import os
import confuse

class MissingCredentials(Exception):
    """
    Credentials are missing, see the error output to find possible causes
    """
    pass


class CredentialProvider:
    credentials = None

    def __init__(self, account='default', credentials=None):
        self.account = account
        self.from_secrets()
        if credentials:
            self.credentials = self.Config(**credentials)
            missing = self.credentials.check_config()
            if len(missing):
                raise MissingCredentials(f'The following configuration parameters are missing: {missing}')
        else:
            self.from_env()

    def read_config(self):
        try:
            config = confuse.Configuration('python-sp-api')
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

    class Config:
        def __init__(self,
                     refresh_token,
                     client_id,
                     client_secret
                     ):
            self.refresh_token = refresh_token
            self.client_id = client_id
            self.client_secret = client_secret

        def check_config(self):
            errors = []
            for k, v in self.__dict__.items():
                if not v and k != 'refresh_token':
                    errors.append(k)
            return errors
