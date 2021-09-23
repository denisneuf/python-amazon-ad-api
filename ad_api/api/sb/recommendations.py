from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Recommendations(Client):

    @sp_endpoint('/sb​/recommendations​/creative​/headline', method='POST')
    def list_recommendations(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)
