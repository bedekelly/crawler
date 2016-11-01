"""
testing_tools.py:
    Similar to the ubiquitous "utilities.py", this file should
    contain miscellaneous tools for testing. Currently, it has
    the function which mocks the functionality of requests.get
    so that we don't have to go out over the network for every
    unit-test.
"""

import requests
from unittest.mock import MagicMock

from .fixtures import MOCK_GET_DATA


def mock_requests_get(url):
    """
    Pretend to fetch the data from a URL, as requests.get does.

    :param url: The URL to fetch data from.
    :return: A mocked Requests response.
    """
    try:
        mock_data = MOCK_GET_DATA[url]
    except KeyError:
        raise requests.exceptions.ConnectionError()

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.content = mock_data

    return mock_response
