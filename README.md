# PYTHON-AMAZON-AD-API

![CodeQL](https://img.shields.io/badge/coverage-95%25-green)
![CodeQL](https://img.shields.io/badge/Docs-sphinx-green)
![CodeQL](https://img.shields.io/github/v/release/denisneuf/python-amazon-ad-api)
[![Documentation Status](https://readthedocs.org/projects/python-amazon-ad-api/badge/?version=latest)](https://python-amazon-ad-api.readthedocs.io/en/latest/?badge=latest)
![PyPI Downloads](https://static.pepy.tech/badge/python-amazon-ad-api)
[![Downloads](https://static.pepy.tech/badge/python-amazon-ad-api/month)](https://pepy.tech/project/python-amazon-ad-api)
[![Downloads](https://static.pepy.tech/badge/python-amazon-ad-api/week)](https://pepy.tech/project/python-amazon-ad-api)

## Amazon's Advertising API

A python 3 wrapper to access Amazon's Advertising API with an easy-to-use interface.

### Install

[![Badge](https://img.shields.io/pypi/v/python-amazon-ad-api?style=for-the-badge)](https://pypi.org/project/python-amazon-ad-api/)

```
pip install python-amazon-ad-api
```

### Donate

If you find this project is useful consider donating or [sponsor](https://github.com/sponsors/denisneuf) it to keep on going on it, thank you.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate?hosted_button_id=G3KB6M2G9YV9C)

![alt text](https://github.com/denisneuf/python-amazon-ad-api/blob/main/test/codigo-QR.png?raw=true)


### Overview

You need obtain your own credentials with Amazon that may include an amazon developer account and access as seller or vendor. Please view the checklist of [Amazon Ads API onboarding overview](https://advertising.amazon.com/API/docs/en-us/setting-up/overview) 


### Code Credentials
You can use your credentials as follows passing it to the client as a dict. Please review the full [documentation](https://github.com/sponsors/denisneuf) to see all posibilities to include your credentials.

```javascript
from ad_api.api import ads_api_v1


my_credentials = dict(
    refresh_token='your-refresh_token',
    client_id='your-client_id',
    client_secret='your-client_secret',
    profile_id='your-profile_id',
)

info = {
    "adProductFilter":
        {
            "include": [
                "SPONSORED_PRODUCTS"
            ]
        },
    "stateFilter":
        {
            "include": [
                "ENABLED"
            ]
        }
}

result = ads_api_v1.Campaigns(credentials=my_credentials).query_campaigns(
    body=info
)

```

### YAML Credentials
Use a credentials.yml file with your credentials for more convenience and manage diferent accounts or profiles. Amazon requires one profile per marketplace so it is helpful to keep all in one file and switch directly from the code, using the account.

Create a file credentials.yml

```javascript
version: '1.0'

default:
  refresh_token: 'your-refresh-token'
  client_id: 'your-client-id'
  client_secret: 'your-client-secret'
  profile_id: 'your-profile-id'

germany:
  refresh_token: 'other-refresh-token'
  client_id: 'other-client-id'
  client_secret: 'other-client-secret'
  profile_id: 'other-profile-id'

```

Python code

```python
from ad_api.api import ads_api_v1

info = {
    "adProductFilter":
        {
            "include": [
                "SPONSORED_PRODUCTS"
            ]
        }
}

# Leave empty will use the 'default' account
result=ads_api_v1.Campaigns().query_campaigns(body=info)
# will use germany account data
result=ads_api_v1.Campaigns(account="germany").query_campaigns(body=info)
```



### Search path for credentials.yml

* macOS and Other Unix: `~/.config/python-ad-api`
* Windows: `%APPDATA%\python-ad-api` where the <cite>APPDATA</cite> environment variable falls
back to `%HOME%\AppData\Roaming` if undefined


[Confuse Help](https://confuse.readthedocs.io/en/latest/usage.html#search-paths)


### Marketplaces

Marketplaces are used to define basically the [API endpoints](https://advertising.amazon.com/API/docs/en-us/info/api-overview#api-endpoints) Amazon need to use depending on the regions, by default it will use EU so if you are using one of the marketplaces that are under the Europe (EU). Covers UK, FR, IT, ES, DE, NL, AE, SE, PL, and TR marketplaces you can skip. If you are using either North America (NA) or Far East (FE), you will need import from base and pass the marketplace as follows:

```python
from ad_api.api import ads_api_v1
from ad_api.base import Marketplaces

info = {
        "adProductFilter":
            {
                "include": [
                    "SPONSORED_PRODUCTS"
                ]
            }
    }

# You can pass NA or US, CA, MX or BR for North America and JP, AU or SG for Far East
result=ads_api_v1.Campaigns(marketplace=Marketplaces.NA).query_campaigns(body=info)

```

### Exceptions

You can use a [try](https://docs.python.org/3.10/reference/compound_stmts.html#try) except statement when you call the API and catch exceptions if some problem ocurred:

```python
from ad_api.api import ads_api_v1
from ad_api.base import AdvertisingApiException

info = {
    "adProductFilter":
        {
            "include": [
                "SPONSORED_PRODUCTS"
            ]
        },
    "stateFilter":
        {
            "include": [
                "ENABLED"
            ]
        }
}

try:

    result = ads_api_v1.Campaigns().query_campaigns(
        body=info
    )

    logging.info(result)

except AdvertisingApiException as error:
    logging.info(error)
```

### Debug

Use debug=True if you want see some logs like the header you submit to the api endpoint, the method and path used among the params and the data submitted if any, to trace some possible errors. Note that the header includes the Authorization bearer token, so do not leave debug output in shared logs.

```python
from ad_api.api import ads_api_v1
from ad_api.base import AdvertisingApiException


info = {
    "adProductFilter":
        {
            "include": [
                "SPONSORED_PRODUCTS"
            ]
        },
    "stateFilter":
        {
            "include": [
                "ENABLED"
            ]
        }
}

try:

    result = ads_api_v1.Campaigns(debug=True).query_campaigns(
        body=info
    )

    logging.info(result)

except AdvertisingApiException as error:
    logging.info(error)
```


### [Modules Available Common Resources](https://python-amazon-ad-api.readthedocs.io/en/latest/api.html)

| Module | Vendor contract | Vendor docs |
|---|---|---|
| [Profiles](https://python-amazon-ad-api.readthedocs.io/en/latest/api/profiles.html) | [contract](https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/profiles/3-0/openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/reference/profiles) |
| [Manager Accounts](https://python-amazon-ad-api.readthedocs.io/en/latest/api/manager_accounts.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ManagerAccount_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/reference/v0/managerAccount) |
| [PortfoliosV3](https://python-amazon-ad-api.readthedocs.io/en/latest/api/portfoliosV3.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Portfolios_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/reference/portfolios) |
| [Invoices](https://python-amazon-ad-api.readthedocs.io/en/latest/api/invoices.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdvertisingBilling_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/billing) |
| [Billing](https://python-amazon-ad-api.readthedocs.io/en/latest/api/billing.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdvertisingBilling_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/billing) |
| [Account Budgets](https://python-amazon-ad-api.readthedocs.io/en/latest/api/account_budgets.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Advertisers_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/account-budgets/) |
| [Audiences](https://python-amazon-ad-api.readthedocs.io/en/latest/api/audiences.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Audiences_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/audiences/) |
| [Change History](https://python-amazon-ad-api.readthedocs.io/en/latest/api/history.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Changehistory_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/change-history/) |
| [Creative Assets](https://python-amazon-ad-api.readthedocs.io/en/latest/api/creative_assets.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/creative-asset-library-openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/creative-asset-library) |
| [Eligibility](https://python-amazon-ad-api.readthedocs.io/en/latest/api/eligibility.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Eligibility_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/eligibility-prod-3p) |
| [Insights](https://python-amazon-ad-api.readthedocs.io/en/latest/api/insights.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Insights_prod_3p.json) | - |
| [Localization](https://python-amazon-ad-api.readthedocs.io/en/latest/api/localization.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Localization_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/localization/) |
| [Product Selector](https://python-amazon-ad-api.readthedocs.io/en/latest/api/metadata.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ProductSelector_prod_3p.json) | - |
| [Validation Configurations](https://python-amazon-ad-api.readthedocs.io/en/latest/api/validation_configurations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ValidationConfigurationsAPI_prod_3p.json) | - |
| [Tactical recommendations](https://python-amazon-ad-api.readthedocs.io/en/latest/api/recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Recommendations_prod_3p.json) | - |
| [Exports](https://python-amazon-ad-api.readthedocs.io/en/latest/api/exports.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIExports_prod_3p.json) | - |

### [Amazon Attribution open beta](https://python-amazon-ad-api.readthedocs.io/en/latest/api/attribution.html)

| Operation | Vendor contract | Vendor docs |
|---|---|---|
| [Advertisers](https://python-amazon-ad-api.readthedocs.io/en/latest/api/attribution.html#ad_api.api.Attribution.Attribution.get_advertisers) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/amazon-attribution-prod-3p) |
| [Publishers](https://python-amazon-ad-api.readthedocs.io/en/latest/api/attribution.html#ad_api.api.Attribution.Attribution.get_publishers) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/amazon-attribution-prod-3p) |
| [Macro tags](https://python-amazon-ad-api.readthedocs.io/en/latest/api/attribution.html#ad_api.api.Attribution.Attribution.get_macro_tag) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/amazon-attribution-prod-3p) |
| [Non Macro tags](https://python-amazon-ad-api.readthedocs.io/en/latest/api/attribution.html#ad_api.api.Attribution.Attribution.get_non_macro_template_tag) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/amazon-attribution-prod-3p) |
| [Reports](https://python-amazon-ad-api.readthedocs.io/en/latest/api/attribution.html#ad_api.api.Attribution.Attribution.post_report) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/amazon-attribution-prod-3p) |

### [Brand Metrics open beta](https://python-amazon-ad-api.readthedocs.io/en/latest/api/brand_metrics.html)

| Operation | Vendor contract | Vendor docs |
|---|---|---|
| [Post Report](https://python-amazon-ad-api.readthedocs.io/en/latest/api/brand_metrics.html#ad_api.api.BrandMetrics.BrandMetrics.post_report) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/BrandMetrics_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/guides/reporting/brand-metrics/overview) |
| [Get Report](https://python-amazon-ad-api.readthedocs.io/en/latest/api/brand_metrics.html#ad_api.api.BrandMetrics.BrandMetrics.get_report) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/BrandMetrics_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/guides/reporting/brand-metrics/overview) |
| [Download Report](https://python-amazon-ad-api.readthedocs.io/en/latest/api/brand_metrics.html#ad_api.api.BrandMetrics.BrandMetrics.download_report) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/BrandMetrics_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/guides/reporting/brand-metrics/overview) |

### [Advertising Test Account](https://python-amazon-ad-api.readthedocs.io/en/latest/api/advertising_test_account.html)

| Operation | Vendor contract | Vendor docs |
|---|---|---|
| [Create test account](https://python-amazon-ad-api.readthedocs.io/en/latest/api/advertising_test_account.html#ad_api.api.AdvertisingTestAccount) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdvertisingTestAccount_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/test-accounts/openapi) |
| [Get test account information](https://python-amazon-ad-api.readthedocs.io/en/latest/api/advertising_test_account.html#ad_api.api.AdvertisingTestAccount.AdvertisingTestAccount.get_test_account) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdvertisingTestAccount_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/test-accounts/openapi) |

### [Amazon Ads API v1 (new, unified)](https://python-amazon-ad-api.readthedocs.io/en/latest/v1.html)

> The v1 API lives under `/adsApi/v1/` and is **not** split by product: every call targets the same resource and the product is selected in the request body with `adProductFilter`. It supersedes the per-product v3 endpoints.

| Module | Vendor contract | Vendor docs |
|---|---|---|
| [Campaigns](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/campaigns.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLCampaignsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-campaigns) |
| [Ad Groups](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/ad_groups.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLAdGroupsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-adgroups) |
| [Ads](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/ads.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLAdsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-ads) |
| [Targets](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/targets.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLTargetsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-targets) |
| [Ad Extensions](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/ad_extensions.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLAdExtensionsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-adextensions) |
| [Advertiser Accounts](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/advertiser_accounts.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLAdvertiserAccountsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-advertiseraccounts) |
| [Ad Associations](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/ad_associations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLAdAssociationsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-adassociations) |
| [Brand Store Edition Publish Versions](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/brand_store_edition_publish_versions.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLBrandStoreEditionPublishVersionsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-brandstoreeditionpublishversions) |
| [Brand Stores](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/brand_stores.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLBrandStoresContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-brandstores) |
| [Brand Store Editions](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/brand_store_editions.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLBrandStoreEditionsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-brandstoreeditions) |
| [Brand Store Pages](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/brand_store_pages.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLBrandStorePagesContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-brandstorepages) |
| [Reports](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/reports.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLReportsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-reports) |
| [Labels](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/labels.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLLabelsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-labels) |
| [Manager Accounts](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/manager_accounts.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLManagerAccountsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-manager-accounts) |
| [Recommendations](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLRecommendationsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-recommendations) |
| [Selling Accounts](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/selling_accounts.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLSellingAccountsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-selling-accounts) |
| [Label Object Associations](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/label_object_associations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLLabelObjectAssociationsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-label-object-associations) |
| [Geo Locations](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/geo_locations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLGeoLocationsContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-geolocations) |
| [Location Indexes](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/location_indexes.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLLocationIndexesContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-locationindexes) |
| [Recommendation Types](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/recommendation_types.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLRecommendationTypesContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-recommendation-types) |
| [Portfolios](https://python-amazon-ad-api.readthedocs.io/en/latest/v1/portfolios.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLPortfoliosContract_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/api-spec-v1-portfolios) |

### [Modules Available Sponsored Products](https://python-amazon-ad-api.readthedocs.io/en/latest/sp.html)

> The campaign, ad group and product ad operations are deprecated in favour of the v1 endpoints. In product targeting only the four CRUD operations are deprecated; its helper endpoints remain supported. Keywords, negative keywords and negative product targeting have no v1 equivalent yet and stay supported.

| Module | Vendor contract | Vendor docs |
|---|---|---|
| [ThemeBased Bid Recommendation](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/bid_recommendations_v3.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Keyword Recommendations](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/ranked_keywords_recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Keywords](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/keywords_v3.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Negative Keywords](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/negative_keywords_v3.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Product Targeting](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/product_targeting_v3.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Campaign Optimization](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/campaign_optimization_rules.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Budget Rules](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/budget_rules.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Product Ads](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/product_ads_v3.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Negative Targeting Clauses](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/negative_product_targeting_v3.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Campaign Negative Targeting Clauses](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/campaign_negative_targets.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Budget recommendations and missed opportunities](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/product_recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Budget Rules Recommendation](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/budget_rules_recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Campaigns](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/campaignsv3.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Ad Groups](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/ad_groups_v3.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Consolidated Recommendations](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/campaigns_consolidated_recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Campaign Negative Keywords](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/campaign_negative_keywords_v3.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Product Recommendations](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/budget_recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Budget Usage](https://python-amazon-ad-api.readthedocs.io/en/latest/sp/campaign_budget_usage.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod) |
| [Reports](https://python-amazon-ad-api.readthedocs.io/en/latest/api/reports.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json) | [docs](https://advertising.amazon.com/API/docs/en-us/offline-report-prod-3p) |

### [Modules Available Sponsored Brands 3.0](https://python-amazon-ad-api.readthedocs.io/en/latest/sb_v3.html)

> Campaigns and Ad Groups are deprecated in v3: Amazon answers `403 Endpoint has been deprecated` and points to the v4 API. Use the 4.0 section below for those two.

| Module | Vendor contract | Vendor docs |
|---|---|---|
| [Campaigns (deprecated)](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/campaigns.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Ad Groups (deprecated)](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/ad_groups.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Keywords](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/keywords.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Negative Keywords](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/negative_keywords.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Keywords Recommendations](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/keywords_recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Product Targeting](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/product_targeting.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Negative Product Targeting](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/negative_product_targeting.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Targeting Recommendations](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/targeting_recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Bid Recommendations](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/bid_recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Benchmarks](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/benchmarks.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Stores](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/stores.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Landing Page Asins](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/landing_page_asins.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Media](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/media.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Brands](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/brands.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Themes](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/themes.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |
| [Reports](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/reports.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi) |

### [Modules Available Sponsored Brands 4.0](https://python-amazon-ad-api.readthedocs.io/en/latest/sb_v4.html)

> The 4.0 contract is fully covered: every operation is implemented except the campaign moderation route, which the service answers with a router `404`, and the report download, which resolves through the shared `_download` helper.

| Module | Vendor contract | Vendor docs |
|---|---|---|
| [Campaigns](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/campaigns_v4.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_4-0_openapi.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod) |
| [Ad Groups](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/ad_groups_v4.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_4-0_openapi.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod) |
| [Ads](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/ads_v4.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_4-0_openapi.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod) |
| [Ad Creatives](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/ad_creatives_v4.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_4-0_openapi.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod) |
| [Forecast](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/forecast.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_4-0_openapi.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod) |
| [Recommendations](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_4-0_openapi.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod) |
| [Budget Rules](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/budget_rules.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_4-0_openapi.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod) |
| [Optimization Rules](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/optimization_rules.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_4-0_openapi.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod) |
| [Targeting Categories](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/targeting_categories.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_4-0_openapi.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod) |
| [Migration](https://python-amazon-ad-api.readthedocs.io/en/latest/sb/migration.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-brands_4-0_openapi.json) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod) |

> Most 4.0 routes take a versioned media type and the service routes on it. With `application/json` they answer `404 Could not find resource`, which reads like a missing route but is only the wrong media type. This affects forecasts, budget recommendations, optimization rules, migrations, insights, negative brand recommendations and the collection creatives.

### [Modules Available Sponsored Display](https://python-amazon-ad-api.readthedocs.io/en/latest/sd.html)

| Module | Vendor contract | Vendor docs |
|---|---|---|
| [Campaigns](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/campaigns.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |
| [Ad Groups](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/ad_groups.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |
| [Reports](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/reports.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |
| [Product Ads](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/product_ads.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |
| [Targets](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/product_targeting.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |
| [Negative Targets](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/negative_product_targeting.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |
| [Targets Recommendations](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/targeting_recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |
| [Bid Recommendations](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/bid_recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |
| [Creatives](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/creatives.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |
| [Brand Safety List](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/brand_safety.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |
| [Budget Rules](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/budget_rules.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |
| [Campaigns Budget Usage](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/campaign_budget_usage.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |
| [Forecasts](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/forecast.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |
| [Recommendations](https://python-amazon-ad-api.readthedocs.io/en/latest/sd/recommendations.html) | [contract](https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/sponsored-display_3-0_openapi.yaml) | [docs](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi) |

### Amazon Ads API v1 - basic example

Both `v1` and `ads_api_v1` name the same namespace, so pick whichever reads
clearer: `from ad_api.api import v1` is shorter, and `ads_api_v1` makes it
obvious at the call site that the v1 API is being used.

```python
from ad_api.api import v1

result = v1.Campaigns(credentials=credentials, debug=True).query_campaigns(
    body={
        "adProductFilter": {"include": ["SPONSORED_PRODUCTS"]},
        "stateFilter": {"include": ["ENABLED"]},
        "maxResults": 100,
    }
)

campaigns = result.payload.get("campaigns")
next_token = result.payload.get("nextToken")
```

### Simple Example Usage Campaigns with Credentials (v3, legacy)

> This example uses `CampaignsV3.list_campaigns`, which is deprecated. See the v1 `query_campaigns` example above.

```python
import logging
from ad_api.base import AdvertisingApiException
from ad_api.api import sponsored_products

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

def sp_list_campaigns_v3(info: dict = None):

    credentials = dict(
        refresh_token='your-refresh_token',
        client_id='your-client_id',
        client_secret='your-client_secret',
        profile_id='your-profile_id',
    )

    try:
        result = sponsored_products.CampaignsV3(credentials=credentials, debug=True).list_campaigns(
            body=info
        )
        payload = result.payload
        return payload
    except AdvertisingApiException as error:
        logging.error(error)
        logging.error(error.code)


state_filter = \
    {
        "stateFilter":
            {
                "include": [
                    "ENABLED"
                ]
            }
    }

enabled_campaigns = sp_list_campaigns_v3(state_filter).get("campaigns")


for campaign in enabled_campaigns:
    logging.info(campaign)

logging.info(len(campaigns))



```

### API NOTICE

This API is based on the [API Client](https://github.com/saleweaver/rapid_rest_client) created by [@saleweaver](https://github.com/saleweaver) but adapted to amazon advertising authentication requeriments

### DISCLAIMER

We are not affiliated with Amazon but they used our api :)

### LICENSE

![License](https://img.shields.io/badge/license-MIT-green)


---
*Last release: v1.6.0*
