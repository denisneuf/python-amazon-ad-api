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

.. warning::

    On a Sponsored Ads seller profile this family is not reachable. Probing both
    reads answers ``401 Customer <id> is not authorized to access account``,
    although the contract declares ``campaign_view`` as enough to list and
    retrieve. The routes exist and the module matches the contract; the account
    scope is what declines. Create and update were never sent, since they write
    into the account.

.. autoclass:: ad_api.api.v1.LocationIndexes
    :members:

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

        result = LocationIndexes(account=store).list_location_indexes()

        for index in result.payload.get("locationIndexes", []):
            print(index["indexId"], index["indexName"], index["status"])
