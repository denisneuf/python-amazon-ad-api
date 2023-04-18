Brand Safety List
=================

.. warning::

    Sponsored Display is not available for Sandbox endpoint

.. autoclass:: ad_api.api.sd.BrandSafety

    Endpoints available

    .. csv-table::
        :widths: 25, 25, 50
        :header: "Method", "Endpoint", "Description"

        "GET", "/sd/brandSafety/deny", "Gets a list of websites/apps that are on the advertiser's Brand Safety Deny List."
        "POST", "/sd/brandSafety/deny", "Creates one or more domains to add to a Brand Safety Deny Lis"
        "DELETE", "/sd/brandSafety/deny", "Archives all of the domains in the Brand Safety Deny List."
        "GET", "/sd/brandSafety/{requestId}/results", "Gets the results for the given request"
        "GET", "/sd/brandSafety/{requestId}/status", "Gets the status for the given request"
        "GET", "/sd/brandSafety/status", "List status of all Brand Safety List requests."

    .. autofunction:: ad_api.api.sd.BrandSafety.list_brand_safety(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.BrandSafety.post_brand_safety(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.BrandSafety.delete_brand_safety(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.BrandSafety.get_result_brand_safety_request(self, requestId, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.BrandSafety.get_status_brand_safety_request(self, requestId, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.BrandSafety.list_brand_safety_requests_history(self, **kwargs) -> ApiResponse: