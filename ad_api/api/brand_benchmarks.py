from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class BrandBenchmarks(Client):
    """
    Brand Benchmarks surfaces the advertiser and brand benchmark reports
    (ABVP) published for a brand: a metadata listing of every report available
    for an advertiser, and a download link for one report at one index date.

    Documentation: https://advertising.amazon.com/API/docs/en-us/brand-benchmarks

    Both routes require the Amazon-Advertising-API-Manager-Account header in
    addition to the client id, which is unusual in this package: the other
    families travel on the profile scope alone. Pass it as the
    ``Amazon-Advertising-API-Manager-Account`` entry of the client headers.
    """

    @sp_endpoint('/insights/brandBenchmarks/advertisers/{}/allReportMetadata', method='GET')
    def list_advertiser_report_metadata(self, advertiserId, **kwargs) -> ApiResponse:
        r"""Lists the benchmark reports published for an advertiser.

        Each entry carries ``advertiserId``, ``indexDate``, ``reportType`` and
        ``obfuscatedMarketplaceId``, which together identify one report: pass the
        first three to :meth:`get_advertiser_report` to get its download link.

        Keyword Args
            | path **advertiserId** (string): [required] The advertiser identifier.
            | **nextToken** (string): [optional] Token for the next page.
            | **maxResults** (number): [optional] Page size.
            | **latestOnly** (boolean): [optional] Only the most recent index date per report type.

        Request headers
            | **Amazon-Advertising-API-ClientId** (string): [required]
            | **Amazon-Advertising-API-Manager-Account** (string): [required]

        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), advertiserId), params=kwargs)

    @sp_endpoint('/insights/brandBenchmarks/advertisers/{}/reports/{}/indexDates/{}', method='GET')
    def get_advertiser_report(self, advertiserId, reportType, indexDate, **kwargs) -> ApiResponse:
        r"""Gets the download link for one benchmark report.

        The answer is not the data: it carries ``downloadLink``, a presigned S3 url.
        Download it straight away, because a presigned link expires.

        ``indexDate`` is validated against ``^[0-9]{4}-(0*[1-9]|1[0-2])-(0*[1-9]|[1-2][0-9]|3[0-1])$``,
        so the month and day may keep their leading zero or drop it.
        ``reportType`` is a free string in the contract; the values to use come from
        the ``reportType`` member of :meth:`list_advertiser_report_metadata`.

        Keyword Args
            | path **advertiserId** (string): [required] The advertiser identifier.
            | path **reportType** (string): [required] The report type, as listed in the metadata.
            | path **indexDate** (string): [required] The report index date, YYYY-MM-DD.

        Request headers
            | **Amazon-Advertising-API-ClientId** (string): [required]
            | **Amazon-Advertising-API-Manager-Account** (string): [required]

        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), advertiserId, reportType, indexDate), params=kwargs)
