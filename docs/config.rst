Config File
===========

An example config file is provided in this repository, it supports multiple accounts.
The program looks for a file called `credentials.yml`_

The config is parsed by `confused`_, see their docs for more in depth information.
Search paths are:

..  code-block:: bash

    macOS: ~/.config/python-sp-api
    Other Unix: ~/.config/python-sp-api
    Windows: %APPDATA%\python-sp-api where the APPDATA environment variable falls back to %HOME%\AppData\Roaming if undefined

If you're only using one account, place it under default. You can pass the account's name to the client to use any other account used in the `credentials.yml`_ file.

..  code-block:: yaml

    version: '1.0'

    default:
      refresh_token: ''
      client_id: ''
      client_secret: ''
      profile_id: ''
      account_id: ''
      manager_account_id: ''

    another_account:
      refresh_token: ''
      client_id: ''
      client_secret: ''
      profile_id: ''
      account_id: ''
      manager_account_id: ''


**************************
Usage with default account
**************************

..  code-block:: python

    Campaigns().list_campaigns()


**************************
Usage with another_account
**************************

You can use every account's name from the config file for account

..  code-block:: python

	Campaigns(account="another_account", marketplace=Marketplaces.ES).list_campaigns()


.. rubric:: References

.. target-notes::

.. _`credentials.yml`: https://github.com/denisneuf/python-amazon-ad-api/#credentials
.. _`confused`: https://confuse.readthedocs.io/en/latest/usage.html#search-paths




******************************
Identifiers and route headers
******************************

Every account has three identifiers and the API sends at most one of them per
request, in a header:

.. list-table::
    :header-rows: 1

    * - credentials.yml key
      - header
      - scope of the answer
    * - ``profile_id``
      - ``Amazon-Advertising-API-Scope``
      - one marketplace
    * - ``account_id``
      - ``Amazon-Ads-AccountId``
      - every marketplace
    * - ``manager_account_id``
      - ``Amazon-Advertising-API-Manager-Account``
      - the accounts of a manager

.. note::

    **A first group of routes is marked in 2.1.14.** The rest still behave as
    they did in 2.1.12 and send whatever the credentials carry. The routes that
    declare a header, and the call that proved each one, are on
    :doc:`route_headers`. Families are marked release by release as each one is
    verified against the service.

Not every route accepts all three. Each route declares the ones it takes, and
the client sends only those: a route marked with the scope never receives the
account header, even when the credentials carry both.

.. rubric:: The scope is the default

With no further argument the client sends ``profile_id`` as
``Amazon-Advertising-API-Scope``, which is what this package has always done.
An account with only ``profile_id`` in its entry needs no change.

.. code-block:: yaml

    another_account:
      refresh_token: '...'
      client_id: '...'
      client_secret: '...'
      profile_id: 'your-profile-id'

.. rubric:: When the credentials hold more than one identifier

A route that accepts several identifiers cannot guess which answer you want:
the same billing query returns one marketplace for the scope and every
marketplace for the account. The call has to say it, through ``selector=``:

.. code-block:: python

    from ad_api.api import Billing

    api = Billing(account="another_account")

    api.invoice_summaries(body={}, selector="profile_id")           # one marketplace
    api.invoice_summaries(body={}, selector="account_id")           # all of them
    api.invoice_summaries(body={}, selector="manager_account_id")   # via the manager

The value is the key you already write in ``credentials.yml``. Leave it out when
the account holds a single identifier, and the default applies.

.. rubric:: Routes that need no identifier

Some routes answer with the token alone: they are the ones that list the
identifiers themselves. ``Profiles.list_profiles`` and
``AdvertiserAccounts.query_advertiser_accounts`` work with no ``profile_id``,
no ``account_id`` and no ``manager_account_id`` in the entry, which is what makes
them the place to start on a new account:

.. code-block:: python

    from ad_api.api import Profiles

    Profiles(account="new_account").list_profiles()

They are marked with an empty header list, so the client drops every identity
header even when the credentials carry one.

.. rubric:: Errors that name what is missing

Two exceptions replace the silent request that used to leave without a header:

::

    MissingEndpointHeader: POST /sp/campaigns/list needs one of
    ['Amazon-Advertising-API-Scope']; profile_id is missing from credentials.yml
    (account 'another_account'). It does hold: account_id, manager_account_id

    AmbiguousEndpointHeader: POST /invoiceSummaries/list can use any of
    ['Amazon-Advertising-API-Scope', 'Amazon-Ads-AccountId'] and they are all
    available for account 'another_account'. Pick one: selector='profile_id',
    selector='account_id'

The first says what the route needs and where to add it. The second says the
route could use several and the call did not choose.

A third shape covers the case where the selector names an identifier the route
does not accept. It is not a missing credential and the message says so:

::

    MissingEndpointHeader: POST /history only accepts
    ['Amazon-Advertising-API-Scope']; the selector asked for manager_account_id,
    which credentials.yml (account 'another_account') does hold. Drop the
    selector or pick one the route declares.
