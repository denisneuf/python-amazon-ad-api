Recommendations
===============

Amazon Ads API v1 - recommendations

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-recommendations
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLRecommendationsContract_prod_3p.json

Three routes, two generic and one per product:

    POST /adsApi/v1/query/recommendations       QueryRecommendation
    GET  /adsApi/v1/recommendations             ListRecommendation
    POST /adsApi/v1/create/recommendations/sb   SBCreateRecommendation

Only the create carries a product suffix in its path. The query and the list
are generic and take the product in ``adProductFilter``, so a Sponsored
Products or Sponsored Display create would sit beside the SB one under its own
suffix without touching the other two.

The query requires ``accessRequestedAccounts``, the same account selector the
v1 reports family uses: the account travels in the body and not only in the
headers. Its ``maxResults`` accepts 1 to 100 and the answer carries up to 300
recommendations plus ``totalResults``.

``list_recommendations`` is a GET with query parameters rather than a body.

.. warning::

    ``create_recommendations_sb`` creates a recommendation in the account: it
    is not a read. It takes exactly one entry in ``recommendations`` and
    answers a 207 multi-status indexed the same way as the other write routes.

The Sponsored Brands segment is the only one in the published contract, and
its schemas are prefixed SB (``SBCreateRecommendationRequest``,
``SBRecommendationCreate``, ``SBRecommendationMultiStatusResponse``).

.. warning::

    Both reads answer ``401 Unauthorized`` on a Sponsored Ads seller profile,
    and the two messages name two different layers:

        GET  /adsApi/v1/recommendations
            3P Request: Customer <account> is not authorized to access account

        POST /adsApi/v1/query/recommendations
            3P Multi-Accounts Request: Bulk account authorization denied: DENY

    The GET carries no ``accessRequestedAccounts`` at all, so the selector in
    the body is not what triggers the refusal: the family itself is not
    enabled for this profile, the same way Reports and Labels are not.

    The calls stay built from the contract and verified offline.

.. autoclass:: ad_api.api.v1.Recommendations
    :members:
