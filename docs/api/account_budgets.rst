Account Budgets
===============
`https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Advertisers_prod_3p.json`_

.. _https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Advertisers_prod_3p.json: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Advertisers_prod_3p.json

The budget settings an account holds at account level, above any single
campaign.

.. autoclass:: ad_api.api.AccountBudgets
    :members:

    .. note::

        The contract is ``Advertisers`` version 3.0, the smallest this package
        reads at about six kilobytes. It carries two routes, both on the same
        path, and one setting behind them.

    ### Endpoint map

    .. list-table::
        :header-rows: 1

       * - Path
         - Method
         - Kind
         - Answer
       * - ``GET /accountBudgets/featureFlags``
         - ``get_feature_flags``
         - read
         - ``200``
       * - ``POST /accountBudgets/featureFlags``
         - ``update_feature_flags``
         - write
         - ``200``

    Both use ``application/vnd.accountBudgetFeatureFlags.v1+json``.

    ### The only setting

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Meaning
       * - ``isOptedOutForAverageDailyBudgetIncrease``
         - boolean
         - At ``true`` the account has opted out and the service will not raise a
           campaign's daily budget on its own. At ``false`` it may.

    That is the whole of it. This route does not read a budget amount, a spend
    or a usage figure; it reads whether Amazon is allowed to increase daily
    budgets by itself.

    ### The answer to a write is not the new state

    ``update_feature_flags`` answers with ``code`` and ``details``:

    .. list-table::
        :header-rows: 1

       * - Code
         - Meaning
       * - ``OK``
         - The change landed.
       * - ``ENTRY_NOT_FOUND``
         - There was no entry to change.
       * - ``INVALID_PARAMETER_VALUE``
         - A value was refused.

    A ``200`` carrying something other than ``OK`` means the change did not
    happen. Read the flags again with ``get_feature_flags`` rather than trusting
    the status.

    ### What turning this off means

    With the flag at ``false``, the service may lift a campaign's daily budget on
    its own. Spend follows the budget, so a lifted budget is a lifted spend. The
    route exists so an account can refuse that, and an account that has refused
    will show ``true`` here.

    ### Example: read the setting

    .. code-block:: python

        from ad_api.api import AccountBudgets

        client = AccountBudgets(account='my_account', debug=False)

        res = client.get_feature_flags()
        flags = res.payload["featureFlags"]
        print(flags["isOptedOutForAverageDailyBudgetIncrease"])

    ### Example: opt out

    This changes the account. Read the value first, and read it again after to
    confirm the change landed.

    .. code-block:: python

        from ad_api.api import AccountBudgets

        client = AccountBudgets(account='my_account', debug=False)

        res = client.update_feature_flags(body={
            "featureFlags": {
                "isOptedOutForAverageDailyBudgetIncrease": True,
            },
        })

        print(res.payload)   # {"code": "OK", "details": "..."}

    The write was not exercised here: the setting belongs to the account holder.
