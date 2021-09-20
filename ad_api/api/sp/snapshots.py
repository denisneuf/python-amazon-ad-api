from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Snapshots(Client):

    @sp_endpoint('/v2/sp/{}/snapshots', method='POST')
    def post_snapshot(self, recordType, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), recordType), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/v2/snapshots/{}', method='GET')
    def get_snapshot(self, reportId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), reportId), params=kwargs)
