Campaigns
=========

Amazon Ads API v1 - unified Campaigns endpoints

The product is selected in the request body with ``adProductFilter``, not in the
URL. All four methods talk to ``/adsApi/v1/*/campaigns``.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-campaigns
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLCampaignsContract_prod_3p.json

.. currentmodule:: ad_api.api.v1

.. autosummary::
    :toctree: campaigns/
    :nosignatures:

    Campaigns
    Campaigns.create_campaigns
    Campaigns.delete_campaigns
    Campaigns.query_campaigns
    Campaigns.update_campaigns
