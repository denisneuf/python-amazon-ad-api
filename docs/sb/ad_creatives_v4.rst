Ad Creatives
============

Sponsored Brands 4.0 ad creatives.

.. autoclass:: ad_api.api.sb.AdCreativesV4

    .. autofunction:: ad_api.api.sb.AdCreativesV4.list_ad_creatives(self, version=4, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.AdCreativesV4.create_video_ad_creative(self, version=4, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.AdCreativesV4.create_new_version_video_ad_creative(self, version=4, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.AdCreativesV4.create_new_version_product_collection_ad_creative(self, version=4, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.AdCreativesV4.create_new_version_store_spotlight_ad_creative(self, version=4, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.AdCreativesV4.create_auto_collection_ad_creative(self, version=4, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.AdCreativesV4.create_manual_collection_ad_creative(self, version=4, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.AdCreativesV4.create_new_version_product_collection_extended_ad_creative(self, version=4, **kwargs) -> ApiResponse:

    ### Request format

    Not every method here sends the same media type. The collection creative
    routes take the ads family one, ``application/vnd.sbadresource.v4+json``;
    the rest take ``application/vnd.sbAdCreativeResource.v4+json``:

    ============================================================  ======================================
    Route                                                         Media type
    ============================================================  ======================================
    ``/sb/ads/creatives/autoCollection``                          ``vnd.sbadresource.v4``
    ``/sb/ads/creatives/manualCollection``                        ``vnd.sbadresource.v4``
    ``/sb/ads/creatives/productCollectionExtended``               ``vnd.sbAdCreativeResource.v4``
    every other route in this class                               ``vnd.sbAdCreativeResource.v4``
    ============================================================  ======================================

    .. note::
        ``autoCollection`` and ``manualCollection`` answered ``400`` when called
        with ``sbAdCreativeResource`` as well, so the service tolerates both
        versioned types on those two. Plain ``application/json`` answers
        ``404 Could not find resource``: the versioned type is what routes the
        call at all.

    ### Endpoint map

    ==========================================================  =========================================
    Path                                                        Method
    ==========================================================  =========================================
    ``POST /sb/ads/creatives/list``                             ``list_ad_creatives``
    ``POST /sb/ads/creatives/brandVideo``                       ``create_video_ad_creative``
    ``POST /sb/ads/creatives/video``                            ``create_new_version_video_ad_creative``
    ``POST /sb/ads/creatives/productCollection``                ``create_new_version_product_collection_ad_creative``
    ``POST /sb/ads/creatives/storeSpotlight``                   ``create_new_version_store_spotlight_ad_creative``
    ``POST /sb/ads/creatives/autoCollection``                   ``create_auto_collection_ad_creative``
    ``POST /sb/ads/creatives/manualCollection``                 ``create_manual_collection_ad_creative``
    ``POST /sb/ads/creatives/productCollectionExtended``        ``create_new_version_product_collection_extended_ad_creative``
    ==========================================================  =========================================

    .. warning::
        ``POST /sb/ads/creatives/productCollection`` is flagged **deprecated** in
        the 4.0 contract, together with ``productCollectionExtended``. The method
        carries ``@Utils.deprecated``. New integrations should use the ad creation
        routes in :doc:`ads_v4` instead.

    ### Example python

    .. code-block:: python

        from ad_api.api.sb import AdCreativesV4

        creatives = AdCreativesV4(account='account_name', debug=False)

        response = creatives.list_ad_creatives(body={})
        print(response.payload)

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi
