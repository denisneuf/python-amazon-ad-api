from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class GlobalRecommendations(Client):
    r"""
    Amazon Ads API - Sponsored Products recommendations across marketplaces.

    These two routes answer for several countries at once, given the same
    product or the same ad group in each of them, where the per-marketplace
    routes answer for one country.

    Both are version 5 of the same idea and both take a recommendationType
    that decides which of two request shapes is expected:

        BIDS_FOR_NEW_AD_GROUP / KEYWORDS_FOR_ASINS
            a list of products, one per country
        BIDS_FOR_EXISTING_AD_GROUP / KEYWORDS_FOR_ADGROUP
            a campaign and ad group that already exist
    """

    @sp_endpoint('/sp/global/targets/bid/recommendations', method='POST')
    def get_multi_country_bid_recommendations(self, **kwargs) -> ApiResponse:
        r"""
        Recommends bids for targets across several countries.

        Two request shapes, chosen by recommendationType:

            BIDS_FOR_EXISTING_AD_GROUP
                adGroupId, campaignId, targetingExpressions, countryCodes.
            BIDS_FOR_NEW_AD_GROUP
                bidding, countryCodes, targetingExpressions, products.
                No adGroupId and no campaignId, the ad group does not exist yet.

        Request Body [Required]
            | **recommendationType** (string): [required] one of the two above.
            | **countryCodes** (array): target countries. Required by the
            |   new-ad-group shape.
            | **targetingExpressions** (array): required by both shapes.
            | **includeAnalysis** (boolean): defaults to false. Set it to true to
            |   get the estimated impressions for a range of eight bids per
            |   target. The contract says the analysis is only available for
            |   existing ad groups in the US marketplace.
            | **adGroupId** (string): existing ad group only.
            | **campaignId** (string): existing ad group only.
            | **products** (array): new ad group only, a list of countryProducts.
            | **bidding** (object): new ad group only.
            |   **strategy** (string): [required] the bidding strategy.
            |   **adjustments** (array): 1 to 3 placement adjustments.

        A 422 comes back when the marketplace or the target is not supported.

        Returns:

            ApiResponse

        """
        json_version = 'application/json'
        response_version = 'application/vnd.spthemebasedglobalbidrecommendation.v1+json'

        headers = {"Accept": response_version, "Content-Type": json_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/sp/global/targets/keywords/recommendations/list', method='POST')
    def list_multi_country_keyword_recommendations(self, **kwargs) -> ApiResponse:
        r"""
        Recommends keyword targets, with their bids, across several countries.

        Two request shapes, chosen by recommendationType:

            KEYWORDS_FOR_ASINS
                products, a list of countryProducts where each item maps a
                two-letter country code to a product.
            KEYWORDS_FOR_ADGROUP
                adGroupId and campaignId of a global campaign and ad group.

        Request Body [Required]
            | **recommendationType** (string): [required] KEYWORDS_FOR_ASINS or
            |   KEYWORDS_FOR_ADGROUP.
            | **products** (array): up to 50 countryProducts.
            | **targets** (array): up to 100 countryTargets. Each one is an
            |   object with matchType and countryKeywords, a map from a
            |   two-letter country code to a keyword object.
            | **adGroupId** (string): global ad group, second shape only.
            | **campaignId** (string): global campaign, second shape only.

        Each country is processed in parallel with the rules of version 5 of the
        per-marketplace keyword recommendation route.

        Returns:

            ApiResponse

        """
        json_version = 'application/vnd.spkeywordsrecommendation.v5+json'

        headers = {"Accept": json_version, "Content-Type": json_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
