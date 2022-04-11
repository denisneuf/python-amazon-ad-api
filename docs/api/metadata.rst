Metadata
=================

.. autoclass:: ad_api.api.Metadata

    `Product Selector 3.0`_.

    .. _Product Selector 3.0: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/ProductSelector_prod_3p.json

    .. autofunction:: ad_api.api.Metadata.get_products_metadata

    ### Example getting the metadata of a search string

    .. code-block:: python

        import logging
        from ad_api.api import Metadata
        from ad_api.base import AdvertisingApiException


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )


        def get_products_metadata(data: (str, dict)):

            try:

                result = Metadata(debug=True).get_products_metadata(
                    body=data
                )

                logging.info(result)

                product_metadata_list = result.payload.get("ProductMetadataList")

                logging.info(len(product_metadata_list))

                for product_metadata in product_metadata_list:
                    logging.info(product_metadata)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            search_dict = \
                {
                    'checkItemDetails': True,
                    'adType': 'SP',
                    'checkEligibility': True,
                    'searchStr': 'obd2',
                    'pageIndex': 1,
                    'pageSize': 20,
                    'sortBy': 'CREATED_DATE',
                    'locale': 'es_ES'
                }

            get_products_metadata(search_dict)

