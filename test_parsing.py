import unittest

from .parsing import on_same_domain


class TestParsing(unittest.TestCase):
    """
    Test the functionality contained within `parsing.py`.
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
