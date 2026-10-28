Brand Store Editions
=====================

Amazon Ads API v1 - unified BrandStoreEditions endpoints

One method, and it is a ``GET`` with query parameters rather than the POST body
the rest of v1 uses:

```
GET /adsApi/v1/brandStoreEditions?brandStoreId=<id>
```

Permissions, either: ``amazon_stores_edit`` or ``amazon_stores_view``.

This is the middle link of the Stores chain:

- :class:`~ad_api.api.v1.BrandStores` gives the ``storeId``.
- here that becomes ``brandStoreId`` and returns the ``editionId``.
- :class:`~ad_api.api.v1.BrandStoreEditionPublishVersions` needs both.

.. note::

    ``maxResults`` is unusual: the range is 11 to 50 with a default of 50, not the
    1-based range the other families use.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-brandstoreeditions
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLBrandStoreEditionsContract_prod_3p.json

.. autoclass:: ad_api.api.v1.BrandStoreEditions
    :members:

