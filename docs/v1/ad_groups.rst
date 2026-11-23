Ad Groups
=========

Amazon Ads API v1 - unified Ad Groups endpoints

The product is selected in the request body with ``adProductFilter``, not in the
URL. All four methods talk to ``/adsApi/v1/*/adGroups``.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-adgroups
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLAdGroupsContract_prod_3p.json

.. rubric:: Two ways to query

``query_ad_groups`` accepts an optional ``account_id``, which becomes the
``Amazon-Ads-AccountId`` header. It is removed from ``kwargs`` before the query
is built, so it never travels as a query parameter. The two modes are not
interchangeable: **the body changes with them.**

.. list-table::
    :header-rows: 1
    :widths: 26 26 48

    * - Mode
      - Headers
      - Body and result
    * - Scope
      - profile scope only
      - ``adProductFilter``, plus ``maxResults``, ``stateFilter`` and the other
        filters. Answers 200 and pages with ``nextToken``.
    * - Account
      - profile scope + ``Amazon-Ads-AccountId``
      - ``adProductFilter`` **and a primary resource id**: ``adGroupIdFilter``
        or ``campaignIdFilter``. Answers 200 with that resource, one page.
    * - Account + ``maxResults``
      - profile scope + ``Amazon-Ads-AccountId``
      - **Refused**, 400 ``Multi marketplace query requests only support
        query by primary resource id``. The same goes for ``stateFilter``.

``adProductFilter`` is required by the contract in both modes: leaving it out
answers 400 ``object has missing required properties (["adProductFilter"])``
before the mode is even considered.

The contract declares three parameters on this route: the client id, required
and always sent; the profile scope, optional and sent from the ``profile_id``
in the credentials; and ``Amazon-Ads-AccountId``, optional. **There is no
manager-account header on this route.**

.. rubric:: Example: query by ad group id

.. code-block:: python

    from ad_api.api.v1 import AdGroups

    AdGroups(account='my_store', marketplace=Marketplaces.EU).query_ad_groups(
        body={
            'adProductFilter': {'include': ['SPONSORED_PRODUCTS']},
            'adGroupIdFilter': {'include': ['12345678901234']},
        },
        account_id='amzn1.ads-account.g.xxxxxxxxxxxxxxxxxxxxxxxx',
    )

Answers one page with that ad group:

.. code-block:: python

    {
      'adGroups': [
        {
          'adGroupId': '12345678901234',
          'adProduct': 'SPONSORED_PRODUCTS',
          'bid': {'currencyCode': 'EUR', 'defaultBid': 1.81},
          'campaignId': '98765432109876',
          'marketplaces': ['FR'],
          'name': 'My ad group',
          'state': 'ENABLED',
          'status': {
            'deliveryReasons': ['CAMPAIGN_PAUSED'],
            'deliveryStatus': 'NOT_DELIVERING',
          },
        }
      ],
      'nextToken': None,
    }

With ``campaignIdFilter`` instead of ``adGroupIdFilter`` the same call answers
400: on this route the primary resource is the ad group, and the campaign
filter is not what the service accepts alongside the account header.

.. currentmodule:: ad_api.api.v1

.. autosummary::
    :toctree: ad_groups/
    :nosignatures:

    AdGroups
    AdGroups.create_ad_groups
    AdGroups.delete_ad_groups
    AdGroups.query_ad_groups
    AdGroups.update_ad_groups
