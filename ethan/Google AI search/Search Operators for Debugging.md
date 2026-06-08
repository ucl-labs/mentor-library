# Debugging with Google Search Operators

Source: https://developers.google.com/search/docs/monitor-debug/search-operators

## Overview

Google Search supports multiple operators useful for refining searches and debugging websites. The documentation notes that "the `site:` search operator may be useful to monitor comment spam on your website, and the image search `imagesize:` operator may be helpful to find images on your site that are small."

However, the page emphasizes an important limitation: "Because search operators are bound by indexing and retrieval limits, the URL Inspection tool in Search Console is more reliable for debugging purposes."

## Available Search Operators

### `filetype:`

Locates results in specific file types defined by HTTP content-type headers or extensions. Example: `filetype:rtf galway`

### `imagesize:`

Works exclusively on Google Images to find pages containing images with specific dimensions. Example: `imagesize:1200x800`

### `site:`

Retrieves results from particular domains, URLs, or URL prefixes. Example: `site:https://www.google.com/`

### `src:`

Functions only on Google Images to find pages referencing particular image URLs in the `src` attribute. Example: `src:https://www.example.com/images/peanut-butter.png`

## Key Takeaway

While search operators offer debugging utility, Google recommends using the URL Inspection tool within Search Console for more dependable site analysis, given the technical constraints affecting operator accuracy.
