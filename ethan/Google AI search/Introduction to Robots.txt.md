# Introduction to robots.txt

Source: https://developers.google.com/search/docs/crawling-indexing/robots/intro

A robots.txt file is a text file that tells search engine crawlers which URLs on a website they can access. It is "used mainly to avoid overloading your site with requests" but is "not a mechanism for keeping a web page out of Google."

## Primary Uses

The file serves different purposes depending on file type:

**For web pages (HTML, PDF, etc.):** Manages crawler traffic to prevent server overload or avoid crawling unimportant pages. However, Google warns: "Don't use a robots.txt file as a means to hide your web pages from Google Search results."

**For media files:** Can prevent images, videos, and audio from appearing in Google Search results while managing crawl traffic.

**For resource files:** Can block unimportant image, script, or style files if pages function adequately without them.

## Key Limitations

- Not all search engines respect robots.txt rules; compliance depends on crawler behavior
- Different crawlers may interpret syntax differently
- A disallowed URL can still appear in search results if linked from other websites
- To truly prevent indexing, use alternatives like password protection or the `noindex` meta tag

## Alternative Methods for Content Protection

- Password-protecting files on your server
- Using the `noindex` meta tag or response header
- Removing pages entirely

If a page is blocked via robots.txt, search results may display the URL without a description, and embedded media files will be excluded from crawling.
