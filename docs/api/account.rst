Advertising accounts
=====================

.. list-table::
    :header-rows: 0
    :widths: 18 82

    * - **Vendor docs**
      - https://advertising.amazon.com/API/docs/en-us/accounts/openapi
    * - **Specification**
      - https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AdvertisingAccounts_prod_3p.json

Public API for managing advertising accounts. Contract version 3.0.

Advertisement accounts are the containers campaigns live in. An account is tied
to an Amazon vendor, seller or author, or to a business that does not sell on
Amazon. ``RegisterAdsAccount`` creates one; ``ListAdsAccounts`` and
``GetAccount`` read them back.

The account id is the global advertising account id, in the form
``amzn1.ads-account.g.xxx``. The list and register operations take versioned
media types, ``application/vnd.listaccountsresource.v1+json`` and
``application/vnd.registeradsaccountresource.v1+json``; the get operation
answers ``application/vnd.accountresource.v1+json``.

.. list-table::
    :header-rows: 1
    :widths: 10 32 26 32

    * - Method
      - Endpoint
      - Operation
      - Python
    * - POST
      - ``/adsAccounts``
      - RegisterAdsAccount
      - :meth:\`ad_api.api.Account.create_account\`
    * - POST
      - ``/adsAccounts/list``
      - ListAdsAccounts
      - :meth:\`ad_api.api.Account.list_accounts\`
    * - GET
      - ``/adsAccounts/{advertisingAccountId}``
      - GetAccount
      - :meth:\`ad_api.api.Account.get_account\`
    * - POST
      - ``/termsTokens``
      - CreateTermsToken
      - :meth:`ad_api.api.Account.create_terms_token`
    * - GET
      - ``/termsTokens/{termsToken}``
      - GetTermsToken
      - :meth:`ad_api.api.Account.get_terms_token`

Terms Token
-----------

``CreateTermsToken`` mints a UUID terms token and answers the URL the customer
has to open to accept the ads agreement:

.. code-block:: json

    {
      "termsToken": "4de3327e-a595-44cb-b689-f7f746805c02",
      "termsUrl": "https://advertising.amazon.com/terms/agreement/4de3327e-a595-44cb-b689-f7f746805c02"
    }

``GetTermsToken`` answers only the acceptance state, ``ACCEPTED`` or not. The
body of the create takes ``accountId`` (optional) and ``termsType``, one of
``ADSP``, ``ADVERTISING``, ``MARKETING_CLOUD`` or ``PARTNER_NETWORK``.
