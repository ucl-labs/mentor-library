# Fix Lazy-Loaded Website Content

Source: https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading

## Overview

Google Search Central's documentation addresses how lazy-loading - deferring non-critical content - can inadvertently hide material from search crawlers. The guide emphasizes that "if not implemented correctly, this technique can inadvertently hide content from Google."

## Key Implementation Methods

The documentation recommends three approaches:

1. **Browser built-in lazy-loading** for images and iframes
2. **IntersectionObserver API** with polyfill support
3. **JavaScript libraries** that load data when entering the viewport

Critically, these methods should not depend on user interactions like scrolling or clicking, since "Google Search does not interact with your page."

## Infinite Scroll Best Practices

For infinite scroll implementation, the guide recommends:

- Assigning "each chunk its own persistent, unique URL"
- Using absolute page numbers (e.g., `?page=12`) rather than relative parameters
- Linking sequentially between URLs for discoverability
- Updating displayed URLs via the History API when chunks load

## Testing Recommendations

Developers should use the URL Inspection Tool in Search Console to verify lazy-loaded content appears in rendered HTML, specifically checking that image or video `src` attributes display correctly in rendered elements.

The documentation emphasizes avoiding lazy-loading on immediately visible content to prevent user-facing performance degradation.
