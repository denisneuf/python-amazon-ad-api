# PYTHON-AMAZON-AD-API [AMAZON ADVERTISING]

![CodeQL](https://img.shields.io/badge/coverage-15%25-yellow)

Python Amazon Advertising Api

### Usage

```
import logging
from ad_api.base import SellingApiException, Marketplaces

def get_marketplace(argument):
    switcher = {
        'ES': Marketplaces.ES,
        'GB': Marketplaces.GB,
        'IT': Marketplaces.IT,
        'FR': Marketplaces.FR,
        'DE': Marketplaces.DE,
    }

    logging.info(switcher.get(argument))
    return switcher.get(argument)

marketplace = 'ES'
states = 'enabled'

# campaigns API
try:
    res = Campaigns(get_marketplace(marketplace)).list_campaigns_request(
        stateFilter=states
    )
except SellingApiException as ex:
    print(ex)

```

### LICENSE

![License](https://img.shields.io/badge/license-MIT-green)
