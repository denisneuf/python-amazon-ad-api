from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


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
