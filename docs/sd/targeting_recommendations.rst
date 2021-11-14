Targeting Recommendations
=========================

.. warning::

    Sponsored Display is not available for Sandbox endpoint

.. autoclass:: ad_api.api.sd.TargetsRecommendations

    Endpoint available

    .. csv-table::
        :widths: 25, 25, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/sd/targets/recommendations", "Returns a set of bid recommendations for targeting clauses"

    .. autofunction:: ad_api.api.sd.TargetsRecommendations.list_targets_recommendations(self, **kwargs) -> ApiResponse:


