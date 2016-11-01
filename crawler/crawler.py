"""
crawler.py:
    This module contains much of the business logic to crawl a webpage.

    It delegates to the other Python source files in this package for things
    like network interaction and parsing HTML data.
"""


import requests.exceptions as exc

from .networking import get_raw_data
from .parsing import parse_data, on_same_domain
from .utilities import add_to_sitemap


def _crawl(url, sitemap=None, max_depth=2):
    """
    Internal implementation of the `crawl` function. This is separate so
    as not to expose the `sitemap` parameter, which is used for recursion
    and shouldn't ever be manually passed in by the user.

    :param max_depth: How many site-links we should follow in this crawl.
    :param url: The URL to crawl.
    :return: A sitemap of the given URL, with static assets and page links.
    """

    # Initialise the sitemap with an empty mapping.
    if sitemap is None:
        sitemap = {}

    # Don't crawl too deeply or too greedily!
    if max_depth < 0:
        return

    # Retrieve data from the website and parse it for useful information.
    try:
        site_data = get_raw_data(url)
        data = parse_data(site_data, url)
    except (exc.InvalidURL, exc.MissingSchema, exc.ConnectionError):
        sitemap[url] = {"error": "Couldn't connect to URL: \"{}\"".format(url)}
        return sitemap

    # Add the data we've found into the sitemap.
    add_to_sitemap(
        sitemap=sitemap,
        url=url,
        data=data
    )

    # Recursively crawl links and add them to the sitemap too.
    for link in data.links:
        if link not in sitemap and on_same_domain(link, url):
            _crawl(link, sitemap=sitemap, max_depth=max_depth-1)

    return sitemap


def crawl(url, max_depth=2):
    """
    Crawl a URL, to return a sitemap limited by domain which includes
    information about which static assets each page may depend on, and
    the links between pages.
    :param url: The URL to start crawling with.
    :param max_depth: How many site-links we should follow in this crawl.
    :return: A sitemap in Python dict format.
    """
    return _crawl(url, max_depth=max_depth)
