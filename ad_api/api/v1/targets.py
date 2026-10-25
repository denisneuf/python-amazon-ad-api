from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Targets(Client):
    r"""
    Targets(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified Targets endpoints

    The v1 API is not split by product: every call goes to the same resource
    (``/adsApi/v1/...``) and the product is selected in the request body via
    ``adProductFilter``.

    """

    @sp_endpoint('/adsApi/v1/query/targets', method='POST')
    def query_targets(self, **kwargs) -> ApiResponse:
        r"""
        query_targets(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query Targets (operationId: QueryTarget)

        Request Body [Required]
            | **adProductFilter** (dict) : [required]
                | **include** (list<AdProduct>) : Enum [ AMAZON_DSP, SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS, SPONSORED_TELEVISION ]
            | **targetIdFilter** (dict) [optional]
                | **include** (list<string>) : Target identifiers
            | **adGroupIdFilter** (dict) [optional]
                | **include** (list<string>) : Ad group identifiers
            | **campaignIdFilter** (dict) [optional]
                | **include** (list<string>) : Campaign identifiers
            | **keywordFilter** (dict) [optional]
                | **include** (list<string>) : Keyword texts
                | **queryTermMatchType** (string) : [required] Enum [ BROAD_MATCH, EXACT_MATCH ]
            | **productIdFilter** (dict) [optional]
                | **include** (list<string>) : Product identifiers
                | **queryTermMatchType** (string) : [required] Enum [ BROAD_MATCH, EXACT_MATCH ]
            | **matchTypeFilter** (dict) [optional]
                | **include** (list<MatchType>) : Enum [ BROAD, EXACT, INTERESTED_AUDIENCE, KEYWORDS_CLOSE_MATCH, KEYWORDS_LOOSE_MATCH, KEYWORDS_RELATED_TO_GIFTS, KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY, KEYWORDS_RELATED_TO_PRIME_DAY, KEYWORDS_RELATED_TO_YOUR_BRAND, KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES, KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY, PHRASE, PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS, PRODUCT_COMPLEMENTS, PRODUCT_EXACT, PRODUCT_REMARKETING, PRODUCT_SIMILAR, PRODUCT_SUBSTITUTES ]
            | **negativeFilter** (dict) [optional]
                | **include** (list<boolean>) : Keep only negative or non-negative targets
            | **targetTypeFilter** (dict) [optional]
                | **include** (list<TargetType>) : Enum [ AD_INITIATION, AD_PLAYER_SIZE, APP, AUDIENCE, BRAND_SAFETY_CATEGORY, BRAND_SAFETY_TIER, CONTENT_CATEGORY, CONTENT_GENRE, CONTENT_INSTREAM_POSITION, CONTENT_OUTSTREAM_POSITION, CONTENT_RATING, DAYPART, DEVICE, DOMAIN, FOLD_POSITION, INVENTORY_SOURCE, KEYWORD, LOCATION, NATIVE_CONTENT_POSITION, PLACEMENT_TYPE, PRODUCT, PRODUCT_AUDIENCE, PRODUCT_CATEGORY, SKIPPABILITY, THEME, THIRD_PARTY, VIDEO_AD_FORMAT, VIDEO_CONTENT_DURATION ]
            | **nativeLanguageLocaleFilter** (dict) [optional]
                | **include** (list<string>) : Locales of the unlocalized keyword text
            | **retailerIdFilter** (dict) [optional]
                | **include** (list<string>) : Retailer identifiers
            | **stateFilter** (dict) [optional]
                | **include** (list<State>) : Enum [ ARCHIVED, DRAFT, ENABLED, PAUSED ]
            | **marketplaceScopeFilter** (dict) [optional]
                | **include** (list<MarketplaceScope>) : Enum [ GLOBAL, SINGLE_MARKETPLACE ]
            | **retailerScopeFilter** (dict) [optional]
                | **include** (list<RetailerScope>) : Enum [ AMAZON, OTHER_RETAILERS ]
            | **maxResults** (int) [optional] Maximum number of records in the response
            | **nextToken** (string) [optional] Token to navigate to the next page

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **targets** (list), **nextToken** (string)

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/create/targets', method='POST')
    def create_targets(self, **kwargs) -> ApiResponse:
        r"""
        create_targets(body: dict) -> ApiResponse

        Amazon Ads API v1 - Create Targets (operationId: CreateTarget)

        Request Body [Required]
            | **targets** (list<dict>) : [required] One or more target objects.
              Each object requires **adProduct**, **negative**, **state**,
              **targetDetails** and **targetType**.

        Target fields
            | **adProduct** (string) : [required] Enum [ AMAZON_DSP, SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS, SPONSORED_TELEVISION ]
            | **negative** (boolean) : [required] True for a negative target
            | **state** (string) : [required] Enum [ DRAFT, ENABLED, PAUSED ]
            | **targetDetails** (dict) : [required] Exactly one of the variants below
            | **targetType** (string) : [required] Enum [ AD_INITIATION, AD_PLAYER_SIZE, APP, AUDIENCE, BRAND_SAFETY_CATEGORY, BRAND_SAFETY_TIER, CONTENT_CATEGORY, CONTENT_GENRE, CONTENT_INSTREAM_POSITION, CONTENT_OUTSTREAM_POSITION, CONTENT_RATING, DAYPART, DEVICE, DOMAIN, FOLD_POSITION, INVENTORY_SOURCE, KEYWORD, LOCATION, NATIVE_CONTENT_POSITION, PLACEMENT_TYPE, PRODUCT, PRODUCT_AUDIENCE, PRODUCT_CATEGORY, SKIPPABILITY, THEME, THIRD_PARTY, VIDEO_AD_FORMAT, VIDEO_CONTENT_DURATION ]
            | **adGroupId** (string) [optional] Identifier of the parent ad group
            | **campaignId** (string) [optional] Identifier of the parent campaign
            | **bid** (dict) [optional]
                | **bid** (number) : Bid value
                | **marketplaceSettings** (list<dict>) : Per marketplace bids
            | **marketplaceScope** (string) : Enum [ GLOBAL, SINGLE_MARKETPLACE ]
            | **marketplaces** (list<dict>) : Marketplaces where the target runs
            | **marketplaceConfigurations** (list<dict>) : Each with **marketplace** and **overrides** (both required)
            | **tags** (list<dict>) : Each with **key** and **value** (both required)

        targetDetails variants (use exactly one key, matching ``targetType``)
            | **keywordTarget** : requires ``keyword`` + ``matchType`` (Enum BROAD, EXACT, PHRASE);
              optional ``nativeLanguageKeyword``, ``nativeLanguageLocale``
            | **productTarget** : requires ``matchType``, ``product``, ``productIdType``
            | **productCategoryTarget** : requires ``productCategoryRefinement``;
              optional ``matchType``, ``productGenreRefinement``
            | **productAudienceTarget** : requires ``asin``, ``event``, ``lookback``, ``matchType``
            | **audienceTarget** : requires ``audienceId``; optional ``acrossGroupOperator``, ``groupId``, ``inGroupOperator``
            | **locationTarget** : requires ``locationId``; optional ``locationIdResolved``
            | **domainTarget** : requires ``domainTargetDetails``, ``domainTargetType``
            | **appTarget** : requires ``appId``, ``appType``
            | **deviceTarget** : requires ``deviceType``; optional ``deviceOrientation``, ``mobileDevice``, ``mobileEnvironment``, ``mobileOs``
            | **dayPartTarget** : requires ``dayOfWeek``, ``timeOfDay``
            | **contentCategoryTarget** : requires ``contentCategoryId``
            | **contentGenreTarget** : requires ``contentGenre``
            | **contentRatingTarget** : requires ``contentRatingType``, ``contentRatingTypeDetails``
            | **brandSafetyTierTarget** : requires ``brandSafetyTier``
            | **brandSafetyCategoryTarget** : requires ``brandSafetyCategory``
            | **inventorySourceTarget** : requires ``inventorySourceId``, ``inventorySourceType``
            | **adInitiationTarget** : requires ``videoInitiationType``
            | **adPlayerSizeTarget** : requires ``adPlayerSize``
            | **videoAdFormatTarget** : requires ``videoAdFormat``
            | **thirdPartyTarget** : requires ``thirdPartyTargetDetails``, ``thirdPartyTargetType``
            | **themeTarget** : requires ``matchType``
            | **contentInstreamPositionTarget** : requires ``instreamPosition``
            | **contentOutstreamPositionTarget** : requires ``outstreamPosition``
            | **videoContentDurationTarget** : requires ``duration``
            | **foldPositionTarget** : requires ``foldPosition``
            | **nativeContentPositionTarget** : requires ``nativePosition``
            | **placementTypeTarget** : requires ``placementType``
            | **skippabilityTarget** : requires ``skippabilityType``

            Example of the envelope::

                {"targetDetails": {"keywordTarget": {"keyword": "running shoes", "matchType": "EXACT"}}}

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **207** MultiStatus response with partial errors. Inspect the payload
                  to know which targets were created and which failed.

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/update/targets', method='POST')
    def update_targets(self, **kwargs) -> ApiResponse:
        r"""
        update_targets(body: dict) -> ApiResponse

        Amazon Ads API v1 - Update Targets (operationId: UpdateTarget)

        Request Body [Required]
            | **targets** (list<dict>) : [required] One or more target objects.
              Each object requires **targetId** and may include any of the fields below.

        Target fields [optional except targetId]
            | **targetId** (string) : [required] The identifier of the target to update.
            | **state** (string) : Enum [ DRAFT, ENABLED, PAUSED ]
            | **bid** (dict) : ``bid`` (number) and ``marketplaceSettings``
            | **campaignId** (string)
            | **marketplaceScope** (string) : Enum [ GLOBAL, SINGLE_MARKETPLACE ]
            | **marketplaces** (list<dict>)
            | **marketplaceConfigurations** (list<dict>)
            | **tags** (list<dict>)

            Note: ``targetDetails``, ``targetType``, ``negative`` and ``adProduct``
            are not part of the update body. To change what a target points at,
            delete it and create a new one.

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **207** MultiStatus response with partial errors. Inspect the payload
                  to know which targets were updated and which failed.

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/delete/targets', method='POST')
    def delete_targets(self, **kwargs) -> ApiResponse:
        r"""
        delete_targets(body: dict) -> ApiResponse

        Amazon Ads API v1 - Delete Targets (operationId: DeleteTarget)

        Request Body [Required]
            | **targetIds** (list<string>) : [required] Target identifiers to delete

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **207** MultiStatus response with partial errors. Inspect the payload
                  to know which target ids succeeded and which failed.

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
