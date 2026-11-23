Location Indexes
================

Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLLocationIndexesContract_prod_3p.json
Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-locationindexes

A Smart Location Index is a named dataset that maps postal codes to index values,
expressing relative audience quality or sales potential for one advertiser. The
values come from the caller; the service stores them and serves them for smart
location targeting on a campaign.

Writes are asynchronous. A newly created index arrives as ``PENDING`` and only
reads ``ENABLED`` once the service has processed the data; an update sends an
existing index back to ``PENDING`` until the new values are read. A failure
leaves ``FAILED``, or ``UPDATE_FAILED`` when the failure belongs to a rewrite.

Account headers
---------------

This family does not declare ``Amazon-Advertising-API-Scope`` in its contract,
and the Scope the client sends anyway does not help. Without one of the two
account headers the route answers 401, with or without Scope.

``list_location_indexes`` accepts two optional keyword arguments that become
headers, not query parameters:

.. list-table::
    :header-rows: 1

    * - Keyword argument
      - Header sent
      - Result
    * - none
      - -
      - 401, not authorized to access account
    * - ``account_id``
      - ``Amazon-Ads-AccountId``
      - 200
    * - ``manager_account_id``
      - ``Amazon-Ads-Manager-AccountId``
      - 200
    * - both
      - both
      - 400, multi marketplace query requests not supported

Measured on 2026-11-15 with two accounts, one with a manager and one without.

.. warning::

    An empty ``locationIndexes`` list is a working call on an account with no
    indexes created. It is not the same as the ``None`` returned when the
    request fails, which is what a 401 produces.

.. warning::

    This family used to answer ``401`` on a seller profile although the
    contract declared ``campaign_view`` as enough. The cause was the missing
    account header, not the permissions: with ``account_id`` or
    ``manager_account_id`` the read answers 200. Create and update were never
    sent, since they write into the account.
.. currentmodule:: ad_api.api.v1

.. autosummary::
    :toctree: location_indexes/
    :nosignatures:

    LocationIndexes
    LocationIndexes.create_location_index
    LocationIndexes.list_location_indexes
    LocationIndexes.retrieve_location_indexes
    LocationIndexes.update_location_indexes

### Endpoint map

.. list-table::
    :header-rows: 1

    * - Path
      - Method
      - Operation
    * - ``/adsApi/v1/create/locationIndexes``
      - POST
      - CreateLocationIndex
    * - ``/adsApi/v1/locationIndexes``
      - GET
      - ListLocationIndex
    * - ``/adsApi/v1/retrieve/locationIndexes``
      - POST
      - RetrieveLocationIndex
    * - ``/adsApi/v1/update/locationIndexes``
      - POST
      - UpdateLocationIndex

### Example python

.. code-block:: python

    from ad_api.api.v1 import LocationIndexes

    from ad_api.api.v1 import LocationIndexes

    api = LocationIndexes(account=store)

    # Without an account header this route answers 401. Either one works.
    result = api.list_location_indexes(
        account_id="amzn1.ads-account.g.<id>",   # or manager_account_id=...
    )

    payload = result.payload or {}
    for index in payload.get("locationIndexes", []):
        print(index.get("indexId"), index.get("indexName"), index.get("status"))
