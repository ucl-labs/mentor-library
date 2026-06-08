# Manage Your Sitemaps With Sitemap Index Files

Source: https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps

When a sitemap exceeds size limits, you need to split it into multiple sitemaps and use a sitemap index file to submit them all at once to Google.

## Sitemap Index Best Practices

The XML format follows the Sitemap Protocol specification. Key requirements include:

- Referenced sitemaps must be hosted on the same site as the index file (unless cross-site submission is configured)
- Sitemaps must be in the same directory as the index file or deeper in the hierarchy
- You can submit up to 500 sitemap index files per site in Search Console

## Required Tags

The sitemap index requires:
- `sitemapindex` (root element)
- `sitemap` (parent tag for each sitemap entry)
- `loc` (the sitemap URL; up to 50,000 allowed per index)

## Optional Tags

The `lastmod` tag identifies when a sitemap was last modified, using W3C Datetime format.
