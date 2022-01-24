## PYTHON-AMAZON-AD-API [AMAZON ADVERTISING]

![CodeQL](https://img.shields.io/badge/coverage-59%25-yellow)
![CodeQL](https://img.shields.io/badge/Docs-sphinx-green)
![CodeQL](https://img.shields.io/github/v/release/denisneuf/python-amazon-ad-api)
[![Documentation Status](https://readthedocs.org/projects/python-amazon-ad-api/badge/?version=latest)](https://python-amazon-ad-api.readthedocs.io/en/latest/?badge=latest)

Python Amazon Advertising Api

### Install

[![Badge](https://img.shields.io/pypi/v/python-amazon-ad-api?style=for-the-badge)](https://pypi.org/project/python-amazon-ad-api/)

```
pip install python-amazon-ad-api
```


### Donate

If you find this project is useful consider donating to keep on going on it, thank you.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate?hosted_button_id=G3KB6M2G9YV9C)

![alt text](https://github.com/denisneuf/python-amazon-ad-api/blob/main/test/codigo-QR.png?raw=true)


### Set Up

Create a .env file and put in the root of your project ( SANDBOX or PRODUCTION )
```
# environment variables defined inside a .env file
AWS_ENV=SANDBOX
```
<pre><code>.
├── .env
└── campaign_client.py
</code></pre>


### Switcher SandBox Environment
Use a .env to manage the environment. Is high recommended try the SANDBOX environment as some features may delete (archive) modules as campaigns, ad groups,...etc and this cannot be undone.

```javascript
AWS_ENV=SANDBOX
# AWS_ENV=PRODUCTION
```
You may create a test profile id to include in your credentials with a curl command, note the ***{"countryCode":"ES"}*** that refers to the marketplace you will operate.


```javascript
curl \
    -X PUT \
    -H "Content-Type:application/json" \
    -H "Authorization: Bearer Your-Token \
    -H "Amazon-Advertising-API-ClientId: your-client-id" \
    --data '{"countryCode":"ES"}' \
     https://advertising-api-test.amazon.com/v2/profiles/register

```

### Credentials
Use a credentials.yml file with your credentials if you dont know how to obtain your refresh token, please visit:

[Login with Amazon application](https://advertising.amazon.com/API/docs/en-us/setting-up/step-1-create-lwa-app)

```javascript
version: '1.0'

default:
  refresh_token: 'your-refresh-token'
  client_id: 'your-client-id'
  client_secret: 'your-client-secret'
  profile_id: 'your-profile-id'

```

### Search path for credentials.yml

* macOS and Other Unix: `~/.config/python-ad-api`
* Windows: `%APPDATA%\python-ad-api` where the <cite>APPDATA</cite> environment variable falls
back to `%HOME%\AppData\Roaming` if undefined


[Confuse Help](https://confuse.readthedocs.io/en/latest/usage.html#search-paths)


### Modules Available Common Resources

* Profiles
* Invoices aka Billing
* Elegibility
* Metadata aka Product metadata
* History
* Localization
* Audiences
* Portfolios
* Insights

### Amazon Attribution open beta
* Advertisers
* Publishers
* Attribution tags
* Reports


### Modules Available Sponsored Products 2.0

* Ad Groups
* Bid Recommendations
* Campaigns
* Keywords
* Negative Keywords
* Product Ads
* Suggested Keywords
* Product Targeting
* Negative Product Targeting
* Campaign Negative Keywords
* Reports
* Snapshots

### Modules Available Sponsored Products 3.0


* Budget Rules
* Campaign Optimization Rules
* Ranked Keywords Recommendations
* Product Targeting
* Budget Recommendations
* Budget Rules Recommendations
* Product Recommendations


### Modules Available Sponsored Brands

* Campaigns
* Ad Groups
* Keywords
* Negative Keywords
* Product Targeting
* Negative Product Targeting
* Targeting Recommendations
* Bid Recommendations
* Stores
* Landing Page Asins
* Media
* Brands
* Moderation
* Reports

### Modules Available Sponsored Display

* Campaigns
* Ad Groups
* Reports
* Product Ads
* Targets
* Negative Targets
* Targets Recommendations
* Bid Recommendations
* Creatives


### Example Usage Campaigns

```python
import logging
from ad_api.base import AdvertisingApiException, Marketplaces
from ad_api.api.sp import Campaigns

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

try:

    states = 'enabled'

    res = Campaigns().list_campaigns_extended(
        stateFilter=states
    )

    campaigns = res.payload
    for campaign in campaigns:
        logging.info(campaign)

    logging.info(len(campaigns))


except AdvertisingApiException as error:
    logging.info(error)

```

### LICENSE

![License](https://img.shields.io/badge/license-MIT-green)
