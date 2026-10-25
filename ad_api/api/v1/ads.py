from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Ads(Client):
    r"""
    Ads(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified Ads endpoints

    The v1 API is not split by product: every call goes to the same resource
    (``/adsApi/v1/...``) and the product is selected in the request body via
    ``adProductFilter``.

    """

    @sp_endpoint('/adsApi/v1/query/ads', method='POST')
    def query_ads(self, **kwargs) -> ApiResponse:
        r"""
        query_ads(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query Ads (operationId: QueryAd)

        Request Body [Required]
            | **adProductFilter** (dict) : [required]
                | **include** (list<AdProduct>) : Enum [ AMAZON_DSP, SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS, SPONSORED_TELEVISION ]
            | **adIdFilter** (dict) [optional]
                | **include** (list<string>) : Ad identifiers
            | **adGroupIdFilter** (dict) [optional]
                | **include** (list<string>) : Ad group identifiers
            | **campaignIdFilter** (dict) [optional]
                | **include** (list<string>) : Campaign identifiers
            | **marketplaceScopeFilter** (dict) [optional]
                | **include** (list<MarketplaceScope>) : Enum [ GLOBAL, SINGLE_MARKETPLACE ]
            | **nameFilter** (dict) [optional]
                | **include** (list<string>) : Ad names
                | **queryTermMatchType** (string) : [required] Enum [ BROAD_MATCH, EXACT_MATCH ]
            | **retailerScopeFilter** (dict) [optional]
                | **include** (list<RetailerScope>) : Enum [ AMAZON, OTHER_RETAILERS ]
            | **stateFilter** (dict) [optional]
                | **include** (list<State>) : Enum [ ARCHIVED, DRAFT, ENABLED, PAUSED ]
            | **maxResults** (int) [optional] Maximum number of records in the response
            | **nextToken** (string) [optional] Token to navigate to the next page

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **ads** (list), **nextToken** (string)

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/create/ads', method='POST')
    def create_ads(self, **kwargs) -> ApiResponse:
        r"""
        create_ads(body: dict) -> ApiResponse

        Amazon Ads API v1 - Create Ads (operationId: CreateAd)

        Request Body [Required]
            | **ads** (list<dict>) : [required] One or more ad objects.
              Each object requires **adProduct**, **adType**, **creative** and **state**.

        Ad fields
            | **adProduct** (string) : [required] Enum [ AMAZON_DSP, SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS, SPONSORED_TELEVISION ]
            | **adType** (string) : [required] Enum [ AUDIO, COMPONENT, DISPLAY, PRODUCT_AD, THIRD_PARTY, VIDEO ]
            | **creative** (dict) : [required] Exactly one of the six variants below
            | **state** (string) : [required] Enum [ DRAFT, ENABLED, PAUSED ]
            | **adGroupId** (string) [optional] Identifier of the parent ad group
            | **name** (string) [optional] Name of the ad
            | **marketplaceScope** (string) : Enum [ GLOBAL, SINGLE_MARKETPLACE ]
            | **marketplaces** (list<dict>) : Marketplaces where the ad runs
            | **marketplaceConfigurations** (list<dict>) : Per marketplace overrides
            | **tags** (list<dict>) : Each with **key** and **value** (both required)

        Creative variants (use exactly one, matching ``adType``)
            | **audioCreative** (dict) : For ``AUDIO``
            | **displayCreative** (dict) : For ``DISPLAY``, carries ``standardDisplaySettings``
            | **videoCreative** (dict) : For ``VIDEO``, carries ``onlineVideoSettings`` / ``streamingTvSettings``
            | **thirdPartyCreative** (dict) : For ``THIRD_PARTY``, carries ``thirdPartyDisplaySettings`` / ``thirdPartyVideoSettings``
            | **componentCreative** (dict) : For ``COMPONENT``, carries ``assetBasedCreativeSettings``,
              ``autoCollectionSettings``, ``brandGallerySettings``, ``brandStoreSettings``,
              ``manualCollectionSettings``, ``productCollectionSettings``,
              ``productVideoSettings``, ``responsiveEcommerceSettings``,
              ``storeSpotlightSettings``
            | **productCreative** (dict) : For ``PRODUCT_AD``, carries ``productCreativeSettings``

            Example of the envelope::

                {"creative": {"productCreative": {"productCreativeSettings": {...}}}}

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **207** MultiStatus response with partial errors. Inspect the payload
                  to know which ads were created and which failed.

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/update/ads', method='POST')
    def update_ads(self, **kwargs) -> ApiResponse:
        r"""
        update_ads(body: dict) -> ApiResponse

        Amazon Ads API v1 - Update Ads (operationId: UpdateAd)

        Request Body [Required]
            | **ads** (list<dict>) : [required] One or more ad objects.
              Each object requires **adId** and may include any of the fields below.

        Ad fields [optional except adId]
            | **adId** (string) : [required] The identifier of the ad to update.
            | **creative** (dict) : Same six-variant envelope as in create
            | **name** (string) : Name of the ad
            | **state** (string) : Enum [ DRAFT, ENABLED, PAUSED ]
            | **marketplaceScope** (string) : Enum [ GLOBAL, SINGLE_MARKETPLACE ]
            | **marketplaces** (list<dict>)
            | **marketplaceConfigurations** (list<dict>)
            | **tags** (list<dict>)

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **207** MultiStatus response with partial errors. Inspect the payload
                  to know which ads were updated and which failed.

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/delete/ads', method='POST')
    def delete_ads(self, **kwargs) -> ApiResponse:
        r"""
        delete_ads(body: dict) -> ApiResponse

        Amazon Ads API v1 - Delete Ads (operationId: DeleteAd)

        Request Body [Required]
            | **adIds** (list<string>) : [required] Ad identifiers to delete

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **207** MultiStatus response with partial errors. Inspect the payload
                  to know which ad ids succeeded and which failed.

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
