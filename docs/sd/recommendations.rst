Recommendations
===============


.. autoclass:: ad_api.api.sd.Recommendations

    Endpoints available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/sd/recommendations/creative/headline", "Retrieve creative headline recommendations."


    .. autofunction:: ad_api.api.sd.Recommendations.list_headline_recommendations(self, **kwargs) -> ApiResponse:

