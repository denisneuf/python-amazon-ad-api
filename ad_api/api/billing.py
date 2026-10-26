from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class Billing(Client):
    @sp_endpoint('/billing/statuses', method='POST')
    def list_billing_status(self, **kwargs) -> ApiResponse:
        r"""
        Get the billing status for a list of advertising accounts.

        Request Body
            | Bulk Get Billing Statuses Request Body {
            | The properties needed to get the billing statuses for a set of advertisers.
            | **advertiserMarketplaces**\* (array) minItems: 0 maxItems: 100 [
            |   advertiserMarketplace {
            |       **marketplaceId**\* (string)
            |       **advertiserId**\* (string)
            |       }
            |   ]
            | **locale** (string) Locale. Enum: ['ar_AE', 'cs_CZ', 'de_DE', 'en_AU', 'en_CA', 'en_GB', 'en_IN', 'en_SG', 'es_ES', 'es_MX', 'fr_CA', 'fr_FR', 'he_IL', 'hi_IN', 'it_IT', 'ja_JP', 'ko_KR', 'nl_NL', 'pl_PL', 'pt_BR', 'sv_SE', 'ta_IN', 'tr_TR', 'zh_CN', 'zh_TW']
            | }
        Returns
            ApiResponse
        """

        request_contentType = 'application/vnd.bulkgetbillingstatusrequestbody.v1+json'
        accept_contentType = 'application/vnd.bulkgetbillingstatusresponse.v1+json'
        headers = {'Content-Type': request_contentType, 'Accept': accept_contentType}

        body = Utils.convert_body(kwargs.pop('body'), False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/billing/notifications', method='POST')
    def list_billing_notifications(self, **kwargs) -> ApiResponse:
        r"""
        Get the billing notifications for a list advertising accounts.

        Request Body
            | Bulk Get Billing Notifications Request Body {
            | The properties needed to get the billing notifications for a set of advertisers.
            | **advertiserMarketplaces**\* (array) minItems: 0 maxItems: 100 [
            |   advertiserMarketplace {
            |       **marketplaceId**\* (string)
            |       **advertiserId**\* (string)
            |       }
            |   ]
            | **locale** (string) Locale. Enum: ['ar_AE', 'cs_CZ', 'de_DE', 'en_AU', 'en_CA', 'en_GB', 'en_IN', 'en_SG', 'es_ES', 'es_MX', 'fr_CA', 'fr_FR', 'he_IL', 'hi_IN', 'it_IT', 'ja_JP', 'ko_KR', 'nl_NL', 'pl_PL', 'pt_BR', 'sv_SE', 'ta_IN', 'tr_TR', 'zh_CN', 'zh_TW']
            | }
        Returns
            ApiResponse
        """

        request_contentType = 'application/vnd.billingnotifications.v1+json'
        accept_contentType = 'application/vnd.bulkgetbillingnotificationsresponse.v1+json'
        headers = {'Content-Type': request_contentType, 'Accept': accept_contentType}

        body = Utils.convert_body(kwargs.pop('body'))
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/billing/paymentMethods/list', method='POST')
    def get_customer_payment_methods(self, **kwargs) -> ApiResponse:
        r"""
        Lists the ways this account can pay.

        Query

        - ``criteriaType`` (string): required. ``PAY_NOW`` or ``AUTO_PAY``. The
          service answers ``400 Value null at 'criteriaType' failed to satisfy
          constraint`` when it is missing. It does not go in the body; this route
          takes no body.

        Returns
            ApiResponse carrying five lists, always the same five, some empty:

            - ``creditCardPaymentMethods``
            - ``externalDeductFromPaymentPaymentMethods``
            - ``externalPayByInvoicePaymentMethods``
            - ``payByInvoicePaymentMethods``
            - ``sellerPayablePaymentMethods``

            A card entry carries ``brand``, ``tail`` (the last four digits),
            ``expiryDetails`` with ``month`` and ``year``, ``eligibleCountries``
            and an ``instrumentId`` that identifies the instrument for later
            calls. Treat the ``instrumentId`` as a credential.

        """
        accept_contentType = 'application/vnd.paymentmethods.v1+json'
        headers = {'Accept': accept_contentType}
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)

    @sp_endpoint('/billing/invoices/pay', method='POST')
    def pay_invoices(self, **kwargs) -> ApiResponse:
        r"""
        Collects the outstanding balance for one or more countries.

        This does not name invoices. The body carries no invoice ids: it names the
        countries whose debt is collected, and the service settles whatever is
        open there through a payment agreement. To read which invoices exist, use
        ``Invoices.list_invoices``.

        .. warning::

            Written from the contract. No live call was possible: the account
            held no ISSUED invoice, and ``EXECUTE`` moves money.

        Request Body (required)

        - ``idempotenceId`` (string): required, and the only required member. Two
          requests carrying the same id are treated as one, so a retry after a
          timeout does not charge twice.
        - ``mode`` (string): ``EXECUTE`` charges, ``PREVIEW`` simulates and moves
          nothing. Use ``PREVIEW`` to check a body before committing to it.
        - ``paymentAgreementId`` (string): the agreement to charge, whose payment
          profile decides the method. Omit it and the advertiser's latest
          agreement is used.
        - ``reasonLocale`` (string): the locale of the reason text, such as
          ``es_ES``.
        - ``targetCountryCodes`` (array): the countries whose balance is
          collected. This is what selects the debt.

        Returns
            ApiResponse carrying ``success`` and ``failure``, both always present.
            An empty ``failure`` means every collection went through. A ``200``
            does not by itself mean the money moved: read ``failure``.

        """
        accept_contentType = 'application/vnd.invoices.v1+json'
        headers = {'Accept': accept_contentType}
        body = Utils.convert_body(kwargs.pop('body'), False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/billing/paymentAgreements/list', method='POST')
    def get_payment_agreements(self, **kwargs) -> ApiResponse:
        r"""
        Lists the payment agreements this account holds.

        Query

        - ``agreementType`` (string): required. ``AUTO_PAY`` or ``PAY_NOW``. The
          service answers ``400 Value null at 'agreementType' failed to satisfy
          constraint`` when it is missing. It does not go in the body; this route
          takes no body.

        Returns
            ApiResponse with ``paymentAgreements``, a list. An account that pays
            automatically holds ``AUTO_PAY`` agreements and answers an empty list
            for ``PAY_NOW``, and the reverse, so an empty answer here means the
            account holds none of that type rather than that the call failed.

            Each agreement carries a ``paymentAgreementId`` and a
            ``paymentProfile`` whose ``paymentMethods`` are ordered by
            ``priority``, starting at 0. The lowest priority is tried first and
            the next covers if it cannot be charged.

        """
        accept_contentType = 'application/vnd.paymentagreements.v1+json'
        headers = {'Accept': accept_contentType}
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)

    @sp_endpoint('/billing/paymentAgreements', method='POST')
    def create_payment_agreements(self, **kwargs) -> ApiResponse:
        r"""
        Creates a payment agreement, which decides how an account gets charged.

        .. warning::

            Written from the contract, and the contract describes this route
            thinly: it names the media type and nothing else. No body is
            documented here because none is documented there, and the call was
            not made because a payment agreement is not something to create by
            way of a test.

            What the route takes can be inferred from
            ``get_payment_agreements``, which returns the shape it produces: an
            agreement carries a ``paymentProfile`` whose ``paymentMethods`` are
            ordered by ``priority``. Building one means naming those methods.

            Read the live schema before using this. Until then, treat the body as
            unknown rather than copying a guess from here.

        Returns
            ApiResponse with the created agreement, in the shape
            ``get_payment_agreements`` lists.

        """
        accept_contentType = 'application/vnd.paymentagreements.v1+json'
        headers = {'Accept': accept_contentType}
        body = Utils.convert_body(kwargs.pop('body'), False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/invoiceSummaries/list', method='POST')
    def invoice_summaries(self, **kwargs) -> ApiResponse:
        r"""
        Lists invoice summaries with filters, sorting and paging.

        This is the route to reach for when the question is "which invoices fall
        in this period". ``Invoices.list_invoices`` returns a flat page and leaves
        the filtering to the caller; this one filters on the service, by issued
        date, due date, status, country, invoice number and payment method.

        Note the date format. Here it is ISO-8601 with the date alone,
        ``"2026-09-01"``. ``Invoices.list_invoices`` answers dates as
        ``"20260902"``. The two shapes are not interchangeable.

        Request Body (optional)

        Every member is optional. An empty object returns the first page.

        - ``invoiceIssuedDateRangeFilter`` (object): ``startDate`` and
          ``endDate``, both inclusive, both ``"YYYY-MM-DD"``.
        - ``invoiceDueDateRangeFilter`` (object): same shape, for the due date.
        - ``statusValueFilter`` (object): ``include``, a list of statuses such as
          ``PAID_IN_FULL`` or ``ACCUMULATING``.
        - ``countryValueFilter`` (object): ``include``, up to 30 country codes.
        - ``invoiceNumberFilter`` (object): ``include``, up to 30 invoice numbers.
        - ``paymentMethodTypeValueFilter`` (object): ``include``, up to 10 method
          types.
        - ``reserveOrderNumberFilter`` (object): ``include``, up to 30 reserve
          order numbers.
        - ``sort`` (object): ``attribute`` and ``direction``. The only
          attributes the service accepts are ``invoiceIssuedDate`` and
          ``invoiceDueDate``; anything else answers
          ``400 Invalid input because of error(s): [sort:attribute field is
          invalid]``. Those are the names the answer uses, not the filter names:
          ``invoiceDate``, ``issuedDate``, ``dueDate``, ``amountDue`` and
          ``status`` are all refused.
        - ``maxResults`` (integer): page size.
        - ``nextToken`` (string): token from a previous answer.
        - ``aggregation`` (object): ``attribute`` and ``groupBy``, to total
          rather than list.

        The ``include`` filters also accept ``queryTermMatchType``, which decides
        how the term is matched.

        Returns
            ApiResponse with ``invoiceSummaries``. Each entry is richer than what
            ``Invoices.list_invoices`` returns and shaped differently: dates come
            as ``"2026-10-26"`` rather than ``"20261026"``, and most fields are
            ``{"code": ..., "value": ...}`` pairs rather than plain strings. A
            summary carries ``id``, ``invoiceIssuedDate``, ``invoiceDueDate``,
            ``amountDue`` and ``remainingAmountDue`` (each with a
            ``currencyCode`` and a ``value``), ``status``, ``paymentStatus``,
            ``country``, ``product``, ``paymentMethodType``, ``invoicingLevel``
            and ``fxInformation``.

        """
        headers = {
            'Accept': 'application/vnd.billingInvoiceSummary.v1+json',
            'Content-Type': 'application/vnd.billingInvoiceSummary.v1+json',
        }
        body = Utils.convert_body(kwargs.pop('body'), False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/billingProfiles/list', method='POST')
    def list_billing_profiles(self, **kwargs) -> ApiResponse:
        r"""
        Lists the billing profiles of the account.

        A billing profile decides who gets invoiced and with which payment
        method, so this is the starting point before reading usages or creating
        a statement.

        Request Body (optional)

        - ``filters`` (object): narrow the list.
        - ``maxResults`` (integer): page size.
        - ``nextToken`` (string): token from a previous answer.

        .. warning::

            The service refuses marketplace accounts. Called from a regional
            seller account it answers ``400 The API doesnot support marketplace
            accounts``. It wants a Global, Manager or Sponsored Ads account.

        Returns
            ApiResponse with the profiles and the token for the next page.

        """
        headers = {
            'Accept': 'application/vnd.billingProfile.v1+json',
            'Content-Type': 'application/vnd.billingProfile.v1+json',
        }
        body = Utils.convert_body(kwargs.pop('body'), False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/billingProfileUsages/list', method='POST')
    def list_billing_profile_usages(self, **kwargs) -> ApiResponse:
        r"""
        Lists which billing profile each country uses.

        The answer links a country to a ``billingProfileId``. With
        ``expandBillingProfile`` it carries the whole profile rather than the
        identifier.

        Request Body (optional)

        - ``expandBillingProfile`` (boolean): return the full profile, not only
          its id.
        - ``expandFallbackBillingProfile`` (boolean): also return the profile
          that would apply if the main one could not be used.
        - ``filters`` (object): narrow by country or profile.
        - ``maxResults`` (integer): page size.
        - ``nextToken`` (string): token from a previous answer.

        .. warning::

            Same account restriction as ``list_billing_profiles``, and the
            message names what it wants: ``only Global, Manager and Sponsored
            Ads marketplace accounts are supported``.

        Returns
            ApiResponse with one entry per country and profile pairing.

        """
        headers = {
            'Accept': 'application/vnd.billingProfileUsage.v1+json',
            'Content-Type': 'application/vnd.billingProfileUsage.v1+json',
        }
        body = Utils.convert_body(kwargs.pop('body'), False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/billing/documents/{}', method='GET')
    def get_billing_document(self, documentId, **kwargs) -> ApiResponse:
        r"""
        Reads one billing document.

        Path

        - ``documentId`` (string): required.

        Query

        - ``docType`` (string): required in practice, though the contract lists
          it as a plain parameter. Without it the service answers
          ``400 Value null at 'docType' failed to satisfy constraint``.

        Returns
            ApiResponse with the document.

        """
        headers = {'Accept': 'application/vnd.billingDocuments.v1+json'}
        return self._request(fill_query_params(kwargs.pop('path'), documentId),
                             params=kwargs, headers=headers)

    @sp_endpoint('/billingProfileAgreementContents/{}', method='GET')
    def get_billing_profile_agreement_content(self, billingProfileAgreementContentId, **kwargs) -> ApiResponse:
        r"""
        Reads the agreement text attached to a billing profile.

        Path

        - ``billingProfileAgreementContentId`` (string): required.

        Query

        - ``languageOfPreference`` (string): the language the text comes back in.

        Returns
            ApiResponse with the agreement content.

        """
        headers = {'Accept': 'application/vnd.billingProfileAgreement.v1+json'}
        return self._request(
            fill_query_params(kwargs.pop('path'), billingProfileAgreementContentId),
            params=kwargs, headers=headers)

    @sp_endpoint('/billingStatements/{}', method='GET')
    def get_billing_statement(self, billingStatementRequestId, **kwargs) -> ApiResponse:
        r"""
        Reports on a billing statement request.

        The identifier comes from the route that creates the statement request,
        and this reads its progress or its result.

        .. note::

            The contract answers this read with
            ``vnd.createbillingstatementsrequest.v1``, the same media type the
            creation route uses. That is what it declares, odd as the name is.

        Path

        - ``billingStatementRequestId`` (string): required. Three names are in
          play for this one value: the contract calls it
          ``billingStatementRequestId``, the method takes
          ``billingStatementRequestId``, and a rejected call comes back naming
          ``billingStatementId``.

        The error for a malformed value also mentions a ``request`` parameter the
        contract does not list.

        Returns
            ApiResponse with the state of that request.

        """
        headers = {'Accept': 'application/vnd.createbillingstatementsrequest.v1+json'}
        return self._request(fill_query_params(kwargs.pop('path'), billingStatementRequestId),
                             params=kwargs, headers=headers)

    @sp_endpoint('/billingStatements', method='POST')
    def create_billing_statement(self, **kwargs) -> ApiResponse:
        r"""
        Asks the service to generate a billing statement for a period.

        The work is asynchronous. This answers a ``requestId``, and
        ``get_billing_statement`` reads the state of that request.

        Request Body (required)

        - ``startDate`` (string): required. The first day of the period.
        - ``endDate`` (string): required. The last day of the period.
        - ``locale`` (string): required. The language the statement comes back
          in.
        - ``countryCodes`` (array): the countries to cover.
        - ``format`` (string): ``CSV`` is the only value the contract lists.

        Returns
            ApiResponse with the request identifier. The contract answers
            ``207``, a multi-status, not ``200``.

        """
        headers = {
            'Accept': 'application/vnd.createbillingstatementsrequest.v1+json',
            'Content-Type': 'application/vnd.createbillingstatementsrequest.v1+json',
        }
        body = Utils.convert_body(kwargs.pop('body'), False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/billingProfileUsages', method='POST')
    def apply_billing_profile(self, **kwargs) -> ApiResponse:
        r"""
        Links one or more countries to a billing profile.

        The service calls this applying a profile: after it, the countries named
        charge through that profile.

        Request Body (required)

        - ``billingProfileUsages`` (array): required. One entry per country and
          profile pairing, which reads back in the same shape
          ``list_billing_profile_usages`` returns.

        The contract does not describe the fields inside each entry, so read one
        back from ``list_billing_profile_usages`` before building a body here.

        .. warning::

            Not exercised. Applying a profile changes how an account gets
            charged.

        Returns
            ApiResponse. The contract answers ``207``, a multi-status, not
            ``200``.

        """
        headers = {
            'Accept': 'application/vnd.billingProfileUsage.v1+json',
            'Content-Type': 'application/vnd.billingProfileUsage.v1+json',
        }
        body = Utils.convert_body(kwargs.pop('body'), False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/billingProfiles', method='POST')
    def create_billing_profiles(self, **kwargs) -> ApiResponse:
        r"""
        Creates one or more billing profiles.

        Request Body (required)

        - ``billingProfiles`` (array): required, between 0 and 100 entries. Each
          one describes a profile to create.

        The contract names the list and stops there: the fields of an entry are
        not described. Read one back from ``list_billing_profiles`` for the
        shape, rather than guessing at it.

        .. warning::

            Not exercised. Creating a billing profile changes how an account gets
            invoiced.

        Returns
            ApiResponse. The contract answers ``207``, a multi-status, not
            ``200``.

        """
        headers = {
            'Accept': 'application/vnd.billingProfile.v1+json',
            'Content-Type': 'application/json',
        }
        body = Utils.convert_body(kwargs.pop('body'), False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/billingProfiles', method='PUT')
    def update_billing_profiles(self, **kwargs) -> ApiResponse:
        r"""
        Updates one or more billing profiles.

        Request Body

        - ``billingProfiles`` (array): between 0 and 100 entries. Each one names
          a profile and the fields to change.

        The same gap as ``create_billing_profiles``: the contract does not
        describe the fields inside an entry.

        .. warning::

            Not exercised, for the same reason as the create route.

        Returns
            ApiResponse. The contract answers ``207``, a multi-status, not
            ``200``.

        """
        headers = {
            'Accept': 'application/vnd.billingProfile.v1+json',
            'Content-Type': 'application/json',
        }
        body = Utils.convert_body(kwargs.pop('body'), False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/billing/paymentProfiles', method='POST')
    def create_payment_profiles(self, **kwargs) -> ApiResponse:
        r"""
        Creates one or more payment profiles.

        Request Body (required)

        - ``paymentProfiles`` (array): required. Each entry describes a profile:
          which payment methods to use and in what order.

        The contract names the list and does not describe its entries. The shape
        of a payment method reads back from ``get_payment_agreements``, whose
        agreements carry a ``paymentProfile`` holding ``paymentMethods`` ordered
        by ``priority``.

        .. warning::

            Not exercised. A payment profile decides where money is taken from.

        Returns
            ApiResponse. The contract answers ``207``, a multi-status, not
            ``200``.

        """
        headers = {
            'Accept': 'application/vnd.paymentprofiles.v1+json',
            'Content-Type': 'application/json',
        }
        body = Utils.convert_body(kwargs.pop('body'), False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)
