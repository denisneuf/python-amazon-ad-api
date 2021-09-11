class AdvertisingApiException(Exception):
    code = 999
    def __init__(self, error):
        try:
            self.amzn_code = error
        except IndexError:
            pass
        self.error = error

class AdvertisingApiBadRequestException(AdvertisingApiException):
    """
    400	Request has missing or invalid parameters and cannot be parsed.
    """
    code = 400

    def __init__(self, error):
        super(SellingApiBadRequestException, self).__init__(error)


class AdvertisingApiForbiddenException(AdvertisingApiException):
    """
    403	Indicates access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature.
    """
    code = 403

    def __init__(self, error):
        super(SellingApiForbiddenException, self).__init__(error)


def get_exception_for_code(code: int):
    return {
        400: SellingApiBadRequestException,
        403: SellingApiForbiddenException,
        429: SellingApiRequestThrottledException,
        500: SellingApiServerException,
        503: SellingApiTemporarilyUnavailableException
    }.get(code, SellingApiException)


def get_exception_for_content(content: object):
    return {
        'UNAUTHORIZED': SellingApiUnauthorizedException
    }.get(content.get('code'), SellingApiException)
