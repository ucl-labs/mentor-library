# Build and Submit a Sitemap

Source: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap

Google supports the sitemap formats defined by the sitemaps protocol, offering three main options: XML, RSS/Atom feeds, and text format.

## Sitemap Format Comparison

**XML Sitemaps** are "the most versatile of the sitemaps formats" and can supply information about images, video, and news content. They work well with most content management systems.

**RSS, mRSS, and Atom 1.0** feeds are "often the easiest to provide because CMSes automatically create them," though they're limited to video information beyond HTML content.

**Text Sitemaps** are "the simplest of sitemap formats" but can only list URLs to HTML and indexable pages.

## Key Best Practices

- All formats limit a single sitemap to 50MB (uncompressed) or 50,000 URLs
- Sitemaps must be UTF-8 encoded
- Use "fully-qualified, absolute URLs" rather than relative paths
- Google "ignores `<priority>` and `<changefreq>` values" in XML sitemaps
- Google uses `<lastmod>` only when "consistently and verifiably accurate"

## Submission Methods

Sites can submit sitemaps through:
- Google Search Console's Sitemaps report
- The Search Console API
- The robots.txt file using: `Sitemap: https://example.com/my_sitemap.xml`

Note: "Submitting a sitemap is merely a hint: it doesn't guarantee that Google will download the sitemap."
