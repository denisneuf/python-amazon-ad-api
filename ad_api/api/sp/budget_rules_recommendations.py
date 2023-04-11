from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils

class BudgetRulesRecommendations(Client):

    @sp_endpoint('/sp/campaigns/budgetRules/recommendations', method='POST')
    def list_campaigns_budget_rules_recommendations(self, **kwargs) -> ApiResponse:
        contentType = 'application/vnd.spbudgetrulesrecommendation.v3+json'
        headers = {'Content-Type': contentType, "Accept": contentType}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
