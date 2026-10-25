Ad Groups
=========

Amazon Ads API v1 - unified Ad Groups endpoints

The product is selected in the request body with ``adProductFilter``, not in the
URL. All four methods talk to ``/adsApi/v1/*/adGroups``.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-adgroups
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLAdGroupsContract_prod_3p.json

.. autoclass:: ad_api.api.v1.AdGroups

    .. autofunction:: ad_api.api.v1.AdGroups.query_ad_groups

    .. autofunction:: ad_api.api.v1.AdGroups.create_ad_groups

    .. autofunction:: ad_api.api.v1.AdGroups.update_ad_groups

    .. autofunction:: ad_api.api.v1.AdGroups.delete_ad_groups
