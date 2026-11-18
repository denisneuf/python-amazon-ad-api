from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class MarketingMixModeling(Client):
    """
    Marketing Mix Modeling provides aggregated Amazon sales and media performance
    signals for building MMM datasets: the brand groups an advertiser can report on,
    the campaigns and products behind each group, per-group overrides that include or
    exclude individual ASINs or campaigns, and an asynchronous report that returns a
    list of signed urls.

    Documentation: https://advertising.amazon.com/API/docs/en-us/marketing-mix-modeling
    """

    @sp_endpoint('/mmm/v1/brandGroups/list', method='POST')
    def list_brand_groups(self, **kwargs) -> ApiResponse:
        r"""Lists the brand groups available to the advertiser.

        Request body
            | **brandGroupIdFilter** (BrandGroupIdFilter): [optional] Only list brand groups with one of these ID values.
                | **include** (list > string): [required] Between 1 and 100 identifiers.
            | **countryCodeFilter** (CountryCodeFilter): [optional] Only list brand groups with one of these ISO 3166 country codes.
                | **include** (list > string): [required] Between 1 and 100 country codes.
            | **maxResults** (integer): [optional] 1 to 100, defaults to the max page size.
            | **nextToken** (string): [optional] Token for the next page.

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)

    @sp_endpoint('/mmm/v1/brandGroups/{}/campaigns', method='GET')
    def get_brand_group_campaigns(self, brandGroupId, **kwargs) -> ApiResponse:
        r"""Lists the campaigns that belong to a brand group.

        Keyword Args
            | path **brandGroupId** (string): [required] The brand group identifier.
            | **nextToken** (string): [optional] Token for the next page.
            | **maxResults** (integer): [optional] Number of records per page.

        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), brandGroupId), params=kwargs)

    @sp_endpoint('/mmm/v1/brandGroups/{}/products', method='GET')
    def get_brand_group_products(self, brandGroupId, **kwargs) -> ApiResponse:
        r"""Lists the products (ASINs) that belong to a brand group.

        Keyword Args
            | path **brandGroupId** (string): [required] The brand group identifier.
            | **nextToken** (string): [optional] Token for the next page.
            | **maxResults** (integer): [optional] Number of records per page.

        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), brandGroupId), params=kwargs)

    @sp_endpoint('/mmm/v1/brandGroupOverrides', method='POST')
    def create_brand_group_overrides(self, **kwargs) -> ApiResponse:
        r"""Creates overrides that force a product or campaign in or out of a brand group report.

        The answer is 207 MultiStatus: success holds the accepted overrides and error
        the refused ones, so one call can both accept and refuse.

        Request body
            | **overrides** (list > object): [required] Between 1 and 100 overrides.
                | **brandGroupId** (string): [required] The brand group to override.
                | **identifierType** (string): [required] Enum: ASIN, CAMPAIGN_ID.
                | **identifierValue** (string): [required] The identifier value.
                | **overrideType** (string): [required] Enum: INCLUDE, EXCLUDE.

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)

    @sp_endpoint('/mmm/v1/brandGroupOverrides/list', method='POST')
    def list_brand_group_overrides(self, **kwargs) -> ApiResponse:
        r"""Lists the overrides defined on the advertiser brand groups.

        Every filter is optional; the filters that are present narrow the answer.

        Request body
            | **brandGroupIdFilter** (BrandGroupIdFilter): [optional]
                | **include** (list > string): [required] Between 1 and 100 identifiers.
            | **overrideIdFilter** (OverrideIdFilter): [optional]
                | **include** (list > string): [required] Between 1 and 100 identifiers.
            | **maxResults** (integer): [optional] 1 to 100, defaults to the max page size.
            | **nextToken** (string): [optional] Token for the next page.

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)

    @sp_endpoint('/mmm/v1/brandGroupOverrides/delete', method='POST')
    def delete_brand_group_overrides(self, **kwargs) -> ApiResponse:
        r"""Deletes overrides by id.

        overrideIdFilter is required: the route has no path variant, so the ids travel
        in the body. The answer is 207 MultiStatus.

        Request body
            | **overrideIdFilter** (OverrideIdFilter): [required]
                | **include** (list > string): [required] Between 1 and 100 override identifiers.

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)

    @sp_endpoint('/mmm/v1/reports', method='POST')
    def create_report(self, **kwargs) -> ApiResponse:
        r"""Requests an MMM report.

        The answer is a handle, not the data: it carries reportId and status. Poll
        get_report until the status reads SUCCEEDED and read the urls list, which is
        signed and expires at urlsExpireAt.

        With timeUnit set to WEEKLY the contract bounds the dates: the start must be a
        Sunday or Monday and the end a Saturday or Sunday.

        Request body
            | **configuration** (MmmReportConfiguration): [required]
                | **brandGroupId** (string): [required] The brand group being reported on.
                | **geoDimension** (string): [required] Enum: COUNTRY, DMA (US only), POSTAL_CODE (select countries).
                | **metricsType** (string): [required] Enum: MEDIA_ONLY, MEDIA_AND_SALES.
                | **timeUnit** (string): [required] Enum: DAILY, WEEKLY.
            | **startDate** (string): [required] Inclusive start, YYYY-MM-DD.
            | **endDate** (string): [required] Inclusive end, YYYY-MM-DD.
            | **description** (string): [optional] A description of the report.
            | **dueDate** (string): [optional] Due date, used for prioritisation, YYYY-MM-DD.
            | **reportName** (string): [optional] The display name of the report.

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)

    @sp_endpoint('/mmm/v1/reports/list', method='POST')
    def list_reports(self, **kwargs) -> ApiResponse:
        r"""Lists the MMM reports requested on the account.

        Request body
            | **maxResults** (integer): [optional] 1 to 100, defaults to the max page size.
            | **nextToken** (string): [optional] Token for the next page.

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)

    @sp_endpoint('/mmm/v1/reports/{}', method='GET')
    def get_report(self, reportId, **kwargs) -> ApiResponse:
        r"""Gets one MMM report: its status, its dates and its signed urls.

        status runs PENDING, PROCESSING, SUCCEEDED, FAILED, CANCELED. A failure carries
        failureCode and failureMessage instead of a url.

        Keyword Args
            | path **reportId** (string): [required] The report identifier.

        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), reportId), params=kwargs)

    @sp_endpoint('/mmm/v1/reports/{}', method='DELETE')
    def delete_report(self, reportId, **kwargs) -> ApiResponse:
        r"""Deletes an MMM report by id.

        The service answers 204 No Content on success.

        Keyword Args
            | path **reportId** (string): [required] The report identifier.

        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), reportId), params=kwargs)
