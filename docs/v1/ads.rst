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

.. autoclass:: ad_api.api.v1.Ads
    :members:
