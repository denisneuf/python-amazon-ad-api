Campaign Negative Targeting Clauses
===================================

.. warning::

    Sponsored Product v3 is not available for Sandbox endpoint

.. list-table::
    :header-rows: 0
    :widths: 18 82

    * - **Vendor docs**
      - https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod
    * - **Specification**
      - https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json

.. note::

    This API is version 3.0

.. autoclass:: ad_api.api.sp.CampaignNegativeTargets
    :members:

    Endpoints available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "DELETE", "/sp/campaignNegativeTargets/delete", "Deletes Campaign Negative Targeting Clauses"
        "POST", "/sp/campaignNegativeTargets", "Create Campaign Negative Targeting Clauses"
        "PUT", "/sp/campaignNegativeTargets", "Updates Campaign Negative Targeting Clauses"
        "POST", "/sp/campaignNegativeTargets/list", "List Campaign Negative Targeting Clauses"
