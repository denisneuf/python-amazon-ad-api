PortfoliosV3
============

`https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Portfolios_prod_3p.json`_

.. _https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Portfolios_prod_3p.json: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Portfolios_prod_3p.json

Manage portfolios that group together campaigns.

.. warning::

    This replaces :doc:`portfolios`. The version 2 routes answer
    ``404 Method Not Found`` and cannot be reached any more.

.. autoclass:: ad_api.api.PortfoliosV3
    :members:

    .. note::

        This API **Portfolios** can be used as sandbox environment for testing

    ### Endpoint map

    .. list-table::
        :header-rows: 1

       * - Path
         - Method
         - Media type
         - Answer
       * - ``POST /portfolios/list``
         - ``list_portfolios``
         - ``vnd.spPortfolio.v3``
         - ``200``
       * - ``POST /portfolios``
         - ``create_portfolios``
         - ``vnd.spPortfolio.v3``
         - ``207``
       * - ``PUT /portfolios``
         - ``edit_portfolios``
         - ``vnd.spPortfolio.v3``
         - ``207``
       * - ``POST /portfolios/budget/usage``
         - ``get_budget_usage_for_portfolios``
         - ``vnd.portfoliobudgetusage.v1``
         - ``207``

    ### What changed from version 2

    .. list-table::
        :header-rows: 1

       * - Version 2
         - Version 3
       * - ``GET /v2/portfolios``
         - ``POST /portfolios/list`` with a filter body
       * - ``GET /v2/portfolios/extended``
         - ``POST /portfolios/list`` with ``includeExtendedDataFields``
       * - ``GET /v2/portfolios/{id}``
         - ``POST /portfolios/list`` with ``portfolioIdFilter``
       * - Filters as comma separated query strings
         - Objects carrying an ``include`` array
       * - ``policy: "dateRange"``
         - ``policy: "DATE_RANGE"``
       * - ``state: "enabled"``
         - ``state: "ENABLED"``
       * - ``startDate: "20220418"``
         - ISO 8601, such as ``2022-04-18``
       * - The answer was a bare list
         - ``{"portfolios": [...], "totalResults": n, "nextToken": ...}``
       * - Writes answered ``200``
         - Writes answer ``207``, a multi-status

    The last row matters when reading a response. A write that succeeds still
    answers ``207`` with the created or updated portfolios in ``success``, and
    the ones that failed in ``error``, each keyed by the ``index`` it held in the
    request body.

    ### list_portfolios body

    Every member is optional. An empty object lists the first page.

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Meaning
       * - ``portfolioIdFilter``
         - object
         - Narrow to those ids. Carries ``include``, a list of portfolio ids.
       * - ``nameFilter``
         - object
         - Narrow by name. Carries ``include``, a list of names, and
           ``queryTermMatchType``, either ``BROAD_MATCH`` or ``EXACT_MATCH``.
       * - ``stateFilter``
         - object
         - Narrow by state. Carries ``include``, a list of states.
       * - ``includeExtendedDataFields``
         - boolean
         - Also return ``creationDateTime``, ``lastUpdateDateTime``,
           ``servingStatus`` and ``statusReasons``.
       * - ``nextToken``
         - string
         - Pagination token taken from a previous answer.

    ### create_portfolios body

    ``portfolios`` is required and holds a list. Each portfolio carries:

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Meaning
       * - ``name``
         - string
         - Required. The portfolio name.
       * - ``state``
         - string
         - Required. The contract lists ``ENABLED`` as the only value.
       * - ``budget.amount``
         - number
         - The budget amount.
       * - ``budget.currencyCode``
         - string
         - Required in practice. One of ``AED``, ``AUD``, ``BRL``, ``CAD``,
           ``CLP``, ``CNY``, ``COP``, ``EGP``, ``EUR``, ``GBP``, ``INR``,
           ``JPY``, ``MXN``, ``NGN``, ``PLN``, ``SAR``, ``SEK``, ``SGD``,
           ``TRY``, ``USD``, ``ZAR``.
       * - ``budget.policy``
         - string
         - ``DATE_RANGE``, ``MONTHLY_RECURRING``, ``NO_CAP`` or ``OTHER``.
       * - ``budget.startDate``
         - string
         - ISO 8601. Required when the policy is ``DATE_RANGE``.
       * - ``budget.endDate``
         - string
         - ISO 8601. Optional under either policy.
       * - ``budgetControls.campaignUnspentBudgetSharing.featureState``
         - string
         - ``ENABLED`` or ``DISABLED``, for sharing unspent campaign budget.

    ### edit_portfolios body

    The same members as above, plus ``portfolioId``, which is required. Only
    ``portfolioId`` is mandatory; the rest updates what it names.

    ### get_budget_usage_for_portfolios body

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Meaning
       * - ``portfolioIds``
         - array
         - The portfolios to measure.

    The answer splits into ``success`` and ``error``. A successful entry holds
    ``portfolioId``, ``index``, ``budget``, ``budgetUsagePercent`` and
    ``usageUpdatedTimestamp``.

    ### Example listing portfolios

    .. code-block:: python

        from ad_api.api import PortfoliosV3

        client = PortfoliosV3(account='my_account', debug=False)

        res = client.list_portfolios(body={"stateFilter": {"include": ["ENABLED"]}})
        print(res.payload)

    ### Example creating a portfolio

    .. code-block:: python

        from ad_api.api import PortfoliosV3

        client = PortfoliosV3(account='my_account', debug=False)

        res = client.create_portfolios(body={"portfolios": [
            {
                "name": "Apple",
                "state": "ENABLED",
                "budget": {
                    "amount": 100,
                    "currencyCode": "EUR",
                    "policy": "MONTHLY_RECURRING",
                    "startDate": "2022-04-18"
                }
            }
        ]})
        print(res.payload)

    ### Example reading budget usage

    .. code-block:: python

        from ad_api.api import PortfoliosV3

        client = PortfoliosV3(account='my_account', debug=False)

        res = client.get_budget_usage_for_portfolios(
            body={"portfolioIds": ["123456789012345"]})
        print(res.payload)

    ### Status codes

    .. list-table::
        :header-rows: 1

       * - Status
         - Meaning
       * - ``200``
         - ``list_portfolios`` answered. The other routes do not use it.
       * - ``207``
         - Multi-status, the success code for the three write routes. Read
           ``success`` and ``error``, not the status alone.
       * - ``400``
         - Bad request. The body names the member that failed.
       * - ``401``
         - Unauthorized.
       * - ``403``
         - Access denied.
       * - ``415``
         - Unsupported media type. The versioned type is what routes the call.
       * - ``429``
         - Throttled. Retry later.
       * - ``500``
         - Internal failure.

    ### What the contract leaves unsaid

    The schema pairs ``policy`` with an ``amount`` but never says which policies
    need one. Reading twenty portfolios on a live account settles it:

    .. list-table::
        :header-rows: 1

       * - Policy
         - ``amount`` in the answer
       * - ``NO_CAP``
         - Absent. Nineteen of twenty portfolios carried only ``currencyCode``
           and ``policy`` under ``budget``.
       * - ``DATE_RANGE``
         - Present. The one such portfolio answered ``10.0``.

    So ``NO_CAP`` means no ceiling and no figure. ``currencyCode`` stays, because
    it still describes the account's money.
