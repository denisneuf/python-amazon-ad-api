Brand Store Edition Publish Versions
=====================================

Amazon Ads API v1 - unified BrandStoreEditionPublishVersions endpoints

Two methods talk to ``/adsApi/v1/*/brandStoreEditionPublishVersions``. Neither
creates nor deletes: a publish version is queried, and its state is moved
between draft and publish.

Permissions: ``amazon_stores_view`` or ``amazon_stores_edit`` for the query,
``amazon_stores_edit`` alone for the update. This is Amazon Stores, not DSP.

.. warning::

    Two enums live here and they are not interchangeable. ``StorePublishState``
    is ``DRAFT`` or ``PUBLISH``, is what the caller decides, and is the only one
    ``update`` accepts. ``StorePublishStatus`` is ``DRAFT`` or
    ``REVIEW_IN_PROGRESS``, is where the content sits, and is the only one the
    query filters on.

    The names differ by one letter and both contain ``DRAFT``, so sending one
    where the other belongs is a rejected request rather than a silent mismatch.

Unlike the rest of v1, the query body is not fully optional: ``storeIdFilter``,
``editionIdFilter`` and ``publishStatusFilter`` are all required, and each accepts
exactly one value.

.. note::

    ``StorePublishStatus`` declares ``DRAFT`` and ``REVIEW_IN_PROGRESS``, but the
    service accepts only the first. Asking for ``REVIEW_IN_PROGRESS`` answers
    ``400 Only DRAFT status query is supported`` on every store. Send ``DRAFT``.

    ``editionId`` is the literal string ``default``, not a UUID: it names the
    store's default edition, so every store answers with the same value.

    The ``storeEditionPublishId`` in the answer is a base64 token holding the
    schema version, store, ``editionIdVersion`` and status -- pass it back to
    update unchanged.

The update array holds exactly one element, not a range.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-brandstoreeditionpublishversions
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLBrandStoreEditionPublishVersionsContract_prod_3p.json

.. autoclass:: ad_api.api.v1.BrandStoreEditionPublishVersions
    :members:

