from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Reports(Client):

    @sp_endpoint('/v2/sp/{}/report', method='POST')
    def post_report_request(self, recordType, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), recordType), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/v2/report/{}', method='GET')
    def get_report_request(self, reportId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), reportId), params=kwargs)

    @sp_endpoint('/v2/sp/{}/snapshot', method='POST')
    def post_snapshot_request(self, recordType, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), recordType), data=kwargs.pop('body'), params=kwargs)