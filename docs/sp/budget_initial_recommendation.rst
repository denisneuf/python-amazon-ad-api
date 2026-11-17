Initial Budget Recommendation
=============================

.. list-table::
    :header-rows: 0
    :widths: 18 82

    * - **Vendor docs**
      - https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod
    * - **Specification**
      - https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json

Returns a suggested daily budget, with benchmark metrics, for a campaign that
has not been created yet. Nothing is created and nothing is charged.

The path carries a capital B, ``initialBudgetRecommendation``. Spelled in lower
case the gateway does not recognise the route and answers 403
``IncompleteSignatureException`` instead of 200, so the case matters here.

Two fields the contract does not declare are required by the service:
``targetingExpressions[].bid`` cannot be null, and ``value`` has to be empty
when ``targetingType`` is ``auto``.

.. autoclass:: ad_api.api.sp.InitialBudgetRecommendation
    :members:
