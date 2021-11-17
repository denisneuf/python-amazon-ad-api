from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class BudgetRecommendations(Client):

    @sp_endpoint('/sp/campaigns/budgetRecommendations', method='POST')
    def list_campaigns_budget_recommendations(self, **kwargs) -> ApiResponse:
        contentType = 'application/vnd.budgetrecommendation.v3+json'
        headers = {'Content-Type': contentType}
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs, headers=headers)
        # return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

