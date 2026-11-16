from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class BudgetRulesRecommendations(Client):
    @sp_endpoint('/sp/campaigns/budgetRules/recommendations', method='POST')
    def list_campaigns_budget_rules_recommendations(self, version: int = 3, **kwargs) -> ApiResponse:
        r"""
        Gets a list of special events with suggested date range and suggested budget increase for a campaign specified by identifier.

        Request Body (required)
            | SPBudgetRulesRecommendationEventRequest {
            |       **campaignId**\* (string) The campaign identifier.
            | }
        Returns
            ApiResponse
        """
        contentType = 'application/vnd.spbudgetrulesrecommendation.v' + str(version) + '+json'
        headers = {'Content-Type': contentType, "Accept": contentType}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/sp/v1/events', method='POST')
    def list_rule_events(self, **kwargs) -> ApiResponse:
        r"""
        Gets every special event, individual and grouped, with the date range
        suggested for each one.

        A rule enables an automatic budget increase for a date range or for a
        special event; this route is what tells you which events exist and
        when, so a rule can point at one.

        The body is empty and, unusually for this resource, the content type is
        plain application/json rather than one of the application/vnd.sp...
        types.

        Returns:

            ApiResponse
            events and groupedEvents, each with its suggested date range.

        """
        json_version = 'application/json'

        headers = {"Accept": json_version, "Content-Type": json_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body', {}), False), params=kwargs, headers=headers)
