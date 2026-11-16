from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class InitialBudgetRecommendation(Client):
    @sp_endpoint('/sp/campaigns/initialBudgetRecommendation', method='POST')
    def initial_campaign_budget_recommendation(self, **kwargs) -> ApiResponse:
        r"""
        Creates a daily budget recommendation, with benchmark metrics, while
        creating a new campaign. Nothing is created and nothing is charged.

        The path carries a capital B: initialBudgetRecommendation. Spelled in
        lower case the gateway does not recognise the route and answers 403
        IncompleteSignatureException, so the case matters here.

        Request Body [Required]
            | **adGroups** (array): exactly one ad group.
            |   **asins** (array): [required] 1 to 50 ASINs.
            |   **targetingExpressions** (array): [required] 1 to 100.
            |     **type** (string): [required] CLOSE_MATCH, COMPLEMENTS,
            |       KEYWORD_BROAD_MATCH, KEYWORD_EXACT_MATCH, KEYWORD_PHRASE_MATCH,
            |       LOOSE_MATCH or SUBSTITUTES.
            |     **value** (string): [required] must be empty when targetingType
            |       is auto. The service rejects a non-empty value with
            |       "Targeting expression's value should be empty for auto".
            |     **bid** (number): [required] the service rejects a null bid with
            |       "TargetingExpression bid cannot be null", even though the
            |       contract does not declare it.
            | **bidding** (object): [required]
            |   **strategy** (string): [required] AUTO_FOR_SALES,
            |     LEGACY_FOR_SALES or MANUAL.
            |   **adjustments** (array): up to 2 placement adjustments.
            | **targetingType** (string): [required] auto or manual.
            | **startDate** (string): YYYYMMDD.
            | **endDate** (string): YYYYMMDD.

        Returns:
            ApiResponse
            dailyBudget, recommendationId, benchmark and specialEvents.
            A dailyBudget of -1 means there is not enough information to
            produce a recommendation.

        """

        json_version = 'application/vnd.spinitialbudgetrecommendation.v3.4+json'

        headers = {"Accept": json_version, "Content-Type": json_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
