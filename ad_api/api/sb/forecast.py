from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Forecast(Client):

    @sp_endpoint('/sb/campaigns/shopperSegments/forecast', method='POST')
    def list_forecast(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)
