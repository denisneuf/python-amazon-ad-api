from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Forecast(Client):
    @sp_endpoint('/sb/campaigns/shopperSegments/forecast', method='POST')
    def list_forecast(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)
