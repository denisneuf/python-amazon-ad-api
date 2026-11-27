User permissions
================

.. list-table::
    :header-rows: 0
    :widths: 18 82

    * - **Vendor docs**
      - https://advertising.amazon.com/API/docs/en-us/user-permissions
    * - **Specification**
      - https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdvertisingUserPermissionsManagement_prod_3p.json

Authorization and permission management for your Amazon Ads accounts.
Contract version 3.0.

A permission set ties a user to a role or a custom set of permissions on an
advertising account, optionally limited to some countries. These five
operations let you grant, revoke, read back and enumerate them, and list the
users of the account.

.. list-table::
    :header-rows: 1
    :widths: 10 30 24 36

    * - Method
      - Endpoint
      - Operation
      - Python
    * - PUT
      - ``/userPermissions``
      - UpdateUserPermissions
      - :meth:`ad_api.api.AdvertisingUserPermissions.update_user_permissions`
    * - POST
      - ``/userPermissions/delete``
      - DeleteUserPermissions
      - :meth:`ad_api.api.AdvertisingUserPermissions.delete_user_permissions`
    * - POST
      - ``/userPermissions/list``
      - QueryUserPermissions
      - :meth:`ad_api.api.AdvertisingUserPermissions.query_user_permissions`
    * - POST
      - ``/userRoles/list``
      - QueryUserRoles
      - :meth:`ad_api.api.AdvertisingUserPermissions.query_user_roles`
    * - POST
      - ``/users/list``
      - ListUsers
      - :meth:`ad_api.api.AdvertisingUserPermissions.list_users`

Media types
-----------

The two operations that write permissions use the long resource media type:

.. code-block:: text

    application/vnd.MinosAuthorizationNativeServicePublicAPI.UpdateUserPermissionsResource.v1+json
    application/vnd.MinosAuthorizationNativeServicePublicAPI.DeleteUserPermissionsResource.v1+json

The three that read use a short one:

.. code-block:: text

    application/vnd.queryuserpermissions.v1+json
    application/vnd.queryuserroles.v1+json
    application/vnd.listusers.v1+json

In all five the same media type goes on ``Accept`` and on ``Content-Type``.

Bodies
------

``UpdateUserPermissions`` takes ``userPermissions``, an array of entries with
``userId``, ``permissionSet`` and ``countryCodes``.

``DeleteUserPermissions`` takes ``users``, an array of ``{userId}``.

``QueryUserPermissions`` and ``QueryUserRoles`` both require ``userId`` and take
``countryCodesFilter``, ``maxResults`` and ``nextToken``; the first one also
takes ``accessScopeFilter``.

``ListUsers`` takes the two filters and the pagination pair, nothing required.

.. autoclass:: ad_api.api.AdvertisingUserPermissions
    :members:
    :noindex:
