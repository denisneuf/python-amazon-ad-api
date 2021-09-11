import urllib.parse

from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Campaigns(Client):

    @sp_endpoint('/v2/sp/campaigns', method='GET')
    def list_campaigns_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'),  params=kwargs)

    @sp_endpoint('/v2/sp/campaigns/extended', method='GET')
    def list_campaigns_extended_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'),  params=kwargs)

    @sp_endpoint('/v2/sp/campaigns/{}', method='GET')
    def get_campaign_request(self, campaignId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), campaignId), params=kwargs)

    @sp_endpoint('/v2/sp/campaigns/extended/{}', method='GET')
    def get_campaign_extended_request(self, campaignId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), campaignId), params=kwargs)

    @sp_endpoint('/v2/sp/campaigns/{}', method='DELETE')
    def delete_campaign_request(self, campaignId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), campaignId), params=kwargs)

    @sp_endpoint('/v2/sp/campaigns', method='POST')
    def create_campaigns_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/v2/sp/campaigns', method='PUT')
    def edit_campaigns_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)