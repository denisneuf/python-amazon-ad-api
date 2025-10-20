from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class KeywordsRecommendations(Client):
    @sp_endpoint('/sb/recommendations/keyword', method='POST')
    def list_keywords_recommendations(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)
