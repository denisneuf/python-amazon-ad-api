from ad_api.base import Client
from ad_api.auth.credentials import BaseCredentials
from ad_api.api.dsp.credential_provider import DspCredentialProvider
from ad_api.api.dsp.access_token_client import DspAccessTokenClient


class DspClient(Client):
    access_token_client_class = DspAccessTokenClient
    credentials_class = BaseCredentials
    credential_provider_class = DspCredentialProvider

    @property
    def headers(self):
        return {
            'User-Agent': self.user_agent,
            'Amazon-Advertising-API-ClientId': self.credentials.client_id,
            'Authorization': 'Bearer %s' % self.auth.access_token,
            'Content-Type': 'application/json',
        }
