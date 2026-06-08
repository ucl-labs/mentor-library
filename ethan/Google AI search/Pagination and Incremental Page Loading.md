# Pagination Best Practices for Google Search

Source: https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading

## Overview

Google's documentation addresses how website pagination, incremental loading, and infinite scroll patterns impact search visibility. The guide helps developers choose appropriate UX patterns while ensuring Google's crawler can discover all content.

## Key UX Patterns

Google describes three main approaches:

**Pagination**: Users navigate through numbered pages or "next/previous" links, viewing one page of results at a time.

**Load More**: A button extends the initial result set, keeping content on a single page.

**Infinite Scroll**: Content automatically loads as users reach the page bottom.

## Critical Implementation Guidelines

Google emphasizes several essential practices:

- **Sequential linking**: Use `<a href>` tags connecting pages in order, helping Googlebot discover subsequent pages
- **Unique URLs**: Assign distinct URLs to each page (e.g., `?page=n` parameters)
- **Canonical tags**: Apply individual canonical URLs per page rather than canonicalizing to the first page
- **Avoid fragments**: Don't use `#` identifiers for pagination since Google ignores them

## Content Discovery Challenges

The documentation notes: "Google's crawlers don't 'click' buttons and generally don't trigger JavaScript functions that require user actions to update the current page contents."

This distinction matters for JavaScript-based implementations. Google recommends using sitemaps or feeds like Google Merchant Center to ensure complete content discovery when JavaScript-heavy pagination is necessary.

## Additional Recommendations

- Use identical titles/descriptions across paginated sequences
- Block filter variations with `noindex` tags or robots.txt rules
- Consider performance hints like preload or prefetch directives
