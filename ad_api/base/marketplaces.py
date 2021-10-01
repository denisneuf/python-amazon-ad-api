import sys
import os
import logging
from enum import Enum
from dotenv import dotenv_values

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

class AuthorizationError(Exception):
    def __init__(self, code, message=".env problem set your file in the root project"):
        logging.warning(message);

class AWS_ENV(Enum):
    PRODUCTION = "PRODUCTION"
    SANDBOX = "SANDBOX"


class Marketplaces(Enum):
    NA = {'sandbox': 'advertising-api-test.amazon.com',
           'prod': 'advertising-api.amazon.com',
           'currency': 'USD',
           'token_url': 'api.amazon.com/auth/o2/token'}

    EU = {'sandbox': 'advertising-api-test.amazon.com',
           'prod': 'advertising-api-eu.amazon.com',
           'currency': 'EUR',
           'token_url': 'api.amazon.com/auth/o2/token'}

    GB = {'sandbox': 'advertising-api-test.amazon.com',
           'prod': 'advertising-api-eu.amazon.com',
           'currency': 'GBP',
           'token_url': 'api.amazon.com/auth/o2/token'}

    ES = {'sandbox': 'advertising-api-test.amazon.com',
           'prod': 'advertising-api-eu.amazon.com',
           'currency': 'EUR',
           'token_url': 'api.amazon.com/auth/o2/token'}

    DE = {'sandbox': 'advertising-api-test.amazon.com',
           'prod': 'advertising-api-eu.amazon.com',
           'currency': 'EUR',
           'token_url': 'api.amazon.com/auth/o2/token'}

    IT = {'sandbox': 'advertising-api-test.amazon.com',
           'prod': 'advertising-api-eu.amazon.com',
           'currency': 'EUR',
           'token_url': 'api.amazon.com/auth/o2/token'}

    FR = {'sandbox': 'advertising-api-test.amazon.com',
           'prod': 'advertising-api-eu.amazon.com',
           'currency': 'EUR',
           'token_url': 'api.amazon.com/auth/o2/token'}

    def __init__(self, info):

        config = dotenv_values(".env")
        AWS_ENVIRONMENT = config.get('AWS_ENV') or os.environ.get('API_PASSWORD')
        if AWS_ENVIRONMENT=="PRODUCTION":
            self.region_url = info.get('prod')
        else:
            self.region_url = info.get('sandbox')

        self.endpoint = 'https://{}'.format(self.region_url)
        self.currency = info.get('currency')
