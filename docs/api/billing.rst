Billing
=======
`https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdvertisingBilling_prod_3p.json`_

.. _https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdvertisingBilling_prod_3p.json: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdvertisingBilling_prod_3p.json

Invoices, payments, the methods an account pays with, and the profiles that
decide who gets charged.

.. autoclass:: ad_api.api.Billing
    :members:

    .. note::

        The contract is ``Advertising Billing`` version 3.0 and carries no beta
        marker. Two invoice routes the contract lists, ``GET /invoices`` and
        ``GET /invoices/{invoiceId}``, live in :class:`ad_api.api.Invoices`
        rather than here, where their subject belongs.

    ### Endpoint map

    .. list-table::
        :header-rows: 1

       * - Path
         - Method
         - Kind
         - Answer
       * - ``POST /billing/statuses``
         - ``list_billing_status``
         - read
         - ``200``
       * - ``POST /billing/notifications``
         - ``list_billing_notifications``
         - read
         - ``200``
       * - ``POST /invoiceSummaries/list``
         - ``invoice_summaries``
         - read
         - ``200``
       * - ``POST /billing/paymentMethods/list``
         - ``get_customer_payment_methods``
         - read
         - ``200``
       * - ``POST /billing/paymentAgreements/list``
         - ``get_payment_agreements``
         - read
         - ``200``
       * - ``GET /billing/documents/{documentId}``
         - ``get_billing_document``
         - read
         - ``200``
       * - ``GET /billingProfileAgreementContents/{id}``
         - ``get_billing_profile_agreement_content``
         - read
         - ``200``
       * - ``POST /billingProfiles/list``
         - ``list_billing_profiles``
         - read
         - ``200``
       * - ``POST /billingProfileUsages/list``
         - ``list_billing_profile_usages``
         - read
         - ``200``
       * - ``GET /billingStatements/{requestId}``
         - ``get_billing_statement``
         - read
         - ``200``
       * - ``POST /billing/invoices/pay``
         - ``pay_invoices``
         - write
         - ``200``
       * - ``POST /billing/paymentAgreements``
         - ``create_payment_agreements``
         - write
         - ``200``
       * - ``POST /billing/paymentProfiles``
         - ``create_payment_profiles``
         - write
         - ``207``
       * - ``POST /billingProfiles``
         - ``create_billing_profiles``
         - write
         - ``207``
       * - ``PUT /billingProfiles``
         - ``update_billing_profiles``
         - write
         - ``207``
       * - ``POST /billingProfileUsages``
         - ``apply_billing_profile``
         - write
         - ``207``
       * - ``POST /billingStatements``
         - ``create_billing_statement``
         - write
         - ``207``

    Five of the writes answer ``207``, a multi-status: the answer reports per
    item rather than as a whole.

    ### Two invoice routes, two date formats

    Both read invoices, and they do not agree on much.

    .. list-table::
        :header-rows: 1

       * - 
         - ``Invoices.list_invoices``
         - ``Billing.invoice_summaries``
       * - Dates as
         - ``"20260902"``
         - ``"2026-09-02"``
       * - Fields as
         - plain strings
         - ``{"code": ..., "value": ...}`` pairs
       * - Payload shape
         - ``{"status": "success", "payload": {...}}``
         - ``{"invoiceSummaries": [...]}``
       * - Filtering
         - by the caller
         - on the service
       * - Page control
         - ``count`` and ``cursor``
         - ``maxResults`` and ``nextToken``

    Reading ``Invoices`` needs the extra layer: the invoices sit at
    ``payload["payload"]["invoiceSummaries"]``, and ``payload["invoiceSummaries"]``
    is ``None`` without complaint.

    ### Marketplace accounts are turned away

    The billing profile routes refuse regional seller accounts:

    .. code-block:: text

        POST /billingProfiles/list
        400 The API doesnot support marketplace accounts

        POST /billingProfileUsages/list
        400 Bad request received: only Global, Manager and Sponsored Ads
            marketplace accounts are supported

    That comes from the service, not the package. A Global, Manager or Sponsored
    Ads account reaches them.

    ### The required parameters the contract calls optional

    Three routes name a query parameter without marking it required, and then
    refuse the call when it is missing.

    .. list-table::
        :header-rows: 1

       * - Route
         - Parameter
         - Accepted values
       * - ``get_customer_payment_methods``
         - ``criteriaType``
         - ``PAY_NOW``, ``AUTO_PAY``
       * - ``get_payment_agreements``
         - ``agreementType``
         - ``PAY_NOW``, ``AUTO_PAY``
       * - ``get_billing_document``
         - ``docType``
         - the kind of document

    Each answers ``400`` naming the member it wanted.

    ### Sorting invoice summaries

    ``invoice_summaries`` accepts ``sort`` with an ``attribute`` and a
    ``direction``. The contract types ``attribute`` as a plain string with no
    list of values, and only two are accepted:

    - ``invoiceIssuedDate``
    - ``invoiceDueDate``

    Anything else answers ``400 Invalid input because of error(s):
    [sort:attribute field is invalid]``. Those two are the names the answer uses,
    not the ones the filters use: ``invoiceDate``, ``issuedDate``, ``dueDate``,
    ``amountDue`` and ``status`` are all refused.

    ### pay_invoices does not name invoices

    Its body carries no invoice ids. It names ``targetCountryCodes`` and settles
    the open balance there through a payment agreement:

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Meaning
       * - ``idempotenceId``
         - string
         - Required, and the only required member. The same id twice counts as
           one request, so a retry after a timeout does not charge twice.
       * - ``mode``
         - string
         - ``EXECUTE`` charges. ``PREVIEW`` simulates and moves nothing.
       * - ``paymentAgreementId``
         - string
         - The agreement to charge. Omit it and the latest agreement is used.
       * - ``reasonLocale``
         - string
         - Locale of the reason text, such as ``es_ES``.
       * - ``targetCountryCodes``
         - array
         - The countries whose balance is collected.

    The answer carries ``success`` and ``failure``, both always present, so a
    ``200`` alone does not mean the money moved.

    ### The writes that were not exercised

    Five routes change how an account is charged, and none was called:

    - ``pay_invoices`` — no ``ISSUED`` invoice existed to settle, and
      ``EXECUTE`` moves money
    - ``create_payment_agreements`` — creates a real agreement
    - ``create_payment_profiles`` — a profile decides where money is taken from
    - ``create_billing_profiles`` and ``update_billing_profiles`` — change who
      gets invoiced
    - ``apply_billing_profile`` — relinks countries to a profile
    - ``create_billing_statement`` — starts a job

    Four of them also have entries the contract never describes:
    ``billingProfiles``, ``billingProfileUsages`` and ``paymentProfiles`` are
    named as lists, and what an entry holds is not written down. Read one back
    from the matching list route before building a body.

    ### Example: the invoices of a period

    .. code-block:: python

        from ad_api.api import Billing

        client = Billing(account='my_account', debug=False)

        res = client.invoice_summaries(body={
            "invoiceIssuedDateRangeFilter": {
                "startDate": "2026-09-01",
                "endDate": "2026-10-31",
            },
            "statusValueFilter": {"include": ["PAID_IN_FULL"]},
            "sort": {"attribute": "invoiceIssuedDate", "direction": "DESC"},
            "maxResults": 50,
        })

        for row in res.payload["invoiceSummaries"]:
            print(row["id"],
                  row["invoiceIssuedDate"],
                  row["status"]["code"],
                  row["amountDue"]["value"],
                  row["amountDue"]["currencyCode"])

    ### Example: what the account pays with

    .. code-block:: python

        from ad_api.api import Billing

        client = Billing(account='my_account', debug=False)

        # criteriaType is required even though the contract lists it as optional
        methods = client.get_customer_payment_methods(criteriaType="AUTO_PAY")
        for card in methods.payload["creditCardPaymentMethods"]:
            print(card["brand"], card["tail"], card["expiryDetails"])

        agreements = client.get_payment_agreements(agreementType="AUTO_PAY")
        for agreement in agreements.payload["paymentAgreements"]:
            for method in agreement["paymentProfile"]["paymentMethods"]:
                print(method.get("priority"), method.get("type"), method.get("brand"))

    ### Example: a statement request

    .. code-block:: python

        from ad_api.api import Billing

        client = Billing(account='my_account', debug=False)

        res = client.create_billing_statement(body={
            "startDate": "2026-09-01",
            "endDate": "2026-09-30",
            "locale": "es_ES",
            "countryCodes": ["ES"],
            "format": "CSV",
        })

        # answers 207 and a request id
        request_id = res.payload.get("requestId")
        print(client.get_billing_statement(request_id).payload)
