from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Labels(Client):
    r"""
    Labels(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified Labels endpoints

    Labels has a single route and it is read only: there is no create, update
    or delete in the contract.

    The required member is not the usual adProductFilter but
    ``labelObjectTypeFilter``, and it takes exactly one value:

        AD_GROUP, CAMPAIGN, DEAL, INVENTORY_GROUP

    ``adProductFilter`` is optional here and also takes exactly one value.
    """

    @sp_endpoint('/adsApi/v1/query/labels', method='POST')
    def query_labels(self, **kwargs) -> ApiResponse:
        r"""
        query_labels(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query Labels (operationId: QueryLabel)

        Request Body [Required]
            | **labelObjectTypeFilter** (dict) : [required] exactly one value
                | **include** (list<LabelObjectType>) : Enum [ AD_GROUP, CAMPAIGN, DEAL, INVENTORY_GROUP ]
            | **adProductFilter** (dict) : [optional] exactly one value
                | **include** (list<AdProduct>) : Enum [ AMAZON_DSP, SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS, SPONSORED_TELEVISION ]
            | **labelIdFilter** (dict) : [optional] 1..50 ids
                | **include** (list<string>)
            | **labelNameFilter** (dict) : [optional] 1..10 names
                | **include** (list<string>)
            | **maxResults** (int) : 1..1000, default 100
            | **nextToken** (string) : token to navigate to the next page

        Returns
            | **labels** (list<Label>) : 0..1000
                | **labelId** (string) : [required]
                | **labelName** (string) : [required]
                | **adProduct** (AdProduct)
            | **nextToken** (string)

        A body without labelObjectTypeFilter is a rejected request, not an
        empty answer, so every call needs that member even when the other
        filters are left out.

        Requires one of these permissions:
            campaign_edit, campaign_view
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
