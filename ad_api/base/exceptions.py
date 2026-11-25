class AmbiguousEndpointHeader(Exception):
    """The route accepts several identity headers and the call did not pick one.

    Only raised when more than one of the route's headers is actually
    available; a route whose single declared header is present never gets
    here. The message lists the candidates and the exact selector= value for
    each, because the service decides what an answer covers from the header:
    the scope answers for one marketplace and the account for every one of
    them, so picking silently would return a different answer than the caller
    asked for.
    """

    SELECTORS = {
        'Amazon-Advertising-API-Scope': 'profile_id',
        'Amazon-Ads-AccountId': 'account_id',
        'Amazon-Advertising-API-Manager-Account': 'manager_account_id',
    }

    def __init__(self, path, method, candidates, account, source='yml'):
        self.path = path
        self.method = method
        self.candidates = candidates
        self.account = account
        self.source = source
        options = ', '.join("selector='" + self.SELECTORS.get(h, h) + "'" for h in candidates)
        super().__init__(
            f"{method} {path} can use any of {candidates} and "
            f"they are all available for account '{account}'. Pick one: {options}"
        )


class MissingEndpointHeader(Exception):
    """The route needs an identity header this account cannot supply.

    Raised before the request leaves. The message names the route, the header
    the route accepts, the credentials.yml key that would satisfy it, which
    of the three the account does hold, and where the credentials came from
    (a dict in code, the AD_API_* variables or the config file). Without it
    the call went out with no identity and the service answered with a 401 or
    a 400 that named none of that.
    """

    KEYS = {
        'Amazon-Advertising-API-Scope': 'profile_id',
        'Amazon-Ads-AccountId': 'account_id',
        'Amazon-Advertising-API-Manager-Account': 'manager_account_id',
    }

    def __init__(self, path, method, required, account, available, source='yml', reason=None):
        self.path = path
        self.reason = reason
        self.method = method
        self.required = required
        self.account = account
        self.available = available
        self.source = source
        self.missing = [self.KEYS.get(h, h) for h in required]
        held = ', '.join(self.KEYS.get(h, h) for h in available) or 'none'
        if source == 'code':
            where = 'the credentials dict passed in code'
        elif source == 'env':
            where = 'the AD_API_* environment variables'
        else:
            where = f"credentials.yml (account '{account}')"
        if reason == 'not-accepted':
            message = (
                f"{method} {path} only accepts {required}; the selector asked "
                f"for {', '.join(self.missing)}, which {where} does hold. "
                f"Drop the selector or pick one the route declares."
            )
        else:
            message = (
                f"{method} {path} needs one of {required}; "
                f"{', '.join(self.missing)} is missing from {where}. "
                f"It does hold: {held}"
            )
        super().__init__(message)


class AdvertisingApiException(Exception):
    def __init__(self, code, error, headers):
        try:
            self.message = error.get('details')
            self.amzn_code = error.get('code')
        except (IndexError, AttributeError):
            pass
        self.code = code
        self.error = error
        self.headers = headers

    def get_code(self):
        return self.code

    def get_error(self):
        return self.error

    def get_headers(self):
        return self.headers

    def get_amzn_code(self):
        return self.amzn_code

    def get_details(self):
        return self.message


class AdvertisingTypeException(Exception):
    code = 888

    def __init__(self, type, error):
        try:
            self.type = type
            self.message = error
        except IndexError:
            pass
        self.error = error


class AdvertisingApiBadRequestException(AdvertisingApiException):
    """
    400	Request has missing or invalid parameters and cannot be parsed.
    """

    code = 400

    def __init__(self, code, error, headers=None):
        super(AdvertisingApiBadRequestException, self).__init__(code, error, headers)


class AdvertisingApiUnauthorizedException(AdvertisingApiException):
    """
    401	Unauthorized. The request failed because the user is not authenticated or is not allowed to invoke the operation.
    """

    code = 401

    def __init__(self, code, error, headers=None):
        super(AdvertisingApiUnauthorizedException, self).__init__(code, error, headers)


class AdvertisingApiForbiddenException(AdvertisingApiException):
    """
    403	Forbidden. The request failed because user does not have access to a specified resource.
    """

    code = 403

    def __init__(self, code, error, headers=None):
        super(AdvertisingApiForbiddenException, self).__init__(code, error, headers)


class AdvertisingApiNotFoundException(AdvertisingApiException):
    """
    404	Not Found
    """

    code = 404

    def __init__(self, code, error, headers=None):
        super(AdvertisingApiNotFoundException, self).__init__(code, error, headers)


class AdvertisingApiUnprocessableEntityException(AdvertisingApiException):
    """
    422	Unprocessable Entity
    """

    code = 422

    def __init__(self, code, error, headers=None):
        super(AdvertisingApiUnprocessableEntityException, self).__init__(code, error, headers)


class AdvertisingApiTooManyRequestsException(AdvertisingApiException):
    """
    429	Too Many Requests. The request was rate-limited. Retry later.
    """

    code = 429

    def __init__(self, code, error, headers=None):
        super(AdvertisingApiTooManyRequestsException, self).__init__(code, error, headers)


class AdvertisingApiInternalServerErrorException(AdvertisingApiException):
    """
    500	Internal Server Error. Something went wrong on the server. Retry later and report an error if unresolved.
    """

    code = 500

    def __init__(self, code, error, headers=None):
        super(AdvertisingApiInternalServerErrorException, self).__init__(code, error, headers)


class AdvertisingApiTemporarilyUnavailableException(AdvertisingApiException):
    """
    503	Temporary overloading or maintenance of the server.
    """

    code = 503

    def __init__(self, code, error, headers=None):
        super(AdvertisingApiTemporarilyUnavailableException, self).__init__(code, error, headers)


class AdvertisingApiInvalidParameterValueException(AdvertisingApiException):
    """
    200	InvalidParameterValue
    """

    code = 200

    def __init__(self, code, error, headers=None):
        super(AdvertisingApiInvalidParameterValueException, self).__init__(code, error, headers)


def get_exception_for_code(code: int):
    return {
        400: AdvertisingApiBadRequestException,
        401: AdvertisingApiUnauthorizedException,
        403: AdvertisingApiForbiddenException,
        404: AdvertisingApiNotFoundException,
        422: AdvertisingApiUnprocessableEntityException,
        429: AdvertisingApiTooManyRequestsException,
        500: AdvertisingApiInternalServerErrorException,
        503: AdvertisingApiTemporarilyUnavailableException,
    }.get(code, AdvertisingApiException)


def get_exception_for_content(content: object):
    return {'InvalidParameterValue': AdvertisingApiInvalidParameterValueException}.get(422, AdvertisingApiException)
