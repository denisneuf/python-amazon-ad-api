from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class BudgetRulesRecommendations(Client):

    @sp_endpoint('/sp/campaigns/budgetRules/recommendations', method='POST')
    def list_campaigns_budget_rules_recommendations(self, **kwargs) -> ApiResponse:
        contentType = 'application/vnd.spbudgetrulesrecommendation.v3+json'
        headers = {'Content-Type': contentType}
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs, headers=headers)
        # return self._request(fill_query_params(kwargs.pop('path')), data=kwargs.pop('body'), params=kwargs)

