Creatives
=========

.. warning::

    Sponsored Display is not available for Sandbox endpoint

Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi

Specification: https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-display/3-0/openapi.yaml

.. autoclass:: ad_api.api.sd.Creatives
    :members:

    Endpoints available

    .. csv-table::
        :widths: 25, 25, 50
        :header: "Method", "Endpoint", "Description"

        "GET", "/sd/creatives", "Gets a list of creatives."
        "PUT", "/sd/creatives", "Updates one or more creatives."
        "POST", "/sd/creatives", "A POST request of one or more creatives."
        "POST", "/sd/creatives/preview", "Gets creative preview HTML."
        "GET", "/sd/moderation/creatives", "Gets a list of creative moderations"
