# Redirects and Google Search

Source: https://developers.google.com/search/docs/crawling-indexing/301-redirects

Redirecting URLs directs visitors and search engines from an existing URL to a different one. This practice proves useful when moving sites to new domains, consolidating multiple URLs for the same content, merging websites, or removing pages while preserving user experience.

## Redirect Types

**Permanent redirects** signal that the redirect target should become the canonical page in search results. Use these when confident the redirect won't be reversed.

**Temporary redirects** don't signal canonicalization to Google. The source page may remain in search results. Use these for brief redirects, such as during temporary service unavailability.

## Recommended Methods (by reliability)

### Server-Side Redirects

These are most reliable for Google to interpret correctly. Implement using HTTP status codes:

- **HTTP 301 (Moved Permanently)** - permanent
- **HTTP 308 (Moved Permanently)** - permanent
- **HTTP 302 (Found)** - temporary
- **HTTP 303 (See Other)** - temporary
- **HTTP 307 (Temporary Redirect)** - temporary

**PHP example for permanent redirect:**
```php
header('HTTP/1.1 301 Moved Permanently');
header('Location: https://www.example.com/newurl');
exit();
```

Web servers like Apache and NGINX support configuration-based redirects through `.htaccess` files and rewrite rules.

### Meta Refresh Redirects

If server-side redirects aren't available, `meta refresh` provides an alternative:

- **Instant redirects** (0 seconds) - treated as permanent
- **Delayed redirects** (>0 seconds) - treated as temporary

```html
<meta http-equiv="refresh" content="0; url=https://example.com/newlocation">
```

### JavaScript Redirects

Only use as a last resort, since rendering may fail:

```javascript
window.location.href = "https://www.example.com/newlocation";
```

## Alternate URLs

When redirecting, both source and target URLs remain tracked by Google. One becomes canonical while the other becomes an alternate name - potentially appearing in results when users' queries suggest they'd trust the older URL more.
