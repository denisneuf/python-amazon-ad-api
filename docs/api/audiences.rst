Audiences
=========

`https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Audiences_prod_3p.json`_.

.. _https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Audiences_prod_3p.json: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Audiences_prod_3p.json

Audience Discovery API

.. autoclass:: ad_api.api.Audiences

    .. autofunction:: ad_api.api.Audiences.list_audiences_taxonomy

    ### Example python

    .. code-block:: python

        import logging
        from ad_api.api import Audiences
        from ad_api.base import AdvertisingApiException, Utils

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )


        def list_audiences_taxonomy(data: (str, dict)):
            try:

                result = Audiences(debug=True).list_audiences_taxonomy(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            category_path = "Lifestyle" # In-market

            request = \
                {
                    "adType": "SD",
                    "categoryPath": [
                        category_path
                    ]
                }

            list_audiences_taxonomy(request)

    ### Example query_taxonomy.json

    .. literalinclude:: ../../test/audiences/query_taxonomy.json

    Download :download:`json <../../test/audiences/query_taxonomy.json>` the file to use

    # Result using the request query above

    .. literalinclude:: ../../test/audiences/result_query_taxonomy.json

    .. autofunction:: ad_api.api.Audiences.list_audiences

    ### Example python

    .. code-block:: python

        import logging
        from ad_api.api import Audiences
        from ad_api.base import AdvertisingApiException

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )


        def list_audiences(**kwargs):
            try:

                result = Audiences(debug=True).list_audiences(
                    **kwargs
                )

                logging.info(result)
                print (result.payload)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            audience_name = "Automotive Ownership"

            request = \
                {
                    "adType": "SD",
                    "filters": [
                        {
                            "field": "audienceName",
                            "values": [
                                audience_name
                            ]
                        }
                    ]
                }

            list_audiences(body=request, maxResults=2)

    # Result using the request query above

    .. literalinclude:: ../../test/audiences/result_query_general.json

    .. note::

        If you do not provide any filter it will return all the audiences

    ### Example python retrieving all the audiences with Utils a decorator in sets of 20 with a delay of 5 seconds betwwen query

    .. code-block:: python

        import logging
        from ad_api.api import Audiences
        from ad_api.base import AdvertisingApiException, Utils

        @Utils.load_all_categories(throttle_by_seconds=5, next_token_param="nextToken")
        def get_all_categories(**kwargs):
            return Audiences(debug=True).list_audiences(**kwargs)

        if __name__ == '__main__':

            request = \
                {
                    "adType": "SD",
                }

            for page in get_all_categories(maxResults=20,body=request):
                result = page.payload
                audiences = result.get("audiences")
                for audience in audiences:
                    logging.info(audience)



    ### Example query_general.json

    .. literalinclude:: ../../test/audiences/query_general.json
