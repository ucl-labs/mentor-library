# Fix Search-Related JavaScript Problems

Source: https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript

This guide helps developers identify and resolve JavaScript issues that may prevent pages or content from appearing in Google Search results.

## Testing and Diagnosis

Use the Rich Results Test or URL Inspection Tool to examine how Google crawls and renders URLs, including viewing loaded resources, console output, and rendered DOM.

## Critical Issues to Address

1. **Soft 404 errors**: Single-page applications should redirect to proper 404 status codes or add `noindex` meta tags for missing content rather than showing error pages with 200 status codes.

2. **User permissions**: "Features that require user permission don't make sense for Googlebot, or for all users."

3. **URL fragments**: The deprecated AJAX-crawling scheme means URL fragments shouldn't determine content loading; use the History API instead.

4. **Data persistence**: Web Rendering Service (WRS) clears Local Storage, Session Storage, and HTTP Cookies across page loads.

5. **Caching strategies**: Implement content fingerprinting (e.g., `main.2bb85551.js`) to avoid stale resource issues.

6. **Feature detection**: Provide fallbacks for APIs that Googlebot may not support, such as WebGL or WebSockets.

7. **Web components**: Ensure proper rendering using the `<slot>` mechanism for light DOM content.

8. **Paywall implementations**: Avoid JavaScript-only content hiding; confirm subscription status server-side before serving full content.

After making fixes, use the URL Inspection Tool and Rich Results Test to verify they have resolved indexing issues.
