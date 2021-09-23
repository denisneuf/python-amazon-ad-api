from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class KeywordsRecommendations(Client):

    @sp_endpoint('/sb/recommendations/keyword', method='POST')
    def list_keywords_recommendations(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)
