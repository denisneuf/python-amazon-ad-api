from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Insights(Client):
    """ """

    @sp_endpoint('/insights/audiences/{}/overlappingAudiences', method='GET')
    def get_insights(self, audienceId: str, version: int = 2, **kwargs) -> ApiResponse:
        r"""
        Returns the audiences that overlap with the one given, ranked by affinity.

        Keyword Args

        - ``version`` (int): the ``Accept`` version. **Only 2 answers**; 1 was
          retired and replies ``415`` naming v2 as the sole supported type.
          Defaults to 2. [optional]

        Path

        - ``audienceId`` (string): required. The audience to measure against.

        Query

        - ``adType`` (string): required in practice, ``SD`` or ``DSP``. When it
          is left out the service assumes ``DSP`` and answers
          ``400 Missing advertiserId parameter for DSP request``, which names the
          wrong parameter. Send it explicitly.
        - ``advertiserId`` (string): required for ``DSP``, ignored for ``SD``.
        - ``audienceCategory`` (string): keep only audiences of that category,
          such as ``"In-market"``. The contract calls it an array; a plain string
          is what the service accepts and applies.
        - ``maxResults`` (integer): how many overlaps to return. Default 30.
          Works, and the count follows it.
        - ``nextToken`` (string): token from a previous answer. Subsequent calls
          must repeat the same parameters.

        Three parameters are accepted and then ignored: ``minimumAudienceSize``,
        ``maximumAudienceSize`` and ``minimumOverlapAffinity``. The call answers
        ``200`` with the same count as without them, so a filter that was never
        applied is indistinguishable from one that matched everything. Check the
        count, not the status.

        Returns
            ApiResponse with ``requestedAudienceMetadata``, ``overlappingAudiences``,
            ``marketplace`` and ``nextToken``. Each overlap carries
            ``audienceMetadata`` and ``affinity``, a number where higher means a
            closer match.

        """
        contentType = 'application/vnd.insightsaudiencesoverlap.v' + str(version) + '+json'
        headers = {'Accept': contentType}
        return self._request(fill_query_params(kwargs.pop('path'), audienceId), params=kwargs, headers=headers)
