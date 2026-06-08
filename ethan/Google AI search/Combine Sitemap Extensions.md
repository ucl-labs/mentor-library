# How to Combine Sitemap Extensions

Source: https://developers.google.com/search/docs/crawling-indexing/sitemaps/combine-sitemap-extensions

## Overview

The documentation explains how to use multiple sitemap extensions together on a single website. When pages contain different content types - like news articles with embedded videos and images, or localized content - you can combine extensions to provide comprehensive metadata to Google.

## Namespaces

To use sitemap extensions, declare their namespaces in the `urlset` tag using `xmlns` attributes. Supported extensions and their namespaces include:

| Extension | Namespace |
|-----------|-----------|
| Image | `http://www.google.com/schemas/sitemap-image/1.1` |
| News | `http://www.google.com/schemas/sitemap-news/0.9` |
| Video | `http://www.google.com/schemas/sitemap-video/1.1` |
| XHTML (hreflang) | `http://www.w3.org/1999/xhtml` |

### Declaring Multiple Namespaces

Add namespace references to your sitemap's opening tag. The documentation provides this example structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
   xmlns:news="http://www.google.com/schemas/sitemap-news/0.9"
   xmlns:video="http://www.google.com/schemas/sitemap-video/1.1"
   xmlns:xhtml="http://www.w3.org/1999/xhtml">
```

## Implementation Strategy

After declaring namespaces, add extension tags sequentially within each `<url>` tag, following individual extension documentation. The ordering of extensions is irrelevant after the location tag. However, combining extensions significantly increases file size, so monitor sitemap limits.

## Troubleshooting

For investigation assistance, use Google Search Console's sitemap troubleshooting resources.
