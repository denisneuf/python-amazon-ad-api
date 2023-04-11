Campaigns Budget Usage
======================

.. warning::

    Sponsored Product v3 is not available for Sandbox endpoint

.. note::

    This API is version 3.0


.. autoclass:: ad_api.api.sp.CampaignsBudgetUsage

    Endpoints available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/sp/campaigns/budget/usage", "Budget usage API for SP campaigns"


    .. autofunction:: ad_api.api.sp.CampaignsBudgetUsage.list_campaigns_budget_usage(self, version: int = 1, **kwargs) -> ApiResponse:

