Version 3 reporting
===================


.. list-table::
    :header-rows: 0
    :widths: 18 82

    * - **Vendor docs**
      - https://advertising.amazon.com/API/docs/en-us/offline-report-prod-3p
    * - **Specification**
      - https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/OfflineReport_prod_3p.json

.. toctree::
    :maxdepth: 1
    :titlesonly:

    reports/post_report
    reports/get_report
    reports/download_report
    reports/delete_report

Rate limits and polling
-----------------------

Amazon publishes no requests-per-second figure. Throttling is dynamic and
follows the overall system load; for the reporting API it follows the size of
the per-region report queue, so the same polling rate can pass at one hour and
be rejected at a regional peak. The API returns no rate-limit headers, so
there is no way to read the remaining budget either.

A throttled call answers 429 with a ``Retry-After`` header in seconds. When the
header is missing, fall back to exponential backoff with a ceiling and some
jitter rather than a fixed delay: Amazon recommends exponential backoff on a
run of 429s, with longer periods for report generation because the dynamic
limits move slowly.

A 425 on the create call is not throttling. ``The Request is a duplicate of : <reportId>`` means the report already exists: take that id and poll it instead
of creating another. Resending keeps answering 425. This behaviour is not part
of Amazon's rate limiting documentation; it is what the API returns in
practice.

Design rules, all of them from Amazon's page unless marked otherwise:

* Distribute report generation through the day rather than in batches, and
  request older periods in smaller increments.
* Use exponential backoff on repeated 429s, longer for reports.
* Do not call list extended data operations when the extended properties are
  not needed, and avoid list operations across all entities.
* Poll the report id instead of re-creating the report (community practice,
  see the 425 note above).

.. note::

    Source: https://advertising.amazon.com/API/docs/en-us/reference/concepts/rate-limiting
    That page is a JavaScript application that plain fetchers read as an empty
    shell; the text above was taken from it with a renderer.

Report type catalogue
----------------------

The contract ships 35 full request examples, one per supported report, and they
are the reference for which values are valid together. Each example carries its
own ``adProduct``, ``reportTypeId``, ``timeUnit``, ``groupBy``, filters and the
complete column list.

**``timeUnit`` is fixed per product.** Sponsored Brands and Sponsored Television
only publish ``DAILY`` examples; DSP only ``SUMMARY``; Sponsored Products and
Sponsored Display publish both. Sending a time unit a report does not support is
answered by the service, not by the contract.

``adProduct`` accepts ``ALL``, ``DEMAND_SIDE_PLATFORM``, ``SPONSORED_BRANDS``,
``SPONSORED_DISPLAY``, ``SPONSORED_PRODUCTS`` and ``SPONSORED_TELEVISION``.

.. list-table:: Report types by product
    :header-rows: 1
    :widths: 22 26 10 20 22

    * - adProduct
      - reportTypeId
      - timeUnit
      - groupBy
      - filters
    * - SPONSORED_PRODUCTS (6)
      - spCampaigns
      - DAILY, SUMMARY
      - campaign
      - campaignStatus
    * -
      - spCampaigns
      - DAILY
      - adGroup, campaign
      - —
    * -
      - spCampaigns
      - SUMMARY
      - campaign, campaignPlacement
      - —
    * -
      - spAdvertisedProduct
      - DAILY
      - advertiser
      - campaignStatus
    * -
      - spTargeting
      - SUMMARY
      - targeting
      - keywordType, adKeywordStatus
    * -
      - spSearchTerm
      - SUMMARY
      - searchTerm
      - keywordType
    * -
      - spPurchasedProduct
      - DAILY
      - asin
      - keywordType
    * -
      - spGrossAndInvalids
      - DAILY
      - campaign
      - —
    * - SPONSORED_BRANDS (8)
      - sbCampaigns
      - DAILY
      - campaign
      - campaignStatus
    * -
      - sbCampaignPlacement
      - DAILY
      - campaignPlacement
      - —
    * -
      - sbAdGroup
      - DAILY
      - adGroup
      - adStatus
    * -
      - sbAds
      - DAILY
      - ads
      - adStatus
    * -
      - sbSearchTerm
      - DAILY
      - searchTerm
      - keywordStatus, keywordType
    * -
      - sbTargeting
      - DAILY
      - targeting
      - keywordStatus, keywordType
    * -
      - sbPurchasedProduct
      - DAILY
      - purchasedAsin
      - —
    * -
      - sbGrossAndInvalids
      - DAILY
      - campaign
      - —
    * - SPONSORED_DISPLAY (6)
      - sdCampaigns
      - DAILY, SUMMARY
      - campaign
      - —
    * -
      - sdCampaigns
      - DAILY
      - campaign, matchedTarget
      - —
    * -
      - sdAdGroup
      - DAILY
      - adGroup
      - —
    * -
      - sdAdvertisedProduct
      - DAILY
      - advertiser
      - —
    * -
      - sdTargeting
      - DAILY
      - targeting
      - —
    * -
      - sdPurchasedProduct
      - DAILY
      - asin
      - —
    * -
      - sdGrossAndInvalids
      - SUMMARY
      - campaign
      - —
    * - DEMAND_SIDE_PLATFORM (7)
      - dspCampaign
      - SUMMARY
      - creative
      - advertiserId
    * -
      - dspAudience
      - SUMMARY
      - lineItem
      - advertiserId
    * -
      - dspProduct
      - SUMMARY
      - lineItem
      - advertiserId
    * -
      - dspGeo
      - SUMMARY
      - postalCode
      - advertiserId
    * -
      - dspInventory
      - SUMMARY
      - site
      - advertiserId
    * -
      - dspTech
      - SUMMARY
      - lineItem
      - advertiserId
    * -
      - dspAudioAndVideo
      - SUMMARY
      - ad, campaign, content, creative, supplySource
      - advertiserId
    * - SPONSORED_TELEVISION (2)
      - stCampaigns
      - DAILY
      - campaign
      - —
    * -
      - stTargeting
      - DAILY
      - targeting
      - —

A DSP report needs the ``Amazon-Ads-AccountId`` header in addition to the
profile, and its ``advertiserId`` filter. The route takes three optional headers
in total; the create call is the only one whose body is versioned, and the media
type is ``application/vnd.createasyncreportrequest.v3+json``, not
``application/json``.

.. note::

    The column lists are long (11 for spGrossAndInvalids up to 384 for
    dspCampaign) and the service is the only authority on them. Read the
    example for the report wanted straight from the contract, and let a wrong
    name fail with the 400 that names the accepted values.

.. autoclass:: ad_api.api.Reports
    :noindex:

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
