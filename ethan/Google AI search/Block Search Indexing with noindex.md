# Block Search Indexing with noindex

Source: https://developers.google.com/search/docs/crawling-indexing/block-indexing

The `noindex` directive prevents search engines like Google from indexing specific pages. "When Googlebot crawls that page and extracts the tag or header, Google will drop that page entirely from Google Search results, regardless of whether other sites link to it."

## Critical Requirement

For `noindex` to work, the page must be accessible to crawlers and not blocked by robots.txt. "If the page is blocked by a robots.txt file or the crawler can't access the page, the crawler will never see the `noindex` rule, and the page can still appear in search results."

## Implementation Methods

### Meta Tag Approach

**All search engines:**
```
<meta name="robots" content="noindex">
```

**Google only:**
```
<meta name="googlebot" content="noindex">
```

### HTTP Response Header

For non-HTML resources (PDFs, videos, images):
```
X-Robots-Tag: noindex
```

## Combined Rules

The `noindex` directive can be paired with other indexing controls, such as combining it with `nofollow`.

## Troubleshooting

Pages may still appear in results if Google hasn't recrawled since adding the rule. Use the URL Inspection tool to request recrawling, or check the Page Indexing report to verify proper implementation.
