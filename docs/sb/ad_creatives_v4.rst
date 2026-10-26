Ad Creatives
============

Sponsored Brands 4.0 ad creatives.

.. autoclass:: ad_api.api.sb.AdCreativesV4

    .. autofunction:: ad_api.api.sb.AdCreativesV4.list_ad_creatives(self, version=4, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.AdCreativesV4.create_video_ad_creative(self, version=4, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.AdCreativesV4.create_new_version_video_ad_creative(self, version=4, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.AdCreativesV4.create_new_version_product_collection_ad_creative(self, version=4, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.AdCreativesV4.create_new_version_store_spotlight_ad_creative(self, version=4, **kwargs) -> ApiResponse:

    ### Request format

    Every method sends and receives ``application/vnd.sbAdCreativeResource.v4+json``.

    ====================  =======================================================
    Header                Value
    ====================  =======================================================
    ``Accept``            ``application/vnd.sbAdCreativeResource.v4+json``
    ``Content-Type``      same as ``Accept``
    ====================  =======================================================

    ### Endpoint map

    ==========================================================  =========================================
    Path                                                        Method
    ==========================================================  =========================================
    ``POST /sb/ads/creatives/list``                             ``list_ad_creatives``
    ``POST /sb/ads/creatives/brandVideo``                       ``create_video_ad_creative``
    ``POST /sb/ads/creatives/video``                            ``create_new_version_video_ad_creative``
    ``POST /sb/ads/creatives/productCollection``                ``create_new_version_product_collection_ad_creative``
    ``POST /sb/ads/creatives/storeSpotlight``                   ``create_new_version_store_spotlight_ad_creative``
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
