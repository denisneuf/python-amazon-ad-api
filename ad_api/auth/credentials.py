import os

class Credentials:
    def __init__(self, refresh_token, credentials):
        self.client_id = credentials.client_id
        self.client_secret = credentials.client_secret
        self.refresh_token = refresh_token or credentials.refresh_token
        self.profile_id = credentials.profile_id
