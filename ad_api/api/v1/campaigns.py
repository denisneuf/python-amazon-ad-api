from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Campaigns(Client):
    r"""
    Campaigns(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified Campaigns endpoints

    The v1 API is not split by product: every call goes to the same resource
    (``/adsApi/v1/...``) and the product is selected in the request body via
    ``adProductFilter``.

    """


    @sp_endpoint('/adsApi/v1/query/campaigns', method='POST')
    def query_campaigns(self, **kwargs) -> ApiResponse:
        r"""
        query_campaigns(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query Campaigns (operationId: QueryCampaign)

        Request Body [Required]
            | **adProductFilter** (dict): [required]
                | **include** (list<AdProduct>) : Enum [ AMAZON_DSP, SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS, SPONSORED_TELEVISION ]
            | **campaignIdFilter** (dict) [optional]
                | **include** (list<string>) : Campaign identifiers
            | **goalFilter** (dict) [optional]
                | **include** (list<Goal>) : Enum [ AWARENESS, CONSIDERATION, CONVERSIONS ]
            | **marketplaceScopeFilter** (dict) [optional]
                | **include** (list<MarketplaceScope>) : Enum [ GLOBAL, SINGLE_MARKETPLACE ]
            | **nameFilter** (dict) [optional]
                | **include** (list<string>) : Campaign names
                | **queryTermMatchType** (string) : [required] Enum [ BROAD_MATCH, EXACT_MATCH ]
            | **portfolioIdFilter** (dict) [optional]
                | **include** (list<string>) : Portfolio identifiers
            | **retailerScopeFilter** (dict) [optional]
                | **include** (list<RetailerScope>) : Enum [ AMAZON, OTHER_RETAILERS ]
            | **stateFilter** (dict) [optional]
                | **include** (list<State>) : Enum [ ARCHIVED, DRAFT, ENABLED, PAUSED ]
            | **maxResults** (int) [optional] Minimum 1, Maximum 1000
            | **nextToken** (string) [optional] Token to navigate to the next page

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **campaigns** (list), **nextToken** (string)

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/delete/campaigns', method='POST')
    def delete_campaigns(self, **kwargs) -> ApiResponse:
        r"""
        delete_campaigns(body: dict) -> ApiResponse

        Amazon Ads API v1 - Delete Campaigns (operationId: DeleteCampaign)

        Request Body [Required]
            | **campaignIds** (list<string>) : [required] Campaign identifiers to delete

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **207** MultiStatus response with partial errors. Inspect the payload
                  to know which campaign ids succeeded and which failed.

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/update/campaigns', method='POST')
    def update_campaigns(self, **kwargs) -> ApiResponse:
        r"""
        update_campaigns(body: dict) -> ApiResponse

        Amazon Ads API v1 - Update Campaigns (operationId: UpdateCampaign)

        Request Body [Required]
            | **campaigns** (list<dict>) : [required] One or more campaign objects to update.
              Each object requires **campaignId** and may include any of the fields below.

        Campaign fields [optional except campaignId]
            | **campaignId** (string) : [required] The identifier of the campaign to update.
            | **adProduct** (string) : Enum [ AMAZON_DSP, SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS, SPONSORED_TELEVISION ]
            | **name** (string) : The name of the campaign.
            | **state** (string) : Enum [ DRAFT, ENABLED, PAUSED ]
            | **budgets** (list<dict>) : Budget objects for the campaign.
            | **startDateTime** (string) : Campaign start date and time.
            | **endDateTime** (string) : Campaign end date and time.
            | **portfolioId** (string) : The identifier of the portfolio.
            | **purchaseOrderNumber** (string) : Advertiser purchase order number.
            | **tags** (list<dict>) : Advertiser-specified custom identifiers.
            | **marketplaces** (list<dict>) : Marketplaces where the campaign runs.
            | **marketplaceConfigurations** (list<dict>) : Per-marketplace overrides.
            | **countries** (list<string>) : Country codes.
            | **costType** (string) : Enum [ CPC, CPM, FIXED_PRICE, VCPM ]
            | **fees** (list<dict>) : Fee definitions.
            | **flights** (list<dict>) : Flight schedules.
            | **frequencies** (list<dict>) : Frequency cap definitions.
            | **optimizations** (dict) : Campaign optimization settings.
            | **siteRestrictions** (list<dict>) : Site restrictions.
            | **skanAppId** (string) : SKAdNetwork app id.
            | **targetedPGDealId** (string) : Targeted programmatic guaranteed deal id.
            | **adomains** (list<string>) : Ad domains.

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **207** MultiStatus response with partial errors. Inspect the payload
                  to know which campaigns succeeded and which failed.

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/create/campaigns', method='POST')
    def create_campaigns(self, **kwargs) -> ApiResponse:
        r"""
        create_campaigns(body: dict) -> ApiResponse

        Amazon Ads API v1 - Create Campaigns (operationId: CreateCampaign)

        Request Body [Required]
            | **campaigns** (list<dict>) : [required] One or more campaign objects to create.
              Each object requires **adProduct**, **name** and **state**.

        Campaign fields
            | **adProduct** (string) : [required] Enum [ AMAZON_DSP, SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS, SPONSORED_TELEVISION ]
            | **name** (string) : [required] The name of the campaign.
            | **state** (string) : [required] Enum [ DRAFT, ENABLED, PAUSED ]
            | **budgets** (list<dict>) : Budget objects for the campaign.
                | **budgetType** (string) : [required] Budget type.
                | **budgetValue** (dict) : [required] Budget amount.
                | **recurrenceTimePeriod** (string) : [required] Recurrence period.
            | **startDateTime** (string) : Campaign start date and time.
            | **endDateTime** (string) : Campaign end date and time.
            | **portfolioId** (string) : The identifier of the portfolio.
            | **purchaseOrderNumber** (string) : Advertiser purchase order number.
            | **tags** (list<dict>) : [required key+value] Advertiser-specified custom identifiers.
            | **marketplaces** (list<dict>) : Marketplaces where the campaign runs.
            | **marketplaceConfigurations** (list<dict>) : Per-marketplace overrides, each with
              **marketplace** and **overrides** (both required).
            | **countries** (list<string>) : Country codes.
            | **costType** (string) : Enum [ CPC, CPM, FIXED_PRICE, VCPM ]
            | **fees** (list<dict>) : [required feeType+feeValue+feeValueType] Fee definitions.
            | **flights** (list<dict>) : [required budget+startDateTime+endDateTime] Flight schedules.
            | **frequencies** (list<dict>) : [required eventMaxCount+frequencyTargetingSetting+
              timeCount+timeUnit] Frequency cap definitions.
            | **optimizations** (dict) : Campaign optimization settings.
            | **siteRestrictions** (list<dict>) : Site restrictions.
            | **brandId** (string) : Brand identifier.
            | **skanAppId** (string) : SKAdNetwork app id.
            | **targetedPGDealId** (string) : Targeted programmatic guaranteed deal id.
            | **adomains** (list<string>) : Ad domains.
            | **autoCreationSettings** (dict) : Automatic creation settings.

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            ApiResponse
                | **207** MultiStatus response with partial errors. Inspect the payload
                  to know which campaigns were created and which failed.

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
