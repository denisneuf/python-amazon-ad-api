Product Recommendation Service
==============================

.. warning::

    Sponsored Product v3 is not available for Sandbox endpoint

.. note::

    This API is version 3.0



.. autoclass:: ad_api.api.sp.ProductRecommendations

    Endpoint available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/sp/targets/products/recommendations", "Suggested target ASINs for your advertised product."


    .. autofunction:: ad_api.api.sp.ProductRecommendations.list_products_recommendations(self, **kwargs) -> ApiResponse:


