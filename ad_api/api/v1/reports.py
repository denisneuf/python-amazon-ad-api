from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Reports(Client):
    r"""
    Reports(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified Reports endpoints

    Reports in v1 are asynchronous and take three routes, not the four of the
    entity families:

        POST /adsApi/v1/create/reports      queue a report
        POST /adsApi/v1/retrieve/reports    read its state
        POST /adsApi/v1/delete/reports      drop it

    There is no GET by id: the state is read by posting the id back to
    retrieve, and the pair of routes is what carries the status through
    PENDING, PROCESSING, COMPLETED and FAILED.

    This generation is shaped differently from the v3 reporting route the
    package already ships as ad_api.api.Reports:

        v1 uses fields, v3 uses columns
        v1 has no reportTypeId, adProduct, groupBy or timeUnit at all
        v1 filters are a predicate tree, v3 filters are a flat list
        v1 answers a list of report parts, v3 answers one url

    v1 reports are addressed by advertiser account, and the account travels in
    the body rather than only in the headers.

    The field catalogue is not part of the contract: query.fields accepts any
    string up to 1000 entries and the service decides which ones exist for each
    product, so a wrong name is answered with a 400 naming the accepted values
    rather than with a local rejection.
    """

    @sp_endpoint('/adsApi/v1/create/reports', method='POST')
    def create_report(self, **kwargs) -> ApiResponse:
        r"""
        create_report(body: dict) -> ApiResponse

        Amazon Ads API v1 - Create a report (operationId: AdsApiv1CreateReport)

        Request Body [Required]
            | **accessRequestedAccounts** (list<ReportCreateAccessRequestedAccountItem>) : [required] 1..2000
                | oneOf **advertiserAccountId** (string) : the advertiser account the report is for
                | oneOf **managerAccountId** (string) : the manager account the report is for
            | **reports** (list<ReportCreate>) : [required] exactly 1
                | **format** (ReportFormat) : [required] Enum [ CSV, GZIP_JSON, PARTITIONED_CSV, PARTITIONED_GZIP_JSON ]
                | **periods** (list<CreateReportPeriod>) : [required] exactly 1
                    | **datePeriod** (CreateDatePeriod) : [required]
                        | **startDate** (date) : [required]
                        | **endDate** (date) : [required]
                | **query** (CreateReportingQuery) : [required]
                    | **fields** (list<string>) : [required] 1..1000
                    | **filter** (CreateFilter) : [optional]
                        | **on** (CreateComparisonPredicate)
                            | **field** (string) : [required] pattern ^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$
                            | **comparisonOperator** (ComparisonOperator) : [required] Enum [ EQUALS, IN ]
                            | **values** (list<string>) : [required] 1..2000
                            | **not** (boolean) : [required]
                        | **and** (CreateCompositePredicate)
                            | **filters** (list<CreateFilter>) : [required] 1..10
                | **currencyOfView** (CurrencyCode) : [optional]
                | **managerAccountDspGrouping** (ManagerAccountDspGrouping) : [optional]

        Answer
            207 MultiStatus with success[] carrying the created report ids and
            error[] carrying the index and reason of the ones refused.

        Requires one of these permissions:
            ManagerAccount_Dev, advertiser_campaign_edit, nemo_report_view,
            MasterAccount_Viewer, MA_ReadOnly, advertiser_campaign_view,
            reports_edit, MasterAccount_Manager, nemo_report_edit,
            view_performance_dashboard
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/retrieve/reports', method='POST')
    def retrieve_report(self, **kwargs) -> ApiResponse:
        r"""
        retrieve_report(body: dict) -> ApiResponse

        Amazon Ads API v1 - Retrieve a report by id (operationId: AdsApiv1RetrieveReport)

        Request Body [Required]
            | **reportIds** (list<string>) : [required] exactly 1

        Answer
            The report object, with the members that matter here:

            | **reportId** (string)
            | **status** (ReportStatus) : Enum [ COMPLETED, FAILED, PENDING, PROCESSING ]
            | **format** (ReportFormat)
            | **periods** (list<ReportPeriod>)
            | **query** (ReportingQuery) : the fields and filter the report was built from
            | **creationDateTime**, **lastUpdatedDateTime**, **completedDateTime** (date-time)
            | **failureCode** (string), **failureReason** (string) : set when status is FAILED
            | **warnings** (list<ReportWarning>) : non-fatal notes about the generated report
            | **completedReportParts** (list<ReportPart>) : 0..100
                | **url** (string) : signed download url for this part
                | **urlExpirationDateTime** (date-time)
                | **sizeInBytes** (int64) : up to 100GB for a single part

            A report split in parts answers more than one entry, so a caller that
            only reads the first url loses data.

        Requires one of these permissions:
            none declared
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/delete/reports', method='POST')
    def delete_report(self, **kwargs) -> ApiResponse:
        r"""
        delete_report(body: dict) -> ApiResponse

        Amazon Ads API v1 - Delete a report by id (operationId: AdsApiv1DeleteReport)

        Request Body [Required]
            | **reportIds** (list<string>) : [required] exactly 1

        Requires one of these permissions:
            none declared
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
