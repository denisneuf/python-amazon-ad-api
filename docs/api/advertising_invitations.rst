User invitations
================

.. list-table::
    :header-rows: 0
    :widths: 18 82

    * - **Vendor docs**
      - https://advertising.amazon.com/API/docs/en-us/user-invitations
    * - **Specification**
      - https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AdvertisingInvitations_prod_3p.json

Manage invitations for advertising accounts. Contract version 3.0.

An invitation grants a person access to an advertising account, with a
permission set and a list of countries. It is created, listed, read back,
revoked through an update, and finally redeemed by the invited person.

Every operation carries its own versioned media type, used for both ``Accept``
and ``Content-Type``: ``application/vnd.<Operation>.v1+json``.

.. list-table::
    :header-rows: 1
    :widths: 10 32 26 32

    * - Method
      - Endpoint
      - Operation
      - Python
    * - POST
      - ``/user-invitations``
      - CreateUserInvitations
      - :meth:`ad_api.api.AdvertisingInvitations.create_user_invitations`
    * - PUT
      - ``/user-invitations``
      - UpdateUserInvitations
      - :meth:`ad_api.api.AdvertisingInvitations.update_user_invitations`
    * - POST
      - ``/user-invitations/list``
      - ListUserInvitations
      - :meth:`ad_api.api.AdvertisingInvitations.list_user_invitations`
    * - PUT
      - ``/user-invitations/redeem``
      - RedeemUserInvitation
      - :meth:`ad_api.api.AdvertisingInvitations.redeem_user_invitation`
    * - GET
      - ``/user-invitations/{invitationId}``
      - GetUserInvitation
      - :meth:`ad_api.api.AdvertisingInvitations.get_user_invitation`

Bodies
------

``CreateUserInvitations`` takes ``userInvitationRequests``, the only required
member, and an optional ``notifyInvitedUsers``. Each request carries a ``user``
with ``emailAddress`` and ``userName``, a ``permissionSet``, and ``countries`` as
two-letter ISO codes.

``UpdateUserInvitations`` takes ``updates``, each with ``invitationId`` and the
``state`` to move it to. ``REVOKE`` is the state the contract names.

``ListUserInvitations`` takes ``maxResults`` and ``nextToken``, neither required.

``RedeemUserInvitation`` takes ``invitationId``, the only required member.

.. note::

   The contract declares no 2xx response for ``RedeemUserInvitation``: only 400,
   403, 404 and 500. The operation exists and is implemented; the success code
   is simply not written down in the specification.

.. autoclass:: ad_api.api.AdvertisingInvitations
    :members:
    :noindex:
