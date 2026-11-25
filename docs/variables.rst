Environment Variables
=====================

*********************************
Use with environment variables
*********************************

.. list-table::
    :header-rows: 1

    * - Environment variable
      - Description
    * - ``AD_API_REFRESH_TOKEN``
      - The refresh token obtained via authorization
    * - ``AD_API_CLIENT_ID``
      - Your Login with Amazon app id
    * - ``AD_API_CLIENT_SECRET``
      - Your Login with Amazon client secret
    * - ``AD_API_PROFILE_ID``
      - Your profile id, sent as ``Amazon-Advertising-API-Scope``
    * - ``AD_API_DEFAULT_MARKETPLACE``
      - Marketplace used when the client is built without one. One of
        ``NA``, ``EU``, ``FE``; defaults to ``EU``

The first four are read together: if any of the three OAuth values is missing,
none of them is used and the client falls back to ``credentials.yml``.

To set environment variables in your python script, use:

..  code-block:: python

    import os

    os.environ.setdefault('AD_API_REFRESH_TOKEN', 'Your-Token-Here')
    os.environ.setdefault('AD_API_CLIENT_ID', 'Your-Client_Id-Here')
    os.environ.setdefault('AD_API_CLIENT_SECRET', 'Your-Client_Secret-Here')
    os.environ.setdefault('AD_API_PROFILE_ID', 'Your-Profile_Id-Here')

*********************************
Choosing the marketplace
*********************************

Without a marketplace the client points at the EU host. Set
``AD_API_DEFAULT_MARKETPLACE`` to change that for every call, or pass
``marketplace=Marketplaces.NA`` to a single client:

..  code-block:: bash

    export AD_API_DEFAULT_MARKETPLACE=NA

*********************************
Token cache
*********************************

The access token is held in an in-process cache, so a script that makes many
calls does not request a new token for each one. Two caches are kept, both sized
by the same variable:

..  code-block:: python

    cache = TTLCache(maxsize=int(os.environ.get('AD_API_AUTH_CACHE_SIZE', 10)), ttl=3200)
    grantless_cache = TTLCache(maxsize=int(os.environ.get('AD_API_AUTH_CACHE_SIZE', 10)), ttl=3200)

``cache`` holds tokens obtained with the scopes a call asks for;
``grantless_cache`` holds the ones obtained without them. ``AD_API_AUTH_CACHE_SIZE``
sets how many entries each keeps (10 by default), and the entry lives 3200
seconds, a little under the hour an access token lasts. One long-running process
serving several accounts is the case where raising it matters. The lifetime is
not configurable.

.. note::

    ``AD_API_ACCOUNT_ID`` and ``AD_API_MANAGER_ACCOUNT_ID`` are not read: the
    environment source only carries the profile id. Use ``credentials.yml`` or
    a dict in code when the call needs an account or a manager header.
