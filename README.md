# PYTHON-AMAZON-AD-API [AMAZON ADVERTISING]

![CodeQL](https://img.shields.io/badge/coverage-15%25-yellow)

Python Amazon Advertising Api

### Set Up

Create a .env file and put in the root of your project ( SANDBOX or PRODUCTION )
```
# environment variables defined inside a .env file
AWS_ENV=SANDBOX
```


### Usage Campaigns

```
import logging
from ad_api.base import AdvertisingApiException, Marketplaces
from ad_api.api.sp import Campaigns

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

try:

    states = 'enabled'

    res = Campaigns(Marketplaces.ES).list_campaigns_extended_request(
        stateFilter=states
    )

    campaigns = res.payload
    for campaign in campaigns:
        logging.info(campaign)

    logging.info(len(campaigns))


except AdvertisingApiException as ex:
    print(ex)

```

### LICENSE

![License](https://img.shields.io/badge/license-MIT-green)
