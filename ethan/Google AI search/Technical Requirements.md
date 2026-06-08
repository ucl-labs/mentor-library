# Google Search Technical Requirements

Source: https://developers.google.com/search/docs/essentials/technical

Achieving visibility in search results is free and requires meeting three minimum technical criteria:

1. **Googlebot access**: "Googlebot isn't blocked" from finding and accessing the page
2. **Functional page**: The page returns an "HTTP `200 (success)` status code"
3. **Indexable content**: The page contains text in supported file formats that complies with spam policies

Meeting these requirements makes a page *eligible* for indexing, though indexing is not guaranteed.

## Key Requirements Explained

**Accessibility**: Pages must be publicly accessible without login requirements. Google indexes only content that Googlebot can crawl, respecting mechanisms like robots.txt and noindex directives.

**HTTP Status**: Only pages returning success codes are indexed; error pages are excluded. The URL Inspection tool in Search Console can verify status codes.

**Content Quality**: Content must be in supported file types and comply with Google's spam policies to be considered indexable.

## Verification Tools

Google recommends using:
- Page Indexing report
- Crawl Stats report
- URL Inspection tool

These resources help identify why pages may not appear in search results.
