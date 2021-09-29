from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Campaigns(Client):

    @sp_endpoint('/v2/sd/campaigns', method='GET')
    def list_campaigns(self, **kwargs) -> ApiResponse:
        r"""
        list_campaigns(self, **kwargs) -> ApiResponse

        Gets an array of campaigns.

            query **startIndex**:*integer* | Optional. 0-indexed record offset for the result set. Default value : 0

            query **count**:*integer* | Optional. Number of records to include in the paged response. Defaults to max page size.

            query **stateFilter**:*string* | Optional. The returned array is filtered to include only ad groups with state set to one of the values in the specified comma-delimited list. Available values : enabled, paused, archived, enabled, paused, enabled, archived, paused, archived, enabled, paused, archived Default value : enabled, paused, archived.

            query **name**:*string* | Optional. Restricts results to campaigns with the specified name.

            query **portfolioIdFilter**:*string* | Optional. A comma-delimited list of portfolio identifiers.

            query **campaignIdFilter**:*string* | Optional. A comma-delimited list of campaign identifiers.

        Returns:

            ApiResponse

        """
        return self._request(kwargs.pop('path'),  params=kwargs)
