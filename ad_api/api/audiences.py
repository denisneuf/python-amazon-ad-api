from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Audiences(Client):
    """
    Audience Discovery API
    """
    @sp_endpoint('/audiences/taxonomy/list', method='POST')
    def list_audiences_taxonomy(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/audiences/list', method='POST')
    def list_audiences(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)
