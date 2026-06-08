# Troubleshoot Google Search Crawling Errors

Source: https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors

## Overview

This Google Search Central guide outlines five key steps for resolving crawling issues:

1. Identify Googlebot availability problems
2. Find uncrawled pages that should be indexed
3. Ensure timely updates to existing content
4. Enhance crawl efficiency
5. Address overcrawling situations

## Key Diagnostic Areas

### Availability Issues

Google provides the **Crawl Stats report** to monitor when availability errors occur. The **URL Inspection Tool** can reveal "Hostload exceeded" warnings indicating capacity constraints. Solutions include:

- Blocking non-critical pages from crawling
- Improving page load speeds
- Increasing server capacity if Google consistently hits serving limits

### Missing Content

When pages aren't being crawled despite being published:

- Update sitemaps with new URLs
- Review robots.txt for accidental blocking
- Assess crawl budget allocation
- Verify adequate server capacity

### Update Frequency

The documentation states that "for most sites, this is three days or more" for indexing new or updated content. To improve discovery:

- Use news sitemaps for time-sensitive content
- Include `<lastmod>` tags in sitemaps
- Provide crawlable `<a>` links
- Ensure mobile versions have equivalent navigation

## Crawl Efficiency Optimization

### Page Speed

Faster response times enable more crawling. Best practices include:

- Blocking large non-critical resources via robots.txt
- Minimizing redirect chains
- Optimizing embedded resource loading

### HTTP Status Codes

Google supports conditional request headers like `If-Modified-Since`. Servers can return `304 (Not Modified)` responses to save resources when content hasn't changed.

## Soft 404 Errors

These occur when pages display error messages but return `200 (success)` codes. Solutions depend on the scenario:

- **Page removed**: Return `404` or `410` status codes
- **Content relocated**: Use `301` permanent redirects
- **Content exists**: Use URL Inspection Tool to diagnose resource loading issues

## Overcrawling Emergencies

Temporary measures include:

- Returning `503` or `429` status codes to slow requests
- Discontinuing these codes after 2 days to prevent index removal
- For AdsBot issues, review Dynamic Search Ad targets or increase capacity
