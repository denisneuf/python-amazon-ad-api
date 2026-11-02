from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class GeoLocations(Client):
    r"""
    GeoLocations(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - geographic locations for targeting

    One route, and it only creates:

        POST /adsApi/v1/create/geoLocations

    The contract declares no query and no delete, so a location created here
    cannot be read back or removed through this family. Treat it as a write
    that leaves an object in the account rather than as a lookup.

    Two shapes sit under ``location``, exactly one of them per entry:

        radiusLocation   a point of interest and a radius around it
        smartLocation    postal codes picked by a sales index percentile
    """

    @sp_endpoint('/adsApi/v1/create/geoLocations', method='POST')
    def create_geo_locations(self, **kwargs) -> ApiResponse:
        r"""
        create_geo_locations(body: dict) -> ApiResponse

        Amazon Ads API v1 - Create Geo Locations (operationId: CreateGeoLocation)

        Request Body [Required]
            | **geoLocations** (list<GeoLocationCreate>) : [required] 1..100
                | **location** (CreateGeoLocationUnion) : [required] one of:
                    | **radiusLocation** (CreateRadiusLocation)
                        | **pointOfInterestRadius** (double) : [required] kilometres or miles
                        | **units** (DistanceUnit) : [required] Enum [ KILOMETERS, MILES ]
                        | **coordinates** (CreateGeoLocationCoordinates) : latitude and longitude
                        | **pointOfInterestAddress** (string) : an address or a place name
                    | **smartLocation** (CreateSmartLocation)
                        | **locationIndexId** (string) : [required] the index the selection is based on
                        | **name** (string) : [required]
                        | **minIndexValuePercentile** (int) : 0..100
                        | **maxIndexValuePercentile** (int) : 0..100, greater than the minimum

        Answer
            207 MultiStatus with success[] and error[] indexed the same way;
            each success carries the created GeoLocation and its position.

        A radius needs at least 0.37 miles (2000 ft, 0.6 km), and the two
        percentile values must not cross.
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
