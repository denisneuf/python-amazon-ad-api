Campaigns
=========

.. deprecated:: 1.0.8
    The Sponsored Brands v3 campaign endpoints are closed. Amazon answers
    ``403 Endpoint has been deprecated`` and points to the v4 API. Use
    :doc:`campaigns_v4` instead.

.. autoclass:: ad_api.api.sb.Campaigns

    .. autofunction:: ad_api.api.sb.Campaigns.list_campaigns(self, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.sb.campaigns import Campaigns

        res = Campaigns().list_campaigns()

        print(result)




    .. deprecated:: 4.0.2

    .. autofunction:: ad_api.api.sb.Campaigns.create_campaigns(self, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.sb.campaigns import Campaigns

        file = open("SBCreateCampaignWithKeywords.json")
        data = file.read()
        file.close()

        result = Campaigns().create_campaigns(
            body=data
        )
        print(result)

    ### Example json

    .. literalinclude:: ../../test/campaigns/sb-sx-create-campaign-keywords.json

    .. deprecated:: 4.0.2

    .. autofunction:: ad_api.api.sb.Campaigns.edit_campaigns(self, **kwargs) -> ApiResponse:

    ### Example json

    .. literalinclude:: ../../test/campaigns/sb-sx-edit-campaign.json

    .. autofunction:: ad_api.api.sb.Campaigns.get_campaign(self, campaignId, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.sb.campaigns import Campaigns

        campaign_id = 144329325594765093

        result = Campaigns().get_campaign(
            campaignId=campaign_id
        )
        print(result)


    .. deprecated:: 4.0.2

    .. autofunction:: ad_api.api.sb.Campaigns.delete_campaign(self, campaignId, **kwargs) -> ApiResponse:

    .. code-block:: python

        from ad_api.api.sb.campaigns import Campaigns

        campaign_id = 144329325594765093

        result = Campaigns().delete_campaign(
            campaignId=campaign_id
        )
        print(result)


NOT AVAILABLE SANDBOX [INTERNAL_ERROR - HTTP 500 Internal Server Error]
