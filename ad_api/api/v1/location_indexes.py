from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class LocationIndexes(Client):
    """
    Manage Smart Location Indexes for a campaign.

    A Smart Location Index is a named dataset that maps postal codes to index
    values, expressing relative audience quality or sales potential for one
    advertiser. The values are supplied by the caller; the service only stores
    and serves them for smart location targeting.

    Writes are asynchronous. Creating or updating an index leaves it in PENDING
    until the service has processed the data, and only then does it read ENABLED
    and become usable for targeting. An index that fails processing carries
    FAILED, or UPDATE_FAILED when it was an existing index being rewritten.

    The contract requires one of advertiser_campaign_edit, campaign_edit,
    dsp_campaign_edit or MasterAccount_Manager to write, and campaign_view
    among others to read. On a Sponsored Ads seller profile this family is not
    reachable: a probe answers 401 Customer <id> is not authorized to access
    account, even though campaign_view is declared as enough.
    """

    @sp_endpoint('/adsApi/v1/create/locationIndexes', method='POST')
    def create_location_index(self, **kwargs) -> ApiResponse:
        r"""
        Creates one or more Smart Location Indexes.

        The index is processed asynchronously: it arrives with status PENDING and
        only turns ENABLED once the service has read the data.

        Request body
            | **locationIndexes** (array): [required] one or more indexes.
                | **indexName** (string): [required] the name of the index.
                | **indexData** (dict): [required] the values.
                | **campaignId** (string): the campaign the index belongs to.
                | **countryCode** (string): one of AU, BE, BR, CA, DE, ES, FR,
                  GB, IE, IN, IT, JP, MX, NL, SE, TR, US.

        Returns:
            | ApiResponse

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/locationIndexes', method='GET')
    def list_location_indexes(self, **kwargs) -> ApiResponse:
        r"""
        Lists every Smart Location Index of the advertiser, with its status.

        Answers a page and a nextToken; when that token is empty there are no
        more pages.

        Keyword Args
            | **maxResults** (int): page size.
            | **nextToken** (string): the token from the previous page.

        Returns:
            | ApiResponse
                | **locationIndexes** (array), **nextToken** (string)

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/retrieve/locationIndexes', method='POST')
    def retrieve_location_indexes(self, **kwargs) -> ApiResponse:
        r"""
        Reads one or more Smart Location Indexes by id.

        An index still in PENDING is being processed and cannot yet be used for
        smart location targeting.

        Request body
            | **indexIds** (array): [required] the identifiers to read.

        Returns:
            | ApiResponse

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/update/locationIndexes', method='POST')
    def update_location_indexes(self, **kwargs) -> ApiResponse:
        r"""
        Replaces the data of existing Smart Location Indexes.

        The supplied values replace the ones the index held. The update is
        asynchronous too: the index returns to PENDING until the new data has
        been processed, and UPDATE_FAILED if that processing fails.

        Request body
            | **locationIndexes** (array): [required] one or more updates.
                | **indexId** (string): [required] the index to rewrite.
                | **indexData** (dict): the new values.

        Returns:
            | ApiResponse

        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
