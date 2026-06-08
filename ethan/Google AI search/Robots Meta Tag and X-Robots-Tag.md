# Robots Meta Tag, Data-nosnippet, and X-Robots-Tag Specifications

Source: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag

This documentation explains how to use meta tags and HTTP headers to control indexing and serving of web content in search results.

## Key Control Methods

**Robots Meta Tag**: Place in the HTML `<head>` section to specify page-level indexing rules. Supports user agent tokens like `googlebot` and `googlebot-news`.

**X-Robots-Tag HTTP Header**: An alternative for non-HTML resources (PDFs, images, videos) or sitewide rules via server configuration.

**Data-nosnippet Attribute**: Applied to `span`, `div`, or `section` elements to exclude specific text portions from search snippets.

## Valid Rules

- `noindex`: Prevents page from appearing in search results
- `nofollow`: Prevents following links on the page
- `nosnippet`: Blocks text snippets and video previews
- `max-snippet:[number]`: Limits snippet length to specified characters
- `max-image-preview:[setting]`: Controls image preview sizes (none, standard, large)
- `max-video-preview:[number]`: Limits video preview duration in seconds
- `notranslate`: Prevents search result translation
- `noimageindex`: Blocks image indexing on the page
- `unavailable_after:[date]`: Removes page from results after specified date

## Important Limitation

Crawlers must have access to a page to read these directives. If a page is blocked in robots.txt, any meta tags or headers won't be discovered or applied.
