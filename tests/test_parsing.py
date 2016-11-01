"""
test_parsing.py:
    Test the functionality of the `parsing.py` module.
    These tests should be small and self-contained.
"""

import unittest

from crawler.parsing import on_same_domain


class TestParsing(unittest.TestCase):
    """
    Test functionality inside the parsing module.
    """

    def test_on_same_domain(self):
        """
        Test the functionality of the `on_same_domain` function. It should
        return True if the URLs given are on the same domain, or False if
        they aren't.
        """
        self.assertTrue(on_same_domain(
            "https://google.com/a/b",
            "http://sub-domain.google.com?time=0400"
        ))

    def test_not_on_same_domain(self):
        """
        Test the `on_same_domain` function returns false for two URLs
        which happen to be on different domains.
        """
        self.assertFalse(on_same_domain(
            "https://google.com",
            "https://google.goggle.com/google.com/google"
        ))
