import json

from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Reports(Client):
    @sp_endpoint("/attribution/report", method="POST")
    def post_report(self, **kwargs) -> ApiResponse:
        """Gets an attribution report for a specified list of advertisers.

        Args:
            **kwargs:

        Request body:
            | **reportType** (string): The type of report. Either `PERFORMANCE` or `PRODUCTS`. It is an optional parameter. If not used in request body, default reportType is `PERFORMANCE`. Each report type is aggregated at different levels. See below table for list of dimensions available within each report type.
            | **advertiserIds** (string): One or more advertiser Ids to filter reporting by. If requesting reporting for multiple advertiser Ids, input via a comma-delimited list.
            | **endDate** (string): The end date for the report, form as "YYYYMMDD"
            | **count** (integer): maximum: 10000, minimum:1, The number of entries to include in the report.
            | **metrics** (string):
            | **startDate** (string): The start date for the report, in "YYYYMMDD" format. For reportType PRODUCTS, startDate can only be within last 90 days from current date.
            | **cursorId** (string): The value of cursorId must be set to null without "", or set to "" for the first request. For each following request, the value of cursorId from the previous response must be included in the current request. Note that for the cursorId values the " character must be escaped with \.

        Returns:
            ApiResponse
        """
        data = json.dumps(kwargs.pop("body"))
        resp = self._request(
            fill_query_params(kwargs.pop("path")),
            data=data,
            params=kwargs,
        )
        resp.set_next_token(resp.payload.pop("cursorId"))
        return resp
