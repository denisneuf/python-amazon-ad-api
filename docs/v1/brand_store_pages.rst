Brand Store Pages
==================

Amazon Ads API v1 - unified BrandStorePages endpoints

One method talks to ``/adsApi/v1/query/brandStorePages``.

Permissions, either: ``amazon_stores_edit`` or ``amazon_stores_view``.

Three filters are required and each accepts exactly one value: ``storeIdFilter``,
``editionIdFilter`` and ``pageIdFilter``. There is no way to list every page of a
store through this route — the page identifiers come from
:class:`~ad_api.api.v1.BrandStores`, whose ``pageInfos`` carries one ``tag`` per
page, and that tag is the ``pageId`` used here.

``editionId`` is the literal string ``default`` for a store's default edition, as
in the rest of the family.

A fourth filter, ``storeEditionPublishIdFilter``, is optional and takes the base64
token from BrandStoreEditionPublishVersions.

.. note::

    The answer carries ``content``, the page body itself, which is why this
    contract is far larger than its siblings. Read the shape before dumping it:
    a single page can be tens of kilobytes of nested JSON.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-brandstorepages
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLBrandStorePagesContract_prod_3p.json

.. autoclass:: ad_api.api.v1.BrandStorePages
    :members:

