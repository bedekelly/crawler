# Crawler

Crawler is a simple (but effective!) web crawler written in Python. It 
outputs a flat dictionary which shows each page crawled, along with the 
static assets (e.g. images) found and the links between pages.

Key features:

* Fast LRU Cache from Python's standard library
* Unit tests (more to come soon!)
* Outputs a flat Python dict — easily serializable to JSON
* Configurable maximum recursion depth
* Restricted to crawling same-domain pages.



A sample of the output format:

```json
{
  "https://website.tld": {
    "assets": {
      "images": ["https://website.tld/image.png"],
      "scripts": ["https://othersite.tld/script.js"]
    },
    "links": "https://website.tld/page.html"
  },
  
  "https://website.tld/page.html": {
    "assets": {
      "images": [],
      "scripts": ["https://website.tld/scripts/counter.js"]
    },
    "links": []
  }
}
```

Tests can be run in the root of this repository with 
`python -m unittest`.