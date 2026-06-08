# How to Move a Site

Source: https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes

This guide outlines the process for changing existing page URLs while minimizing negative impact on search results. Covers scenarios including HTTP to HTTPS migrations, domain changes, and URL path modifications.

## Key Steps

1. **Understand best practices** for site moves and their effects
2. **Prepare the new site** thoroughly with proper testing
3. **Create URL mappings** from old to new formats
4. **Configure server redirects** from old to new URLs
5. **Monitor traffic** on both old and new sites

## General Best Practices

- **Segment large moves**: For substantial sites, consider moving sections sequentially rather than all at once to test effects
- **Change one element at a time**: Avoid simultaneous modifications like domain changes, CMS updates, and layout redesigns
- **Time strategically**: Schedule moves during low-traffic periods when possible
- **Accept temporary fluctuations**: Rankings typically stabilize after several weeks as Google recrawls and reindexes
- **Preserve link credit**: Permanent redirects maintain PageRank
- **Use Search Console**: Monitor progress through Google's verification and reporting tools

## Technical Requirements

**Redirect strategy**: Use server-side permanent redirects (301/308 status codes) rather than client-side alternatives. Avoid redirect chains exceeding 5 hops, ideally keeping them under 3.

**Timeline expectations**: Medium-sized sites typically require several weeks for indexing migration; larger sites take longer.

**Keep redirects active**: Maintain redirects for at least one year to allow Google to transfer all ranking signals to new URLs.

## Common Mistakes to Avoid

- Failing to remove `noindex` tags or robots.txt blocks meant only for development
- Incorrect redirect destinations pointing to non-existent pages
- Insufficient server capacity during increased crawling
- Outdated sitemaps with old URLs
