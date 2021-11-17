from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class BudgetRules(Client):

    @sp_endpoint('/sp/campaigns/{}/budgetRules/budgetHistory', method='GET')
    def get_budget_history(self, campaignId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), campaignId), params=kwargs)

    @sp_endpoint('/sp/budgetRules', method='POST')
    def create_budget_rules(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sp/budgetRules', method='GET')
    def list_budget_rules(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'),  params=kwargs)

    @sp_endpoint('/sp/budgetRules', method='PUT')
    def edit_budget_rules(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sp/budgetRules/{}', method='GET')
    def get_budget_rule(self, budgetRuleId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), budgetRuleId), params=kwargs)

    @sp_endpoint('/sp/budgetRules/{}/campaigns', method='GET')
    def get_campaigns_budget_rule(self, budgetRuleId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), budgetRuleId), params=kwargs)

    @sp_endpoint('/sp/campaigns/{}/budgetRules', method='POST')
    def create_campaign_budget_rules(self, campaignId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), campaignId), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sp/campaigns/{}/budgetRules', method='GET')
    def get_budget_rules_campaign(self, campaignId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), campaignId), params=kwargs)

    @sp_endpoint('/sp/campaigns/{}/budgetRules/{}', method='DELETE')
    def delete_budget_rule_campaign(self, campaignId, budgetRuleId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), campaignId, budgetRuleId), params=kwargs)
