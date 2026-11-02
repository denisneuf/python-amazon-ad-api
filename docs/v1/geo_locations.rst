Geo Locations
=============

Amazon Ads API v1 - geographic locations for targeting

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-geo-locations
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLGeoLocationsContract_prod_3p.json

One route, and it only creates:

    POST /adsApi/v1/create/geoLocations

.. warning::

    The contract declares **no query and no delete**, so a location created
    through this family cannot be read back or removed from it. Treat the call
    as a write that leaves an object in the account, not as a lookup, and do
    not fire it to see what happens.

Two shapes sit under ``location``, exactly one of them per entry:

``radiusLocation``
    A point of interest and a radius around it. ``pointOfInterestRadius`` and
    ``units`` are required, with ``units`` one of ``KILOMETERS`` or ``MILES``.
    The centre is either ``coordinates`` (latitude and longitude) or
    ``pointOfInterestAddress``, which accepts an address or a place name. The
    minimum radius is 0.37 miles (2000 ft, 0.6 km).

``smartLocation``
    Postal codes chosen by a sales index percentile. ``locationIndexId`` and
    ``name`` are required; ``minIndexValuePercentile`` and
    ``maxIndexValuePercentile`` take 0 to 100 with the minimum below the
    maximum.

Up to 100 locations per call, and the answer is a 207 multi-status indexed the
same way as the other write routes.

.. autoclass:: ad_api.api.v1.GeoLocations
    :members:
