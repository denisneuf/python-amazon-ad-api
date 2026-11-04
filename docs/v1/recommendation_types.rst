Recommendation Types
====================

Amazon Ads API v1 - recommendation types for Sponsored Brands

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-recommendationtypes
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLRecommendationTypesContract_prod_3p.json

One route, read only, and the product is in the path:

    POST /adsApi/v1/query/recommendationTypes/sb

This family lists the kinds of recommendation that exist. ``Recommendations``
itself lists the ones the account actually has.

Only the Sponsored Brands segment is published, and its schemas are prefixed SB
(``SBQueryRecommendationTypeRequest``, ``SBRecommendationType``). The route keeps
no SB in its name, so another product would arrive as ``.../sp`` or ``.../sd``
beside it.

Every member of the request is optional, so an empty body is valid and asks for
the defaults. ``maxResults`` accepts 50 to 500 and starts at 50, so a smaller
value is a rejected body rather than a shorter page.

.. autoclass:: ad_api.api.v1.RecommendationTypes
    :members:
