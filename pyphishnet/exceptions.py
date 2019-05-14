# https://docs.python.org/3/tutorial/errors.html


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class ResponseError(Error):
    """Exception raised for errors in the API response.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class ApiKeyError(Error):
    """Exception raised for when the user API key is not found in
    the environment variables.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
