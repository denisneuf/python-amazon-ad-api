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
        | campaignId (string) : The identifier of the campaign to which the keyword is associated.
        | name (string) : The name of the ad group.
        | state (CreateOrUpdateEntityState > string) : Entity state for create or update operation. Enum : [ENABLED, PAUSED]

        Returns
            ApiResponse

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sb/v4/adGroups', method='PUT')
    def update_ad_group_v4(self, **kwargs) -> ApiResponse:
        """
        Update Sponsored Brand Ad groups.

         Request Body
        | campaignId (string) : The identifier of the campaign to which the keyword is associated. [optional]
        | name (string) : The name of the ad group. [optional]
        | state (CreateOrUpdateEntityState > string) : Entity state for create or update operation. Enum : [ENABLED, PAUSED]

        Returns
            ApiResponse

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sb/v4/adGroups/list', method='GET')
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

    @sp_endpoint("/sb/v4/adGroups/delete", method="POST")
    def delete_ad_groups(self, **kwargs) -> ApiResponse:
        """
        Delete Sponsored Brands ad groups.

        Request Body (optional) :
            **adGroupIdFilter** (dict) : Filter entities by the list of objectIds. [optional]
                include (list) : Entity object identifier.

        Returns
            ApiResponse
        """
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint("/sb/v4/adGroups/{}", method="DELETE")
    def delete_ad_group_by_id(self, ad_group_id, **kwargs) -> ApiResponse:
        """
        Delete a specific Sponsored Brand Ad Group by its identifier id.

        Keyword Args
            | query **adGroupId** (integer): The identifier of an existing AdGroup. [required]

        Returns
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), ad_group_id), params=kwargs)

