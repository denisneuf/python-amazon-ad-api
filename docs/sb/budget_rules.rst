Budget Rules
============

Sponsored Brands budget rules: the rules themselves, their association with
campaigns, budget usage and budget recommendations.

.. note::
    Ten of the eleven routes belong to the 4.0 contract. The eleventh,
    ``get_budget_rules_recommendation``, comes from 3.0 and is marked as such
    below.

.. autoclass:: ad_api.api.sb.BudgetRules

    .. autofunction:: ad_api.api.sb.BudgetRules.list_budget_rules(self, pageSize, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.BudgetRules.get_budget_rule(self, budgetRuleId, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.BudgetRules.list_rule_campaigns(self, budgetRuleId, pageSize, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.BudgetRules.list_campaign_rules(self, campaignId, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.BudgetRules.create_budget_rules(self, budgetRulesDetails, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.BudgetRules.update_budget_rules(self, budgetRulesDetails, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.BudgetRules.associate_budget_rules(self, campaignId, budgetRuleIds, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.BudgetRules.disassociate_budget_rule(self, campaignId, budgetRuleId, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.BudgetRules.get_budget_usage(self, campaignIds, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.BudgetRules.get_budget_recommendations(self, campaignIds, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.BudgetRules.get_budget_rules_recommendation(self, **kwargs) -> ApiResponse:

    ### Endpoint map

    ================================================================  ================================  ====================  ==========
    Path                                                              Method                            Media type            Contract
    ================================================================  ================================  ====================  ==========
    ``GET  /sb/budgetRules``                                          ``list_budget_rules``             ``application/json``  4.0
    ``GET  /sb/budgetRules/{budgetRuleId}``                           ``get_budget_rule``               ``application/json``  4.0
    ``GET  /sb/budgetRules/{budgetRuleId}/campaigns``                 ``list_rule_campaigns``           ``application/json``  4.0
    ``GET  /sb/campaigns/{campaignId}/budgetRules``                   ``list_campaign_rules``           ``application/json``  4.0
    ``POST /sb/budgetRules``                                          ``create_budget_rules``           ``application/json``  4.0
    ``PUT  /sb/budgetRules``                                          ``update_budget_rules``           ``application/json``  4.0
    ``POST /sb/campaigns/{campaignId}/budgetRules``                   ``associate_budget_rules``        ``application/json``  4.0
    ``DELETE /sb/campaigns/{campaignId}/budgetRules/{budgetRuleId}``  ``disassociate_budget_rule``      ``application/json``  4.0
    ``POST /sb/campaigns/budget/usage``                               ``get_budget_usage``              ``vnd.sbcampaignbudgetusage.v1``  4.0
    ``POST /sb/campaigns/budgetRecommendations``                      ``get_budget_recommendations``    ``vnd.sbbudgetrecommendation.v4`` 4.0
    ``POST /sb/campaigns/budgetRules/recommendations``                ``get_budget_rules_recommendation`` ``application/json``  3.0
    ================================================================  ================================  ====================  ==========

    ### What is verified

    The six read routes were probed against a live account:

    ============================================  ==========================================
    Route                                         Answer
    ============================================  ==========================================
    ``GET /sb/budgetRules``                       ``200``, rules under
                                                  ``budgetRulesForAdvertiserResponse``
    ``GET /sb/budgetRules/{id}``                  ``400`` ``InvalidParameterValue`` for an
                                                  unknown id, so the route lives
    ``GET /sb/budgetRules/{id}/campaigns``        same ``400`` for an unknown id
    ``GET /sb/campaigns/{id}/budgetRules``        ``200``, rules under ``associatedRules``
    ``POST /sb/campaigns/budget/usage``           ``200`` with real figures
    ``POST /sb/campaigns/budgetRecommendations``  ``400`` business message with the
                                                  versioned media type
    ============================================  ==========================================

    The five write routes are built from the contract and not exercised, because
    they change budget rules on live campaigns.

    ### Rules of the road

    .. warning::
        ``get_budget_recommendations`` only answers with
        ``application/vnd.sbbudgetrecommendation.v4+json``. With
        ``application/json`` the service answers ``404 Could not find resource``,
        which reads like a missing route but is only the wrong media type. Amazon
        routes on media type.

    .. note::
        An unknown ``budgetRuleId`` answers ``400`` with ``code``
        ``InvalidParameterValue`` and ``errorCode 240002``. The identifier is
        validated before it is looked up, so a bad id never produces a ``404``.

    ### Rule shape

    ``create_budget_rules`` takes a list under ``budgetRulesDetails``:

    .. code-block:: json

        {
            "budgetRulesDetails": [
                {
                    "name": "Weekend boost",
                    "ruleType": "SCHEDULE",
                    "budgetIncreaseBy": {"type": "PERCENT", "value": 0.25},
                    "recurrence": {
                        "type": "WEEKLY",
                        "daysOfWeek": ["SATURDAY", "SUNDAY"]
                    },
                    "duration": {
                        "dateRangeTypeRuleDuration": {"startDate": "2026-11-01"}
                    }
                }
            ]
        }

    A performance rule swaps the schedule for a condition:

    .. code-block:: json

        {
            "budgetRulesDetails": [
                {
                    "name": "Scale what works",
                    "ruleType": "PERFORMANCE",
                    "budgetIncreaseBy": {"type": "PERCENT", "value": 0.15},
                    "performanceMeasureCondition": {
                        "metricName": "ROAS",
                        "comparisonOperator": "GREATER_THAN",
                        "threshold": 3.0
                    }
                }
            ]
        }

    ``update_budget_rules`` takes the same list, each entry keyed by ``ruleId`` and
    carrying ``ruleState`` (``ACTIVE`` or ``PAUSED``).

    ### Enumerations

    ==============================  =========================================================
    Field                           Values
    ==============================  =========================================================
    ``ruleType``                    ``SCHEDULE``, ``PERFORMANCE``
    ``budgetIncreaseBy.type``       ``PERCENT`` (the only value today)
    ``performanceMeasureCondition.metricName``  ``IS``, ``NTB``, ``ROAS``
    ``comparisonOperator``          ``GREATER_THAN``, ``LESS_THAN``,
                                    ``LESS_THAN_OR_EQUAL_TO``, ``GREATER_THAN_OR_EQUAL_TO``
    ``recurrence.type``             ``DAILY``, ``WEEKLY``
    ``daysOfWeek``                  ``MONDAY`` … ``SUNDAY``
    ``ruleState``                   ``ACTIVE``, ``PAUSED``
    ==============================  =========================================================

    ### Example python

    .. code-block:: python

        from ad_api.api.sb import BudgetRules

        rules = BudgetRules(account='account_name', debug=False)

        # list, pageSize is required
        print(rules.list_budget_rules(pageSize=10).payload)

        # rules attached to one campaign
        print(rules.list_campaign_rules(campaignId='95988386496299').payload)

        # budget usage
        print(rules.get_budget_usage(campaignIds=['95988386496299']).payload)

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi
