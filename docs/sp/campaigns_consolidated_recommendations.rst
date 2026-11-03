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

Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json

.. autoclass:: ad_api.api.sp.CampaignsRecommendations
    :members:

    Endpoints available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "GET", "/sp/campaign/recommendations", "Gets the top consolidated recommendations."
