Ad Groups
=========

.. deprecated:: 1.0.8
    The Sponsored Brands v3 ad group endpoints are closed. Amazon answers
    ``403 Endpoint has been deprecated`` and points to the v4 API. Use
    :doc:`ad_groups_v4` instead.

.. autoclass:: ad_api.api.sb.AdGroups
    :members:

    ### Example python

    .. code-block:: python

        from ad_api.api.sb.ad_groups import AdGroups

        res = AdGroups().list_ad_groups()

        print(result)

    ### Example python

    .. code-block:: python

        from ad_api.api.sb.ad_groups import AdGroups

        ad_group_id = 144356535815171236

        res = AdGroups().get_ad_group(
            adGroupId=ad_group_id
        )

        print(res)
