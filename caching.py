from functools import lru_cache

# Create a local cache for requests-get content.
cache = lru_cache(maxsize=256, typed=True)
