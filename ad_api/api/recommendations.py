from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class Recommendations(Client):
    """ """

    @sp_endpoint('/recommendations/list', method='POST')
    def list_recommendations(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Retrieves a list of recommendations.

        Request Body (required)
            | ListRecommendationsRequest {
            | **maxResults** (integer) default: 500 minimum: 1 maximum: 500
            | **nextToken** (string) Token to retrieve the next page of results.
            | **filters** (array) minItems: 1 maxItems: 10 [
            |   ListRecommendationsFilter {
            |       **include** (boolean): Flag to specify if the filter should be included or excluded. default: true
            |       **field**\* FilterField (string): Field to filter by. Enum: ['RECOMMENDATION_ID', 'AD_PRODUCT', 'RECOMMENDATION_TYPE', 'STATUS', 'GROUPING_TYPE', 'CAMPAIGN_ID']
            |       **values**\* (array) minItems: 1 maxItems: 500 [
            |           string
            |       ]
            |       **operator** FilterOperator (string): Operator to filter field by. Enum: ['EXACT']
            |       }
            |   ]
            | }

        The values ``STATUS`` accepts are not the states of a campaign. They are
        the stages a recommendation passes through, and the service names them in
        its rejection message: ``PUBLISHED``, ``APPLY_IN_PROGRESS``,
        ``APPLY_SUCCESS``, ``APPLY_FAILED`` and ``REJECTED``. ``ENABLED`` and
        ``ACTIVE`` are refused.

        ``filters`` behaves oddly. An empty list answers
        ``400 Member must have length greater than or equal to 1``, yet leaving
        the member out altogether answers ``200`` with the account's
        recommendations. So it is required when present, and optional in
        practice.

        A body is required: without one the call fails before reaching the
        service, with ``KeyError: 'body'``.

        Returns
            ApiResponse with ``recommendations``, ``totalResults`` and
            ``nextToken``. The list is empty for an account that has none, which
            is a fact about the account rather than a failed call.

        """
        schema_version = 'application/vnd.listRecommendationsRequest.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/recommendations/apply', method='POST')
    def apply_recommendations(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Applies one or more recommendations.

        Request Body (required)
            | ApplyRecommendationsRequest {
            | **recommendationIds**\* (array) minItems: 1 maxItems: 100 [
            |       (string) Recommendation identifier.
            |   ]
            | }

        .. warning::

            This changes campaigns. Applying a recommendation edits real bidding
            and budgets on the account, and there is no undo richer than
            changing them back by hand.

            Not exercised: no recommendation existed on the account to apply.

        Returns
            ApiResponse
        """
        schema_version = 'application/vnd.applyRecommendationsRequest.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/recommendations/{}', method='PUT')
    def update_recommendation(self, recommendationId, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Updates a recommendation.

        path **recommendationId**:*string* | Required. The identifier of the recommendation.

        Request Body (required)
            | UpdateRecommendationRequest {
            | **ruleBasedBidding** UpdateRuleBasedBidding {
            |       Can only be updated for recommendations with recommendationType NEW_CAMPAIGN_BIDDING_RULE or CAMPAIGN_BIDDING_RULE.
            |       **recommendedRuleRoas**\* (number)
            |   }
            | **recommendedValue** (string) Recommended value of the recommendation. Type of data expected for each recommendation type:
            | **budgetRule** UpdateBudgetRule {
            |       **ruleDetails**\* UpdateBudgetRuleDetails {
            |           **duration** UpdateBudgetRuleDuration {
            |               **dateRangeTypeDuration** UpdateBudgetRuleDurationDateRange {
            |                   **endDate** (string): End date of the budget rule in YYYY-MM-DD format. The end date is inclusive.
            |           }
            |           **budgetIncreaseBy** BudgetRuleIncreaseBy {
            |               **value**\*(number): Budget of the rule.
            |           }
            |           **ruleName**\* (string): Name of the budget rule. Required to be unique within a campaign. minLength: 1 maxLength: 355
            |           **performanceMeasureCondition** BudgetRulePerformanceMeasureCondition {
            |               **threshold**\*(number): Threshold of the performance metric.
            |           }
            |       }
            |   }
            | }

        .. warning::

            This edits a recommendation before it is applied. Read one first with
            ``list_recommendations`` for the shape it expects, since the fields
            change with ``recommendationType``.

            Not exercised, for the same reason as ``apply_recommendations``.

        Returns
            ApiResponse


        """
        schema_version = 'application/vnd.updateRecommendationRequest.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(
            fill_query_params(kwargs.pop('path'), recommendationId),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )
