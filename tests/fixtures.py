EXPECTED_CRAWL_RESULTS = {
    "https://basic-website.com": {
        "https://basic-website.com": {
            "links": [],
            "assets": {
                "images": [],
                "scripts": []
            }
        }
    },

    "https://single-image.com": {
        "https://single-image.com": {
            "links": [],
            "assets": {
                "images": ["https://single-image.com/image.png"],
                "scripts": []
            }
        }
    },

    "https://multiple-scripts.com": {
        "https://multiple-scripts.com": {
            "links": [],
            "assets": {
                "images": [],
                "scripts": [
                    "https://other-site.com/scriptA.js",
                    "https://multiple-scripts.com/scriptB.js"
                ]
            }
        }
    },

    "ConnectionError": lambda url: {
        "{}".format(url): {
                "error": "Couldn't connect to URL: \"{}\"".format(url)
            }
    },

    "https://has-bad-url.com": {
        "https://has-bad-url.com": {
            "links": ["https://bad-domain.has-bad-url.com"],
            "assets": {
                "images": [],
                "scripts": []
            }
        },
        "https://bad-domain.has-bad-url.com": {
            "error": ("Couldn't connect to URL: "
                      "\"https://bad-domain.has-bad-url.com\"")
        }
    }
}

MOCK_GET_DATA = {
    # This basic website doesn't rely on any external sources.
    "https://basic-website.com": """
        <html>
            <head>
                <title>This is a title></title>
            </head>
            <body>
                <h1>Hello, world!</h1>
                <p>This is a paragraph of text.</p>
            </body>
        </html>
    """,

    # This website just contains a single image.
    "https://single-image.com": """
        <html><img src="image.png"></img></html>
    """,

    # This website contains multiple scripts. One doesn't have an `src`.
    "https://multiple-scripts.com": """
        <html>
            <head>
                <script src="https://other-site.com/scriptA.js"></script>
            </head>

            <body>
                <script src="scriptB.js"></script>
            </body>

            <script>alert("hello, world!")</script>
        </html>
    """,

    # This website contains an external site link.
    "https://contains-external-site-link.com": """
        <html>
            <a href="https://external-site.com"></a>
        </html>
    """,

    # This website contains a bad URL on the same domain.
    "https://has-bad-url.com": """
        <html>
            <body>
                <a href="https://bad-domain.has-bad-url.com">Click me!</a>
            </body>
        </html>
    """
}
