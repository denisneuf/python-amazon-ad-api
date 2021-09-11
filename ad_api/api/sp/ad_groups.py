import urllib.parse

from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class AdGroups(Client):

    @sp_endpoint('/v2/sp/adGroups', method='GET')
    def list_ad_groups_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'),  params=kwargs)

    @sp_endpoint('/v2/sp/adGroups/extended', method='GET')
    def list_ad_groups_extended_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'),  params=kwargs)

    @sp_endpoint('/v2/sp/adGroups/{}', method='GET')
    def get_ad_groups_request(self, adGroupId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), adGroupId), params=kwargs)

    @sp_endpoint('/v2/sp/adGroups/extended/{}', method='GET')
    def get_ad_groups_extended_request(self, adGroupId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), adGroupId), params=kwargs)

    @sp_endpoint('/v2/sp/adGroups/{}', method='DELETE')
    def delete_ad_group_request(self, adGroupId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), adGroupId), params=kwargs)

    @sp_endpoint('/v2/sp/adGroups', method='POST')
    def create_ad_group_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/v2/sp/adGroups', method='PUT')
    def edit_ad_group_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)