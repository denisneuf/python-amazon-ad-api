from ad_api.base.credential_provider import CredentialProvider

class BaseClient:
    scheme = 'https://'
    method = 'GET'
    content_type = 'application/x-www-form-urlencoded;charset=UTF-8'
    user_agent = 'python-ad-api'

    def __init__(self, account='default', credentials=None):
        try:
            import pkg_resources
            version = pkg_resources.require("python-amazon-ad-api")[0].version
            self.user_agent += f'-{version}'
        except:
            pass
        self.credentials = CredentialProvider(account, credentials).credentials
