from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class CampaignsRecommendations(Client):
    @sp_endpoint('/sp/campaign/recommendations', method='GET')
    def list_campaigns_recommendations(self, **kwargs) -> ApiResponse:
        r"""
        Gets the top consolidated recommendations across bid, budget, targeting for SP campaigns given an advertiser profile id. The recommendations are refreshed everyday.

        Param:
            | query **nextToken** (string). Optional. Token to retrieve subsequent page of results.
            | query **maxResults** (string). Optional. Limits the number of items to return in the response.

        Returns:

            ApiResponse

        """
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/sp/campaign/recommendations', method='POST')
    def fetch_campaigns_recommendations(self, **kwargs) -> ApiResponse:
        r"""
        Gets the top consolidated recommendations for the campaigns named in the
        body, one recommendation type per campaign. Refreshed every day.

        The GET on the same path takes no body and returns every recommendation
        the account has; this POST narrows it to the campaigns and types asked
        for. It uses its own content type, v2, where the GET uses v1.

        Request Body [Required]
            | **campaigns** (array): 1 to 10 campaigns.
            |   **campaignId** (string): [required] The campaign identifier.
            |   **recommendationType** (string): [required] one of
            |     BIDDING_STRATEGY, BUDGET_STRATEGY, KEYWORD, KEYWORD_GROUP,
            |     PLACEMENT_BIDDING, SHOPPER_COHORT.
            | **maxResults** (integer): 1 to 5. Defaults to 1.
            | **nextToken** (string): Token for the next page.

        Returns:

            ApiResponse

        """
        json_version = 'application/vnd.spgetcampaignrecommendationsrequest.v2+json'
        response_version = 'application/vnd.spgetcampaignrecommendationsresponse.v2+json'

        headers = {"Accept": response_version, "Content-Type": json_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
