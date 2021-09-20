from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class History(Client):
    """History of entity changes.
    Provides information about changes made to campaigns, adgroups, ads, etc

    """
    @sp_endpoint('/history', method='POST')
    def get_history(self, **kwargs) -> ApiResponse:
        r"""

        Returns history of changes for provided event sources that match the filters and time ranges specified. Only events that belong to the authenticated Advertiser can be queried. All times will be in UTC Epoch format. This API accepts identifiers in either the alphamumeric format (default), or the numeric format. If numeric IDs are supplied, then numeric IDs will be returned otherwise, alphanumeric IDs are returned.

        body: | REQUIRED {'description': 'A HistoryQuery}'

            | **from_date** | **int** | Max 90 days of history.
            | **to_date** | **int** |
            | **event_types**
                | HistoryEventType
            | **next_token** | **str** | token from previous response to get next set of data. | [optional]
            | **page_offset** | **int** | Mutually exclusive with &#39;nextToken&#39;. Max results with pageOffset is 10000. Use nextToken instead for more results. | [optional]
            | **count** | **int** | Requested number of results. Default 100. Minimum 50. Maximum 200. | [optional]
            | **sort**
                | HistorySortParameter
            | **any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)