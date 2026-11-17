Campaign Negative Keywords
==========================

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

.. autoclass:: ad_api.api.sp.CampaignNegativeKeywordsV3
    :members:

    Endpoints available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/sp/campaignNegativeKeywords/delete", "Delete campaigns negative keywords"
        "POST", "/sp/campaignNegativeKeywords/list", "List campaigns negative keywords"
        "POST", "/sp/campaignNegativeKeywords", "Create campaigns negative keywords"
        "PUT", "/sp/campaignNegativeKeywords", "Update campaigns negative keywords"
