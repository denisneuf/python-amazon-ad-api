from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class BrandStoreEditionPublishVersions(Client):
    r"""
    BrandStoreEditionPublishVersions(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified BrandStoreEditionPublishVersions endpoints

    Two routes, neither of which creates or deletes anything: a store edition
    publish version is queried, and its state is moved between draft and
    publish.

    Permissions: ``amazon_stores_view`` or ``amazon_stores_edit`` for the
    query, ``amazon_stores_edit`` alone for the update. This is Amazon Stores,
    not DSP.

    Two enums live here and they are not interchangeable:

    - ``StorePublishState`` -- ``DRAFT`` or ``PUBLISH``. What the caller
      decides, and the only one the update accepts.
    - ``StorePublishStatus`` -- ``DRAFT`` or ``REVIEW_IN_PROGRESS``. Where
      the content currently sits, and the only one the query filters on.

    The two differ by one letter in the name and share the ``DRAFT`` value, so
    sending one where the other belongs is a rejected request rather than a
    silent mismatch.

    Unlike the rest of v1, the query has no fully optional body: store, edition
    and publish status are all required, each accepting exactly one value.

    ``StorePublishStatus`` declares two values but the service accepts only one:
    asking for ``REVIEW_IN_PROGRESS`` answers ``400 Only DRAFT status query is
    supported``. The enum is honest about what exists in the data model, not
    about what can be queried.

    The ``storeEditionPublishId`` in the answer is not a plain identifier but a
    base64 token holding the schema version, the store, ``editionIdVersion`` and
    the status -- pass it back to update unchanged.
    """

    @sp_endpoint('/adsApi/v1/query/brandStoreEditionPublishVersions', method='POST')
    def query_brand_store_edition_publish_versions(self, **kwargs) -> ApiResponse:
        r"""
        query_brand_store_edition_publish_versions(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query (operationId: QueryBrandStoreEditionPublishVersion)

        Requires one of these permissions: ["amazon_stores_edit", "amazon_stores_view"]

        Request Body [Required]
            | **editionIdFilter** (dict) [required]
                | **include** (list<string>) : exactly one edition id
            | **storeIdFilter** (dict) [required]
                | **include** (list<string>) : exactly one store id
            | **publishStatusFilter** (dict) [required]
                | **include** (list<StorePublishStatus>) : exactly one value.
                  The contract declares [ DRAFT, REVIEW_IN_PROGRESS ] but the
                  service rejects the second one with
                  "400 Only DRAFT status query is supported". Send DRAFT.
            | **maxResults** (int) [optional]
            | **nextToken** (string) [optional]

        Returns
            ApiResponse. ``payload`` holds ``brandStoreEditionPublishVersions``
            and ``nextToken``. Each entry carries ``editionId``, ``storeId``,
            ``storeEditionPublishId``, ``publishState``, ``publishStatus`` and
            ``pages`` -- the last one appears only in the answer.
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )

    @sp_endpoint('/adsApi/v1/update/brandStoreEditionPublishVersions', method='POST')
    def update_brand_store_edition_publish_versions(self, **kwargs) -> ApiResponse:
        r"""
        update_brand_store_edition_publish_versions(body: dict) -> ApiResponse

        Amazon Ads API v1 - Update (operationId: UpdateBrandStoreEditionPublishVersion)

        Requires one of these permissions: ["amazon_stores_edit"]

        The array holds exactly one element, not a range.

        Request Body [Required]
            | **brandStoreEditionPublishVersions** (list, exactly 1) [required]

              Each element:
                | **storeEditionPublishId** (string) [required] version to move
                | **editionId** (string) [optional]
                | **storeId** (string) [optional]
                | **publishState** (string) [optional]
                  Enum [ DRAFT, PUBLISH ] -- this is StorePublishState, not the
                  StorePublishStatus the query filters on.

        Returns
            ApiResponse
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )
