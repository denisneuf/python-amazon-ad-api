from ad_api.base import Client, sp_endpoint, ApiResponse


class BrandStoreEditions(Client):
    r"""
    BrandStoreEditions(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified BrandStoreEditions endpoints

    One route, and it is a ``GET`` with query parameters rather than the POST
    body the rest of v1 uses:

        GET /adsApi/v1/brandStoreEditions?brandStoreId=<id>

    Permissions (either): ``amazon_stores_edit`` or ``amazon_stores_view``.

    This is the middle link of the Stores chain:

    - :class:`~ad_api.api.v1.BrandStores` gives the ``storeId``.
    - here that becomes ``brandStoreId`` and returns the ``editionId``.
    - :class:`~ad_api.api.v1.BrandStoreEditionPublishVersions` needs both.

    ``maxResults`` is unusual: the range is 11 to 50 with a default of 50, not
    the 1-based range the other families use.
    """

    @sp_endpoint('/adsApi/v1/brandStoreEditions', method='GET')
    def list_brand_store_editions(self, brandStoreId, **kwargs) -> ApiResponse:
        r"""
        list_brand_store_editions(brandStoreId, **kwargs) -> ApiResponse

        Amazon Ads API v1 - List BrandStoreEditions (operationId: ListBrandStoreEdition)

        Requires one of these permissions: ["amazon_stores_edit", "amazon_stores_view"]

        Query parameters
            | **brandStoreId** (string) [required] the store id from BrandStores
            | **maxResults** (int) [optional] range 11..50, default 50
            | **nextToken** (string) [optional] token from a previous answer

        Returns
            ApiResponse. ``payload`` holds ``brandStoreEditions`` (0 to 50) and
            ``nextToken``. Each edition carries ``editionId``, ``editionName``,
            ``storeId`` and ``storeEditionSchedule``.

            The ``editionId`` is what BrandStoreEditionPublishVersions filters on.
        """
        path = kwargs.pop('path')
        kwargs.pop('method', None)
        params = dict(kwargs)
        params['brandStoreId'] = brandStoreId
        return self._request(path, params=params)
