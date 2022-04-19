Invoices
========



`https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Billing_prod_3p.json`_

.. _https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Billing_prod_3p.json: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Billing_prod_3p.json

Get invoice data by invoice ID


.. autoclass:: ad_api.api.Invoices

    .. autofunction:: ad_api.api.Invoices.list_invoices

    ### Example getting a list of invoices

    .. code-block:: python

        import logging
        from ad_api.api import Invoices
        from ad_api.base import AdvertisingApiException

        def list_invoices(**kwargs):

            try:

                result = Invoices(account=store, debug=True).list_invoices(
                    **kwargs
                )
                res = result.payload
                payload = res.get("payload")
                invoice_summaries = payload.get("invoiceSummaries")
                for invoice in invoice_summaries:
                    logging.info(invoice)
            except AdvertisingApiException as error:
                logging.info(error)

        # list_invoices()
        list_invoices(invoiceStatuses="PAID_IN_FULL", count=5)

    .. note::

        Here is an example how to get all the invoices full payed using a decorator in Utils @Utils.load_all_pages

    .. code-block:: python

        import logging
        from ad_api.api import Invoices
        from ad_api.base import Utils

        @Utils.load_all_pages(throttle_by_seconds=1, next_token_param="cursor")
        def get_all_invoices(**kwargs):
            return Invoices(account=store, debug=True).list_invoices(**kwargs)

        bill_status = 'PAID_IN_FULL'

        for page in get_all_invoices(invoiceStatuses=bill_status):
            res = page.payload
            payload = res.get("payload")
            invoice_summaries = payload.get("invoiceSummaries")
            for invoice in invoice_summaries:
                logging.info(invoice)

    ### Will Output the invoices

    .. code-block:: python

        {'id': 'DR0012TTY-75', 'status': 'PAID_IN_FULL', 'fromDate': '20210613', 'toDate': '20210625', 'invoiceDate': '20210624', 'amountDue': {'amount': 500.04, 'currencyCode': 'EUR'}, 'taxAmountDue': {'amount': 0.0, 'currencyCode': 'EUR'}, 'remainingAmountDue': {'amount': 0.0, 'currencyCode': 'EUR'}, 'remainingTaxAmountDue': {'amount': 0.0, 'currencyCode': 'EUR'}}

    .. code-block:: python

        {'id': 'DR0012TTY-76', 'status': 'PAID_IN_FULL', 'fromDate': '20210624', 'toDate': '20210703', 'invoiceDate': '20210702', 'amountDue': {'amount': 332.2, 'currencyCode': 'EUR'}, 'taxAmountDue': {'amount': 0.0, 'currencyCode': 'EUR'}, 'remainingAmountDue': {'amount': 0.0, 'currencyCode': 'EUR'}, 'remainingTaxAmountDue': {'amount': 0.0, 'currencyCode': 'EUR'}}

    .. autofunction:: ad_api.api.Invoices.get_invoice

    .. note::

        You could get a specific invoice by invoiceId which is the string provided

    .. code-block:: python

        import logging
        from ad_api.api import Invoices
        from ad_api.base import AdvertisingApiException

        def get_invoice(invoice_id: str):

            try:

                result = Invoices(account=store, debug=True).get_invoice(
                    invoiceId=invoice_id
                )
                logging.info(result)
            except AdvertisingApiException as error:
                logging.info(error)

        amz_invoice_id = 'DR0012TTY-76'
        get_invoice(amz_invoice_id)

    .. warning::

       This API cannot be used in sandbox mode and will return AdvertisingApiException

    .. code-block:: python

        {
            'status_code': 404,
            'code': 'NOT_FOUND',
            'details': 'Could not find resource for full path: https://advertising-api-test.amazon.com/invoices/DR0012TTY-76',
            'requestId': '1A83K31WYACG6YFG0S17'
        }