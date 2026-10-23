Campaigns
=========

Amazon Ads API - Sponsored Products

The ``Campaigns`` class exposes the v1 endpoints under ``/adsApi/v1/``. The old
v2 methods (``/v2/sp/campaigns``) are deprecated and commented out in the source;
they are kept in the repository for reference only.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-campaigns#tag/Campaigns

.. autoclass:: ad_api.api.sp.Campaigns

    .. autofunction:: ad_api.api.sp.Campaigns.query_campaigns

    .. autofunction:: ad_api.api.sp.Campaigns.create_campaigns

    .. autofunction:: ad_api.api.sp.Campaigns.update_campaigns

    .. autofunction:: ad_api.api.sp.Campaigns.delete_campaigns
