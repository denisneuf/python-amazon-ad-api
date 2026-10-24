Campaigns
=========

Amazon Ads API v1 - unified Campaigns endpoints

The product is selected in the request body with ``adProductFilter``, not in the
URL. All four methods talk to ``/adsApi/v1/*/campaigns``.

.. autoclass:: ad_api.api.v1.Campaigns

    .. autofunction:: ad_api.api.v1.Campaigns.query_campaigns

    .. autofunction:: ad_api.api.v1.Campaigns.create_campaigns

    .. autofunction:: ad_api.api.v1.Campaigns.update_campaigns

    .. autofunction:: ad_api.api.v1.Campaigns.delete_campaigns
