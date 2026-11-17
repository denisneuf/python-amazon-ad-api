Multi Country Recommendations
=============================

.. list-table::
    :header-rows: 0
    :widths: 18 82

    * - **Vendor docs**
      - https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod
    * - **Specification**
      - https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json

Two routes answer for several marketplaces at once, given either the same
product in each of them or a global campaign and ad group:

``POST /sp/global/targets/bid/recommendations``
    bids for the targets of a new or an existing ad group,
    ``BIDS_FOR_NEW_AD_GROUP`` or ``BIDS_FOR_EXISTING_AD_GROUP``.

``POST /sp/global/targets/keywords/recommendations/list``
    keyword targets with their bids, ``KEYWORDS_FOR_ASINS`` or
    ``KEYWORDS_FOR_ADGROUP``.

.. warning::

    A request has to be global for these two routes to answer. Sending a list
    of countries is not enough: the keyword route replies 400 "This endpoint
    only accepts global requests" and the bid route replies 401 Unauthorized,
    because the client sends the profile identifier in
    ``Amazon-Advertising-API-Scope`` and these routes expect the request to
    come from a global account instead. Both were exercised against a seller
    account and neither returned a payload.

.. autoclass:: ad_api.api.sp.GlobalRecommendations
    :members:
