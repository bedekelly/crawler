"""
__init__.py:
    This file's main use is to make the `crawler` directory a Python package.
    But it also defines the namespace of that package, so we'll use it to
    bring in the useful `crawl` name.

    By doing this, `from crawler import crawl` is a reality -- as opposed to
    the much clunkier `from crawler.crawler import crawl`.
"""

from .crawler import crawl
