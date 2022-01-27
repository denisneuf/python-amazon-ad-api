from typing import List

from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Tags(Client):

    @sp_endpoint("/attribution/tags/macroTag", method="GET")
    def get_macro_tag(self, **kwargs) -> ApiResponse:
        """Gets a list of attribution tags for third-party publisher campaigns that support macros.

        Third-party publishers, such as Google Ads, Facebook, Microsoft Ads, and Pinterest support tags that include macro parameters. Using macro parameters, campaign tracking information is dynamically inserted into the click-through URL when an ad is clicked. This resource is a tag pre-populated with campaign, ad group, and ad level publisher macros with the values associated with your campaign.
        For example, a Google Ads macro tag is "?maas=maas_adg_api_123456789_1_99&ref_=aa_maas&tag=maas&aa_campaignid={campaignid}&aa_adgroupid={adgroupid}&aa_creativeid=ad-{creative}_{targetid}_dev-{device}_ext-{feeditemid}"

        Args:
            | **publisherIds** (array[string]): required. a list of publisher identifiers for which to request tags.
            | **advertiserIds** (array[string]: Optional. List of advertiser identifiers for which to request tags. If no values are passed, all advertisers are returned.
           **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop('path'), params=kwargs)


    @sp_endpoint("/attribution/tags/nonMacroTemplateTag", method="GET")
    def get_non_macro_template_tag(self, **kwargs) -> ApiResponse:
        """Gets a list of attribution tags for third-party publisher campaigns that do not support macros.

        Some third-party publishers do not support tags that include macro parameters. In this case, the attribution tag includes a set of 'insertValue' placeholder values. Replace these placeholder values with your campaign, ad group, and ad identifiers to create unique ad-level tags.
        For example: "?maas=maas_adg_api_123456789_static_9_99&ref_=aa_maas&tag=maas&aa_campaignid={insertCampaignId}&aa_adgroupid={insertAdGroupId}&aa_creativeid={insertAdiD}"
        An example of an integrator nonMacro tag with filled campaign, ad group, and ad ID values is "?maas=maas_adg_api_123456789_static_9_99&ref_=aa_maas&tag=maas&aa_campaignid=12345&aa_adgroupid=5678&aa_creativeid=1357"

        Args:
            | **publisherIds** (array[string]): required. a list of publisher identifiers for which to request tags.
            | **advertiserIds** (array[string]): Optional. List of advertiser identifiers for which to request tags. If no values are passed, all advertisers are returned.
            **kwargs:

        Returns:

        """
        return self._request(kwargs.pop('path'), params=kwargs)
