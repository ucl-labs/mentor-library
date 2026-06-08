# How to Specify a Canonical URL with rel="canonical" and Other Methods

Source: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls

Google supports multiple methods for indicating canonical URLs to search engines, ranked by strength of signal:

1. **Redirects** - strongest signal for canonicalization
2. **rel="canonical" link annotations** - strong signal
3. **Sitemap inclusion** - weak signal

These methods can be combined for greater effectiveness.

## Why Specify a Canonical URL?

- Control which URL appears in search results
- Consolidate ranking signals across duplicate pages
- Simplify content metrics tracking
- Reduce unnecessary crawl budget expenditure on duplicates

## Best Practices

- Avoid using robots.txt for canonicalization
- Don't use URL removal tools for this purpose
- Don't specify conflicting canonical URLs across different methods
- Avoid canonical URL fragments
- Prefer rel="canonical" over noindex for same-site duplicates
- Use absolute URLs rather than relative paths
- Link internally to the canonical version
- Ensure canonical information is clear in HTML source code when using JavaScript

## Implementation Methods

### rel="canonical" Link Element

Add a `<link>` element in the HTML `<head>` section:

```html
<link rel="canonical" href="https://example.com/dresses/green-dresses" />
```

Use absolute URLs, not relative paths.

### rel="canonical" HTTP Header

For non-HTML files like PDFs, use an HTTP response header:

```
Link: <https://www.example.com/downloads/white-paper.pdf>; rel="canonical"
```

### Sitemap Method

List preferred canonical URLs in your sitemap. This is simpler for large sites but provides a weaker signal than explicit link annotations.

### Redirects

Use permanent redirects (HTTP 301/308) when deprecating duplicate pages. Server-side redirects work fastest.

## Additional Signals

**HTTPS Preference:** Google prefers HTTPS over HTTP as canonical, except when SSL certificates are invalid or HTTPS pages contain insecure dependencies.

**hreflang Clusters:** URLs appearing in reciprocal hreflang annotations are preferred as canonicals for localization purposes.

## Comparison Table

| Method | Pros | Cons |
|--------|------|------|
| rel="canonical" link | Maps unlimited duplicates | Complex maintenance on large sites |
| rel="canonical" HTTP header | Doesn't increase page size | Complex maintenance |
| Sitemap | Simple, scalable | Weaker signal than link annotations |
| Redirects | Clear preference signal | Only for deprecated pages |
