class Credentials:
    def __init__(self, credentials):
        self.client_id = credentials['client_id']
        self.client_secret = credentials['client_secret']
        self.refresh_token = credentials['refresh_token']
        # Identifiers: not read here, AccessTokenClient only needs the three
        # above. They stay so the class shows every key credentials.yml takes.
        self.profile_id = credentials.get('profile_id')
        self.account_id = credentials.get('account_id')
        self.manager_account_id = credentials.get('manager_account_id')
