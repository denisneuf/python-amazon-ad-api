Brand Metrics API open beta
===========================

.. autoclass:: ad_api.api.BrandMetrics

.. autofunction:: ad_api.api.BrandMetrics.post_report

### Example python

.. code-block:: python

    from ad_api.api import BrandMetrics
    from ad_api.base import Marketplaces, AdvertisingApiException
    import json

    dictionary = {
        "categoryNodeTreeName": "es-automotive",
        "brandName": "BMW",
        "reportStartDate": "2022-03-01",
        "lookBackPeriod": "1w",
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
            body=json.dumps(data)
        )

        print(result)

    except AdvertisingApiException as error:

        print(error)

### Example results

.. literalinclude:: ../../test/brand_metrics/result.json

.. autofunction:: ad_api.api.BrandMetrics.get_report

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

### Result to get the location

.. literalinclude:: ../../test/brand_metrics/location.json

.. autofunction:: ad_api.api.BrandMetrics.download_report


### Example python

.. code-block:: python

    from ad_api.api import BrandMetrics
    from ad_api.base import Marketplaces, AdvertisingApiException

    location = "https://infrastack-prod-eu-eu-we-generatedreportsbucket49-96329mbigajd.s3.eu-west-1.amazonaws.com/[...]"


    try:

        result = BrandMetrics(account=store, marketplace=marketplace, debug=True).download_report(
            url=location,
            format="csv"
        )

        print(result)

    except AdvertisingApiException as error:

        print(error)

### Result of the file downloaded

.. literalinclude:: ../../test/brand_metrics/download.json