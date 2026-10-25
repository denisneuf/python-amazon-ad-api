Reports
=======

.. note::
    These endpoints keep the historical ``/v2/`` path prefix but are part of the
    Sponsored Brands 3.0 documentation
    (see `Amazon's Reports tag <https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Reports>`_).
    The path prefix does **not** indicate the API generation: Sponsored Brands
    mixes ``/sb/...``, ``/v2/hsa/...`` and ``/v2/reports/...`` under the same
    version, and all of them answer.

    Do not delete anything here based on the prefix alone. Only ``404`` with
    *"Could not find resource for full path"* proves a route is gone; a ``404``
    that names a missing identifier means the route is alive.

.. autoclass:: ad_api.api.sb.Reports

    .. autofunction:: ad_api.api.sb.Reports.post_report(self, recordType, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.sb.reports import Reports

        with open("campaigns.json", "r", encoding="utf-8") as f:
            data = f.read()

        # Available values : campaigns, adGroups, targets and keywords
        record_type = 'campaigns'

        result = Reports().post_report(
            recordType=record_type,
            body=data
        )

        payload = result.payload
        report_id = payload.get('reportId')

    ### Example json

    Open this :download:`json <../../test/reports/sb-sx-campaigns-report.json>` file to see the result:

    .. literalinclude:: ../../test/reports/sb-sx-campaigns-report.json




    .. autofunction:: ad_api.api.sb.Reports.get_report(self, reportId, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.sb.reports import Reports

        # this report_id is obtained from post_report method
        report_id = 'amzn1.clicksAPI.v1.p44551.61549C5E.e4599469-7392-4624-a858-fc1fecdb165c'

        result = Reports().get_report(
            reportId=report_id
        )

    ### Result json

    .. code-block:: python

        {'expiration': 1640736000000,
         'fileSize': 6546,
         'location': 'https://advertising-api-eu.amazon.com/v1/reports/amzn1.clicksAPI.v1.p44551.61549C5E.e4599469-7392-4624-a858-fc1fecdb165c/download',
         'reportId': 'amzn1.clicksAPI.v1.p44551.61549C5E.e4599469-7392-4624-a858-fc1fecdb165c',
         'status': 'SUCCESS',
         'statusDetails': 'Report has been successfully generated.'}}

    .. autofunction:: ad_api.api.sb.Reports.download_report(self, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.sb.reports import Reports

        # the url=location is obtained from get_report method need to in stay 'status': 'SUCCESS' if is 'IN_PROGRESS' the report cannot be downloaded
        location = 'https://advertising-api-eu.amazon.com/v1/reports/amzn1.clicksAPI.v1.p44551.61549C5E.e4599469-7392-4624-a858-fc1fecdb165c/download'

        # path = '/Users/your-profile/Downloads/report_name'
        # mode = "data"  # "data (list), raw, url, json, zip, gzip default is url"

        result = Reports().download_report(
            url=location,
            # file=path,
            # format=mode
        )
