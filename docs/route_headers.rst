Credential Headers (Beta)
=========================

Which routes declare which identity header, as of 2.1.14. A route that declares
a header sends only that one; a route with an empty list sends none. The rule
and the selector argument are on :doc:`config`. Every module below was checked
route by route, and the count is how many of its routes carry the mark.

Routes with an empty list
-------------------------

These answer from the token alone, so they never receive an identity header.

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
      - done, plus 5 ``@Utils.deprecated``

Routes marked with the scope
----------------------------

One marketplace per answer. The client sends ``Amazon-Advertising-API-Scope``
and drops the other two headers.

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

Routes that accept several
--------------------------

The call picks with ``selector=``; with several headers present and no
selector the client raises ``AmbiguousEndpointHeader`` instead of guessing.

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
