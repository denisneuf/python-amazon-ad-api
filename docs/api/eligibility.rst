Eligibility
=================
`https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Eligibility_prod_3p.json`_

.. _https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Eligibility_prod_3p.json: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Eligibility_prod_3p.json

Check advertising eligibility of products.

.. autoclass:: ad_api.api.Eligibility

    .. autofunction:: ad_api.api.Eligibility.get_eligibility_assistant

    ### Example getting the elegibility of asin and asin/sku

    .. code-block:: python

        import logging
        from ad_api.api import Eligibility
        from ad_api.base import AdvertisingApiException


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )


        def get_eligibility_assistant(**kwargs):

            try:

                result = Eligibility(debug=True).get_eligibility_assistant(
                    **kwargs
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)



        if __name__ == '__main__':

            d_asin_list = ['B08C1KN5J2', 'B08XM9C8P6']
            d_sku_list = ['SKU-OF-B08C1KN5J2', 'SKU-OF-B08XM9C8P6']
            type_ad = 'sb'
            lang = 'es_ES'

            get_eligibility_assistant(asin_list=d_asin_list, sku_list=d_sku_list, ad_type=type_ad, locale=lang)

            # only by ASIN will return all available sku and show the eligibility
            get_eligibility_assistant(asin_list=d_asin_list, locale=lang)
            # the minimal call must send at least a list with one ASIN. Default: (adType="sp", locale="en-GB")
            get_eligibility_assistant(asin_list=['B08C1KN5J2'])


    .. autofunction:: ad_api.api.Eligibility.get_eligibility

    ### Example getting the elegibility in the regular way sending a dict

    .. code-block:: python

        import logging
        from ad_api.api import Eligibility
        from ad_api.base import AdvertisingApiException

        def get_eligibility(data: (str, dict)):

            try:

                result = Eligibility(debug=True).get_eligibility(
                    body=data
                )

                logging.info(result)


            except AdvertisingApiException as error:
                logging.info(error)

        if __name__ == '__main__':

            dict_asin = \
                {
                    'adType': 'sp',
                    'productDetailsList': [
                        {
                            'asin': 'B08C1KN5J2'
                        }
                    ],
                    'locale': 'es-ES'
                }

            get_eligibility(dict_asin)

            dict_asin_sku = \
                {
                    'adType': 'sp',
                    'productDetailsList': [
                        {
                            'asin': 'B08C1KN5J2',
                            'sku': 'SKU-OF-B08C1KN5J2'
                        }
                    ],
                    'locale': 'es-ES'
                }

            get_eligibility(dict_asin_sku)

            dict_multiple_asin_sku = \
                {
                    'adType': 'sp',
                    'productDetailsList': [
                        {
                            'asin': 'B08C1KN5J2',
                            'sku': 'SKU-OF-B08C1KN5J2'
                        },
                        {
                            'asin': 'B08XM9C8P6',
                            'sku': 'SKU-OF-B08XM9C8P6'
                        }

                    ],
                    'locale': 'es-ES'
                }

            get_eligibility(dict_multiple_asin_sku)
