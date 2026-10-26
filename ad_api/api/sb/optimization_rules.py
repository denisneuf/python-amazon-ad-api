from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class OptimizationRules(Client):
    """Sponsored Brands optimization rules.

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi

    Every route in this family takes a versioned media type on the way in, and the
    service routes on it:

    .. warning::
        With ``application/json`` the router answers ``404 Could not find
        resource`` on every route here, which reads like a missing route but is
        only the wrong media type. Verified on ``list`` and ``recommendations``.

    The two read routes were probed against a live account; the four write routes
    are built from the contract and not exercised.
    """

    _MEDIA_RULES = 'application/vnd.sbruleoptimization.v4+json'
    _MEDIA_RECS = 'application/vnd.sboptimizationrecommendationresource.v4+json'

    @sp_endpoint('/sb/rules/optimization/list', method='POST')
    def list_optimization_rules(self, **kwargs) -> ApiResponse:
        """
        Lists optimization rules.

        Request Body [Optional]
            | **entityFilter** ({}): ``entityType`` and ``entityId``.
            | **optimizationRuleIdFilter** ({}): ``include``, a list of rule ids.
            | **maxResults** (number): Page size.
            | **nextToken** (string): Pagination token.

        Returns:
            | ApiResponse, ``200``, with ``optimizationRules`` and ``totalCount``.

        Example::

            {"optimizationRules": [], "totalCount": 0}
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body(kwargs.pop('body', {}), False),
                             params=kwargs, headers={'Accept': self._MEDIA_RULES,
                                                     'Content-Type': self._MEDIA_RULES})

    @sp_endpoint('/sb/recommendations/optimization', method='POST')
    def get_optimization_recommendation(self, costControlMetric, landingPages, **kwargs) -> ApiResponse:
        """
        Gets an optimization rule recommendation.

        Request Body [Required]
            | **costControlMetric** ({}): [required] Cost control metric.
            | **landingPages** (array): [required] Each entry carries ``pageType``
              and either ``asins`` or ``url``.

        Returns:
            | ApiResponse, status ``207``.

        .. note::
            An empty body answers ``400`` with both members named:
            *"Value null at 'costControlMetric' failed to satisfy constraint"*.
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body({'costControlMetric': costControlMetric,
                                                      'landingPages': landingPages}, False),
                             params=kwargs, headers={'Accept': self._MEDIA_RECS,
                                                     'Content-Type': self._MEDIA_RECS})

    @sp_endpoint('/sb/rules/optimization', method='POST')
    def create_optimization_rules(self, optimizationRules, **kwargs) -> ApiResponse:
        """
        Creates optimization rules.

        Request Body [Required]
            | **optimizationRules** (array): [required]
                | **entityType** (string): Type of the entity the rule applies to.
                | **entityId** (string): Identifier of that entity.
                | **conditions** (array): Each entry needs ``attributeName`` and
                  ``criteria`` with ``comparisonOperator`` and ``value``.

        Returns:
            | ApiResponse, status ``207``.

        .. note::
            Not probed: creates optimization rules on the account.
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body({'optimizationRules': optimizationRules}, False),
                             params=kwargs, headers={'Accept': self._MEDIA_RULES,
                                                     'Content-Type': self._MEDIA_RULES})

    @sp_endpoint('/sb/rules/optimization', method='PUT')
    def update_optimization_rules(self, optimizationRules, **kwargs) -> ApiResponse:
        """
        Updates optimization rules.

        Request Body [Required]
            | **optimizationRules** (array): [required] Each entry needs
              ``optimizationRuleId`` and ``conditions``.

        Returns:
            | ApiResponse, status ``207``.

        .. note::
            Not probed: updates live optimization rules.
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body({'optimizationRules': optimizationRules}, False),
                             params=kwargs, headers={'Accept': self._MEDIA_RULES,
                                                     'Content-Type': self._MEDIA_RULES})

    @sp_endpoint('/sb/rules/optimization/associate', method='POST')
    def associate_optimization_rules(self, optimizationRuleAssociations, **kwargs) -> ApiResponse:
        """
        Associates optimization rules with entities.

        Request Body [Required]
            | **optimizationRuleAssociations** (array): [required] Each entry needs
              ``entityId``, ``entityType`` and ``optimizationRuleId``.

        Returns:
            | ApiResponse, status ``207``.

        .. note::
            Not probed: changes which rules apply to live campaigns.
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body(
                                 {'optimizationRuleAssociations': optimizationRuleAssociations}, False),
                             params=kwargs, headers={'Accept': self._MEDIA_RULES,
                                                     'Content-Type': self._MEDIA_RULES})

    @sp_endpoint('/sb/rules/optimization/disassociate', method='POST')
    def disassociate_optimization_rules(self, optimizationRuleDisassociations, **kwargs) -> ApiResponse:
        """
        Disassociates optimization rules from entities.

        Request Body [Required]
            | **optimizationRuleDisassociations** (array): [required] Each entry
              needs ``entityId``, ``entityType`` and ``optimizationRuleId``.

        Returns:
            | ApiResponse, status ``207``.

        .. note::
            Not probed: changes which rules apply to live campaigns.
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body(
                                 {'optimizationRuleDisassociations': optimizationRuleDisassociations}, False),
                             params=kwargs, headers={'Accept': self._MEDIA_RULES,
                                                     'Content-Type': self._MEDIA_RULES})
