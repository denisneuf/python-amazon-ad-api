Budget Rules
============

.. autoclass:: ad_api.api.sd.BudgetRules

    Endpoints available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "GET", "/sd/campaigns/{campaignId}/budgetRules/budgetHistory", "Gets the budget history for a campaign specified by identifier."
        "POST", "/sd/budgetRules", "Creates one or more budget rules."
        "GET", "/sd/budgetRules", "Get all budget rules created by an advertiser"
        "PUT", "/sd/budgetRules", "Updates one or more budget rules."
        "GET", "/sd/budgetRules/{budgetRuleId}", "Gets a budget rule specified by identifier."
        "GET", "/sd/budgetRules/{budgetRuleId}/campaigns", "Gets all the campaigns associated with a budget rule"
        "POST", "/sd/campaigns/{campaignId}/budgetRules", "Associates one or more budget rules to a campaign specified by identifer."
        "GET", "/sd/campaigns/{campaignId}/budgetRules", "Gets a list of budget rules associated to a campaign specified by identifier."
        "DELETE", "/sd/campaigns/{campaignId}/budgetRules/{budgetRuleId}", "Disassociates a budget rule specified by identifier from a campaign specified by identifier."

    .. autofunction:: ad_api.api.sd.BudgetRules.get_budget_history(self, campaignId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sd.BudgetRules.create_budget_rules(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sd.BudgetRules.list_budget_rules(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sd.BudgetRules.edit_budget_rules(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sd.BudgetRules.get_budget_rule(self, budgetRuleId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sd.BudgetRules.get_campaigns_budget_rule(self, budgetRuleId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sd.BudgetRules.create_campaign_budget_rules(self, campaignId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sd.BudgetRules.get_budget_rules_campaign(self, campaignId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sd.BudgetRules.delete_budget_rule_campaign(self, campaignId, budgetRuleId, **kwargs) -> ApiResponse:




