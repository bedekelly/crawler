"""
utilities.py:
    The ubiquitous "utilities.py" -- also known as "utils.py" -- the last
    resort of the programmer who can't decide where to put a helper function.
"""


def add_to_sitemap(sitemap, url, data):
    """
    Given a wrapped-up set of parsed data from a webpage, add it all to a
    given sitemap. The sitemap is a flat document which contains information
    about every URL we've visited, so there's no complex recursive logic here.

    Note that this mutates `sitemap` in-place, and so doesn't return anything.

    :param sitemap: The sitemap to add our data to.
    :param url: The URL we've just crawled.
    :param data: The data we've found from the given URL.
    """

    sitemap[url] = {
        "links": data.links,
        "assets": {
            "images": data.images,
            "scripts": data.scripts
        }
    }
