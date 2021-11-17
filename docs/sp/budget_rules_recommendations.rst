Budget Rules Recommendations
============================

.. warning::

    Sponsored Product v3 is not available for Sandbox endpoint

.. note::

    This API is version 3.0



.. autoclass:: ad_api.api.sp.BudgetRulesRecommendations

    Endpoint available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/sp/campaigns/budgetRules/recommendations", "Gets a list of special events with suggested date range and suggested budget increase for a campaign specified by identifier."


    .. autofunction:: ad_api.api.sp.BudgetRulesRecommendations.list_campaigns_budget_rules_recommendations(self, **kwargs) -> ApiResponse:


