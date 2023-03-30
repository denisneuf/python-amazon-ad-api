Ad Groups
=========

.. autoclass:: ad_api.api.sb.AdGroups

    .. autofunction:: ad_api.api.sb.AdGroups.list_ad_groups(self, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.sb.ad_groups import AdGroups

        res = AdGroups().list_ad_groups()

        print(result)


    .. autofunction:: ad_api.api.sb.AdGroups.get_ad_group(self, adGroupId, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.sb.ad_groups import AdGroups

        ad_group_id = 144356535815171236

        res = AdGroups().get_ad_group(
            adGroupId=ad_group_id
        )

        print(res)


