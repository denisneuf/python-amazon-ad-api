from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Reports(Client):

    @sp_endpoint('/v2/sp/{}/report', method='POST')
    def post_report(self, recordType, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), recordType), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/v2/report/{}', method='GET')
    def get_report(self, reportId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), reportId), params=kwargs)
