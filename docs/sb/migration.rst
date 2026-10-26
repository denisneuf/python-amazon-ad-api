Migration
=========

Sponsored Brands legacy campaign migration, from the 3.0 API to the 4.0 API.

.. autoclass:: ad_api.api.sb.Migration
    :members:

    ### Endpoint map

    .. list-table::
        :header-rows: 1

       * - Path
         - Method
         - Media type
       * - ``POST /sb/v4/legacyCampaigns/migrationJob``
         - ``start_migration_job``
         - ``vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4``
       * - ``POST /sb/v4/legacyCampaigns/migrationJob/status``
         - ``migration_job_status``
         - ``vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4``
       * - ``POST /sb/v4/legacyCampaigns/migrationJob/results``
         - ``migration_job_results``
         - ``vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4``
       * - ``POST /sb/v4/legacyCampaigns/overallMigrationResults``
         - ``overall_migration_results``
         - ``vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4``
       * - ``POST /sb/v4/migrations/list``
         - ``list_migrations``
         - ``vnd.sbAdMigration.v4``

    Two media types live in this family, and both are required as sent. The legacy
    one has an unusual shape — uppercase words and dots instead of the usual
    ``vnd.sbx…`` pattern — and is copied literally from the contract.

    .. warning::
        This family can move campaigns. ``start_migration_job`` starts a real
        migration of 3.0 campaigns into 4.0 and is **not reversible by a simple
        call**. It was never exercised while building this client, so its shape
        comes from the contract only.

        A timeout does **not** mean the migration failed: the job may still be
        running. Check ``migration_job_status`` before calling it again, or a
        second job may be queued.

    ### What is verified

    .. list-table::
        :header-rows: 1

       * - Route
         - Answer
       * - ``migrationJob/status``
         - ``500 INTERNAL_ERROR`` for an unknown ``jobId``; the route is live
       * - ``migrationJob/results``
         - same ``500`` for an unknown ``jobId``
       * - ``overallMigrationResults``
         - ``200``, an empty object with nothing migrated
       * - ``migrations/list``
         - ``200``, ``{"migrations": [], "totalCount": 0}``

    .. note::
        An unknown ``jobId`` answers ``500`` instead of a 400 or a 404. That is a
        service quirk, not a missing route: with a wrong media type the same
        route answers ``404 Could not find resource``, which looks different.

    .. note::
        ``overall_migration_results`` answers an empty object rather than a list
        when there is nothing to report, so do not assume a ``migrations`` key is
        always there.

    ### Media type, once more

    ``list_migrations`` answers ``404 Could not find resource`` when sent
    ``application/json``. This is the fourth family in the package with that
    behaviour, after :doc:`forecast`, :doc:`budget_rules` and
    :doc:`optimization_rules`.

    ### Start body

    .. code-block:: json

        {
            "campaignIds": ["1234567890"],
            "enableThemeTargeting": true,
            "isStagedMigration": false,
            "newCampaignState": "PAUSED",
            "brandEntityId": "ENTITY000000000000"
        }

    ``campaignIds`` and ``enableThemeTargeting`` are required; the rest are
    optional.

    ### Job bodies

    .. code-block:: json

        {"jobId": "JOB_ID"}
        {"jobId": "JOB_ID", "nextToken": "string"}

    The first goes to ``migration_job_status``, the second to
    ``migration_job_results``.

    ### List body

    .. code-block:: json

        {
            "campaignIdFilter": {"include": ["1234567890"]},
            "adStateFilter": {"include": ["ENABLED", "PAUSED"]},
            "migrationStatusFilter": {"include": ["ELIGIBLE", "MIGRATED"]},
            "maxResults": 10,
            "nextToken": "string"
        }

    Every member is optional. ``adGroupIdFilter`` and ``adIdFilter`` take the same
    ``include`` shape.

    ### Enumerations

    .. list-table::
        :header-rows: 1

       * - Field
         - Values
       * - ``adStateFilter``
         - ``ENABLED``, ``PAUSED``, ``ARCHIVED``
       * - ``migrationStatusFilter``
         - ``ACCEPTED``, ``ELIGIBLE``, ``MIGRATED``, ``MIGRATION_FAILED``

    ### Example python

    .. code-block:: python

        from ad_api.api.sb import Migration

        migration = Migration(account='account_name', debug=False)

        # what has already been migrated
        print(migration.list_migrations(body={}).payload)

        # every result for the advertiser
        print(migration.overall_migration_results(body={}).payload)

        # the status of one job
        print(migration.migration_job_status(jobId='JOB_ID').payload)

        # starting one: this changes the account
        # migration.start_migration_job(
        #     campaignIds=['1234567890'],
        #     enableThemeTargeting=True,
        # )

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi
