from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class BrandMetrics(Client):
    """
    Brand Metrics provides a new measurement solution that quantifies opportunities for your brand at each stage of the customer journey on Amazon, and helps brands understand the value of different shopping engagements that impact stages of that journey. You can now access Awareness and Consideration indices that compare your performance to peers using models predictive of consideration and sales. Brand Metrics quantifies the number of customers in the awareness and consideration marketing funnel stages and is built at scale to measure all shopping engagements with your brand on Amazon, not just ad-attributed engagements. Additionally, BM breaks out key shopping engagements at each stage of the shopping journey, along with the Return on Engagement, so you can measure the historical sales following a consideration event or purchase.
    """

    @sp_endpoint('/insights/brandMetrics/report', method='POST')
    def post_report(self, **kwargs) -> ApiResponse:
        r"""Requests a Brand Metrics report.

        Asks the service to generate the report; the answer is a handle, not the
        data. It carries a ``reportId``, a ``status`` and an empty
        ``location``, and the report is produced asynchronously. Pass the
        ``reportId`` to :meth:`get_report` until ``status`` reads
        ``SUCCESSFUL``, then download ``location``.

        Generates the Brand Metrics report in CSV or JSON format. Customize the report by passing a specific categoryTreeName, categoryPath, brandName, reportStartDate, reportEndDate, lookBackPeriod, format or a list of metrics from the available metrics in the metrics field. If an empty request body is passed, report for the latest available report date in JSON format will get generated with all the available brands and metrics for an advertiser. The report may or may not contain the Brand Metrics data for one or more brands depending on data availability.

        Every field is optional. An empty ``body`` generates the latest
        available report in JSON with every brand and metric on the account.

        Request body
            | **categoryTreeName** (string): [optional] The node at the top of a browse tree. It is the start node of a tree. example: us-home
            | **categoryPath** (array): [optional] The hierarchical path that leads to a node starting with the root node. If no Category Node Name is passed, then all data available for all brands belonging to the entity are retrieved. example: List [ "Categories", "Snack Food", "Granola & Snack Bars" ]]

            | **brandName** (string): [optional] Brand Name. If no Brand Name is passed, then all data available for all brands belonging to the entity are retrieved. example: Mattress Mogul
            | **reportStartDate** (string($date)): [optional] Retrieves metrics with metricsComputationDate between reportStartDate and reportEndDate (inclusive). The date will be in the Coordinated Universal Time (UTC) timezone in YYYY-MM-DD format. If no date is passed in reportStartDate, all available metrics with metricsComputationDate till the reportEndDate will be provided. If no date is passed for either reportStartDate or reportEndDate, the metrics with the most receont metricsComputationDate will be returned. example: 2021-01-01
            | **lookBackPeriod** (string) [optional] Currently supported values: "1W" (one week), "1M" (one month) and "1CM" (one calendar month), which is the enum the v1 contract declares; the v1.1 contract declares the lower case forms and the service accepted both. This defines the period of time used to determine the number of shoppers in the metrics computation. default: 1w
            | **format** (string) [optional] Format of the report. [ JSON, CSV ]. default: JSON
            | **metrics** (list) [optional] Specify an array of string of metrics field names to include in the report. If no metric field names are specified, all metrics are returned.
            | **reportEndDate** (string($date)) [optional] Retrieves metrics with metricsComputationDate between reportStartDate and reportEndDate (inclusive). The date will be in the Coordinated Universal Time (UTC) timezone in YYYY-MM-DD format. If no date is passed in reportEndDate, all available metrics with metricsComputationDate from the reportStartDate will be provided. If no date is passed for either reportStartDate or reportEndDate, the metrics with the most receont metricsComputationDate will be returned. example: 2021-01-30

        The contract names the two category fields ``categoryTreeName`` and
        ``categoryPath``, while the answers come back carrying
        ``categoryNodeTreeName`` and ``categoryNodeName``. Neither spelling
        filters: both were sent with different values, and a tree name that does
        not exist (``zz-no-existe-zz``) was answered with the account's full set
        exactly like a real one. Send the contract names, but do not expect them
        to narrow the report -- filter on ``brandName`` and the date range
        instead, which are the fields the service was seen to honour.

        Returns:
            ApiResponse. ``payload`` holds:

            - ``reportId`` (string): the handle for :meth:`get_report`.
            - ``status`` (string): ``IN_PROGRESS`` on a fresh request.
            - ``statusDetails`` (string): a sentence describing that status.
            - ``expiration`` (integer): how long the result stays available.
            - ``format`` (string): echoes the requested format.
            - ``location`` (string): empty until the report is ready.

        Example:

        .. code-block:: python

            from ad_api.api import BrandMetrics

            bm = BrandMetrics(account="my_account")
            bm.post_report(body={"format": "JSON", "lookBackPeriod": "1w"}).payload
            # {'reportId': '8d3e7143-...', 'status': 'IN_PROGRESS',
            #  'statusDetails': 'Generation of the report is in progress!',
            #  'expiration': 300000, 'format': 'JSON', 'location': ''}

        """
        return self._request(fill_query_params(kwargs.pop('path')), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)

    @sp_endpoint('/insights/brandMetrics/report/{}', method='GET')
    def get_report(self, reportId, **kwargs) -> ApiResponse:
        r"""Gets a previously requested report specified by identifier.

        This is the polling call. A report is generated asynchronously, so call
        this with the ``reportId`` that :meth:`post_report` returned until
        ``status`` reads ``SUCCESSFUL``; only then does ``location`` carry
        a signed S3 address that can be downloaded.

        Keyword Args
            | path **reportId** (string): [required] The report Id to be fetched.

        Returns:
            ApiResponse. ``payload`` holds:

            - ``status`` (string): ``IN_PROGRESS``, ``SUCCESSFUL`` or a
              failure status.
            - ``statusDetails`` (string): the sentence behind that status.
            - ``location`` (string): the signed URL, empty until success.
            - ``format`` (string): the format the report was generated in.
            - ``expiration`` (integer): how long the result stays available.
            - ``brandsInfo`` (array): the brands the report covers, each with
              ``id`` and ``name``. Absent while the report is still running.

        An unknown identifier is not a ``404``: the service answers ``400``
        with ``NoDataFoundException`` and a message naming the id, which means
        the route ran and looked it up.
        """
        return self._request(fill_query_params(kwargs.pop('path'), reportId), params=kwargs)

    def download_report(self, **kwargs) -> ApiResponse:
        r"""Downloads the report previously get report specified by location
        (this is not part of the official Amazon Advertising API, is a helper
        method to download the report).

        In this API the url is self-authorized so to avoid double authorization
        we pass a simple header to ovrewrite the API auth headers that will lead
        to an error.

        kwarg parameter **file** if not provided will take the default amazon
        name from path download (add a path with slash / if you want a specific
        folder, do not add extension as the return will provide the right
        extension based on format choosed if needed)

        kwarg parameter **format** if not provided a format will return a url
        to download the report (this url has a expiration time)

        Keyword Args
            | **url** (string): [required] The location obatined from get_report.
            | **file** (string): [optional] The path to save the file if mode is download `json`, `zip` or `gzip`.
            | **format** (string): [optional] The mode to download the report: `raw`, `url`, `json`, `csv`,  Default (`url`)

        Returns:
            ApiResponse
        """
        headers = {'Accept': '*/*'}
        return self._download(self, params=kwargs, headers=headers)
