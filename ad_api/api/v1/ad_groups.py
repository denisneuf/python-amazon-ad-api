from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class AdGroups(Client):
    r"""
    AdGroups(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified Ad Groups endpoints

    The v1 API is not split by product: every call goes to the same resource
    (``/adsApi/v1/...``) and the product is selected in the request body via
    ``adProductFilter``.

    """

    @sp_endpoint('/adsApi/v1/query/adGroups', method='POST')
    def query_ad_groups(self, **kwargs) -> ApiResponse:
        r"""
        query_ad_groups(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query Ad Groups (operationId: QueryAdGroup)

        Request Body [Required]
            | **adProductFilter** (dict) : [required]
                | **include** (list<AdProduct>) : Enum [ AMAZON_DSP, SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS, SPONSORED_TELEVISION ]
            | **adGroupIdFilter** (dict) [optional]
                | **include** (list<string>) : Ad group identifiers
            | **campaignIdFilter** (dict) [optional]
                | **include** (list<string>) : Campaign identifiers
            | **inventoryTypeFilter** (dict) [optional]
                | **include** (list<InventoryType>) : Enum [ AAP_MOBILE_APP, AMAZON_MOBILE_DISPLAY, AUDIO, AUDIO_AMAZON_DEAL, DISPLAY, LIVE_EVENTS, ONLINE_VIDEO, PODCAST, STANDARD_DISPLAY, STREAMING_TV, STREAMING_TV_AMAZON_DEAL, VIDEO ]
            | **marketplaceScopeFilter** (dict) [optional]
                | **include** (list<MarketplaceScope>) : Enum [ GLOBAL, SINGLE_MARKETPLACE ]
            | **nameFilter** (dict) [optional]
                | **include** (list<string>) : Ad group names
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
                | **adGroups** (list), **nextToken** (string)

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        body = kwargs.pop('body', None)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers,
                             **({'data': Utils.convert_body(body, False)} if body is not None else {}))

    @sp_endpoint('/adsApi/v1/create/adGroups', method='POST')
    def create_ad_groups(self, **kwargs) -> ApiResponse:
        r"""
        create_ad_groups(body: dict) -> ApiResponse

        Amazon Ads API v1 - Create Ad Groups (operationId: CreateAdGroup)

        Request Body [Required]
            | **adGroups** (list<dict>) : [required] One or more ad group objects.
              Each object requires **adProduct**, **campaignId**, **name** and **state**.

        Ad group fields
            | **adProduct** (string) : [required] Enum [ AMAZON_DSP, SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS, SPONSORED_TELEVISION ]
            | **campaignId** (string) : [required] Identifier of the parent campaign
            | **name** (string) : [required] Name of the ad group
            | **state** (string) : [required] Enum [ DRAFT, ENABLED, PAUSED ]
            | **bid** (dict) [optional]
                | **baseBid** (number) : Base bid value
                | **defaultBid** (number) : Default bid value
                | **maxAverageBid** (number) : Maximum average bid
                | **marketplaceSettings** (list<dict>) : Per marketplace bids
                    | **currencyCode** (string) : [required] Enum CurrencyCode (EUR, USD, GBP, ...)
                    | **marketplace** (string) : [required] Marketplace
                    | **defaultBid** (number) : Default bid for that marketplace
            | **budgets** (list<dict>) [optional] See Campaigns budget shape:
              ``budgetType``, ``budgetValue.monetaryBudgetValue.monetaryBudget`` (``currencyCode`` + ``value``), ``recurrenceTimePeriod``
            | **optimization** (dict) [optional]
                | **bidStrategy** (string) : Enum [ MANUAL, NEW_TO_BRAND, PRIORITIZE_KPI_TARGET, RULE_BASED, SALES_DOWN_ONLY, SALES_UP_AND_DOWN, SPEND_BUDGET_IN_FULL, USE_CAMPAIGN_STRATEGY ]
                | **budgetSettings** (dict) : ``budgetAllocation`` (Enum AUTO, MANUAL) and ``dailyMinSpendValue`` (number)
                | **goalSettings** (dict) : ``kpi`` (Enum ADD_TO_CART, APPLICATIONS, CHECKOUTS, CLICKS, CLICK_THROUGH_RATE, COMBINED_RETURN_ON_AD_SPEND, CONTACTS, COST_PER_ACTION, COST_PER_CLICK, COST_PER_CONVERSION_OFF_AMAZON, COST_PER_DETAIL_PAGE_VIEW, COST_PER_FIRST_APP_OPEN, COST_PER_INSTALL, COST_PER_SIGN_UP, COST_PER_UNSKIPPED_IMPRESSION, COST_PER_VIDEO_COMPLETION, DETAIL_PAGE_VIEW_RATE, FREQUENCY_AVERAGE, LEADS, OTHER, PAGE_VIEWS, PURCHASES, REACH, RETURN_ON_AD_SPEND, ROAS, ROAS_COMBINED, ROAS_OFF_AMAZON, ROAS_PROMOTED, SEARCH, SIGN_UP, SUBSCRIBE, TOP_OF_SEARCH_IMPRESSION_SHARE, TOTAL_RETURN_ON_AD_SPEND, VIDEO_COMPLETION_RATE)
            | **pacing** (dict) [optional]
                | **deliveryProfile** (string) : [required] Enum [ ASAP, EVEN, PACE_AHEAD ]
            | **targetingSettings** (dict) [optional]
                | **amazonViewability** (dict) : [required in this object]
                    | **includeUnmeasurableImpressions** (boolean) : [required]
                    | **viewabilityTier** (string) : [required] Enum [ ALL_TIERS, GREATER_THAN_40_PERCENT, GREATER_THAN_50_PERCENT, GREATER_THAN_60_PERCENT, GREATER_THAN_70_PERCENT, LESS_THAN_40_PERCENT ]
                | **automatedTargetingTactic** (string) : Enum [ AWARENESS, CUSTOMER_ACQUISITION, MAXIMIZE_PERFORMANCE, PROSPECTING, REMARKETING, RETENTION, SEARCH ]
                | **defaultAudienceTargetingMatchType** (string) : Enum [ EXACT, SIMILAR ]
                | **enableLanguageTargeting** (boolean)
                | **tacticsConvertersExclusionType** (string) : Enum [ NO_EXCLUSION, RECENT_CONVERTERS ]
                | **targetedPGDealId** (string)
                | **timeZoneType** (string) : Enum [ ADVERTISER_REGION, VIEWER ]
                | **userLocationSignal** (string) : Enum [ CURRENT, MULTIPLE_SIGNALS ]
                | **videoCompletionTier** (string) : Enum [ ALL_TIERS, GREATER_THAN_10_PERCENT, GREATER_THAN_20_PERCENT, GREATER_THAN_30_PERCENT, GREATER_THAN_40_PERCENT, GREATER_THAN_50_PERCENT, GREATER_THAN_60_PERCENT, GREATER_THAN_70_PERCENT, GREATER_THAN_80_PERCENT, GREATER_THAN_90_PERCENT ]
            | **adSettings** (dict) [optional]
                | **productAttributeSetRefinementConfigurationId** (string)
            | **advertisedProductCategoryIds** (list<string>) [optional]
            | **creativeRotationType** (string) : Enum [ RANDOM, WEIGHTED ]
            | **creativeType** (string) : Enum [ IMAGE, VIDEO ]
            | **inventoryType** (string) : Enum [ AAP_MOBILE_APP, AMAZON_MOBILE_DISPLAY, AUDIO, AUDIO_AMAZON_DEAL, DISPLAY, LIVE_EVENTS, ONLINE_VIDEO, PODCAST, STANDARD_DISPLAY, STREAMING_TV, STREAMING_TV_AMAZON_DEAL, VIDEO ]
            | **marketplaceScope** (string) : Enum [ GLOBAL, SINGLE_MARKETPLACE ]
            | **marketplaces** (list<dict>) : Marketplaces where the ad group runs
            | **marketplaceConfigurations** (list<dict>) : Each with **marketplace** and **overrides** (both required)
            | **startDateTime** (string) : Start date and time
            | **endDateTime** (string) : End date and time
            | **fees** (list<dict>) : Each with **addToBudgetSpentAmount**, **feeType**, **feeValue**, **thirdPartyProvider** (all required)
            | **frequencies** (list<dict>) : Frequency cap definitions
            | **purchaseOrderNumber** (string)
            | **retailerId** (string)
            | **tags** (list<dict>) : Each with **key** and **value** (both required)

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **207** MultiStatus response with partial errors. Inspect the payload
                  to know which ad groups were created and which failed.

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/update/adGroups', method='POST')
    def update_ad_groups(self, **kwargs) -> ApiResponse:
        r"""
        update_ad_groups(body: dict) -> ApiResponse

        Amazon Ads API v1 - Update Ad Groups (operationId: UpdateAdGroup)

        Request Body [Required]
            | **adGroups** (list<dict>) : [required] One or more ad group objects.
              Each object requires **adGroupId** and may include any of the fields below.

        Ad group fields [optional except adGroupId]
            | **adGroupId** (string) : [required] The identifier of the ad group to update.
            | **adProduct** (string) : Enum [ AMAZON_DSP, SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS, SPONSORED_TELEVISION ]
            | **name** (string) : Name of the ad group
            | **state** (string) : Enum [ DRAFT, ENABLED, PAUSED ]
            | **bid** (dict) : ``baseBid``, ``defaultBid``, ``maxAverageBid``, ``marketplaceSettings``
            | **budgets** (list<dict>) : Same shape as in create
            | **optimization** (dict) : ``bidStrategy``, ``budgetSettings``, ``goalSettings``
            | **pacing** (dict) : ``deliveryProfile`` Enum [ ASAP, EVEN, PACE_AHEAD ]
            | **targetingSettings** (dict) : ``amazonViewability``, ``defaultAudienceTargetingMatchType``, ``enableLanguageTargeting``, ``tacticsConvertersExclusionType``, ``targetedPGDealId``, ``timeZoneType``, ``userLocationSignal``, ``videoCompletionTier``
            | **adSettings** (dict) : ``productAttributeSetRefinementConfigurationId``
            | **advertisedProductCategoryIds** (list<string>)
            | **creativeRotationType** (string) : Enum [ RANDOM, WEIGHTED ]
            | **creativeType** (string) : Enum [ IMAGE, VIDEO ]
            | **marketplaceScope** (string) : Enum [ GLOBAL, SINGLE_MARKETPLACE ]
            | **marketplaces** (list<dict>)
            | **marketplaceConfigurations** (list<dict>)
            | **startDateTime** (string)
            | **endDateTime** (string)
            | **fees** (list<dict>)
            | **frequencies** (list<dict>)
            | **purchaseOrderNumber** (string)
            | **tags** (list<dict>)

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **207** MultiStatus response with partial errors. Inspect the payload
                  to know which ad groups were updated and which failed.

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/delete/adGroups', method='POST')
    def delete_ad_groups(self, **kwargs) -> ApiResponse:
        r"""
        delete_ad_groups(body: dict) -> ApiResponse

        Amazon Ads API v1 - Delete Ad Groups (operationId: DeleteAdGroup)

        Request Body [Required]
            | **adGroupIds** (list<string>) : [required] Ad group identifiers to delete

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **207** MultiStatus response with partial errors. Inspect the payload
                  to know which ad group ids succeeded and which failed.

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
