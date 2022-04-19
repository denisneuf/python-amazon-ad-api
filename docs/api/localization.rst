Localization
============

`https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Localization_prod_3p.json`_.

.. _https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Localization_prod_3p.json: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Localization_prod_3p.json

This API provides operations to localize data used when creating advertising campaigns. Depending on the type of data, localization may entail translating text, converting monetary amounts, or mapping an entity in a source marketplace to an analogous entity in one or more target marketplaces.

.. autoclass:: ad_api.api.Localization

    .. autofunction:: ad_api.api.Localization.get_currency_extended

    .. warning::

        This method **get_currency_extended** is a helper that will extend the response and return country codes abd currency to contextualize better the results

    .. note::

        If you do not provide any filter or the filters are wide it will return tons the audiences

    ### Example creating a dictionary and using MarketplacesIds Enum to simplify the task

    .. code-block:: python

        import logging
        from ad_api.api import Localization
        from ad_api.base import AdvertisingApiException, MarketplacesIds

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def get_currency_extended(data: (str, dict), version: int = 1):
            try:

                result = Localization(debug=True).get_currency_extended(
                    version=version,
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            source_country_code = "DE"
            source_marketplace_id = MarketplacesIds[source_country_code].value
            target_country_codes = ["GB", "US", "JP"]
            amount_1 = 10
            amount_2 = 15

            request = \
            {
                'localizeCurrencyRequests': [
                    {
                        'currency': {
                            'amount': amount_1
                        }
                    },
                    {
                        'currency': {
                            'amount': amount_2
                        }
                    }

                ],
                'targetCountryCodes': target_country_codes,
                'sourceCountryCode': source_country_code,
                'sourceMarketplaceId': source_marketplace_id,
                'targetMarketplaces': [MarketplacesIds[target_country_code].value for target_country_code in target_country_codes]
            }

            get_currency_extended(request, version=1) # You could submit version=2


    # Static .json file in case want to use as example

    .. literalinclude:: ../../test/localizations/request_currency.json

    Download :download:`json <../../test/localizations/request_currency.json>` the file to use:

    ### Example using the above file as request (MarketplacesIds not needed)

    .. code-block:: python

        import logging
        from ad_api.api import Localization
        from ad_api.base import AdvertisingApiException

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def get_currency_extended(data: (str, dict), version: int = 1):
        try:

            result = Localization(debug=True).get_currency_extended(
                version=version,
                body=data
            )

            logging.info(result)

        except AdvertisingApiException as error:
            logging.info(error)

        if __name__ == '__main__':

            file_name = "../test/localizations/request_currency.json"
            get_currency_extended(file_name) # No version include will get version 1
            # get_currency_extended(file_name, version=2)

    # Result using version=1 application/vnd.currencylocalization.v1+json

    .. literalinclude:: ../../test/localizations/result_currency_extended_v1.json

    # Result using version=2 application/vnd.currencylocalization.v2+json

    .. literalinclude:: ../../test/localizations/result_currency_extended_v2.json

    .. autofunction:: ad_api.api.Localization.get_currency


    # Same json file to use

    .. literalinclude:: ../../test/localizations/request_currency.json

    Download :download:`json <../../test/localizations/request_currency.json>` the file to use:

    ### Example using the above file as request (MarketplacesIds not needed)

    .. code-block:: python

        import logging
        from ad_api.api import Localization
        from ad_api.base import AdvertisingApiException

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def get_currency(data: (str, dict), version: int = 1):

            try:

                result = Localization(debug=True).get_currency(
                    version=version,
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        if __name__ == '__main__':

            file_name = "../test/localizations/request_currency.json"
            try:

                with open(file_name, mode="r", encoding="utf-8") as file:
                    get_currency(file_name, version=1)
                    file.close()

            except FileNotFoundError as e:
                logging.info(e)

    # Result using version=1 application/vnd.currencylocalization.v1+json

    .. literalinclude:: ../../test/localizations/result_currency_v1.json

    # Result using version=2 application/vnd.currencylocalization.v2+json

    .. literalinclude:: ../../test/localizations/result_currency_v2.json

    .. autofunction:: ad_api.api.Localization.get_products

    .. note::

        The **Product Localization** supports 2 different types of content (Content-Type) so is possible get 2 different responses
        Just pass an optional parameter (2) as int if you want different option, default is version 1.

    ### Example with a dictionary using marketplaceId for source and target and version 1

    .. code-block:: python

        import logging
        from ad_api.api import Localization
        from ad_api.base import AdvertisingApiException

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def get_products(data: (str, dict), version: int = 1):

            try:

                result = Localization(debug=True).get_products(
                    version=version,
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            product_request = \
            {
                "localizeProductRequests": [
                    {
                        "product": {
                            "asin": "B000000000",
                            "sku": "SKU-OF-B000000000"
                        }
                    }
                ],
                "adType": "SPONSORED_PRODUCTS",
                "entityType": "SELLER",
                "sourceMarketplaceId": "A1RKKUPIHCS9HS",
                "sourceAdvertiserId": "AD9EUOBWMS33M",
                "targetDetails": [
                    {
                        "marketplaceId": "A1F83G8C2ARO7P",
                        "advertiserId": "AD9EUOBWMS33M"
                    }
                ]
            }

            get_products(product_request)


    ### Example with a dictionary using countryCode for source and target and version 2

    .. code-block:: python

        import logging
        from ad_api.api import Localization
        from ad_api.base import AdvertisingApiException

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def get_products(data: (str, dict), version: int = 1):

            try:

                result = Localization(debug=True).get_products(
                    version=version,
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            product_request = \
            {
                "localizeProductRequests": [
                    {
                        "product": {
                            "asin": "B000000000",
                            "sku": "SKU-OF-B000000000"
                        }
                    }
                ],
                "adType": "SPONSORED_PRODUCTS",
                "entityType": "SELLER",
                "sourceCountryCode": "ES",
                "sourceAdvertiserId": "AD9EUOBWMS33M",
                "targetDetails": [
                    {
                        "countryCode": "FR",
                        "advertiserId": "AD9EUOBWMS33M"
                    }
                ]
            }

            get_products(product_request, version=2)



    # Result using version=1 application/vnd.productlocalization.v1+json

    .. literalinclude:: ../../test/localizations/result_products_v1.json

    # Result when the product can't be localize version=1

    .. literalinclude:: ../../test/localizations/no_result_product_v1.json

    # Result using version=2 application/vnd.productlocalization.v2+json

    .. literalinclude:: ../../test/localizations/result_products_v2.json

    # Result when the product can't be localize version=2

    .. literalinclude:: ../../test/localizations/no_result_product_v2.json

    ### Example Request as json by Country Code

    Download :download:`json <../../test/localizations/request_products_by_country_code.json>` the file to use:

    .. literalinclude:: ../../test/localizations/request_products_by_country_code.json

    ### Example Request as json by Marketplace ID

    Download :download:`json <../../test/localizations/request_products_by_marketplace_id.json>` the file to use:

    .. literalinclude:: ../../test/localizations/request_products_by_marketplace_id.json

    .. autofunction:: ad_api.api.Localization.get_keywords

    .. note::

        The **Keyword Localization** supports 2 different types of content (Content-Type) so is possible get 2 different responses
        Just pass an optional parameter (2) as int if you want different option, default is version 1.

    ### Example creating a dynamic dict based on a list of keywords using countryCode for source and Locale to retrieve the locales of targets

    .. code-block:: python

        import logging
        from ad_api.api import Localization
        from ad_api.base import AdvertisingApiException, Locales

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def get_keywords(data: (str, dict), version: int = 1):
            try:

                result = Localization(debug=True).get_keywords(
                    version=version,
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)
            except KeyboardInterrupt as error:
                logging.info(error)


        if __name__ == '__main__':

            keywords = ['máquina', 'diagnosis', 'diagnosis multimarca', 'coche', 'automóvil', 'frenos', 'presión', 'neumáticos']
            source_country_code = "ES"
            target_country_codes = ["GB", "FR", "IT", "DE", "CN", "NL", "SE"]

            keywords_request = \
                {
                    "localizeKeywordRequests": [{"localizationKeyword": {"keyword": keyword}} for keyword in keywords],
                    "sourceDetails": {
                        "countryCode": source_country_code,
                    },
                    "targetDetails": {
                        "locales": [Locales[target_country_code].value for target_country_code in target_country_codes]
                    }
                }

            get_keywords(keywords_request)
            # get_keywords(keywords_request, version=2)



    ### Example static request_keywords_locale.json

    .. literalinclude:: ../../test/localizations/request_keywords_locale.json

    Download :download:`json <../../test/localizations/request_keywords_locale.json>` the file to use

    ### Example result_keyword_locale.json

    .. literalinclude:: ../../test/localizations/result_keywords_locale.txt

    ### Example creating a dynamic dict based on a list of keywords using Locale for source and Country Codes for targets

    .. code-block:: python

        import logging
        from ad_api.api import Localization
        from ad_api.base import AdvertisingApiException, Locales

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def get_keywords(data: (str, dict), version: int = 1):
            try:

                result = Localization(debug=True).get_keywords(
                    version=version,
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)
            except KeyboardInterrupt as error:
                logging.info(error)


        if __name__ == '__main__':

            keywords = ['máquina', 'diagnosis', 'diagnosis multimarca', 'coche', 'automóvil', 'frenos', 'presión', 'neumáticos']
            source_country_code = "ES"
            source_locale = Locales[source_country_code].value
            target_country_codes = ["GB", "FR", "IT", "DE", "CN", "NL", "SE"]

            keywords_request = \
                {
                    "localizeKeywordRequests": [{"localizationKeyword": {"keyword": keyword}} for keyword in keywords],
                    "sourceDetails": {
                        "locale": source_locale
                    },
                    "targetDetails": {
                        "countryCodes": target_country_codes,
                    }
                }

            get_keywords(keywords_request)
            # get_keywords(keywords_request, version=2)

    ### Example static request_keywords_locales.json

    .. literalinclude:: ../../test/localizations/request_keywords_locales.json

    Download :download:`json <../../test/localizations/request_keywords_locales.json>` the file to use

    ### Example result keyword GB >> DE, SE, IT, FR, ES, NL

    .. literalinclude:: ../../test/localizations/result_keywords_locales.json

    ### Example creating a dynamic dict based on a list of keywords using MarketplacesIds for both source and targets

    .. code-block:: python

        import logging
        from ad_api.api import Localization
        from ad_api.base import AdvertisingApiException, MarketplacesIds

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def get_keywords(data: (str, dict), version: int = 1):
            try:

                result = Localization(debug=True).get_keywords(
                    version=version,
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)
            except KeyboardInterrupt as error:
                logging.info(error)


        if __name__ == '__main__':

            keywords = ['máquina', 'diagnosis', 'diagnosis multimarca', 'coche', 'automóvil', 'frenos', 'presión', 'neumáticos']
            source_country_code = "ES"
            source_marketplace_id = MarketplacesIds[source_country_code].value
            target_country_codes = ["GB", "FR", "IT", "DE", "NL", "SE"]

            keywords_request = \
                {
                    "localizeKeywordRequests": [{"localizationKeyword": {"keyword": keyword}} for keyword in keywords],
                    "sourceDetails": {
                        "marketplaceId": source_marketplace_id
                    },
                    "targetDetails": {
                        "marketplaceIds": [MarketplacesIds[target_country_code].value for target_country_code in target_country_codes],
                    }
                }

            get_keywords(keywords_request)
            # get_keywords(keywords_request, version=2)


    ### Example static request_keywords_marketplace_id.json

    .. literalinclude:: ../../test/localizations/request_keywords_marketplace_id.json

    Download :download:`json <../../test/localizations/request_keywords_marketplace_id.json>` the file to use

    ### Example result keyword FR >> IT, ES, GB

    .. literalinclude:: ../../test/localizations/result_keywords_marketplace_id.json

    .. autofunction:: ad_api.api.Localization.get_targeting_expression

    ### Example creating a dynamic dict based using MarketplacesIds for both source and target and predicate asinSameAs and version 1

    .. code-block:: python

        import logging
        from ad_api.api import Localization
        from ad_api.base import AdvertisingApiException, MarketplacesIds

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )


        def get_targeting_expression(data: (str, dict), version: int = 1):
            try:

                result = Localization(debug=True).get_targeting_expression(
                    version=version,
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            source_country_code = "GB"
            source_marketplace_id = MarketplacesIds[source_country_code].value

            target_country_code = "ES"
            target_marketplace_id = MarketplacesIds[target_country_code].value

            expression_request = \
                {
                    "targetDetailsList": [
                        {
                            "marketplaceId": target_marketplace_id,
                        }
                    ],
                    "requests": [
                        {
                            "targetingExpression": {
                                "isForNegativeTargeting": True,
                                "expression": [
                                    {
                                        "type": "asinSameAs",
                                        "value": "B08SWH2KP4"
                                    }
                                ]
                            }
                        }
                    ],
                    "sourceDetails": {
                        "marketplaceId": source_marketplace_id,
                    }
                }

            get_targeting_expression(expression_request, version=1)

    ### Example result result_targeting_expression_v1.json

    .. literalinclude:: ../../test/localizations/result_targeting_expression_v1.json

    Download :download:`json <../../test/localizations/result_targeting_expression_v1.json>` the file to use

    ### Example when expression is not available (ASIN in this specific case)

    .. literalinclude:: ../../test/localizations/no_result_targeting_expression_v1.json

    ### Example creating a dynamic dict based using countryCode for both source and target and predicate asinCategorySameAs and version 2

    .. code-block:: python

        import logging
        from ad_api.api import Localization
        from ad_api.base import AdvertisingApiException

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )


        def get_targeting_expression(data: (str, dict), version: int = 1):
            try:

                result = Localization(debug=True).get_targeting_expression(
                    version=version,
                    body=data
                )

                logging.info(result)
                print (result.payload)

            except AdvertisingApiException as error:
                logging.info(error)

        if __name__ == '__main__':

            source_country_code = "GB"
            target_country_code = "ES"

            expression_request = \
                {
                    "targetDetailsList": [
                        {
                            "countryCode": target_country_code,
                        }
                    ],
                    "requests": [
                        {
                            "targetingExpression": {
                                "isForNegativeTargeting": False,
                                "expression": [
                                    {
                                        "type": "asinCategorySameAs",
                                        "value": "1730635031"
                                    }
                                ]
                            }
                        }
                    ],
                    "sourceDetails": {
                        "countryCode": source_country_code,
                    }
                }

            get_targeting_expression(expression_request, version=2)

    ### Example static result_targeting_expression_v2.json

    .. literalinclude:: ../../test/localizations/result_targeting_expression_v2.json

    Download :download:`json <../../test/localizations/result_targeting_expression_v2.json>` the file to use

    ### Example when expression is not available (category in this specific case)

    .. literalinclude:: ../../test/localizations/no_result_targeting_expression_v2.json