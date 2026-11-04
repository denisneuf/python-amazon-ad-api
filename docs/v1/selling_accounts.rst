Selling Accounts
=================

Amazon Ads API v1 - selling accounts

Documentation: not indexed by Amazon; the vendor page has not been found yet.
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLSellingAccountsContract_prod_3p.json

One route, read only:

    POST /adsApi/v1/query/sellingAccounts

No ``adProductFilter`` appears here: a selling account is the account behind
the ads, not an ad product.

Every member of the request is optional, so an empty body is a valid request
and asks for the accounts the caller can see. ``maxResults`` starts at 10, so a
smaller value is a rejected body rather than a shorter page.

Each ``SellingAccount`` carries the token that locates the account, the portals
used to reach it, its selling program and the countries the user can advertise
in.

.. autoclass:: ad_api.api.v1.SellingAccounts
    :members:
