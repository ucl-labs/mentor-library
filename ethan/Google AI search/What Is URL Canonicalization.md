# What is URL Canonicalization

Source: https://developers.google.com/search/docs/crawling-indexing/canonicalization

Canonicalization involves selecting a representative "canonical" URL from duplicate content. Google's indexing process identifies the most useful version from multiple similar pages and marks it as canonical, typically showing only that version in search results.

## Common Reasons for Duplicate Content

Sites may have duplicates due to:
- Regional variants (different URLs for USA vs. UK content)
- Device variants (mobile and desktop versions)
- Protocol variants (HTTP and HTTPS versions)
- Site functions (sorting/filtering results)
- Accidental variants (demo versions left accessible)

## How Google Selects Canonical URLs

Google determines the primary content of each page during indexing. When multiple pages appear similar, it selects the most "complete and useful for search users" based on collected signals, marking it as canonical. The canonical page receives more frequent crawling while duplicates are crawled less often.

## Factors Influencing Canonicalization

- Protocol (HTTP vs. HTTPS)
- Redirects
- Sitemap presence
- `rel="canonical"` link annotations

Note: indicating preference is "a hint, not a rule" - Google may choose differently.

## Language Considerations

Pages in different languages are only considered duplicates if the primary content language is identical (translations of headers/footers only, with unchanged body text, qualify as duplicates).

## Search Results Behavior

Google typically displays the canonical page in results, though exceptions exist. For instance, mobile users may see the mobile page even if desktop is canonical.
