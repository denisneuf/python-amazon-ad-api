from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class BudgetRules(Client):
    """Sponsored Brands budget rules.

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi

    Read routes were probed against the live service; the write routes are built
    from the contract and not exercised, because they change campaign budgets.

    .. note::
        ``budget_recommendations`` only answers with the versioned media type.
        Sending ``application/json`` makes the router answer ``404 Could not find
        resource``, as if the route did not exist. Amazon routes on media type.

    .. note::
        An unknown ``budgetRuleId`` answers ``400 InvalidParameterValue`` with
        ``errorCode 240002``, not a 404. The identifier is validated before it is
        looked up.
    """

    _MEDIA_JSON = 'application/json'
    _MEDIA_USAGE = 'application/vnd.sbcampaignbudgetusage.v1+json'
    _MEDIA_RECS = 'application/vnd.sbbudgetrecommendation.v4+json'

    @sp_endpoint('/sb/budgetRules', method='GET')
    def list_budget_rules(self, pageSize, **kwargs) -> ApiResponse:
        """
        Gets the budget rules of the advertiser.

        Keyword Args
            | query **pageSize** (number): [required] Results per page.
            | query **nextToken** (string): Pagination token. [optional]

        Returns:
            | ApiResponse, with the rules under ``budgetRulesForAdvertiserResponse``
              and a ``nextToken``.
        """
        return self._request(kwargs.pop('path'), params=kwargs,
                             headers={'Accept': self._MEDIA_JSON})

    @sp_endpoint('/sb/budgetRules/{}', method='GET')
    def get_budget_rule(self, budgetRuleId, **kwargs) -> ApiResponse:
        """
        Gets one budget rule by identifier.

        Keyword Args
            | path **budgetRuleId** (string): [required]
        """
        return self._request(fill_query_params(kwargs.pop('path'), budgetRuleId),
                             params=kwargs, headers={'Accept': self._MEDIA_JSON})

    @sp_endpoint('/sb/budgetRules/{}/campaigns', method='GET')
    def list_rule_campaigns(self, budgetRuleId, pageSize, **kwargs) -> ApiResponse:
        """
        Gets the campaigns associated with a budget rule.

        Keyword Args
            | path **budgetRuleId** (string): [required]
            | query **pageSize** (number): [required]
            | query **nextToken** (string): [optional]
        """
        return self._request(fill_query_params(kwargs.pop('path'), budgetRuleId),
                             params=kwargs, headers={'Accept': self._MEDIA_JSON})

    @sp_endpoint('/sb/campaigns/{}/budgetRules', method='GET')
    def list_campaign_rules(self, campaignId, **kwargs) -> ApiResponse:
        """
        Gets the budget rules associated with a campaign.

        Keyword Args
            | path **campaignId** (number): [required]

        Returns:
            | ApiResponse, with the rules under ``associatedRules``.
        """
        return self._request(fill_query_params(kwargs.pop('path'), campaignId),
                             params=kwargs, headers={'Accept': self._MEDIA_JSON})

    @sp_endpoint('/sb/budgetRules', method='POST')
    def create_budget_rules(self, budgetRulesDetails, **kwargs) -> ApiResponse:
        """
        Creates budget rules.

        Request Body [Required]
            | **budgetRulesDetails** (array): One entry per rule.
                | **name** (string): Rule name.
                | **ruleType** (string): ``SCHEDULE`` or ``PERFORMANCE``.
                | **budgetIncreaseBy** ({}): ``type`` (``PERCENT``) and ``value``.
                | **performanceMeasureCondition** ({}): ``metricName`` (``IS``,
                  ``NTB`` or ``ROAS``), ``comparisonOperator`` (``GREATER_THAN``,
                  ``LESS_THAN``, ``LESS_THAN_OR_EQUAL_TO``,
                  ``GREATER_THAN_OR_EQUAL_TO``) and ``threshold``.
                | **duration** ({}): ``eventTypeRuleDuration`` with ``eventId``, or
                  ``dateRangeTypeRuleDuration`` with ``startDate``.
                | **recurrence** ({}): ``type`` (``DAILY`` or ``WEEKLY``),
                  ``daysOfWeek`` and ``intraDaySchedule``.

        Returns:
            | ApiResponse, status ``207``.

        .. note::
            Not probed: creates budget rules on the account.
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body({'budgetRulesDetails': budgetRulesDetails}, False),
                             params=kwargs, headers={'Accept': self._MEDIA_JSON,
                                                     'Content-Type': self._MEDIA_JSON})

    @sp_endpoint('/sb/budgetRules', method='PUT')
    def update_budget_rules(self, budgetRulesDetails, **kwargs) -> ApiResponse:
        """
        Updates budget rules.

        Request Body [Required]
            | **budgetRulesDetails** (array): Each entry needs ``ruleId`` and may
              carry ``ruleState`` (``ACTIVE`` or ``PAUSED``) and ``ruleDetails``
              with the same shape used on creation.

        Returns:
            | ApiResponse, status ``207``.

        .. note::
            Not probed: updates live budget rules.
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body({'budgetRulesDetails': budgetRulesDetails}, False),
                             params=kwargs, headers={'Accept': self._MEDIA_JSON,
                                                     'Content-Type': self._MEDIA_JSON})

    @sp_endpoint('/sb/campaigns/{}/budgetRules', method='POST')
    def associate_budget_rules(self, campaignId, budgetRuleIds, **kwargs) -> ApiResponse:
        """
        Associates budget rules with a campaign.

        Keyword Args
            | path **campaignId** (number): [required]

        Request Body [Required]
            | **budgetRuleIds** (array of string): [required]

        Returns:
            | ApiResponse, status ``207``.

        .. note::
            Not probed: changes which rules apply to a live campaign.
        """
        return self._request(fill_query_params(kwargs.pop('path'), campaignId),
                             data=Utils.convert_body({'budgetRuleIds': budgetRuleIds}, False),
                             params=kwargs, headers={'Accept': self._MEDIA_JSON,
                                                     'Content-Type': self._MEDIA_JSON})

    @sp_endpoint('/sb/campaigns/{}/budgetRules/{}', method='DELETE')
    def disassociate_budget_rule(self, campaignId, budgetRuleId, **kwargs) -> ApiResponse:
        """
        Disassociates one budget rule from a campaign.

        Keyword Args
            | path **campaignId** (number): [required]
            | path **budgetRuleId** (string): [required]

        Returns:
            | ApiResponse, status ``200``.

        .. note::
            Not probed: changes which rules apply to a live campaign.
        """
        path = fill_query_params(kwargs.pop('path'), campaignId)
        return self._request(fill_query_params(path, budgetRuleId),
                             params=kwargs, headers={'Accept': self._MEDIA_JSON})

    @sp_endpoint('/sb/campaigns/budget/usage', method='POST')
    def get_budget_usage(self, campaignIds, **kwargs) -> ApiResponse:
        """
        Gets budget usage for campaigns.

        Request Body [Required]
            | **campaignIds** (array of string): [required]

        Returns:
            | ApiResponse, with per-campaign entries under ``success`` and failures
              under ``error``. Each success entry carries ``budget``,
              ``budgetUsagePercent``, ``campaignId``, ``index`` and
              ``usageUpdatedTimestamp``.

        Example::

            {"success": [{"budget": 10.0, "budgetUsagePercent": 0.0,
                          "campaignId": "95988386496299", "index": 0,
                          "usageUpdatedTimestamp": "2026-10-25T00:00:00Z"}],
             "error": []}
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body({'campaignIds': campaignIds}, False),
                             params=kwargs, headers={'Accept': self._MEDIA_USAGE,
                                                     'Content-Type': self._MEDIA_USAGE})

    @sp_endpoint('/sb/campaigns/budgetRecommendations', method='POST')
    def get_budget_recommendations(self, campaignIds, **kwargs) -> ApiResponse:
        """
        Gets budget recommendations for campaigns.

        Request Body [Required]
            | **campaignIds** (array of string): [required]

        Returns:
            | ApiResponse, status ``207``.

        .. warning::
            This route only answers with its versioned media type. With
            ``application/json`` the service answers ``404 Could not find
            resource``, which reads like a missing route but is only the wrong
            media type.
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body({'campaignIds': campaignIds}, False),
                             params=kwargs, headers={'Accept': self._MEDIA_RECS,
                                                     'Content-Type': self._MEDIA_RECS})

    @sp_endpoint('/sb/campaigns/budgetRules/recommendations', method='POST')
    def get_budget_rules_recommendation(self, **kwargs) -> ApiResponse:
        """
        Gets budget rule recommendations.

        Returns:
            | ApiResponse

        .. note::
            Declared in the 3.0 contract, not in 4.0. Not probed.
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body(kwargs.pop('body', {}), False),
                             params=kwargs, headers={'Accept': self._MEDIA_JSON,
                                                     'Content-Type': self._MEDIA_JSON})
