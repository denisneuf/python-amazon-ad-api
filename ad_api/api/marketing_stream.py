from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class MarketingStream(Client):

    @sp_endpoint('/streams/subscriptions', method='POST')
    def create_stream_subscription(self, version: float = 1.0, **kwargs) -> ApiResponse:
        r"""
        Create a new subscription Note

        Request Body (required)
            | '**notes**':  *string*,  | string <= 128 characters | Additional details associated with the subscription
            | '**clientRequestToken**': *string* | string = [ 22 ... 36 ] characters | Unique value supplied by the caller used to track identical API requests. Should request be re-tried, the caller should supply the same value. We recommend using GUID.
            | '**dataSetId**': *string* | Identifier of data set, callers can be subscribed to. Please refer to https://advertising.amazon.com/API/docs/en-us/amazon-marketing-stream/data-guide for the list of all data sets.
            | '**destinationArn**': *string* | string = [ 20 ... 2048 ] characters | AWS ARN of the destination endpoint associated with the subscription. Supported destination types: SQS
        REQUEST BODY SCHEMA: application/vnd.MarketingStreamSubscriptions.StreamSubscriptionResource.v1.0+json

        Returns
            ApiResponse
        """
        json_version = 'application/vnd.MarketingStreamSubscriptions.StreamSubscriptionResource.v' + str(
            version) + "+json"
        headers = {
            "Accept": json_version,
            "Content-Type": json_version
        }
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body(kwargs.pop('body'), False),
                             params=kwargs,
                             headers=headers)

    @sp_endpoint('/streams/subscriptions', method='GET')
    def list_stream_subscription(self, version: float = 1.0, **kwargs) -> ApiResponse:
        r"""
        List subscriptions Note

        Param:
            | query **maxResults** (string). Optional. number = [ 1 ... 5000 ] desired number of entries in the response, defaults to maximum value
            | query **startingToken** (string). Optional. Token which can be used to get the next page of results, if more entries exist

        Returns
            ApiResponse
        """
        json_version = 'application/vnd.MarketingStreamSubscriptions.StreamSubscriptionResource.v' + str(
            version) + "+json"
        headers = {
            "Accept": json_version,
            "Content-Type": json_version
        }
        return self._request(kwargs.pop('path'),
                             params=kwargs,
                             headers=headers)

    @sp_endpoint('/streams/subscriptions/{}', method='GET')
    def get_stream_subscription(self, subscriptionId, version: float = 1.0, **kwargs) -> ApiResponse:
        r"""
        Retrieves a stream subscription for the specified stream identifier

        Param:
            | query **subscriptionId** (number). Required. The identifier of an existing subscription.

        Returns
            ApiResponse
        """
        json_version = 'application/vnd.MarketingStreamSubscriptions.StreamSubscriptionResource.v' + str(
            version) + "+json"
        headers = {
            "Accept": json_version,
            "Content-Type": json_version
        }
        return self._request(fill_query_params(kwargs.pop('path'), subscriptionId),
                             params=kwargs,
                             headers=headers)

    @sp_endpoint('/streams/subscriptions/{}', method='PUT')
    def update_stream_subscription(self, subscriptionId, version: float = 1.0, **kwargs) -> ApiResponse:
        r"""
        Update an existing subscription

        Param:
            | query **subscriptionId** (number). Required. The identifier of an existing subscription.

        Request Body (required)
            | '**notes**':  *string*,  | string <= 128 characters | Additional details associated with the subscription
            | '**status**':  *string*,  | (UpdateEntityStatus) | Update the status of the entity | Value: "ARCHIVED"
        REQUEST BODY SCHEMA: application/vnd.MarketingStreamSubscriptions.StreamSubscriptionResource.v1.0+json

        Returns
            ApiResponse
        """
        json_version = 'application/vnd.MarketingStreamSubscriptions.StreamSubscriptionResource.v' + str(
            version) + "+json"
        headers = {
            "Accept": json_version,
            "Content-Type": json_version
        }
        return self._request(fill_query_params(kwargs.pop('path'), subscriptionId),
                             data=Utils.convert_body(kwargs.pop('body'), False),
                             params=kwargs,
                             headers=headers)
