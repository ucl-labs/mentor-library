# Remove Images Hosted on Your Site from Search Results

Source: https://developers.google.com/search/docs/crawling-indexing/prevent-images-on-your-page

## Overview

This Google Search Central documentation explains how to remove images from your site that appear in Google's search results.

## Emergency Image Removal

For quick removal, Google offers the **Removals tool** to rapidly delete images from search results. However, this is temporary - "unless you also remove the images from your site or otherwise block the images" the content may reappear once the request expires.

## Non-Emergency Removal Methods

Two permanent approaches exist:

### 1. robots.txt Disallow Rules

Add a robots.txt file to your site's root with image-blocking rules. Example:

```
User-agent: Googlebot-Image
Disallow: /images/dogs.jpg
```

**Key features:**
- Supports wildcard characters (*) for pattern matching
- Takes longer than the Removals tool but offers more control
- Applies to all search engines, not just Google
- Use `Googlebot-Image` to exclude from Google Images only, or `Googlebot` to exclude from all Google searches

### 2. noindex X-Robots-Tag HTTP Header

Add `noindex` directives to HTTP response headers for specific images. This method requires allowing crawling so Googlebot can read the headers.

**Important note:** Using `noimageindex` on a page prevents embedded images from indexing, but those images might still appear through other pages where they're embedded.

## When You Don't Own the Property

For images on sites you don't control, consult Google's help documentation on removing images from search results.
