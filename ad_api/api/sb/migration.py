from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Migration(Client):
    """Sponsored Brands legacy campaign migration from 3.0 to 4.0.

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi

    Two media types live in this family, both versioned and both required:

    ========================================  ==========================================================
    Route                                      Media type
    ========================================  ==========================================================
    ``/sb/v4/legacyCampaigns/*``               ``vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4``
    ``/sb/v4/migrations/list``                 ``vnd.sbAdMigration.v4``
    ========================================  ==========================================================

    .. warning::
        ``list_migrations`` answers ``404 Could not find resource`` when sent
        ``application/json``, the same behaviour already recorded for forecasts,
        budget recommendations and optimization rules. Amazon routes on media
        type; a wrong one reads exactly like a missing route.

    .. note::
        ``migration_job_status`` and ``migration_job_results`` answer ``500
        INTERNAL_ERROR`` for a job identifier that does not exist, instead of a
        400 or a 404. The routes are live; the service trips over an unknown id.
    """

    _MEDIA_LEGACY = ('application/vnd.SponsoredBrands.'
                     'SponsoredBrandsMigrationApi.v4+json')
    _MEDIA_ADMIG = 'application/vnd.sbAdMigration.v4+json'

    @sp_endpoint('/sb/v4/legacyCampaigns/migrationJob', method='POST')
    def start_migration_job(self, campaignIds, enableThemeTargeting, **kwargs) -> ApiResponse:
        """
        Starts a migration job for 3.0 campaigns.

        Request Body [Required]
            | **campaignIds** (array of string): [required] Campaigns to migrate.
            | **enableThemeTargeting** (boolean): [required] Carry theme targets
              into the new campaigns.
            | **isStagedMigration** (boolean): [optional]
            | **newCampaignState** (string): [optional] State for the migrated
              campaigns.
            | **brandEntityId** (string): [optional]

        Returns:
            | ApiResponse, ``200``.

        .. warning::
            **This changes the account.** It starts a real migration of 3.0
            campaigns into 4.0, which is not something a probe or a retry should
            trigger by accident. Because of that it was never exercised here: the
            shape comes from the contract only.

        .. note::
            Do not treat a timeout as a failed migration. The job may be running;
            check ``migration_job_status`` before trying again.
        """
        body = {'campaignIds': campaignIds, 'enableThemeTargeting': enableThemeTargeting}
        for key in ('isStagedMigration', 'newCampaignState', 'brandEntityId'):
            if key in kwargs:
                body[key] = kwargs.pop(key)
        return self._request(kwargs.pop('path'), data=Utils.convert_body(body, False),
                             params=kwargs, headers={'Accept': self._MEDIA_LEGACY,
                                                     'Content-Type': self._MEDIA_LEGACY})

    @sp_endpoint('/sb/v4/legacyCampaigns/migrationJob/status', method='POST')
    def migration_job_status(self, jobId, **kwargs) -> ApiResponse:
        """
        Gets the status of a migration job.

        Request Body [Required]
            | **jobId** (string): [required]

        Returns:
            | ApiResponse, ``200``.

        .. note::
            An unknown ``jobId`` answers ``500 INTERNAL_ERROR`` rather than a
            business error. Not a sign that the route is missing.
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body({'jobId': jobId}, False),
                             params=kwargs, headers={'Accept': self._MEDIA_LEGACY,
                                                     'Content-Type': self._MEDIA_LEGACY})

    @sp_endpoint('/sb/v4/legacyCampaigns/migrationJob/results', method='POST')
    def migration_job_results(self, jobId, **kwargs) -> ApiResponse:
        """
        Lists the per-campaign results of a migration job.

        Request Body [Required]
            | **jobId** (string): [required]
            | **nextToken** (string): [optional]

        Returns:
            | ApiResponse, ``200``.

        .. note::
            An unknown ``jobId`` answers ``500 INTERNAL_ERROR``, as with the
            status route.
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body({'jobId': jobId}, False),
                             params=kwargs, headers={'Accept': self._MEDIA_LEGACY,
                                                     'Content-Type': self._MEDIA_LEGACY})

    @sp_endpoint('/sb/v4/legacyCampaigns/overallMigrationResults', method='POST')
    def overall_migration_results(self, **kwargs) -> ApiResponse:
        """
        Lists every campaign migration result for the advertiser.

        Request Body [Optional]
            | **nextToken** (string): [optional]

        Returns:
            | ApiResponse, ``200``. With nothing migrated yet the service answers
            an empty object rather than a list, so do not assume a ``migrations``
            key is always present.
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body(kwargs.pop('body', {}), False),
                             params=kwargs, headers={'Accept': self._MEDIA_LEGACY,
                                                     'Content-Type': self._MEDIA_LEGACY})

    @sp_endpoint('/sb/v4/migrations/list', method='POST')
    def list_migrations(self, **kwargs) -> ApiResponse:
        """
        Lists ad migrations.

        Request Body [Optional]
            | **adGroupIdFilter** ({}): ``include``, a list of ad group ids.
            | **adIdFilter** ({}): ``include``, a list of ad ids.
            | **campaignIdFilter** ({}): ``include``, a list of campaign ids.
            | **adStateFilter** ({}): ``include`` with ``ENABLED``, ``PAUSED``
              or ``ARCHIVED``.
            | **migrationStatusFilter** ({}): ``include`` with ``ACCEPTED``,
              ``ELIGIBLE``, ``MIGRATED`` or ``MIGRATION_FAILED``.
            | **maxResults** (number): Page size.
            | **nextToken** (string): Pagination token.

        Returns:
            | ApiResponse, ``200``, with ``migrations`` and ``totalCount``.

        Example::

            {"migrations": [], "totalCount": 0}
        """
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body(kwargs.pop('body', {}), False),
                             params=kwargs, headers={'Accept': self._MEDIA_ADMIG,
                                                     'Content-Type': self._MEDIA_ADMIG})
