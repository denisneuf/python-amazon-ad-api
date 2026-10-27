Brand Metrics API
=================

Current contract:

`https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/BrandMetrics_prod_3p.json`_

.. _https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/BrandMetrics_prod_3p.json: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/BrandMetrics_prod_3p.json

Previously, Amazon served the same specification from a different host:

`https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/BrandMetrics_prod_3p.json`_

.. _https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/BrandMetrics_prod_3p.json: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/BrandMetrics_prod_3p.json

.. autoclass:: ad_api.api.BrandMetrics
    :members:

    ### Example python

    .. code-block:: python

        from ad_api.api import BrandMetrics
        from ad_api.base import AdvertisingApiException

        dictionary = {
            "categoryTreeName": "es-automotive",
            "brandName": "BMW",
            "reportStartDate": "2022-03-01",
            "lookBackPeriod": "1W",
            "format": "CSV",
            "metrics": [
                "engagedShopperRateLowerBound",
                "customerConversionRate",
                "newToBrandCustomerRate"
            ],
            "reportEndDate": "2022-03-05"
        }

        try:

            result = BrandMetrics(account=store, marketplace=marketplace, debug=True).post_report(
                body=dictionary
            )

            print(result)

        except AdvertisingApiException as error:

            print(error)

    ### Example results

    The answer is a handle, not the report: it carries a ``reportId`` and
    ``status: IN_PROGRESS``, and the file has to be collected later.

    .. literalinclude:: ../../test/brand_metrics/result.json

    ### Example python

    .. code-block:: python

        from ad_api.api import BrandMetrics
        from ad_api.base import Marketplaces, AdvertisingApiException

        report_id = "820882fa-ff22-4772-99e1-6889e3ae97f8"

        try:

            result = BrandMetrics(account=store, marketplace=marketplace, debug=True).get_report(
                reportId=report_id
            )

            print(result)

        except AdvertisingApiException as error:

            print(error)

    ### Result once the report is ready

    Poll the same ``reportId`` until ``status`` reads ``SUCCESSFUL``; only then
    does ``location`` carry the signed address.

    .. literalinclude:: ../../test/brand_metrics/location.json

    ### Example python

    .. code-block:: python

        from ad_api.api import BrandMetrics
        from ad_api.base import Marketplaces, AdvertisingApiException

        location = "https://infrastack-prod-eu-eu-we-generatedreportsbucket49-96329mbigajd.s3.eu-west-1.amazonaws.com/[...]"

        try:

            result = BrandMetrics(account=store, marketplace=marketplace, debug=True).download_report(
                url=location,
                file="report",
                format="csv"
            )

            print(result)

        except AdvertisingApiException as error:

            print(error)

    Without ``file`` the call returns the Amazon file name instead of writing
    a file, and the ``format`` argument only decides the extension: the bytes
    stay in whichever format the report was generated in.

    ### Result of the file downloaded

    .. literalinclude:: ../../test/brand_metrics/download.json
