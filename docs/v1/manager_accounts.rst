Manager Accounts
================

Amazon Ads API v1 - unified ManagerAccounts endpoints

Documentation: not indexed by Amazon; the vendor page has not been found yet.
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLManagerAccountsContract_prod_3p.json

Three routes, no delete in the contract:

    POST /adsApi/v1/create/managerAccounts
    POST /adsApi/v1/query/managerAccounts
    POST /adsApi/v1/update/managerAccounts

This family is not about ad products, so no ``adProductFilter`` appears
anywhere in it, unlike the campaigns, ad groups, ads and targets siblings.

The query declares no required member at all: an empty body is a valid
request and returns every manager account the caller can see.

``maxResults`` on the query starts at 10, so a smaller value is a rejected
body rather than a shorter page. Both write routes take up to 10 accounts per
call and answer a multi-status indexed the same way.

.. warning::

    ``create`` and ``update`` write into the manager account hierarchy: they
    are not reads, and a body that reaches them creates or changes an account.
    Only the query is exercised by the probes.

The package keeps the legacy manager account reader as
``ad_api.api.ManagerAccounts``, a different class in a different package;
``from ad_api.api import ManagerAccounts`` keeps resolving to that one.

.. note::

    The legacy reader is **not** deprecated and should not be: it exposes
    ``managerAccountId``, which the v1 ``ManagerAccount`` schema does not carry,
    plus ``associate`` and ``disassociate``, which have no v1 route. Create is
    not interchangeable either: the legacy method takes ``managerAccountName``
    and ``managerAccountType``, while the v1 body carries ``displayName``,
    ``currencyCode``, ``timeZoneIana``, ``industryVertical``,
    ``accountUsageType`` and ``businessDetails``.

.. autoclass:: ad_api.api.v1.ManagerAccounts
    :members:
