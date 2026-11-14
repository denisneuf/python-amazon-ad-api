Portfolios
==========

Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json
Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-portfolios

A portfolio groups campaigns under one name, one budget and one set of
marketplace rules. The v1 family is the successor to :doc:`../portfoliosV3`:
that one lives outside ``/adsApi/v1/`` and keeps its own contract, while this
one shares the v1 merged contract with the campaign resources.

Three routes exist, all POST. There is no GET on a path and no DELETE:

    POST /adsApi/v1/create/portfolios
    POST /adsApi/v1/query/portfolios
    POST /adsApi/v1/update/portfolios

Budget sharing
--------------

``budgetControls.campaignBudgetSharing.shareUnspentCampaignBudget``, with
values ``ENABLED`` or ``DISABLED``, lets the campaigns of the portfolio spend
the budget the other campaigns did not use. Without it each campaign is capped
on its own.

Global and per marketplace
--------------------------

A portfolio is either ``GLOBAL``, covering every marketplace listed in
``marketplaces``, or ``SINGLE_MARKETPLACE``. A global portfolio can override
``budgetControls``, ``startDateTime``, ``endDateTime`` and ``state`` for one
marketplace through ``marketplaceConfigurations``, up to 30 overrides. What is
not overridden carries the global value.

Archiving instead of deleting
-----------------------------

There is no delete route. A portfolio is retired by updating ``state`` to
``ARCHIVED``, which is terminal and cannot be reverted.

.. warning::

    Create and update answer ``207 MultiStatus``, not ``200``. A batch can
    create some portfolios and reject others, so ``success`` and ``error``
    are indexed together and both have to be read. These routes write into
    the account; they were not probed against a live account.

.. autoclass:: ad_api.api.v1.Portfolios
    :members:

    ### Endpoint map

    .. list-table::
        :header-rows: 1

       * - Path
         - Method
         - Operation
       * - ``/adsApi/v1/create/portfolios``
         - POST
         - CreatePortfolio
       * - ``/adsApi/v1/query/portfolios``
         - POST
         - QueryPortfolio
       * - ``/adsApi/v1/update/portfolios``
         - POST
         - UpdatePortfolio

    ### Example python

    .. code-block:: python

        from ad_api.api.v1 import Portfolios

        api = Portfolios(account=store)

        result = api.query_portfolios(body={"maxResults": 10})

        for portfolio in result.payload.get("portfolios", []):
            print(portfolio["portfolioId"], portfolio["name"], portfolio["state"])

    Reading the 207 of a write:

    .. code-block:: python

        result = api.create_portfolios(body={"portfolios": [
            {"name": "Q4", "state": "ENABLED", "marketplaceScope": "GLOBAL",
             "marketplaces": ["ES", "FR"],
             "budget": {"budgetType": "MONETARY",
                        "budgetValue": {"monetaryBudget": {"value": 100.0}},
                        "recurrenceTimePeriod": "DAILY"},
             "budgetControls": {"campaignBudgetSharing":
                                {"shareUnspentCampaignBudget": "ENABLED"}}}
        ]})

        payload = result.payload
        print(payload.get("success"), payload.get("error"))
