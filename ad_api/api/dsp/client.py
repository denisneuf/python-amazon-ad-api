from ad_api.base import Client


class DspClient(Client):
    @property
    def headers(self):
        return {
            'User-Agent': self.user_agent,
            'Amazon-Advertising-API-ClientId': self.credentials.client_id,
            'Authorization': 'Bearer %s' % self.auth.access_token,
            'Content-Type': 'application/json',
        }
