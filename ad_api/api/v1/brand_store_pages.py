from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class BrandStorePages(Client):
    r"""
    BrandStorePages(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified BrandStorePages endpoints

    One route, the query:

        POST /adsApi/v1/query/brandStorePages

    Permissions (either): ``amazon_stores_edit`` or ``amazon_stores_view``.

    Three filters are required and each accepts exactly one value:
    ``storeIdFilter``, ``editionIdFilter`` and ``pageIdFilter``. There is no way to
    list every page of a store through this route -- the page identifiers come
    from :class:`~ad_api.api.v1.BrandStores`, whose ``pageInfos`` carries one
    ``tag`` per page, and that tag is the ``pageId`` used here.

    A fourth filter, ``storeEditionPublishIdFilter``, is optional and takes the
    base64 token from BrandStoreEditionPublishVersions.

    The answer carries ``content``, the page body itself, which is why this
    contract is far larger than its siblings. Read the shape before dumping it.
    """

    @sp_endpoint('/adsApi/v1/query/brandStorePages', method='POST')
    def query_brand_store_pages(self, **kwargs) -> ApiResponse:
        r"""
        query_brand_store_pages(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query BrandStorePages (operationId: QueryBrandStorePage)

        Requires one of these permissions: ["amazon_stores_edit", "amazon_stores_view"]

        Request Body [Required]
            | **storeIdFilter** (dict) [required]
                | **include** (list<string>) : exactly one store id
            | **editionIdFilter** (dict) [required]
                | **include** (list<string>) : exactly one edition id, "default"
                  for a store's default edition
            | **pageIdFilter** (dict) [required]
                | **include** (list<string>) : exactly one page id, the tag seen
                  in BrandStores' pageInfos
            | **storeEditionPublishIdFilter** (dict) [optional]
                | **include** (list<string>) : one base64 publish token
            | **maxResults** (int) [optional]
            | **nextToken** (string) [optional]

        Returns
            ApiResponse. ``payload`` holds ``brandStorePages`` and ``nextToken``.
            Each page carries ``storeId``, ``editionId``, ``pageId``, ``pageType``,
            ``content`` and, when published, ``storeEditionPublishId`.
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )
