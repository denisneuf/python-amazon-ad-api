Negative targeting
==================

.. warning::

    Sponsored Display is not available for Sandbox endpoint

.. autoclass:: ad_api.api.sd.NegativeTargets

    Endpoints available

    .. csv-table::
        :widths: 25, 25, 50
        :header: "Method", "Endpoint", "Description"

        "GET", "/sd/negativeTargets", "Gets a list of negative targeting clauses."
        "PUT", "/sd/negativeTargets", "Updates one or more negative targeting clauses."
        "POST", "/sd/negativeTargets", "Creates one or more negative targeting clauses."
        "GET", "/sd/negativeTargets/{negativeTargetId}", "Gets a negative targeting clause specified by identifier."
        "DELETE", "/sd/negativeTargets/{negativeTargetId}", "Sets the `state` of a negative targeting clause to `archived`."
        "GET", "/sd/negativeTargets/extended", "Gets a list of negative targeting clause objects with extended fields."
        "GET", "/sd/negativeTargets/extended/{negativeTargetId}", "Gets extended information for a negative targeting clause."


    .. autofunction:: ad_api.api.sd.NegativeTargets.list_negative_targets(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.NegativeTargets.edit_negative_targets(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.NegativeTargets.create_negative_targets(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.NegativeTargets.get_negative_target(self, targetId, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.NegativeTargets.delete_negative_targets(self, targetId, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.NegativeTargets.list_negative_targets_extended(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sd.NegativeTargets.get_negative_target_extended(self, targetId, **kwargs) -> ApiResponse:

