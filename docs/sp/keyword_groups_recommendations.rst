Keyword Group Targeting Recommendations
=======================================

.. list-table::
    :header-rows: 0
    :widths: 18 82

    * - **Vendor docs**
      - https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod
    * - **Specification**
      - https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json

Keyword Groups is a control for keyword-based campaigns: a collection of
keywords that reaches a relevant audience as one unit. Once a keyword group is
created, its performance shows up in the search terms report.

Send a list of ad ASINs and the route answers the groups worth creating, each
with a name, a description and a sample of the keywords inside it. The route is
in beta, as the contract states.

.. autoclass:: ad_api.api.sp.KeywordGroupsRecommendations
    :members:
