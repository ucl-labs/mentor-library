# Image Sitemaps

Source: https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps

Image sitemaps serve as a mechanism for notifying Google about images on your website, particularly those that may not be discoverable through standard crawling methods (such as images loaded via JavaScript).

## Creating Image Sitemaps

You have two options: develop a dedicated image sitemap or incorporate image sitemap tags into your current sitemap. Google treats both approaches equivalently.

## Required Tags

Two essential elements are mandatory:

- **`<image:image>`**: Contains information about a single image; each URL element can have up to 1,000 image tags.
- **`<image:loc>`**: Specifies the image's URL. Images may be hosted on different domains, provided both domains are verified in Search Console and robots.txt permits crawling.

## Deprecated Elements

The following tags have been removed: "caption," "geo_location," "title," and "license."
