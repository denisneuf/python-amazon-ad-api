Store insights
==============

.. list-table::
    :header-rows: 0
    :widths: 18 82

    * - **Vendor docs**
      - https://advertising.amazon.com/API/docs/en-us/reference/2/stores
    * - **Specification**
      - https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Stores_prod_3p.json

Amazon Ads API - store insights


Two routes, both scoped by a brand entity id in the path:

    POST /stores/<brandEntityId>/asinMetrics
    GET  /stores/<brandEntityId>/insights

Both pick their media type by version, and the version travels in the header
rather than in the body:

    Content-Type  application/vnd.GetAsinEngagementForStoreRequest.v1+json
    Accept        application/vnd.GetAsinEngagementForStoreResponse.v1+json

The class docstring in the module speaks about Brand Metrics, which is a
different family; the routes here are the store ones.

.. toctree::
    :maxdepth: 1
    :titlesonly:

    stores/get_asin_engagement_for_store
    stores/get_insights_for_store_api

.. autoclass:: ad_api.api.Stores
    :noindex:
