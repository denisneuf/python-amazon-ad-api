from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class PortfoliosV3(Client):
    """ """

    @sp_endpoint('/portfolios/list', method='POST')
    def list_portfolios(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
        r"""
        Lists portfolios. Replaces the retired ``GET /v2/portfolios``.

        Keyword Args

        - ``prefer`` (bool): send ``Prefer: return=representation`` so the answer
          carries the full portfolio objects rather than only the ids. [optional]

        Request Body (optional)

        - ``portfolioIdFilter`` (object): narrow to those ids. Carries
          ``include``, a list of portfolio ids.
        - ``nameFilter`` (object): narrow by name. Carries ``include``, a list of
          names, and ``queryTermMatchType``, ``BROAD_MATCH`` or ``EXACT_MATCH``.
        - ``stateFilter`` (object): narrow by state. Carries ``include``, a list
          of states.
        - ``includeExtendedDataFields`` (boolean): also return
          ``creationDateTime``, ``lastUpdateDateTime``, ``servingStatus`` and
          ``statusReasons``.
        - ``nextToken`` (string): pagination token from a previous answer.

        Returns
            ApiResponse with ``portfolios``, ``totalResults`` and ``nextToken``.
            Answers ``200``.

        """

        schema_version = 'application/vnd.spPortfolio.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        prefer_value = 'return=representation'
        if prefer:
            headers.update({"Prefer": prefer_value})

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)



    @sp_endpoint('/portfolios', method='POST')
    def create_portfolios(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
        r"""
        Creates portfolios.

        Keyword Args

        - ``prefer`` (bool): send ``Prefer: return=representation`` so the answer
          carries the created portfolio objects rather than only the ids.
          [optional]

        Request Body (required)

        - ``portfolios`` (array): the portfolios to create.

          Each one carries:

          - ``name`` (string): required. The portfolio name.
          - ``state`` (string): required. The contract lists ``ENABLED`` as the
            only value.
          - ``budget.amount`` (number): the budget amount. Absent when the policy
            is ``NO_CAP``.
          - ``budget.currencyCode`` (string): one of ``AED``, ``AUD``, ``BRL``,
            ``CAD``, ``CLP``, ``CNY``, ``COP``, ``EGP``, ``EUR``, ``GBP``,
            ``INR``, ``JPY``, ``MXN``, ``NGN``, ``PLN``, ``SAR``, ``SEK``,
            ``SGD``, ``TRY``, ``USD``, ``ZAR``.
          - ``budget.policy`` (string): ``DATE_RANGE``, ``MONTHLY_RECURRING``,
            ``NO_CAP`` or ``OTHER``.
          - ``budget.startDate`` (string): ISO 8601. Required when the policy is
            ``DATE_RANGE``.
          - ``budget.endDate`` (string): ISO 8601. Optional under either policy.
          - ``budgetControls.campaignUnspentBudgetSharing.featureState``
            (string): ``ENABLED`` or ``DISABLED``.

        Returns
            ApiResponse with ``success`` and ``error`` lists, each item keyed by
            the ``index`` it held in the body. Answers ``207``, a multi-status,
            not ``200``.

        """
        schema_version = 'application/vnd.spPortfolio.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        prefer_value = 'return=representation'
        if prefer:
            headers.update({"Prefer": prefer_value})

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/portfolios', method='PUT')
    def edit_portfolios(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
        r"""
        Updates portfolios.

        Keyword Args

        - ``prefer`` (bool): send ``Prefer: return=representation`` so the answer
          carries the updated portfolio objects rather than only the ids.
          [optional]

        Request Body (required)

        - ``portfolios`` (array): the portfolios to update.

          Each one carries ``portfolioId``, which is required, plus any of the
          members ``create_portfolios`` accepts. Only what is sent is changed:

          - ``portfolioId`` (string): required. The portfolio to update.
          - ``name`` (string): the portfolio name.
          - ``state`` (string): ``ENABLED``.
          - ``budget.amount``, ``budget.currencyCode``, ``budget.policy``,
            ``budget.startDate`` and ``budget.endDate`` as above.
          - ``budgetControls.campaignUnspentBudgetSharing.featureState`` as above.

        Returns
            ApiResponse with ``success`` and ``error`` lists, each item keyed by
            the ``index`` it held in the body. Answers ``207``, a multi-status,
            not ``200``.

        """
        schema_version = 'application/vnd.spPortfolio.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        prefer_value = 'return=representation'
        if prefer:
            headers.update({"Prefer": prefer_value})

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @sp_endpoint('/portfolios/budget/usage', method='POST')
    def get_budget_usage_for_portfolios(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Reports how much of each portfolio budget has been spent.

        Request Body (required)

        - ``portfolioIds`` (array): the portfolios to measure.

        Returns
            ApiResponse split into ``success`` and ``error``. A successful entry
            carries ``portfolioId``, ``index``, ``budget``,
            ``budgetUsagePercent`` and ``usageUpdatedTimestamp``. Answers
            ``207``, a multi-status, not ``200``.

        """
        schema_version = 'application/vnd.portfoliobudgetusage.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)