# Understand How AMP Works in Search Results

Source: https://developers.google.com/search/docs/crawling-indexing/amp/about-amp

## Overview

Google Search indexes AMP pages to deliver fast, dependable web experiences. When AMP pages are available, they can appear in mobile search results as part of rich results and carousels. "While AMP itself isn't a ranking factor, speed is a ranking factor for Google Search."

Google applies the same ranking standards to all pages regardless of technology. AMP pages on mobile are served from the Google AMP Cache with optimizations like prerendering. Desktop AMP pages are treated as standard results.

## Initial Display in Search Results

AMP pages can appear as rich results similar to other web pages. Adding structured data helps Google understand your content better, though "Google doesn't guarantee that adding structured data will enable a rich result in Search results."

For duplicate content, place identical structured data on all versions, not just canonical pages. AMP pages can also appear as Web Stories.

## After Users Click AMP Content

AMP content displays in two ways:

1. **Google AMP Viewer** - Shows the publisher's domain at the top so users know the content source
2. **Signed Exchange** - Technology allowing browsers to treat documents as belonging to your origin

### Google AMP Viewer Details

This hybrid environment allows data collection in compatible browsers. Publisher data collection follows your privacy policy; Google's collection follows Google's privacy policy. Publishers control behaviors and vendor integrations, thus remain responsible for compliance obligations.

### Signed Exchange Details

Signed exchange enables first-party cookies for content customization and analytics. Your page appears under your URL instead of `google.com/amp`. Google prioritizes signed exchange over the Google AMP Viewer in supported browsers. Currently supported for rich and basic results, not carousels.
