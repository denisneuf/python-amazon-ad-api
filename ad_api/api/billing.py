from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils

class Billing(Client):

    @sp_endpoint('/billing/statuses', method='POST')
    def list_billing_status(self, **kwargs) -> ApiResponse:
        r"""
        list_billing_status(body: dict or str) -> ApiResponse

        Get the billing status for a list of advertising accounts.

        """

        request_contentType = 'application/vnd.bulkgetbillingstatusrequestbody.v1+json'
        accept_contentType = 'application/vnd.bulkgetbillingstatusresponse.v1+json'
        headers = {'Content-Type': request_contentType, 'Accept': accept_contentType}

        body = Utils.convert_body(kwargs.pop('body'))
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)


    @sp_endpoint('/billing/notifications', method='POST')
    def list_billing_notifications(self, **kwargs) -> ApiResponse:
        r"""

        list_billing_notifications(body: str) -> ApiResponse

        """

        request_contentType = 'application/vnd.billingnotifications.v1+json'
        accept_contentType = 'application/vnd.bulkgetbillingnotificationsresponse.v1+json'
        headers = {'Content-Type': request_contentType, 'Accept': accept_contentType}

        body = Utils.convert_body(kwargs.pop('body'))
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)