Advertiser Accounts
===================

Amazon Ads API v1 - unified AdvertiserAccounts endpoints

Three methods talk to ``/adsApi/v1/*/advertiserAccounts``. There is no delete.

This is not an ad-product resource, so unlike Ads, Targets or AdExtensions there
is no ``adProductFilter```; the query filters by ``advertiserAccountIdFilter`` or
``isGlobalAccountFilter``.

``AdvertiserAccountCreate`` requires ``businessDetails``, a list holding exactly
one element that carries either ``addressToken`` for an existing selling account
address or ``address`` when that account has none. The surrounding
``advertiserAccounts`` list accepts 1 to 100 entries per call.

``managerAccountId`` decides what the account can run: without it the account is
created for Sponsored Ads only, and DSP requires it.

Update takes ``advertiserAccountId`` plus the mutable fields — currency, time
zone, display name, industry and manager link.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-advertiseraccounts
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLAdvertiserAccountsContract_prod_3p.json

.. autoclass:: ad_api.api.v1.AdvertiserAccounts
    :members:

