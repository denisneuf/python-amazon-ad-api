Ads
===

Amazon Ads API v1 - unified Ads endpoints

The product is selected in the request body with ``adProductFilter``, not in the
URL. All four methods talk to ``/adsApi/v1/*/ads``.

``AdCreate`` requires ``adProduct``, ``adType``, ``creative`` and ``state``.
``creative`` carries exactly one of ``audioCreative``, ``displayCreative``,
``videoCreative``, ``thirdPartyCreative``, ``componentCreative`` or
``productCreative``, matching ``adType``.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-ads
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLAdsContract_prod_3p.json

.. rubric:: Account header

``query_ads`` accepts ``account_id`` as a keyword argument, and so do the other
three methods of this family. It is turned into the ``Amazon-Ads-AccountId``
header and removed from ``kwargs`` before the call is built, so it never
travels in the query string:

.. code-block:: python

    Ads(account='my_store', marketplace=Marketplaces.EU).query_ads(
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
    * - ``/adsApi/v1/create/ads``
      - CreateAd
      - ads
    * - ``/adsApi/v1/delete/ads``
      - DeleteAd
      - adIds
    * - ``/adsApi/v1/query/ads``
      - QueryAd
      - adProductFilter
    * - ``/adsApi/v1/update/ads``
      - UpdateAd
      - ads

.. currentmodule:: ad_api.api.v1

.. autosummary::
    :toctree: ads/
    :nosignatures:

    Ads
    Ads.delete_ads
    Ads.create_ads
    Ads.query_ads
    Ads.update_ads

