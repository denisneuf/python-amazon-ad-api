Product Targeting
=================

.. warning::

    Sponsored Display is not available for Sandbox endpoint

.. autoclass:: ad_api.api.sd.Targets
    :members:

    Endpoints available

    .. csv-table::
        :widths: 25, 25, 50
        :header: "Method", "Endpoint", "Description"

        "GET", "/sd/targets", "Gets a list of targeting clauses."
        "PUT", "/sd/targets", "Updates one or more targeting clauses."
        "POST", "/sd/targets", "Creates one or more targeting clauses."
        "GET", "/sd/targets/{targetId}", "Gets a targeting clause specified by identifier."
        "DELETE", "/sd/targets/{targetId}", "Sets the `state` of a targeting clause to `archived`."
        "GET", "/sd/targets/extended", "Gets a list of targeting clause objects with extended fields."
        "GET", "/sd/targets/extended/{targetId}", "Gets extended information for a targeting clause."
