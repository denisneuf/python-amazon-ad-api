Snapshots
=========

.. autoclass:: ad_api.api.sp.Snapshots

    .. autofunction:: ad_api.api.sp.Snapshots.post_snapshot(self, recordType, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.sp.snapshots import Snapshots

        file = open("request.json")
        data = file.read()
        file.close()

        # Available values : campaigns, adGroups, keywords, negativeKeywords, campaignNegativeKeywords, productAds, targets, negativeTargets

        record_type = 'campaigns'

        result = Snapshots().post_snapshot(
            recordType=record_type,
            body=data
        )

    ### Example json

    Open this :download:`json <../../test/snapshots/sp-sx-state-filter.json>` file to see the result:

    .. literalinclude:: ../../test/snapshots/sp-sx-state-filter.json

    .. autofunction:: ad_api.api.sp.Snapshots.get_snapshot(self, reportId, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.sp.snapshots import Snapshots

        # this snapshot_id is obtained from post_snapshot method
        snapshot_id = "amzn1.clicksAPI.v1.p44551.614D9309.84477233-ccc8-4591-80f2-1f96b7ea9c7e"

        result = Snapshots().get_snapshot(
            snapshotId=snapshot_id
        )

    ### Result json

    .. code-block:: python

        {'expiration': 1640304000000,
         'fileSize': 1241,
         'location': 'https://advertising-api-eu.amazon.com/v1/snapshots/amzn1.clicksAPI.v1.p44551.614D9309.84477233-ccc8-4591-80f2-1f96b7ea9c7e/download',
         'snapshotId': 'amzn1.clicksAPI.v1.p44551.614D9309.84477233-ccc8-4591-80f2-1f96b7ea9c7e',
         'status': 'SUCCESS',
         'statusDetails': 'Snapshot has been successfully generated.'}}

    .. autofunction:: ad_api.api.sp.Snapshots.download_snapshot(self, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.sp.snapshots import Snapshots

        # the url=location is obtained from get_snapshot method need to in stay 'status': 'SUCCESS' if is 'IN_PROGRESS' the snapshot cannot be downloaded
        location = 'https://advertising-api-eu.amazon.com/v1/snapshots/amzn1.clicksAPI.v1.p44551.614D9309.84477233-ccc8-4591-80f2-1f96b7ea9c7e/download'

        # path = '/Users/your-profile/Downloads/report_name'
        # mode = "data"  # "data (list), raw, url, json, zip, gzip default is url"

        result = Reports().download_report(
            url=location,
            # file=path,
            # format=mode
        )


