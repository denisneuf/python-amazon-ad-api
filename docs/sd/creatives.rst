Creatives
=========

.. warning::

    Sponsored Display is not available for Sandbox endpoint

.. autoclass:: ad_api.api.sd.Creatives

    Endpoints available

    .. csv-table::
        :widths: 25, 25, 50
        :header: "Method", "Endpoint", "Description"

        "GET", "/sd/creatives", "Gets a list of creatives."
        "PUT", "/sd/creatives", "Updates one or more creatives."
        "POST", "/sd/creatives", "A POST request of one or more creatives."
        "POST", "/sd/creatives/preview", "Gets creative preview HTML."
        "GET", "/sd/moderation/creatives", "Gets a list of creative moderations"

    .. autofunction:: ad_api.api.sd.Creatives.list_creatives(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.Creatives.edit_creatives(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.Creatives.create_creatives(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.Creatives.list_moderation_creatives(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.Creatives.show_creative_preview(self, **kwargs) -> ApiResponse:
