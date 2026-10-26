Optimization Rules
==================

Sponsored Brands optimization rules: the rules themselves, their association with
entities, and optimization recommendations.

.. autoclass:: ad_api.api.sb.OptimizationRules
    :members:

    ### Endpoint map

    .. list-table::
        :header-rows: 1

       * - Path
         - Method
         - Media type
       * - ``POST /sb/rules/optimization/list``
         - ``list_optimization_rules``
         - ``vnd.sbruleoptimization.v4``
       * - ``POST /sb/recommendations/optimization``
         - ``get_optimization_recommendation``
         - ``vnd.sboptimizationrecommendationresource.v4``
       * - ``POST /sb/rules/optimization``
         - ``create_optimization_rules``
         - ``vnd.sbruleoptimization.v4``
       * - ``PUT  /sb/rules/optimization``
         - ``update_optimization_rules``
         - ``vnd.sbruleoptimization.v4``
       * - ``POST /sb/rules/optimization/associate``
         - ``associate_optimization_rules``
         - ``vnd.sbruleoptimization.v4``
       * - ``POST /sb/rules/optimization/disassociate``
         - ``disassociate_optimization_rules``
         - ``vnd.sbruleoptimization.v4``

    ### Media type, again

    .. warning::
        Every route in this family takes a versioned media type, and the service
        routes on it. With ``application/json`` the router answers ``404 Could not
        find resource``, which reads like a missing route but is only the wrong
        media type. Verified on ``list`` and ``recommendations``.

    This is the third family with the same behaviour, after
    :doc:`forecast` and :doc:`budget_rules`.

    ### What is verified

    .. list-table::
        :header-rows: 1

       * - Route
         - Answer
       * - ``POST /sb/rules/optimization/list``
         - ``200``, ``{"optimizationRules": [], "totalCount": 0}``
       * - ``POST /sb/recommendations/optimization``
         - ``400`` naming both required members, so the route lives

    The four write routes are built from the contract and not exercised, because
    they change optimization rules on live campaigns.

    ### Rule shape

    ``create_optimization_rules`` takes a list under ``optimizationRules``:

    .. code-block:: json

        {
            "optimizationRules": [
                {
                    "entityType": "CAMPAIGN",
                    "entityId": "95988386496299",
                    "conditions": [
                        {
                            "attributeName": "ROAS",
                            "criteria": {
                                "comparisonOperator": "LESS_THAN",
                                "value": 2.0
                            }
                        }
                    ]
                }
            ]
        }

    ``update_optimization_rules`` takes the same list, each entry keyed by
    ``optimizationRuleId`` instead of the entity pair:

    .. code-block:: json

        {
            "optimizationRules": [
                {
                    "optimizationRuleId": "RULE_ID",
                    "conditions": [
                        {"attributeName": "ROAS",
                         "criteria": {"comparisonOperator": "LESS_THAN", "value": 1.5}}
                    ]
                }
            ]
        }

    ### Association shape

    ``associate`` and ``disassociate`` take the same mapping list under different
    keys:

    .. code-block:: json

        {
            "optimizationRuleAssociations": [
                {"entityId": "95988386496299", "entityType": "CAMPAIGN",
                 "optimizationRuleId": "RULE_ID"}
            ]
        }

    ``disassociate_optimization_rules`` uses ``optimizationRuleDisassociations``.

    ### Listing shape

    .. code-block:: json

        {
            "entityFilter": {"entityType": "CAMPAIGN", "entityId": "95988386496299"},
            "optimizationRuleIdFilter": {"include": ["RULE_ID"]},
            "maxResults": 10,
            "nextToken": "string"
        }

    Every member is optional; an empty body lists everything.

    ### Recommendation shape

    Both members are required:

    .. code-block:: json

        {
            "costControlMetric": {},
            "landingPages": [
                {"pageType": "STORE", "url": "https://www.amazon.es/stores/page/XXXX"}
            ]
        }

    A ``landingPages`` entry carries ``pageType`` and either ``asins`` or ``url``.

    ### Example python

    .. code-block:: python

        from ad_api.api.sb import OptimizationRules

        rules = OptimizationRules(account='account_name', debug=False)

        # list everything
        print(rules.list_optimization_rules(body={}).payload)

        # list the rules of one campaign
        print(rules.list_optimization_rules(body={
            "entityFilter": {"entityType": "CAMPAIGN", "entityId": "95988386496299"}
        }).payload)

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi
