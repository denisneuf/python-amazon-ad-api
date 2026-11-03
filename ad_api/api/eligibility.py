from ad_api.base import Client, sp_endpoint, ApiResponse, Utils
import logging


class Eligibility(Client):
    r"""Product and program eligibility for Amazon ads."""

    @sp_endpoint('/eligibility/product/list', method='POST')
    def get_eligibility(self, **kwargs) -> ApiResponse:
        r"""
        get_eligibility(body: (dict, str)) -> ApiResponse

        Product eligibility for a set of ASINs. Only products sold by the
        merchant behind the profile are accepted. The request carries ASINs,
        but several SKUs may come back for one ASIN, and an ineligible
        product comes back with the reasons rather than being left out.

        body: | REQUIRED
            '**adType**': *string* [dsp, sb, sd, sp] default sp
            '**productDetailsList**': list of {asin, sku}
            '**locale**': *string*
        """
        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs)

    @sp_endpoint('/eligibility/product/list', method='POST')
    def get_eligibility_assistant(self, asin_list: list, sku_list: list = None,
                                  ad_type: str = 'sp', locale: str = 'en-GB',
                                  **kwargs) -> ApiResponse:
        r"""
        get_eligibility_assistant(asin_list, sku_list=None, ad_type='sp', locale='en-GB')

        Builds the body for get_eligibility from plain lists.

        sku_list is optional. When given it must be a list of the same length
        as asin_list, so each entry pairs by position; a mismatch raises here
        rather than sending a body the service will refuse.
        """

        if not asin_list:
            raise ValueError('asin_list is empty; at least one ASIN is required')

        if sku_list is not None:
            if not isinstance(sku_list, list):
                raise TypeError(
                    'sku_list must be a list or None, got %s' % type(sku_list).__name__
                )
            if len(sku_list) != len(asin_list):
                raise ValueError(
                    'asin_list and sku_list must have the same length: %d != %d'
                    % (len(asin_list), len(sku_list))
                )

        details = []

        for index, asin in enumerate(asin_list):
            entry = {'asin': asin}
            if sku_list is not None:
                entry['sku'] = sku_list[index]
            details.append(entry)

        body = {'adType': ad_type, 'productDetailsList': details, 'locale': locale}

        logging.debug('get_eligibility_assistant body: %s', body)

        return self.get_eligibility(body=body, **kwargs)

    @sp_endpoint('/eligibility/programs', method='POST')
    def get_program_eligibility(self, **kwargs) -> ApiResponse:
        r"""
        get_program_eligibility(body: dict) -> ApiResponse

        Account level eligibility for the Amazon ad programs, not for a
        product: Sponsored Products, Sponsored Brands, Sponsored Display,
        Stores, DirectToConsumer, Amazon Attribution and the rest.

        Two media types are declared:

            application/json                      the default shape, with skipChecks
            application/vnd.programeligibility.v2+json
                                                  v2, with maxResults and nextToken

        Pass media_type='v2' for the paginated one.
        """

        media_type = kwargs.pop('media_type', None)

        if media_type == 'v2':
            content_type = 'application/vnd.programeligibility.v2+json'
        else:
            content_type = 'application/json'

        headers = {'Content-Type': content_type, 'Accept': 'application/json'}

        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), wrap=False),
            params=kwargs,
            headers=headers,
        )
