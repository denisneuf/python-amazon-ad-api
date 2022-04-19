Insights
========

`https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Insights_prod_3p.json`_

.. _https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Insights_prod_3p.json: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Insights_prod_3p.json

.. autoclass:: ad_api.api.Insights

    .. autofunction:: ad_api.api.Insights.get_insights

    .. note::

        This **Insights** supports 2 different types of content (Accept) so is possible get 2 different responses
        Just pass an optional parameter (2) as int if you want different option, default is version 1.

    ### Example getting overlapping categories using keyword arguments

    .. code-block:: python

        import logging
        from ad_api.api import Insights
        from ad_api.base import AdvertisingApiException


        def get_insights(audience_id: str, ad_type: str, version:int = 1, **kwargs):

            try:

                result = Insights(debug=True).get_insights(
                    audienceId=audience_id,
                    adType=ad_type,
                    version=version,
                    **kwargs
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        if __name__ == '__main__':
            id_audience = "427339506193361161"
            ad_type = "SD"

            get_insights(id_audience, ad_type)
            # With max and min minimumAudienceSize and maximumAudienceSize (version 1)
            # get_insights(id_audience, ad_type, minimumAudienceSize=7, maximumAudienceSize=8)
            # With minimumOverlapAffinity (version 2)
            # get_insights(id_audience, ad_type, 2, minimumOverlapAffinity=10)
            # With maximumOverlapAffinity (version 2)
            # get_insights(id_audience, ad_type, 2, maximumOverlapAffinity=5)
            # With Category Lifestyle (version 2)
            # get_insights(id_audience, ad_type, 2, audienceCategory="Lifestyle")
            # With Category Interest (version 2)
            # get_insights(id_audience, ad_type, 2, audienceCategory="Interest")
            # With a maxResults filter (version 2)
            # get_insights(id_audience, ad_type, 2, maxResults=10)


    .. note::

        If you do not provide any filter it will return all the audiences

    ### Example python retrieving all the audiences with Utils a decorator in sets of 10 with a delay of 5 seconds between query and query


    .. code-block:: python

        import logging
        from ad_api.api import Insights
        from ad_api.base import AdvertisingApiException, Utils

        @Utils.load_all_categories(throttle_by_seconds=5, next_token_param="nextToken")
        def get_all_categories(**kwargs):
            return Insights(debug=True).get_insights(**kwargs)

        if __name__ == '__main__':

            id_audience = "427339506193361161"
            ad_type = "SD"

            for page in get_all_categories(audienceId=id_audience, adType=ad_type, version=2, maxResults=10):
                result = page.payload
                overlapping_audiences = result.get("overlappingAudiences")
                for audience in overlapping_audiences:
                    logging.info(audience.get("affinity"))
                    logging.info(audience.get("audienceMetadata"))
