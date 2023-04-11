Product Targeting
=================

.. warning::

    Sponsored Product v3.0 is not available for Sandbox endpoint while v2.0 it is

.. note::

    This API contains version 2.0 and some endpoints of 3.0 for older version compatibility please migrate to v3.0


.. autoclass:: ad_api.api.sp.Targets

    Endpoints available version 2.0

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/v2/sp/targets", "Creates one or more targeting expressions."
        "PUT", "/v2/sp/targets", "Updates one or more targeting clauses."
        "GET", "/v2/sp/targets", "Gets a list of targeting clauses filtered by specified criteria."
        "GET", "/v2/sp/targets/{targetId}", "Get a targeting clause specified by identifier."
        "DELETE", "/v2/sp/targets/{targetId}", "Archives a targeting clause."
        "GET", "/v2/sp/targets/extended", "Gets a list of targeting clauses filtered by specified criteria."
        "GET", "/v2/sp/targets/extended/{targetId}", "Get a targeting clause specified by identifier."
        "POST", "/v2/sp/targets/productRecommendations", "Gets a list of recommended products for targeting."
        "GET", "/v2/sp/targets/brands", "Get recommended brands for Sponsored Products."

    Endpoints available version 3.0

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/sp/targets/categories/recommendations", "Returns a list of category recommendations for the input list of ASINs."
        "GET", "/sp/negativeTargets/brands/recommendations", "Returns brands recommended for negative targeting."
        "POST", "/sp/targets/products/count", "Get number of targetable asins based on refinements provided by the user."
        "GET", "/sp/targets/categories", "Returns all targetable categories."
        "POST", "/sp/negativeTargets/brands/search", "Returns brands related to keyword input for negative targeting."
        "GET", "/sp​/targets​/category​/{categoryId}​/refinements", "Returns refinements according to category input."


    .. autofunction:: ad_api.api.sp.Targets.create_products_targets(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.Targets.edit_products_targets(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.Targets.list_products_targets(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.Targets.get_products_target(self, targetId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.Targets.delete_products_target(self, targetId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.Targets.list_products_targets_extended(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.Targets.get_products_target_extended(self, targetId, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.Targets.get_products_targets_recommendations(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.Targets.get_brand_targets(self, **kwargs) -> ApiResponse:


    .. autofunction:: ad_api.api.sp.Targets.list_products_targets_categories_recommendations(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.Targets.list_negative_targets_brands_recommendations(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.Targets.get_products_targets_count(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.Targets.list_targets_categories(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.Targets.list_negative_targets_brands_search(self, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.Targets.list_products_targets_category_refinements(self, categoryId, **kwargs) -> ApiResponse: