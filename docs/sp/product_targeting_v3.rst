Product Targeting
=================

.. warning::

    Sponsored Product v3.0 is not available for Sandbox endpoint

.. note::

    This documentation API 3.0

Endpoints available version 3.0

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"


        "POST", "/sp/targets/list", "Listing product targets."
        "POST", "/sp/targets", "Creating product targets."
        "PUT", "/sp/targets", "Creating product targets."
        "POST", "/sp/targets/delete", "Deleting product targets."
        "POST", "/sp/targets/categories/recommendations", "Returns a list of category recommendations for the input list of ASINs."
        "POST", "/sp/targets/products/count", "Get number of targetable asins based on refinements provided by the user."
        "GET", "/sp/targets/categories", "Returns all targetable categories."
        "GET", "/sp​/targets​/category​/{categoryId}​/refinements", "Returns refinements according to category input."






.. autoclass:: ad_api.api.sp.TargetsV3

    .. autofunction:: ad_api.api.sp.TargetsV3.list_product_targets(self, version: int = 3, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.TargetsV3.create_product_targets(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.TargetsV3.edit_product_targets(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.TargetsV3.delete_product_targets(self, version: int = 3, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sp.TargetsV3.list_products_targets_categories_recommendations(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.TargetsV3.get_products_targets_count(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.TargetsV3.list_targets_categories(self, prefer: bool = False, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.TargetsV3.list_products_targets_category_refinements(self, categoryId, prefer: bool = False, **kwargs) -> ApiResponse: