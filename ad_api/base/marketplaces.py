import sys
from enum import Enum
from dotenv import dotenv_values

class AWS_ENV(Enum):
    PRODUCTION = "PRODUCTION"
    SANDBOX = "SANDBOX"

config = dotenv_values(".env")

AWS_ENVIRONMENT = config.get('AWS_ENV')

BASE_URL_EU = "https://advertising-api-eu.amazon.com"
BASE_URL_US = "https://advertising-api.amazon.com"

if AWS_ENV(AWS_ENVIRONMENT) is AWS_ENV.SANDBOX:
    BASE_URL_EU = "https://advertising-api-test.amazon.com"
    BASE_URL_US = "https://advertising-api-test.amazon.com"

class Marketplaces(Enum):
    """Enumeration for MWS marketplaces, containing endpoints and marketplace IDs.
    Example, endpoint and ID for UK marketplace:
        endpoint = Marketplaces.UK.endpoint
        marketplace_id = Marketplaces.UK.marketplace_id
    """

    US = (f"{BASE_URL_US}", 'EUR')
    ES = (f"{BASE_URL_EU}", 'EUR')
    GB = (f"{BASE_URL_EU}", 'GBP')
    IT = (f"{BASE_URL_EU}", 'EUR')
    FR = (f"{BASE_URL_EU}", 'EUR')
    DE = (f"{BASE_URL_EU}", 'EUR')


    def __init__(self, endpoint, currency):
        """Easy dot access like: Marketplaces.endpoint ."""
        self.endpoint = endpoint
        self.currency = currency
