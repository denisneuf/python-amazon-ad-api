from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class Stores(Client):
    """
    Read engagement and insight metrics for a Brand Store.

    Both routes are keyed by the brand entity id and both answer a versioned
    media type: the client asks for v1 by default and the service picks the
    shape of the answer from it. The 3.0 contract declares both as POST, which
    is why they carry a body even though they only read.
    """

    @sp_endpoint('/stores/{}/asinMetrics', method='POST')
    def get_asin_engagement_for_store(self, brandEntityId, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Engagement figures for the ASINs of a store.

        Keyword Args
            | path **brandEntityId** (string): the brand entity id of the store. [required]
            | **version** (int): the media type version asked for. Defaults to 1.
            | body **body** (string | dict): the ASIN list to measure. [required]

        Returns:
            | ApiResponse
        """
        content_type = 'application/vnd.GetAsinEngagementForStoreRequest.v'+ str(version) +'+json'
        accept = 'application/vnd.GetAsinEngagementForStoreResponse.v'+ str(version) +'+json'
        headers = {'Content-Type': content_type, 'Accept': accept}
        return self._request(fill_query_params(kwargs.pop('path'), brandEntityId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/stores/{}/insights', method='POST')
    def get_insights_for_store_api(self, brandEntityId, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Insight metrics for a store, over the period named in the body.

        The contract declares this route as POST, so a body is expected even
        though the call only reads. An earlier version of this method sent the
        same body on a GET.

        Keyword Args
            | path **brandEntityId** (string): the brand entity id of the store. [required]
            | **version** (int): the media type version asked for. Defaults to 1.
            | body **body** (string | dict): the period and grouping to report. [required]

        Returns:
            | ApiResponse

        Documentation: https://advertising.amazon.com/API/docs/en-us/stores
        """
        content_type = 'application/vnd.GetInsightsForStoreRequest.v'+ str(version) +'+json'
        headers = {'Content-Type': content_type}
        return self._request(fill_query_params(kwargs.pop('path'), brandEntityId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
