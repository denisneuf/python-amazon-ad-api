import logging
from ad_api.base import AdvertisingApiException
from ad_api.api.sp import Campaigns

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

try:
    states = 'enabled'
    result = Campaigns().list_campaigns_extended_request(
        stateFilter=states
    )

    campaigns = result.payload
    for campaign in campaigns:
        logging.info(campaign)


except AdvertisingApiException as e:
    logging.error(e)
