Budget Rules
============

.. warning::

    Sponsored Product v3 is not available for Sandbox endpoint

.. note::

    This API is version 3.0

.. autoclass:: ad_api.api.sp.BudgetRules

    Endpoints available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "GET", "/sp/campaigns/{campaignId}/budgetRules/budgetHistory", "Gets the budget history for a campaign specified by identifier."
        "POST", "/sp/budgetRules", "Creates one or more budget rules."
        "GET", "/sp/budgetRules", "Get all budget rules created by an advertiser"
        "PUT", "/sp/budgetRules", "Updates one or more budget rules."
        "GET", "/sp/budgetRules/{budgetRuleId}", "Gets a budget rule specified by identifier."
        "GET", "/sp/budgetRules/{budgetRuleId}/campaigns", "Gets all the campaigns associated with a budget rule"
        "POST", "/sp/campaigns/{campaignId}/budgetRules", "Associates one or more budget rules to a campaign specified by identifer."
        "GET", "/sp/campaigns/{campaignId}/budgetRules", "Gets a list of budget rules associated to a campaign specified by identifier."
        "DELETE", "/sp/campaigns/{campaignId}/budgetRules/{budgetRuleId}", "Disassociates a budget rule specified by identifier from a campaign specified by identifier."

    .. autofunction:: ad_api.api.sp.BudgetRules.get_budget_history(self, campaignId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.BudgetRules.create_budget_rules(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.BudgetRules.list_budget_rules(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.BudgetRules.edit_budget_rules(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.BudgetRules.get_budget_rule(self, budgetRuleId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.BudgetRules.get_campaigns_budget_rule(self, budgetRuleId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.BudgetRules.create_campaign_budget_rules(self, campaignId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.BudgetRules.get_budget_rules_campaign(self, campaignId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.BudgetRules.delete_budget_rule_campaign(self, campaignId, budgetRuleId, **kwargs) -> ApiResponse:




