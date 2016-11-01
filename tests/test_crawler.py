"""
test_crawler:
    Test the functionality of the crawler itself. These tests
    tend to be fairly end-to-end, mocking out services like
    requests.get where necessary.
"""

import unittest
from unittest.mock import patch

from crawler import crawl

from .testing_tools import mock_requests_get
from .fixtures import EXPECTED_CRAWL_RESULTS


class TestCrawler(unittest.TestCase):

    @patch("requests.get", mock_requests_get)
    def test_basic_webpage(self):
        """
        Test that crawling a website with no links returns a correctly
        formatted, but empty, sitemap.
        """
        self.assertEqual(
            crawl("https://basic-website.com"),
            EXPECTED_CRAWL_RESULTS["https://basic-website.com"]
        )

    @patch("requests.get", mock_requests_get)
    def test_single_image(self):
        """
        Test that crawling a website with a single image returns a sitemap
        with a single image in the `assets` key.
        """
        self.assertEqual(
            crawl("https://single-image.com"),
            EXPECTED_CRAWL_RESULTS["https://single-image.com"]
        )

    @patch("requests.get", mock_requests_get)
    def test_multiple_scripts(self):
        """
        Test that crawling a website with multiple scripts returns a sitemap
        with each script in the `assets` key.
        """
        self.assertEqual(
            crawl("https://multiple-scripts.com"),
            EXPECTED_CRAWL_RESULTS["https://multiple-scripts.com"]
        )

    @patch("requests.get", mock_requests_get)
    def test_external_site(self):
        """
        Test that crawling a page with a link to an external site won't
        lead to following that external site.
        """
        result_sitemap = crawl("https://contains-external-site-link.com")
        self.assertNotIn("https://external-site.com", result_sitemap)

    def test_manual_invalid_url(self):
        """
        Check that when the user provides an invalid URL to the crawler,
        the crawler will raise an appropriate error.
        """

        bad_urls = [
            "http://", "https://", "google.com", "http://google"
        ]

        for bad_url in bad_urls:
            result = crawl(bad_url)
            self.assertEqual(
                result,
                EXPECTED_CRAWL_RESULTS["ConnectionError"](bad_url)
            )

    @patch("requests.get", mock_requests_get)
    def test_href_invalid_url(self):
        """
        Check that when a webpage contains an invalid URL, we add that URL
        to the sitemap with a clear error result.

        N.B. that to test this, we have to specify a bad URL on the same
        domain. If we specify a bad URL on a different domain, the crawler
        won't try to retrieve data from it *anyway*, because it's restricted
        to a single second-level domain.
        """
        self.maxDiff = None
        result = crawl("https://has-bad-url.com")
        self.assertEqual(
            result, EXPECTED_CRAWL_RESULTS["https://has-bad-url.com"]
        )
