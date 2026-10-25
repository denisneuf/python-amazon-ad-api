Ad Groups
=========

Amazon Ads API v1 - unified Ad Groups endpoints

The product is selected in the request body with ``adProductFilter``, not in the
URL. All four methods talk to ``/adsApi/v1/*/adGroups``.

.. autoclass:: ad_api.api.v1.AdGroups

    .. autofunction:: ad_api.api.v1.AdGroups.query_ad_groups

    .. autofunction:: ad_api.api.v1.AdGroups.create_ad_groups

    .. autofunction:: ad_api.api.v1.AdGroups.update_ad_groups

    .. autofunction:: ad_api.api.v1.AdGroups.delete_ad_groups
