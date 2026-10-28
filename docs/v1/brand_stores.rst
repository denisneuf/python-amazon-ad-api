Brand Stores
============

Amazon Ads API v1 - unified BrandStores endpoints

One method talks to ``/adsApi/v1/query/brandStores``. A brand store is listed,
never created here.

Permissions, any one of: ``advertiser_campaign_edit``, ``creatives_view``,
``account_view``, ``creatives_edit``, ``account_edit``, ``campaign_view``,
``advertiser_campaign_view``, ``campaign_edit``.

``storeNameFilter`` is required and takes exactly one name, so this route cannot
list every store on the account.

The answer is the way in to the rest of the Stores family: the ``storeId`` it
returns is what BrandStoreEditionPublishVersions needs as ``storeIdFilter``.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-brandstores
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLBrandStoresContract_prod_3p.json

.. autoclass:: ad_api.api.v1.BrandStores
    :members:

