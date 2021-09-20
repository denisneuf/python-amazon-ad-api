from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Localization(Client):
    """
    This API provides operations to localize data used when creating advertising campaigns. Depending on the type of data, localization may entail translating text, converting monetary amounts, or mapping an entity in a source marketplace to an analogous entity in one or more target marketplaces.
    """
    @sp_endpoint('/currencies/localize', method='POST')
    def get_currency(self, **kwargs) -> ApiResponse:
        r"""

        Gets an array of localized currencies in their target marketplaces, with the advertiser ID and source marketplace ID passed in through the header and body

        Returns localized currencies within specified marketplaces.

        **Requires one of these permissions**: [\"advertiser_campaign_edit\",\"advertiser_campaign_view\"]

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/products/localize', method='POST')
    def get_products(self, **kwargs) -> ApiResponse:
        r"""

        Localizes (maps) products from a source marketplace to one or more target marketplaces. The localization process succeeds for a given target marketplace if a product matching the source product can be found there and the advertiser is eligible to advertise it. Seller requests have an additional condition: the SKU of a localized product must match the SKU of the source product.

        **Requires one of these permissions**: [\"advertiser_campaign_edit\",\"advertiser_campaign_view\"]

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/keywords/localize', method='POST')
    def get_keywords(self, **kwargs) -> ApiResponse:
        r"""
        Returns localized keywords.

        Returns localized keywords within specified marketplaces or locales.

        **Requires one of these permissions**: [\"advertiser_campaign_edit\",\"advertiser_campaign_view\"]

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/targetingExpression/localize', method='POST')
    def get_targeting_expression(self, **kwargs) -> ApiResponse:
        r"""
        Localizes targeting expressions used for advertising targeting.

        Localizes (maps) targeting expressions from a source marketplace to one or more target marketplaces.

        **Requires one of these permissions**: [\"advertiser_campaign_edit\",\"advertiser_campaign_view\"]

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

