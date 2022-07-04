class BaseCredentials:
    def __init__(self, credentials):
        self.client_id = credentials.client_id
        self.client_secret = credentials.client_secret
        self.refresh_token = credentials.refresh_token


class Credentials(BaseCredentials):
    def __init__(self, credentials):
        super().__init__(credentials)
        self.profile_id = credentials.profile_id
