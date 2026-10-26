Product Targeting
=================

.. warning::

    Deprecated since 1.0.4. The four CRUD operations on this page —
    ``list_product_targets``, ``create_product_targets``,
    ``edit_product_targets`` and ``delete_product_targets`` — are deprecated in
    favour of ``ad_api.api.v1.Targets``.

    The helper endpoints listed below remain supported and are **not**
    deprecated: ``categories/recommendations``, ``products/count``,
    ``categories`` and ``category/{categoryId}/refinements``.

.. note::

    Sponsored Product v3.0 is not available for Sandbox endpoint

Endpoints available version 3.0

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/sp/targets/list", "Listing product targets. [deprecated]"
        "POST", "/sp/targets", "Creating product targets. [deprecated]"
        "PUT", "/sp/targets", "Updating product targets. [deprecated]"
        "POST", "/sp/targets/delete", "Deleting product targets. [deprecated]"
        "POST", "/sp/targets/categories/recommendations", "Returns a list of category recommendations for the input list of ASINs."
        "POST", "/sp/targets/products/count", "Get number of targetable asins based on refinements provided by the user."
        "GET", "/sp/targets/categories", "Returns all targetable categories."
        "GET", "/sp/targets/category/{categoryId}/refinements", "Returns refinements according to category input."

.. autoclass:: ad_api.api.sp.TargetsV3
    :members:
