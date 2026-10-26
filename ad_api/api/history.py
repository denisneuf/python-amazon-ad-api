from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class History(Client):
    """ """

    @sp_endpoint('/history', method='POST')
    def get_history(self, version: str = "1.0", **kwargs) -> ApiResponse:
        r"""
        Returns the changes made to campaigns, ad groups, ads and the rest of the
        entity tree, within a time range. Only events belonging to the
        authenticated advertiser come back.

        Keyword Args

        - ``version`` (string): the ``Accept`` version, ``"1.0"`` by default.
          Pass ``"1.1"`` to query the ``THEME`` event type, which the service
          refuses at 1.0. The other six types work at either. [optional]

        Request Body (required)

        - ``fromDate`` (integer): epoch in **milliseconds**, not seconds.
        - ``toDate`` (integer): epoch in milliseconds.
        - ``eventTypes`` (object): one or more of ``AD``, ``AD_GROUP``,
          ``CAMPAIGN``, ``KEYWORD``, ``NEGATIVE_KEYWORD``, ``PRODUCT_TARGETING``
          and ``THEME``. Each carries an object, usually ``{}`` or
          ``{"filters": [...]}``.
        - ``count`` (integer): page size. Default 100, minimum 50, maximum 200.
        - ``nextToken`` (string): token from a previous answer. Mutually
          exclusive with ``pageOffset``.
        - ``pageOffset`` (integer): alternative to ``nextToken``, up to 10000.
        - ``sort`` (object): ``{"direction": "ASC"|"DESC", "key": "DATE"}``.

        The field names are camelCase and the service rejects anything else: a
        body written with ``from_date`` answers ``400`` naming ``fromDate`` as a
        required field. The dates are counted back from the moment of the
        request, so a window computed once and reused drifts out of range: the
        service measures 90 days from its own clock, and a few seconds of drift
        past the edge answers ``400 fromDate is more than 90 days ago``.

        This route throttles. Seven calls within twelve seconds answered ``429``.

        Returns
            ApiResponse with ``events``, ``pageSize``, ``pageOffset``,
            ``maxPageNumber`` and ``totalRecords``. An empty ``events`` with
            ``totalRecords`` at ``0`` means the account saw no change in the
            window, not that the call failed.

        """
        accept = 'application/vnd.historyresponse.v' + version + '+json'
        headers = {'Accept': accept}
        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)
