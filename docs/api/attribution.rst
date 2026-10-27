Amazon Attribution API open beta
================================

Current contract:

`https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json`_

.. _https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json

Previously, Amazon served the same specification from a different host:

`https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json`_

.. _https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json

**Amazon Attribution**

Amazon Attribution is an advertising measurement product that enables advertisers to understand the impact that their non-Amazon ads (i.e. Google Ads, Facebook, Microsoft Ads) have in driving shopping activity on Amazon. Measuring ads using Amazon Attribution is done through implementing Attribution tags on non-Amazon ads. Amazon Attribution is currently available in beta for US, CA, UK, DE, FR, IT, and ES vendors and professional sellers enrolled in Brand Registry.

**Amazon Attribution API**

The Amazon Attribution API enables agencies and integrators to easily retrieve their advertiser client's non-Amazon publisher attribution tags to automate tag implementation on their non-Amazon ads that link to an Amazon product or Stores page. The API also enables agencies and integrators to create and retrieve reporting on behalf of their advertiser clients to better understand Amazon conversion performance on their campaigns.

Note that you must pass a header named Amazon-Advertising-Api-Scope with each call to an Amazon Attribution API URI, including GET /advertisers. The value for this header is the profileId available from the Profiles resource (/v2/profiles).

.. autoclass:: ad_api.api.Attribution
    :members:
