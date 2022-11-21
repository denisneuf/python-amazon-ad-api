Reports
=======

.. autoclass:: ad_api.api.Reports

    .. autofunction:: ad_api.api.Reports.post_report(self, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.reports import Reports

        with open("advertised_product.json", "r", encoding="utf-8") as f:
            data = f.read()

        result = Reports().post_report(body=data)
        payload = result.payload
        report_id = payload.get('reportId')

    ### Example json

    Open this :download:`json <../../test/reports/sp-sx-advertised_product-report.json>` file to see the result:

    .. literalinclude:: ../../test/reports/sp-sx-advertised_product-report.json

    .. autofunction:: ad_api.api.Reports.get_report(self, reportId, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.reports import Reports

        # this report_id is obtained from post_report method
        report_id = '8877234e-bdaa-165d-21ee-45e2e4d8b746'

        result = Reports().get_report(reportId=report_id)

    ### Result json

    .. code-block:: python

        {
          'configuration':
          {
            'adProduct': 'SPONSORED_PRODUCTS',
            'columns': ['impressions', 'clicks', 'cost', 'campaignStatus', 'advertisedAsin', 'date'],
            'filters': None,
            'format': 'GZIP_JSON',
            'groupBy': ['advertiser'],
            'reportTypeId': 'spAdvertisedProduct',
            'timeUnit': 'DAILY'
          },
          'createdAt': '2022-11-21T12:00:52.528Z',
          'endDate': '2022-11-01',
          'failureReason': None,
          'fileSize': 51199,
          'generatedAt': '2022-11-21T12:01:53.255Z',
          'name': None,
          'reportId': '8877234e-bdaa-165d-21ee-45e2e4d8b746',
          'startDate': '2022-11-01',
          'status': 'COMPLETED',
          'updatedAt': '2022-11-21T12:01:53.255Z',
          'url': 'https://offline-report-storage-eu-west-1-prod.s3.eu-west-1.amazonaws.com/8877234e-bdaa-165d-21ee-45e2e4d8b746/report-8877234e-bdaa-165d-21ee-45e2e4d8b746.json.gz?X-Amz-Security-Token=****************&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221121T120227Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=*********************&X-Amz-Signature=*************************************************',
          'urlExpiresAt': '2022-11-21T13:02:27.915577Z'
        }

    .. autofunction:: ad_api.api.Reports.download_report(self, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.reports import Reports

        # the url=url is obtained from get_report method need to in stay 'status': 'SUCCESS' if is 'IN_PROGRESS' the report cannot be downloaded
        url = 'https://offline-report-storage-eu-west-1-prod.s3.eu-west-1.amazonaws.com/8877234e-bdaa-165d-21ee-45e2e4d8b746/report-8877234e-bdaa-165d-21ee-45e2e4d8b746.json.gz?X-Amz-Security-Token=****************&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221121T120227Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=*********************&X-Amz-Signature=*************************************************'

        # path = '/Users/your-profile/Downloads/report_name'
        # mode = "data"  # "data (list), raw, url, json, zip, gzip default is url"

        result = Reports().download_report(
            url=url,
            # file=path,
            # format=mode
        )
