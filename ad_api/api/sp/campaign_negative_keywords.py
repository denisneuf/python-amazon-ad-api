from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class CampaignNegativeKeywords(Client):

    @sp_endpoint('/v2/sp/campaignNegativeKeywords', method='GET')
    def list_campaign_negative_keywords_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/v2/sp/campaignNegativeKeywords/extended', method='GET')
    def list_campaign_negative_keywords_extended_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/v2/sp/campaignNegativeKeywords/{}', method='GET')
    def get_campaign_negative_keywords_request(self, keywordId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), keywordId), params=kwargs)

    @sp_endpoint('/v2/sp/campaignNegativeKeywords/extended/{}', method='GET')
    def get_campaign_negative_keywords_extended_request(self, keywordId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), keywordId), params=kwargs)

    @sp_endpoint('/v2/sp/campaignNegativeKeywords/{}', method='DELETE')
    def delete_campaign_negative_keywords_request(self, keywordId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), keywordId), params=kwargs)

    @sp_endpoint('/v2/sp/campaignNegativeKeywords', method='POST')
    def create_campaign_negative_keywords_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/v2/sp/campaignNegativeKeywords', method='PUT')
    def edit_campaign_negative_keywords_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)