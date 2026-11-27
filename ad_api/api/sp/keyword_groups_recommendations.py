from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class KeywordGroupsRecommendations(Client):
    r"""
    Amazon Ads API - Sponsored Products keyword group recommendations.

    Keyword Groups is a control for keyword-based campaigns: a collection of
    keywords that reaches a relevant audience as one unit. Once a keyword group
    is created its performance shows up in the search terms report.

    The route is in beta.
    """

    @sp_endpoint('/sp/targeting/recommendations/keywordGroups', method='POST')
    def get_keyword_group_recommendations(self, **kwargs) -> ApiResponse:
        r"""
        Recommends keyword group targets for a list of ad ASINs.

        Request Body [Required]
            | **asins** (array): [required] 1 to 1000 ASINs, 32 characters each.
            | **countryCode** (string): origin country of the ASIN list, used to
            |   generate the recommendations.
            | **nextToken** (string): set when the previous answer had more items.

        Returns:

            ApiResponse

        """
        json_version = 'application/vnd.spkeywordgroupsrecommendations.v1.0+json'

        headers = {"Accept": json_version, "Content-Type": json_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
