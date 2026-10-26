from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Invoices(Client):
    @sp_endpoint('/invoices', method='GET')
    def list_invoices(self, **kwargs) -> ApiResponse:
        r"""
        Get invoices for advertiser. Requires one of these permissions: ["nemo_transactions_view","nemo_transactions_edit"]

            query **invoiceStatuses**:*string* | Optional. Available values : ISSUED, PAID_IN_PART, PAID_IN_FULL, WRITTEN_OFF. (Not documented: ACCUMULATING)

            query **count**:*string* | Optional. Number of records to include in the paged response. Defaults to 100. Cannot be combined with the cursor parameter.

            query **cursor**:*string* | Optional. A cursor representing how far into a result set this query should begin. In the absence of a cursor the request will default to start index of 0 and page size of 100.


        Returns:

            ApiResponse whose payload carries a second layer::

                {"status": "success",
                 "payload": {"nextCursor": "...", "invoiceSummaries": [...]}}

            The invoices sit at ``res.payload["payload"]["invoiceSummaries"]``.
            Reading ``res.payload["invoiceSummaries"]`` gives ``None``, because
            that key belongs to the inner object.

        """
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/invoices/{}', method='GET')
    def get_invoice(self, invoiceId, **kwargs) -> ApiResponse:
        r"""
        Get invoice data by invoice ID. Requires one of these permissions: ["nemo_transactions_view","nemo_transactions_edit"]

            path **invoiceId**:*string* | required. ID of invoice to fetch

        Returns:

            ApiResponse with the same two layers as ``list_invoices``: the
            invoice data sits under ``res.payload["payload"]``.

        """
        return self._request(fill_query_params(kwargs.pop('path'), invoiceId), params=kwargs)
