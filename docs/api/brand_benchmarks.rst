Brand Benchmarks
================

.. list-table::
    :header-rows: 0
    :widths: 18 82

    * - **Vendor docs**
      - https://advertising.amazon.com/API/docs/en-us/brand-benchmarks
    * - **Specification**
      - https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/BrandBenchmarks_prod_3p.json

.. toctree::
    :maxdepth: 1
    :titlesonly:

    brand_benchmarks/list_advertiser_report_metadata
    brand_benchmarks/get_advertiser_report

Two routes, both ``GET``, and the second one needs a pair of values the first
returns:

    GET /insights/brandBenchmarks/advertisers/{advertiserId}/allReportMetadata
    GET /insights/brandBenchmarks/advertisers/{advertiserId}/reports/{reportType}/indexDates/{indexDate}

The metadata listing answers ``reportsMetadata``, an array of objects that each
carry ``advertiserId``, ``reportType``, ``indexDate`` and
``obfuscatedMarketplaceId``. Those four together identify one report;
``reportType`` and ``indexDate`` are what the second route takes in its path.

``reportType`` is a plain string in the contract with no enum, so the accepted
values are the ones the listing returns, never a list written here.
``indexDate`` is checked against
``^[0-9]{4}-(0*[1-9]|1[0-2])-(0*[1-9]|[1-2][0-9]|3[0-1])$``: a fixed
``YYYY-MM-DD`` shape, and the month and day accept a missing leading zero.

The second route does not return data. It returns ``downloadLink``, a presigned
S3 url, so download it immediately; a presigned link expires and cannot be
re-derived without calling again.

.. warning::

    **Both routes declare** ``Amazon-Advertising-API-Manager-Account`` **as a
    required header**, next to ``Amazon-Advertising-API-ClientId``. That is not
    the rule in the rest of this package, where the profile scope alone
    identifies the account. Send it in the client headers before calling; a
    request without it is refused with ``415``/``400`` rather than a missing
    scope.

    Amazon's operation index marks the Benchmark APIs as **deprecated**, with
    data stopping on 2026-12-17 and migration to Unified Reporting. The
    contract still serves and these two routes are built from it, but new
    integrations should plan the migration.

.. autoclass:: ad_api.api.BrandBenchmarks
    :noindex:

    ### Example python

    .. code-block:: python

        from ad_api.api import BrandBenchmarks

        benchmarks = BrandBenchmarks()

        metadata = benchmarks.list_advertiser_report_metadata('A1', latestOnly=True).payload
        first = metadata['reportsMetadata'][0]

        link = benchmarks.get_advertiser_report(
            first['advertiserId'],
            first['reportType'],
            first['indexDate'],
        ).payload['downloadLink']
