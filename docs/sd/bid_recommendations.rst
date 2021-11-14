Bid Recommendations
===================

.. warning::

    Sponsored Display is not available for Sandbox endpoint

.. autoclass:: ad_api.api.sd.BidRecommendations

    Endpoint available

    .. csv-table::
        :widths: 25, 25, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/sd/targets/bid/recommendations", "Returns a set of bid recommendations for targeting clauses"

    .. autofunction:: ad_api.api.sd.BidRecommendations.list_targets_bid_recommendations(self, **kwargs) -> ApiResponse:


