import time
import os
import json
from json.decoder import JSONDecodeError
from io import TextIOWrapper
from ad_api.base import AdvertisingTypeException

class Utils:

    @staticmethod
    def convert_body(body, wrap: bool = True):

        if isinstance(body, str):

            if os.path.isfile(body):
                body = open(body, mode="r", encoding="utf-8")
                body = body.read()
                try:
                    json.loads(body)
                except JSONDecodeError as error:
                    raise AdvertisingTypeException(f"{type(error)}", error)
            else:
                try:
                    body = json.loads(body)
                except ValueError as error:
                    raise AdvertisingTypeException(f"{type(error)}", error)
                pass

        if isinstance(body, dict) and wrap:
            try:
                body = json.dumps([body])
            except TypeError as error:
                raise AdvertisingTypeException(f"{type(error)}", error)

        if isinstance(body, dict) and wrap is False:
            try:
                body = json.dumps(body)
            except TypeError as error:
                raise AdvertisingTypeException(f"{type(error)}", error)

        if isinstance(body, list):
            try:
                body = json.dumps(body)
            except TypeError as error:
                raise AdvertisingTypeException(f"{type(error)}", error)

        if isinstance(body, TextIOWrapper):
            body = body.read()
            try:
                json.loads(body)
            except JSONDecodeError as error:
                raise AdvertisingTypeException(f"{type(error)}", error)

        return body

    def load_all_pages(throttle_by_seconds: float = 2, next_token_param='NextToken',
                       use_rate_limit_header: bool = False,
                       extras: dict = None):
        """
        Load all pages if a next token is returned

        Args:
            throttle_by_seconds: float
            next_token_param: str | The param amazon expects to hold the next token
            use_rate_limit_header: if the function should try to use amazon's rate limit header
            extras: additional data to be sent with NextToken, e.g `dict(QueryType='NEXT_TOKEN')` for `FulfillmentInbound`
        Returns:
            Transforms the function in a generator, returning all pages
        """
        if not extras:
            extras = {}

        def decorator(function):
            def wrapper(*args, **kwargs):
                res = function(*args, **kwargs)
                yield res
                if "nextCursor" in res.payload.get("payload"):
                    kwargs.clear()
                    kwargs.update({next_token_param: res.payload.get("payload")["nextCursor"], **extras})
                    sleep_time = throttle_by_seconds
                    for x in wrapper(*args, **kwargs):
                        yield x
                        if sleep_time > 0:
                            time.sleep(throttle_by_seconds)

            wrapper.__doc__ = function.__doc__
            return wrapper

        return decorator


    def load_all_categories(throttle_by_seconds: float = 2, next_token_param='NextToken',
                       use_rate_limit_header: bool = False,
                       extras: dict = None):
        """
        Load all pages if a next token is returned

        Args:
            throttle_by_seconds: float
            next_token_param: str | The param amazon expects to hold the next token
            use_rate_limit_header: if the function should try to use amazon's rate limit header
            extras: additional data to be sent with NextToken, e.g `dict(QueryType='NEXT_TOKEN')` for `FulfillmentInbound`
        Returns:
            Transforms the function in a generator, returning all pages
        """
        if not extras:
            extras = {}

        def decorator(function):
            def wrapper(*args, **kwargs):
                res = function(*args, **kwargs)
                yield res
                if next_token_param in res.payload:
                    # kwargs.clear()
                    kwargs.update({next_token_param: res.payload[next_token_param], **extras})
                    sleep_time = throttle_by_seconds
                    for x in wrapper(*args, **kwargs):
                        yield x
                        if sleep_time > 0:
                            time.sleep(throttle_by_seconds)

            wrapper.__doc__ = function.__doc__
            return wrapper

        return decorator