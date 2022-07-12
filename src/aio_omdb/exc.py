class OMDBClientError(Exception):
    pass


class InvalidAPIKey(OMDBClientError):
    pass


class MovieNotFound(OMDBClientError):
    pass
