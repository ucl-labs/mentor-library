# Understand JavaScript SEO Basics

Source: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics

This documentation explains how Google processes JavaScript-powered websites and provides best practices for optimization.

## How Google Processes JavaScript

Google handles JavaScript through three main phases:

1. **Crawling** - Googlebot fetches URLs and checks robots.txt permissions
2. **Rendering** - A headless Chromium browser executes JavaScript on queued pages
3. **Indexing** - Google indexes the rendered HTML content

"All pages with a `200` HTTP status code are sent to the rendering queue, no matter whether JavaScript is present" - this ensures JavaScript content gets processed.

## Key Recommendations

**Unique Titles and Meta Descriptions**
Use JavaScript to set or modify `<title>` elements and meta descriptions to help users identify relevant results.

**Canonical URLs**
"The best way to set the canonical URL is to use HTML, but if you have to use JavaScript, make sure that you always set the canonical URL to the same value as the original HTML."

**HTTP Status Codes**
Use meaningful status codes (404 for not found, 401 for login-required pages) to communicate page status to Googlebot. For single-page apps, avoid soft 404 errors by either redirecting to a server-side 404 page or adding a `noindex` meta tag via JavaScript.

**History API Over Fragments**
Use the History API for client-side routing instead of URL fragments, allowing Googlebot to discover and parse links correctly.

**Structured Data**
"You can use JavaScript to generate the required JSON-LD and inject it into the page" while testing implementation thoroughly.

**Web Components**
Google supports web components and flattens shadow DOM content during rendering, making content visible in rendered HTML indexable.

**Lazy-Loading**
Follow guidelines for search-friendly lazy-loading implementation for images.

**Caching Strategy**
Use content fingerprinting in filenames to avoid outdated cached resources.
