from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class CampaignOptimization(Client):
    """
    Sponsored Products Targeting API.

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod#/

    Specification: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json

    """

    @sp_endpoint('/sp/rules/campaignOptimization/eligibility', method='POST')
    def list_campaigns_optimization_eligibility(self, **kwargs) -> ApiResponse:
        contentType = 'application/vnd.optimizationrules.v1+json'
        headers = {'Content-Type': contentType}
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs, headers=headers)

    @sp_endpoint('/sp/rules/campaignOptimization/{}', method='GET')
    def get_budget_campaign_optimization(self, campaignOptimizationId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), campaignOptimizationId), params=kwargs)

    @sp_endpoint('/sp/rules/campaignOptimization/{}', method='DELETE')
    def delete_budget_campaign_optimization(self, campaignOptimizationId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), campaignOptimizationId), params=kwargs)

    @sp_endpoint('/sp/rules/campaignOptimization', method='POST')
    def create_budget_campaign_optimization(self, **kwargs) -> ApiResponse:
        contentType = 'application/vnd.optimizationrules.v1+json'
        headers = {'Content-Type': contentType}
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs, headers=headers)

    @sp_endpoint('/sp/rules/campaignOptimization', method='PUT')
    def edit_budget_campaign_optimization(self, **kwargs) -> ApiResponse:
        contentType = 'application/vnd.optimizationrules.v1+json'
        headers = {'Content-Type': contentType}
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs, headers=headers)

    @sp_endpoint('/sp/rules/campaignOptimization/state', method='POST')
    def get_state_budget_campaign_optimization(self, **kwargs) -> ApiResponse:
        contentType = 'application/vnd.optimizationrules.v1+json'
        headers = {'Content-Type': contentType}
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs, headers=headers)
