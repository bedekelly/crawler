from unittest.mock import MagicMock

import requests

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
