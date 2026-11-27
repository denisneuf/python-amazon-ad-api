import json
from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Attribution(Client):
    r""" """

    @sp_endpoint("/attribution/advertisers", method="GET")
    def get_advertisers(self, **kwargs) -> ApiResponse:
        r"""
        Gets a list of advertisers associated with an Amazon Attribution account.

        Takes no query parameters. Send the request as is.

        Returns:
            ApiResponse. ``payload`` holds ``{"advertisers": [...]}`` with one
            entry per advertiser:

            - ``advertiserId`` (string): the identifier the other Attribution
              routes accept as ``advertiserIds``.
            - ``advertiserName`` (string): the display name.

        Example:

        .. code-block:: python

            from ad_api.api import Attribution

            attribution = Attribution(account="my_account")
            attribution.get_advertisers().payload
            # {'advertisers': [{'advertiserName': 'MY BRAND SPAIN',
            #                   'advertiserId': '586616515354498787'}]}

        An account without Attribution access answers ``200`` with an empty
        ``advertisers`` list, not a ``403``, so check the list itself.
        ``ApiResponse`` does not carry the HTTP status code.
        """
        return self._request(fill_query_params(kwargs.pop("path")), params=kwargs)

    @sp_endpoint("/attribution/publishers", method="GET")
    def get_publishers(self, **kwargs) -> ApiResponse:
        r"""
        Gets a list of all available publishers.

        Takes no query parameters. Send the request as is. This is the call that
        tells you which of the two tag routes each publisher belongs to.

        Returns:
            ApiResponse. ``payload`` holds ``{"publishers": [...]}`` with one
            entry per publisher:

            - ``id`` (string): the value to pass as ``publisherIds``.
            - ``name`` (string): the display name, such as ``Google Ads``.
            - ``macroEnabled`` (boolean): ``True`` when the publisher expands
              tracking macros in its click-through URLs, and therefore belongs
              to :meth:`get_macro_tag`. ``False`` means it needs fixed values
              and belongs to :meth:`get_non_macro_template_tag`.

        Example:

        .. code-block:: python

            publishers = Attribution(account="my_account").get_publishers().payload["publishers"]
            macro = [p["id"] for p in publishers if p["macroEnabled"]]
            plain = [p["id"] for p in publishers if not p["macroEnabled"]]

        Google Ads, Facebook Ads, Microsoft Ads and Pinterest Ads report
        ``macroEnabled`` true. The rest, among them Snapchat, Twitter, LinkedIn
        and TikTok, report false.
        """
        return self._request(fill_query_params(kwargs.pop("path")), params=kwargs)

    @sp_endpoint("/attribution/report", method="POST")
    def post_report(self, **kwargs) -> ApiResponse:
        r"""
        Gets an attribution report for a specified list of advertisers.

        body: | REQUIRED
            '**reportType**' (string): The type of report. Either `PERFORMANCE` or `PRODUCTS`. It is an optional parameter. If not used in request body, default reportType is `PERFORMANCE`. Each report type is aggregated at different levels. See below table for list of dimensions available within each report type.

            '**advertiserIds**' (string): One or more advertiser Ids to filter reporting by. If requesting reporting for multiple advertiser Ids, input via a comma-delimited list.

            '**endDate**' (string): The end date for the report, form as "YYYYMMDD"

            '**count**' (integer): maximum: 10000, minimum:1, The number of entries to include in the report.

            '**metrics**' (string):

            '**startDate**' (string): The start date for the report, in "YYYYMMDD" format. For reportType PRODUCTS, startDate can only be within last 90 days from current date.

            '**cursorId**' (string): The value of cursorId must be set to null without "", or set to "" for the first request. For each following request, the value of cursorId from the previous response must be included in the current request. Note that for the cursorId values the " character must be escaped with \.


        Returns:
            ApiResponse

        """
        data = json.dumps(kwargs.pop("body"))
        resp = self._request(
            fill_query_params(kwargs.pop("path")),
            data=data,
            params=kwargs,
        )
        resp.set_next_token(resp.payload.pop("cursorId"))
        return resp

    @sp_endpoint("/attribution/tags/macroTag", method="GET")
    def get_macro_tag(self, **kwargs) -> ApiResponse:
        r"""
        Gets a list of attribution tags for third-party publisher campaigns that support macros.

        Third-party publishers, such as Google Ads, Facebook, Microsoft Ads, and Pinterest support tags that include macro parameters. Using macro parameters, campaign tracking information is dynamically inserted into the click-through URL when an ad is clicked. This resource is a tag pre-populated with campaign, ad group, and ad level publisher macros with the values associated with your campaign.

        For example, a Google Ads macro tag is "?maas=maas_adg_api_123456789_1_99&ref_=aa_maas&tag=maas&aa_campaignid={campaignid}&aa_adgroupid={adgroupid}&aa_creativeid=ad-{creative}_{targetid}_dev-{device}_ext-{feeditemid}"

        Args:
            '**publisherIds**' (array[string]): required. a list of publisher identifiers for which to request tags.

            '**advertiserIds**' (array[string]: Optional. List of advertiser identifiers for which to request tags. If no values are passed, all advertisers are returned.

        Returns:
            ApiResponse

        """
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint("/attribution/tags/nonMacroTemplateTag", method="GET")
    def get_non_macro_template_tag(self, **kwargs) -> ApiResponse:
        r"""
        Gets a list of attribution tags for third-party publisher campaigns that do not support macros.

        Some third-party publishers do not support tags that include macro parameters. In this case, the attribution tag includes a set of 'insertValue' placeholder values. Replace these placeholder values with your campaign, ad group, and ad identifiers to create unique ad-level tags.
        For example: "?maas=maas_adg_api_123456789_static_9_99&ref_=aa_maas&tag=maas&aa_campaignid={insertCampaignId}&aa_adgroupid={insertAdGroupId}&aa_creativeid={insertAdiD}"
        An example of an integrator nonMacro tag with filled campaign, ad group, and ad ID values is "?maas=maas_adg_api_123456789_static_9_99&ref_=aa_maas&tag=maas&aa_campaignid=12345&aa_adgroupid=5678&aa_creativeid=1357"

        Args:
            '**publisherIds**' (array[string]): required. a list of publisher identifiers for which to request tags.

            '**advertiserIds**' (array[string]: Optional. List of advertiser identifiers for which to request tags. If no values are passed, all advertisers are returned.

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop('path'), params=kwargs)
