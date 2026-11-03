Budget Rules
============

Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi

Specification: https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-display/3-0/openapi.yaml

.. autoclass:: ad_api.api.sd.BudgetRules
    :members:

    Endpoints available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "GET", "/sd/campaigns/{campaignId}/budgetRules/budgetHistory", "Gets the budget history for a campaign specified by identifier. Not in the 3.0 contract; answers 403 IncompleteSignatureException, so it expects an AWS SigV4 signature rather than the bearer token this client sends."
        "POST", "/sd/budgetRules", "Creates one or more budget rules."
        "GET", "/sd/budgetRules", "Get all budget rules created by an advertiser"
        "PUT", "/sd/budgetRules", "Updates one or more budget rules."
        "GET", "/sd/budgetRules/{budgetRuleId}", "Gets a budget rule specified by identifier."
        "GET", "/sd/budgetRules/{budgetRuleId}/campaigns", "Gets all the campaigns associated with a budget rule"
        "POST", "/sd/campaigns/{campaignId}/budgetRules", "Associates one or more budget rules to a campaign specified by identifer."
        "GET", "/sd/campaigns/{campaignId}/budgetRules", "Gets a list of budget rules associated to a campaign specified by identifier."
        "DELETE", "/sd/campaigns/{campaignId}/budgetRules/{budgetRuleId}", "Disassociates a budget rule specified by identifier from a campaign specified by identifier."
