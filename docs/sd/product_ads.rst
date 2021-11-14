Product Ads
===========
.. role:: strike
    :class: strike

.. warning::

    Sponsored Display is not available for Sandbox endpoint

.. autoclass:: ad_api.api.sd.ProductAds



    .. autofunction:: ad_api.api.sd.ProductAds.list_product_ads(self, **kwargs) -> ApiResponse:

        ### Example python 1

        .. code-block:: python

            from ad_api.base import AdvertisingApiException, Marketplaces
            from ad_api.api import sponsored_display

            try:
                status = 'enabled'
                store = 'my_store'

                result = sponsored_display.ProductAds(account=store,
                                                      marketplace=Marketplaces.ES,
                                                      debug=True).list_product_ads(
                    stateFilter=status
                )
                products_ads = result.payload # <class 'list'>

            except AdvertisingApiException as error:
                logging.error(error)

        ### Example python 2

        The default config in the credentials.yml if not passed as kwargs

        :strike:`account='my_store',`

        The default marketplace is Marketplaces.EU if not passed as kwarg ex. Marketplaces.US

        :strike:`marketplace=Marketplaces.US,`

        Debug info like headers, method and url and raw response will not provided

        :strike:`debug=True`

        .. code-block:: python


            import os
            from ad_api.base import AdvertisingApiException
            from ad_api.api.sd.product_ads import ProductAds

            try:
                status = 'enabled'
                index = 5 # Sets a cursor into the requested set of product ads
                number = 2 # Sets the number of ProductAd objects in the returned array
                result = ProductAds().list_product_ads(
                    stateFilter=status
                )

                products_ads = result.payload # <class 'list'>

            except AdvertisingApiException as error:
                logging.error(error)


    .. autofunction:: ad_api.api.sd.ProductAds.edit_product_ads(self, **kwargs) -> ApiResponse:

        ### Example body json

        An array of ProductAd objects. For each object, specify a product ad identifier and the only mutable field, state. Maximum length of the array is 100 objects.

        .. code-block:: JSON


            [
                {
                    "state": "enabled",
                    "adId": 182575048323550
                }
            ]

        ### Example python

        .. code-block:: python

            import json
            from ad_api.api import sponsored_display

            try:

                dictionary = \
                [
                    {
                        "state": "enabled",
                        "adId": 182575048323550
                    }
                ]

                data = json.dumps(dictionary)

                result = sponsored_display.ProductAds(debug=True).edit_product_ads(
                    body=data
                )

                logging.info(result.payload)
                logging.info(json.dumps(response.payload))

            except AdvertisingApiException as error:
                logging.error(error)



        ### Example response.payload **<class 'list'>**

        .. code-block:: python

            [{'code': 'SUCCESS', 'adId': 182575048323550}]

        ### Example json.dumps(response.payload) **<class 'str'>**

        .. code-block:: JSON

            [{"code": "SUCCESS", "adId": 182575048323550}]