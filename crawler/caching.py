"""
caching.py:
    Define a decorator `cache` to memoize the requests given to `get_raw_data`.

    In future, this should also handle memoizing the requests to `crawl`
    itself, although that's probably outside the scope of an MVP and would
    need some profiling to make sure it's the right thing to optimize.
"""

from functools import lru_cache

# Create a local cache for requests-get content.
cache = lru_cache(maxsize=256, typed=True)
