from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Recommendations(Client):
    @sp_endpoint('/sb​/recommendations​/creative​/headline', method='POST')
    def list_recommendations(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)
