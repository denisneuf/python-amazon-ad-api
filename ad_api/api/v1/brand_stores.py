from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class BrandStores(Client):
    r"""
    BrandStores(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified BrandStores endpoints

    One route: the query. A brand store is listed, never created here.

    Permissions (any one): advertiser_campaign_edit, creatives_view,
    account_view, creatives_edit, account_edit, campaign_view,
    advertiser_campaign_view, campaign_edit.

    ``storeNameFilter`` is required and takes exactly one name, so this route
    cannot list every store on the account. The answer is the way in to the
    rest of the Stores family: ``storeId`` from here is what
    :class:`~ad_api.api.v1.BrandStoreEditionPublishVersions` needs as
    ``storeIdFilter``.
    """

    @sp_endpoint('/adsApi/v1/query/brandStores', method='POST')
    def query_brand_stores(self, **kwargs) -> ApiResponse:
        r"""
        query_brand_stores(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query BrandStores (operationId: QueryBrandStore)

        Requires one of these permissions: ["advertiser_campaign_edit",
        "creatives_view", "account_view", "creatives_edit", "account_edit",
        "campaign_view", "advertiser_campaign_view", "campaign_edit"]

        Request Body [Required]
            | **storeNameFilter** (dict) [required]
                | **include** (list<string>) : exactly one store name
            | **maxResults** (int) [optional]
            | **nextToken** (string) [optional]

        Returns
            ApiResponse. ``payload`` holds ``brandStores`` and ``nextToken``.
            Each store carries ``storeId`` (required), ``storeName`` and
            ``pageInfos``. The ``storeId`` is what the publish-version family
            filters on.
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )
