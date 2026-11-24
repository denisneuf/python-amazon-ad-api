from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class RecommendationTypes(Client):
    r"""
    RecommendationTypes(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - recommendation types for Sponsored Brands

    One route, read only, and the product is in the path:

        POST /adsApi/v1/query/recommendationTypes/sb

    This family lists the kinds of recommendation that exist. Recommendations
    itself, in ad_api.api.v1.Recommendations, lists the ones the account
    actually has.

    Only the Sponsored Brands segment is published, and its schemas are
    prefixed SB. The route keeps no SB in its name, so another product would
    arrive as .../sp or .../sd beside it.
    """

    @sp_endpoint('/adsApi/v1/query/recommendationTypes/sb', method='POST')
    def query_sb_recommendation_types(self, **kwargs) -> ApiResponse:
        r"""
        query_sb_recommendation_types(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query SB Recommendation Types (operationId: SBQueryRecommendationType)

        Request Body [All optional]
            | **maxResults** (int) : 50..500, default 50
            | **nextToken** (string) : token to navigate to the next page

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Returns
            | **recommendationTypes** (list<SBRecommendationType>) : 0..500
                | **recommendationTypeId** (string) : [required] a UUID or a unique descriptive string
                | **recommendationTypeTitle** (string) : [required]
            | **nextToken** (string)

        maxResults starts at 50, so a smaller value is a rejected body rather
        than a shorter page. An empty body is valid and asks for the defaults.

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] Advertiser account identifier

        Requires one of these permissions:
            advertiser_campaign_view
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}

        # Optional account header, taken from kwargs and removed before the
        # call is built: left in kwargs it would travel in the query string.
        account_id = kwargs.pop('account_id', None)
        if account_id:
            headers["Amazon-Ads-AccountId"] = account_id

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
