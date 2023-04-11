Campaign Negative Targeting Clauses
===================================

.. warning::

    Sponsored Product v3 is not available for Sandbox endpoint

.. note::

    This API is version 3.0


.. autoclass:: ad_api.api.sp.CampaignNegativeTargets

    Endpoints available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "DELETE", "/sp/campaignNegativeTargets/delete", "Deletes Campaign Negative Targeting Clauses"
        "POST", "/sp/campaignNegativeTargets", "Create Campaign Negative Targeting Clauses"
        "PUT", "/sp/campaignNegativeTargets", "Updates Campaign Negative Targeting Clauses"
        "POST", "/sp/campaignNegativeTargets/list", "List Campaign Negative Targeting Clauses"


    .. autofunction:: ad_api.api.sp.CampaignNegativeTargets.delete_campaign_negative_targets(self, version: int = 3, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.CampaignNegativeTargets.create_campaign_negative_targets(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.CampaignNegativeTargets.edit_negative_product_targets(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.CampaignNegativeTargets.list_campaign_negative_targets(self, version: int = 3, **kwargs) -> ApiResponse:
