import requests
from .caching import cache


@cache
def get_raw_data(url):
    """
    Given a URL, return the data that webpage returns.

    :param url: The URL to fetch data from.
    :return: Raw text data retrieved from the given URL.
    """
    return requests.get(url).content
