from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class AdGroupsV4(Client):
    """
    Version 4 of Sponsored Brands
    """

    @sp_endpoint('/sb/v4/adGroups', method='POST')
    def create_ad_group_v4(self, **kwargs) -> ApiResponse:
        """
        Creates Sponsored Brand Ad Group.

        Request Body

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sb/v4/adGroups', method='PUT')
    def update_ad_group_v4(self, **kwargs) -> ApiResponse:
        """
        Update Sponsored Brand Ad groups.

        Request Body

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sb/v4/adGroups/list', method='POST')
    def list_ad_group_v4(self, **kwargs) -> ApiResponse:
        """
        List Sponsored Brand Ad groups.

        Request Body (optional)
        | **campaignIdFilter** (dict) : Filter entities by the list of objectIds.
        | **stateFilter** (dict) : Filter entities by state.
        | **maxResults** (int) : Number of records to include in the paginated response. Defaults to max page size for given API.
        | **nextToken** (string) : Token value allowing to navigate to the next response page.
        | **adGroupIdFilter** (dict) : Filter entities by the list of objectIds.
        | **includeExtendedDataFields** (boolean) Setting to true will slow down performance because the API needs to retrieve extra information for each campaign.
        | **nameFilter** (dict) : Filter entities by name.

         Returns:
            | ApiResponse
        """
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/sb/v4/adGroups/{}', method='GET')
    def get_ad_group(self, adGroupId, **kwargs) -> ApiResponse:
        """
        Gets an ad group specified by identifier.

        Keyword Args
            | path **adGroupId**:*number* | Required. The identifier of an existing ad group.

        Returns:
            | ApiResponse

        """
        return self._request(fill_query_params(kwargs.pop('path'), adGroupId), params=kwargs)
