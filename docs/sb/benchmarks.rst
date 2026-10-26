Benchmarks
==========

Brand and category benchmark data.

.. note::
    Neither route appears in the Sponsored Brands 3.0 or 4.0 contract, yet both
    answer ``200`` with an empty collection on an account without data. Probed
    live, so they are kept.

.. autoclass:: ad_api.api.sb.Benchmarks

    .. autofunction:: ad_api.api.sb.Benchmarks.list_brands(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.Benchmarks.list_brand_and_category(self, brandName, categoryId, version=1, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.Benchmarks.list_brands_and_categories(self, version=1, **kwargs) -> ApiResponse:

    ### Endpoint map

    ================================================================  ===================================
    Path                                                              Method
    ================================================================  ===================================
    ``GET  /benchmarks/brands``                                       ``list_brands``
    ``POST /benchmarks/brands/{brandName}/categories/{categoryId}``   ``list_brand_and_category``
    ``POST /benchmarks/brandsAndCategories``                          ``list_brands_and_categories``
    ================================================================  ===================================

    ### Example python

    .. code-block:: python

        from ad_api.api.sb import Benchmarks

        benchmarks = Benchmarks(account='account_name', debug=False)

        print(benchmarks.list_brands().payload)
        print(benchmarks.list_brands_and_categories(body={}).payload)

    Documentation: see the Sponsored Brands guides on advertising.amazon.com.
