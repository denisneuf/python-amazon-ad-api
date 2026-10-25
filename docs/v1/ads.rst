Ads
===

Amazon Ads API v1 - unified Ads endpoints

The product is selected in the request body with ``adProductFilter``, not in the
URL. All four methods talk to ``/adsApi/v1/*/ads``.

``AdCreate`` requires ``adProduct``, ``adType``, ``creative`` and ``state``.
``creative`` carries exactly one of ``audioCreative``, ``displayCreative``,
``videoCreative``, ``thirdPartyCreative``, ``componentCreative`` or
``productCreative``, matching ``adType``.

.. autoclass:: ad_api.api.v1.Ads

    .. autofunction:: ad_api.api.v1.Ads.query_ads

    .. autofunction:: ad_api.api.v1.Ads.create_ads

    .. autofunction:: ad_api.api.v1.Ads.update_ads

    .. autofunction:: ad_api.api.v1.Ads.delete_ads
