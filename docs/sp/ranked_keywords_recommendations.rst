Get Ranked Keywords Recommendations
===================================

.. warning::

    Sponsored Product v3 is not available for Sandbox endpoint

.. note::

    This API is version 3.0

.. autoclass:: ad_api.api.sp.RankedKeywordsRecommendations

    Endpoint available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/sp/targets/keywords/recommendations", "Get ranked keywords recommendations."

    .. autofunction:: ad_api.api.sp.RankedKeywordsRecommendations.list_ranked_keywords_recommendations(self,  version: int = 3, **kwargs) -> ApiResponse:


    ### Example Using the endpoint with version

    .. code-block:: python

        import logging
        import json
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException

        def sp_get_ranked_keywords_recommendations_asin(version:int):

            dictionary = \
                {
                    "asins": [
                        "B08C1KN5J2"
                    ],
                    "recommendationType": "KEYWORDS_FOR_ASINS"
                }

            data = json.dumps(dictionary)


            try:

                result = sponsored_products.RankedKeywordsRecommendations(debug=True).list_ranked_keywords_recommendations(
                    version=version,
                    body=data
                )

            except AdvertisingApiException as error:
                logging.error(error)


            logging.info("version {}".format(str(version)))
            logging.info(result.payload)

        def sp_get_ranked_keywords_recommendations_targets(version:int):

            dictionary = \
                {
                    "maxRecommendations": 10,
                    "sortDimension": "CLICKS",
                    "locale": "zh_CN",
                    "campaignId": 199522597016061,
                    "recommendationType": "KEYWORDS_FOR_ADGROUP",
                    "adGroupId": 261060438275923
                }

            try:

                result = sponsored_products.RankedKeywordsRecommendations(debug=True).list_ranked_keywords_recommendations(
                    version=version,
                    body=dictionary
                )

            except AdvertisingApiException as error:
                logging.error(error)

            logging.info("version {}".format(str(version)))
            logging.info(result.payload)


        if __name__ == '__main__':

            # sp_get_ranked_keywords_recommendations_targets(version=3) # default api endpoint version=3
            sp_get_ranked_keywords_recommendations_targets(version=4)
            sp_get_ranked_keywords_recommendations_targets(version=5)

            # sp_get_ranked_keywords_recommendations_asin(version=3) # default api endpoint version=3
            sp_get_ranked_keywords_recommendations_asin(version=4)
            sp_get_ranked_keywords_recommendations_asin(version=5)


