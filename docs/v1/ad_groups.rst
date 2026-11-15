Ad Groups
=========

Amazon Ads API v1 - unified Ad Groups endpoints

The product is selected in the request body with ``adProductFilter``, not in the
URL. All four methods talk to ``/adsApi/v1/*/adGroups``.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-adgroups
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLAdGroupsContract_prod_3p.json

Account headers on query_ad_groups
----------------------------------

``query_ad_groups`` accepts two optional keyword arguments that become
headers, not query parameters:

.. list-table::
    :header-rows: 1

    * - Keyword argument
      - Header sent
      - Effect on a global advertiser
    * - ``manager_account_id``
      - ``Amazon-Ads-Manager-AccountId``
      - none: the same answer as sending no header at all
    * - ``account_id``
      - ``Amazon-Ads-AccountId``
      - breaks the call, 400 "Multi marketplace query requests only support
        query by primary resource id"

Sending both behaves like ``account_id`` alone. Measured on 2026-11-15 against
an advertiser with eleven marketplaces.

The filtering is done by ``Amazon-Advertising-API-Scope`, which the client
already sends from the ``profile_id`` in the credentials: changing it changes
the marketplace of the results, and neither account header alters that. On a
global account the only useful choice is ``manager_account_id`` or nothing.

.. note::

    Adding ``campaignIdFilter`` does not make ``account_id`` work. The refusal
    is about the header, not about the body.

.. autoclass:: ad_api.api.v1.AdGroups
    :members:
