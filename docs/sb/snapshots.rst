Snapshots
=========

.. warning::

    Currently, the Ads API does not support snapshots for Sponsored Brands video campaigns or campaigns created using the version 4 endpoints. Snapshots include records for version 3, non-video campaigns only.

.. autoclass:: ad_api.api.sb.Snapshots

    .. autofunction:: ad_api.api.sb.Snapshots.post_snapshot(self, recordType, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.Snapshots.get_snapshot(self, reportId, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.Snapshots.download_snapshot(self, **kwargs) -> ApiResponse:
