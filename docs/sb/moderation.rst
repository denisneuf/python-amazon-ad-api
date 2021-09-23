Moderation
==========

.. autoclass:: ad_api.api.sb.Moderation

    .. autofunction:: ad_api.api.sb.Moderation.get_moderation(self, campaignId, **kwargs) -> ApiResponse:

    .. warning::
        Note that this resource is only available for campaigns in the US marketplace.

    ###Example Python

    .. code-block:: python

        campaign_id = 144329324494765093

        result = Moderation().get_moderation(
            campaignId=campaign_id
        )

        print(result)