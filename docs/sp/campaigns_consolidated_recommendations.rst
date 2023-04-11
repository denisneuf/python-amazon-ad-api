Campaign Consolidated Recommendations
=====================================

.. warning::

    Sponsored Product v3 is not available for Sandbox endpoint

.. note::

    This API is version 3.0

.. note::

    This API is not clear which marketplaces are supported


.. code-block:: python

    {
    "code":400,
    "responseHeaders":null,
    "responseBody":null,
    "message":"Marketplace is not supported"
    }


.. autoclass:: ad_api.api.sp.CampaignsRecommendations

    Endpoints available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "GET", "/sp/campaign/recommendations", "Gets the top consolidated recommendations."


    .. autofunction:: ad_api.api.sp.CampaignsRecommendations.list_campaigns_recommendations(self, **kwargs) -> ApiResponse:
