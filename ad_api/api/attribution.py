from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Attribution(Client):
    """Amazon Attribution

    Amazon Attribution is an advertising measurement product that enables advertisers to understand the impact that
    their non-Amazon ads (i.e. Google Ads, Facebook, Microsoft Ads) have in driving shopping activity on Amazon.
    Measuring ads using Amazon Attribution is done through implementing Attribution tags on non-Amazon ads.
    Amazon Attribution is currently available in beta for US, CA, UK, DE, FR, IT, and ES vendors and professional
    sellers enrolled in Brand Registry.

    Amazon Attribution API

    The Amazon Attribution API enables agencies and integrators to easily retrieve their advertiser client's non-Amazon
    publisher attribution tags to automate tag implementation on their non-Amazon ads that link to an Amazon product or
    Stores page. The API also enables agencies and integrators to create and retrieve reporting on behalf of their
    advertiser clients to better understand Amazon conversion performance on their campaigns.

    Note that you must pass a header named Amazon-Advertising-Api-Scope with each call to an Amazon Attribution API URI,
    including GET /advertisers. The value for this header is the profileId available from the Profiles resource
    (/v2/profiles).

    Doc: https://advertising.amazon.com/API/docs/en-us/amazon-attribution/overview
    This specification is available for download from the `Amazon Attribution
    <https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json>`_.

    Version open beta


    """


    @sp_endpoint("/attribution/advertisers", method="GET")
    def get_advertisers(self, **kwargs) -> ApiResponse:
        r"""
        Gets a list of advertisers associated with an Amazon Attribution account.
        """
        return self._request(fill_query_params(kwargs.pop("path")), params=kwargs)

    @sp_endpoint("/attribution/publishers", method="GET")
    def get_publishers(self, **kwargs) -> ApiResponse:
        r"""
        Gets a list of all available publishers.
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
