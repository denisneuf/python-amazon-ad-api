Reports
=======

Amazon Ads API v1 - unified Reports endpoints

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-reports
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLReportsContract_prod_3p.json

Reports in v1 are asynchronous and take three routes instead of a CRUD set:

    POST /adsApi/v1/create/reports
    POST /adsApi/v1/retrieve/reports
    POST /adsApi/v1/delete/reports

There is no GET by id. The state is read by posting the id back to
``retrieve``, and that pair of routes carries the status through
``PENDING``, ``PROCESSING``, ``COMPLETED`` and ``FAILED``.

This generation is shaped differently from the v3 reporting route shipped as
``ad_api.api.Reports``, and the two are not interchangeable:

    v1 uses fields,  v3 uses columns
    v1 has no reportTypeId, adProduct, groupBy or timeUnit at all
    v1 filters are a predicate tree, v3 filters are a flat list
    v1 answers a list of report parts, v3 answers one url

Both classes resolve under their own package, so
``from ad_api.api import Reports`` keeps giving the v3 class and
``from ad_api.api.v1 import Reports`` gives this one.

The account travels in the body, in ``accessRequestedAccounts``, which takes
exactly one of ``advertiserAccountId`` or ``managerAccountId``. It is not
carried by the headers alone as in the entity families.

A create answers ``207 MultiStatus``: ``success[]`` holds the accepted
reports and ``error[]`` the index and reason of the refused ones, so one call
can both queue a report and refuse another.

``completedReportParts`` is a list, not a single URL. A report split in parts
answers more than one entry, each with its own signed ``url``,
``urlExpirationDateTime`` and ``sizeInBytes``. A caller that reads only the
first entry loses data.

.. warning::

    This route answers ``401 Unauthorized`` with
    ``Bulk account authorization denied: DENY`` for a Sponsored Ads seller
    profile. Checked against the service: the body is validated first, so a
    malformed request answers 400, and a valid one answers 401 for every
    identifier carried in ``accessRequestedAccounts`` (``profileId``,
    ``accountInfo.id`` and ``marketplaceStringId``). The calls are built from
    the contract and verified offline; they have not been exercised against
    the service from this account.

.. warning::

    The field catalogue is **not** part of the contract. ``query.fields``
    accepts any string and the service decides which ones exist for each
    product, so a locally built list can only be checked against the service:
    a wrong name is answered with a 400 naming the accepted values. The same
    goes for the filter: ``field`` must match ``^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$``,
    which means ``entity.field`` (``campaign.campaignStatus``), a shape the
    contract states but does not enumerate.

.. autoclass:: ad_api.api.v1.Reports
    :members:
