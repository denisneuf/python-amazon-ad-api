Campaigns
=========

Amazon Ads API v1 - unified Campaigns endpoints

The product is selected in the request body with ``adProductFilter``, not in the
URL. All four methods talk to ``/adsApi/v1/*/campaigns``.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-campaigns
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLCampaignsContract_prod_3p.json

.. rubric:: Account header

``query_campaigns`` accepts ``account_id`` as a keyword argument, and so do the other
three methods of this family. It is turned into the ``Amazon-Ads-AccountId``
header and removed from ``kwargs`` before the call is built, so it never
travels in the query string:

.. code-block:: python

    Campaigns(account='my_store', marketplace=Marketplaces.EU).query_campaigns(
        body={...},
        account_id='amzn1.ads-account.g.xxxxxxxxxxxxxxxxxxxxxxxx',
    )

The contract declares the header as optional on all four routes, alongside the
client id, which is required and always sent, and the profile scope, which
comes from the ``profile_id`` in the credentials. Without ``account_id`` the
call goes out on the profile scope alone.

.. rubric:: Endpoint map

.. list-table::
    :header-rows: 1

    * - Path
      - Operation
      - Body requires
    * - ``/adsApi/v1/create/campaigns``
      - CreateCampaign
      - campaigns
    * - ``/adsApi/v1/delete/campaigns``
      - DeleteCampaign
      - campaignIds
    * - ``/adsApi/v1/query/campaigns``
      - QueryCampaign
      - adProductFilter
    * - ``/adsApi/v1/update/campaigns``
      - UpdateCampaign
      - campaigns

.. currentmodule:: ad_api.api.v1

.. autosummary::
    :toctree: campaigns/
    :nosignatures:

    Campaigns
    Campaigns.create_campaigns
    Campaigns.delete_campaigns
    Campaigns.query_campaigns
    Campaigns.update_campaigns
