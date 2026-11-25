Credential Headers (Beta)
=========================

Which routes need which credentials, as of 2.1.14. Every module below was
checked route by route; the count is how many of its routes carry the mark.
The rule and the ``selector=`` argument are on :doc:`config`.

The OAuth trio is required by every route, wherever it comes from -- the
config file, a dict in code or the environment variables:

..  list-table::
    :header-rows: 1

    * - Credentials key
      - Sent as
    * - ``refresh_token``
      - the bearer token
    * - ``client_id``
      - ``Amazon-Advertising-API-ClientId``
    * - ``client_secret``
      - used to obtain the token

The three identifiers are optional and each route takes a fixed set of them:

..  list-table::
    :header-rows: 1

    * - Credentials key
      - Sent as
    * - ``profile_id``
      - ``Amazon-Advertising-API-Scope``
    * - ``account_id``
      - ``Amazon-Ads-AccountId``
    * - ``manager_account_id``
      - ``Amazon-Advertising-API-Manager-Account``

Routes that need no identifier
-------------------------------

``refresh_token``, ``client_id`` and ``client_secret`` are enough. The three
identifiers may be set and are not sent: these routes list the identifiers
themselves, so they cannot require one.

..  list-table::
    :header-rows: 1

    * - Module
      - Family
      - Routes marked
      - State
    * - ``account.py``
      - v0
      - 5/5
      - done
    * - ``advertising_test_account.py``
      - v0
      - 2/2
      - done
    * - ``manager_accounts.py``
      - v0
      - 4/4
      - done
    * - ``profiles.py``
      - v0
      - 4/4
      - done

Routes that need ``profile_id``
--------------------------------

One marketplace per answer. The client sends ``Amazon-Advertising-API-Scope``
and drops the other two headers, even when the credentials carry them.

..  list-table::
    :header-rows: 1

    * - Module
      - Family
      - Routes marked
      - State
    * - ``history.py``
      - v0
      - 1/1
      - done
    * - ``stores.py``
      - v0
      - 2/2
      - done
    * - ``v1/campaigns.py``
      - v1
      - 1/4
      - query only
    * - ``sp/campaigns_v3.py``
      - v3
      - 1/4
      - list only

Routes that accept any of the three
-----------------------------------

The call picks with ``selector=``. With more than one identifier in the
credentials and no selector, the client raises ``AmbiguousEndpointHeader``
instead of guessing.

..  list-table::
    :header-rows: 1

    * - Module
      - Family
      - Routes marked
      - State
    * - ``billing.py``
      - v0
      - 1/19
      - ``invoice_summaries`` only
