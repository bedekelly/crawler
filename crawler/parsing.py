import urllib.parse
from collections import namedtuple

from bs4 import BeautifulSoup

ParsedData = namedtuple("ParsedData", ["links", "images", "scripts"])


def on_same_domain(url_one, url_two):
    """
    Test whether two URLs are on the same domain.

    :param url_one: The first URL.
    :param url_two: The second URL.
    :return boolean: True if the domains match, false otherwise.
    """
    domain_one = urllib.parse.urlsplit(url_one).netloc
    domain_two = urllib.parse.urlsplit(url_two).netloc

    def get_sld(domain):
        """
        Given a domain name, return the second-level domain to which it
        belongs. For instance:

         get_sld("a.b.google.com") == "google.com"

        :param domain: A domain with any number of sub-domains.
        :return: The second-level domain to which it belongs.
        """
        return ".".join(domain.rsplit(".")[-2:])

    sld_one = get_sld(domain_one)
    sld_two = get_sld(domain_two)

    return sld_one == sld_two


def find_attributes(soup, element, attribute):
    """
    Given a BeautifulSoup `soup` instance, find all the values belonging
    to the given attribute inside the given element type.

    :param soup: A BS4 `soup` instance.
    :param element: The element, e.g. "img", to search within.
    :param attribute: The attribute whose value we're querying, e.g. "src".
    :return: A list of each matching value.
    """
    attributes = [elem.get(attribute) for elem in soup.find_all(element)]
    # Handle the case where an element doesn't have the given attribute.
    attributes = [a for a in attributes if a is not None]
    return attributes


def make_absolute(links, base_url):
    """
    Given a list of links (absolute OR relative), and a base URL, return a
    list of absolute URLs.

    :param links: A list of links, likely parsed from an HTML document.
    :param base_url: The base URL the links were found at.
    :return: A list of absolute URLS.
    """

    def is_absolute(url):
        """
        Given a link, determine whether it's an absolute URL or not.

        :param url: The link whose absoluteness should be tested.
        :return boolean: True if the link is absolute, False otherwise.
        """
        return url.startswith("http://") or url.startswith("https://")

    def absolutify(relative_link, base_link):
        """
        Given a relative link and a base URL, join the two to create an
        absolute link.

        :param relative_link: The link, typically to a static asset.
        :param base_link: The base URL this link is used with.
        :return: An absolute URL to the static asset, usable anywhere.
        """
        return urllib.parse.urljoin(base_link, relative_link)

    absolute_links = []

    for link in links:
        if not is_absolute(link):
            link = absolutify(link, base_url)
        absolute_links.append(link)

    return absolute_links


def parse_data(raw_data, url):
    """
    Given some raw data (assumed to be HTML as readable by BeautifulSoup),
    extract the links to other pages as well as links to static assets.

    :param raw_data: Some HTML data to parse.
    :param url: The URL of the page we're parsing.
    :return ParsedData: A namedtuple of the links, images and scripts found.
    """

    # Make a `soup` to pull data out from.
    soup = BeautifulSoup(raw_data, "html.parser")

    # Retrieve all links and static assets from the page.
    links = find_attributes(soup, element="a", attribute="href")
    images = find_attributes(soup, element="img", attribute="src")
    scripts = find_attributes(soup, element="script", attribute="src")

    # Make sure all URLs found are absolute, for later use.
    links = make_absolute(links, url)
    images = make_absolute(images, url)
    scripts = make_absolute(scripts, url)

    # Wrap up our findings in a lightweight namedtuple.
    return ParsedData(links=links, scripts=scripts, images=images)
