Campaign Negative Keywords
==========================

.. warning::

    Sponsored Product v3 is not available for Sandbox endpoint

.. note::

    This API is version 3.0

.. autoclass:: ad_api.api.sp.CampaignNegativeKeywordsV3

    Endpoints available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/sp/campaignNegativeKeywords/delete", "Delete campaigns negative keywords"
        "POST", "/sp/campaignNegativeKeywords/list", "List campaigns negative keywords"
        "POST", "/sp/campaignNegativeKeywords", "Create campaigns negative keywords"
        "PUT", "/sp/campaignNegativeKeywords", "Update campaigns negative keywords"


    .. autofunction:: ad_api.api.sp.CampaignNegativeKeywordsV3.delete_campaign_negative_keyword(self, version: int = 3, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.CampaignNegativeKeywordsV3.list_campaign_negative_keywords(self, version: int = 3, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.CampaignNegativeKeywordsV3.create_campaign_negative_keywords(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
    .. autofunction:: ad_api.api.sp.CampaignNegativeKeywordsV3.edit_campaign_negative_keywords(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
