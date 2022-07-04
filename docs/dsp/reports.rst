Reports
=======

.. autoclass:: ad_api.api.dsp.Reports

    .. autofunction:: ad_api.api.dsp.Reports.post_report(self, dspAccountId, accept='application/vnd.dspcreatereports.v3+json', **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.dsp.reports import Reports

        with open("campaign.json", "r", encoding="utf-8") as f:
            data = f.read()

        dsp_account_id = '1111111111111'

        result = Reports().post_report(
            dspAccountId=dsp_account_id,
            body=data
        )

        payload = result.payload
        report_id = payload.get('reportId')

    ### Example json

    Open this :download:`json <../../test/reports/dsp-sx-campaign-report.json>` file to see the result:

    .. literalinclude:: ../../test/reports/dsp-sx-campaign-report.json

    .. autofunction:: ad_api.api.dsp.Reports.get_report(self, dspAccountId, reportId, accept='application/vnd.dspgetreports.v3+json', **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.dsp.reports import Reports

        dsp_account_id = '1111111111111'

        # this report_id is obtained from post_report method
        report_id = 'fac0e6e4-0ff7-b9a1-a3a1-9f528bacce9e'

        result = Reports().get_report(
            dspAccountId=dsp_account_id,
            reportId=report_id
        )

    ### Result json

    .. code-block:: python

        {'expiration': '2022-07-04T16:18:48.753Z',
         'format': 'JSON',
         'location': 'https://corvo-reports.s3.amazonaws.com/DSP_API/2022-07-04/fac0e6e4-0ff7-b9a1-a3a1-9f528bacce9e/campaign-report-1111111111111.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220704T151848Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=***************************************************************&X-Amz-Signature=****************************************************************',
         'reportId': 'fac0e6e4-0ff7-b9a1-a3a1-9f528bacce9e',
         'status': 'SUCCESS',
         'statusDetails': 'Success',
         'type': 'CAMPAIGN'}

    .. autofunction:: ad_api.api.dsp.Reports.download_report(self, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.dsp.reports import Reports

        # the url=location is obtained from get_report method need to in stay 'status': 'SUCCESS' if is 'IN_PROGRESS' the report cannot be downloaded
        location = 'https://corvo-reports.s3.amazonaws.com/DSP_API/2022-07-04/fac0e6e4-0ff7-b9a1-a3a1-9f528bacce9e/campaign-report-1111111111111.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220704T151848Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=***************************************************************&X-Amz-Signature=****************************************************************'

        # path = '/Users/your-profile/Downloads/report_name'
        # mode = "data"  # "data (list), raw, url, json, zip, gzip default is url"

        result = Reports().download_report(
            url=location,
            # file=path,
            # format=mode
        )
