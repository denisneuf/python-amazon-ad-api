Campaign Optimization Rules
===========================

.. warning::

    Sponsored Product v3 is not available for Sandbox endpoint

.. note::

    This API is version 3.0

.. note::

    This API requires separated access from Amazon Advertising Support


.. code-block:: python

    {
    'code': 403,
    'message': 'Client does not have access to this API',
    'responseBody': None,
    'responseHeaders': None
    }

.. autoclass:: ad_api.api.sp.CampaignOptimization

    Endpoints available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/sp/rules/campaignOptimization/eligibility", "Gets a campaign optimization rule recommendation for SP campaigns."
        "GET", "/sp/rules/campaignOptimization/{campaignOptimizationId}", "Gets a campaign optimization rule specified by identifier."
        "DELETE", "/sp/rules/campaignOptimization/{campaignOptimizationId}", "Deletes a campaign optimization rule specified by identifier."
        "POST", "/sp/rules/campaignOptimization", "Creates a campaign optimization rule."
        "PUT", "/sp/rules/campaignOptimization", "Updates a campaign optimization rule."
        "POST", "/sp/rules/campaignOptimization/state", "Gets campaign optimization rule state. Recommended refresh frequency is once a day."


    .. autofunction:: ad_api.api.sp.CampaignOptimization.list_campaigns_optimization_eligibility(self, **kwargs) -> ApiResponse:

        .. code-block:: python

            {
              "campaignIds": [
                "string"
              ]
            }


    .. autofunction:: ad_api.api.sp.CampaignOptimization.get_budget_campaign_optimization(self, campaignOptimizationId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.CampaignOptimization.delete_budget_campaign_optimization(self, campaignOptimizationId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.CampaignOptimization.create_budget_campaign_optimization(self, **kwargs) -> ApiResponse:

        .. code-block:: python

            {
              "recurrence": "DAILY",
              "ruleAction": "ADOPT",
              "ruleCondition": [
                {
                  "metricName": "ROAS",
                  "comparisonOperator": "GREATER_THAN",
                  "threshold": "4"
                }
              ],
              "ruleType": "BID",
              "ruleName": "RuleROAS4",
              "campaignIds": [
                "123784",
                "1223785"
              ]
            }

    .. autofunction:: ad_api.api.sp.CampaignOptimization.edit_budget_campaign_optimization(self, **kwargs) -> ApiResponse:

        .. code-block:: python

            {
              "recurrence": "DAILY",
              "ruleAction": "ADOPT",
              "campaignOptimizationId": "10001",
              "ruleCondition": [
                {
                  "metricName": "ROAS",
                  "comparisonOperator": "GREATER_THAN",
                  "threshold": "7"
                }
              ],
              "ruleType": "BID",
              "ruleName": "RuleROAS4",
              "campaignIds": [
                "123784",
                "1223785"
              ]
            }

    .. autofunction:: ad_api.api.sp.CampaignOptimization.get_state_budget_campaign_optimization(self, **kwargs) -> ApiResponse:


