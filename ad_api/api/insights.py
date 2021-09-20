from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Insights(Client):
    """
    Insights API
    """
    @sp_endpoint('/insights/audiences/{}/overlappingAudiences', method='GET')
    def get_insights(self, audienceId, **kwargs) -> ApiResponse:
        r"""
        get_insights(self, audienceId, **kwargs) -> ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), audienceId), params=kwargs)