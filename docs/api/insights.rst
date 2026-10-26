Insights
========

`https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Insights_prod_3p.json`_

.. _https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Insights_prod_3p.json: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Insights_prod_3p.json

Returns the audiences that overlap with the one given, ranked by affinity.

.. autoclass:: ad_api.api.Insights
    :members:

    .. warning::

        Only version **2** answers. Version 1 was retired and replies
        ``415 Unsupported Media Type``, naming v2 as the sole supported type.
        The method defaults to 2, so a call without ``version`` works; a call
        that passes ``version=1`` does not.

    ### Endpoint map

    .. list-table::
        :header-rows: 1

       * - Path
         - Method
         - Media type
         - Answer
       * - ``GET /insights/audiences/{audienceId}/overlappingAudiences``
         - ``get_insights``
         - ``vnd.insightsaudiencesoverlap.v2``
         - ``200``
       * - same path with ``version=1``
         - ``get_insights``
         - ``vnd.insightsaudiencesoverlap.v1``
         - ``415``

    ### Parameters

    .. list-table::
        :header-rows: 1

       * - Parameter
         - Kind
         - Effect
       * - ``audienceId``
         - path, required
         - The audience to measure against.
       * - ``adType``
         - query
         - ``SD`` or ``DSP``. Required in practice: leave it out and the
           service assumes ``DSP`` and complains about ``advertiserId`` instead.
       * - ``advertiserId``
         - query
         - Required for ``DSP``, ignored for ``SD``.
       * - ``audienceCategory``
         - query
         - Keeps that category only, such as ``"In-market"``. A plain string,
           despite the contract calling it an array. **Applied.**
       * - ``maxResults``
         - query
         - How many overlaps to return, default 30. **Applied**: the count
           follows it.
       * - ``nextToken``
         - query
         - Token from a previous answer. Repeat the same parameters on later
           calls.
       * - ``minimumAudienceSize``
         - query
         - **Ignored.** Accepted, answered with 200, no effect on the result.
       * - ``maximumAudienceSize``
         - query
         - **Ignored.** Same.
       * - ``minimumOverlapAffinity``
         - query
         - **Ignored.** Same.
       * - ``maximumOverlapAffinity``
         - query
         - **Ignored.** Not exercised in testing, but the minimum is ignored and
           the pair travel together in the contract.

    .. warning::

        A filter that was never applied answers ``200`` with the same count as
        one that matched everything. Compare the number of
        ``overlappingAudiences`` between calls, not the status, before trusting
        that a parameter did anything.

    ### Answer

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Meaning
       * - ``requestedAudienceMetadata``
         - object
         - The audience the query was built from: id, name, category and
           ``audienceForecast``.
       * - ``overlappingAudiences``
         - array
         - Each carries ``audienceMetadata`` and ``affinity``, where a higher
           number means a closer match.
       * - ``marketplace``
         - string
         - The market the answer belongs to.
       * - ``nextToken``
         - string
         - Present when more pages exist.

    ### Example python

    .. code-block:: python

        from ad_api.api import Insights

        client = Insights(account='my_account', debug=False)

        # version is 2 by default; passing 1 answers 415
        res = client.get_insights(audienceId="431221496046405041", adType="SD")
        payload = res.payload

        print(payload["marketplace"])
        for row in payload["overlappingAudiences"]:
            print(row["audienceMetadata"]["name"], row["affinity"])

    ### Example narrowing the result

    These two parameters are the ones that change the answer.

    .. code-block:: python

        from ad_api.api import Insights

        client = Insights(account='my_account', debug=False)

        res = client.get_insights(
            audienceId="431221496046405041",
            adType="SD",
            audienceCategory="In-market",
            maxResults=10,
        )
        print(len(res.payload["overlappingAudiences"]))   # 10

    ### Reading every page

    ``Utils.load_all_categories`` walks the pages for you. It needs the same
    parameters repeated on every call, which the decorator handles.

    .. code-block:: python

        import logging
        from ad_api.api import Insights
        from ad_api.base import Utils

        @Utils.load_all_categories(throttle_by_seconds=5, next_token_param="nextToken")
        def get_all_categories(**kwargs):
            return Insights(account='my_account', debug=False).get_insights(**kwargs)

        if __name__ == '__main__':
            for page in get_all_categories(
                    audienceId="431221496046405041", adType="SD", maxResults=10):
                for row in page.payload.get("overlappingAudiences", []):
                    logging.info(row.get("affinity"))
