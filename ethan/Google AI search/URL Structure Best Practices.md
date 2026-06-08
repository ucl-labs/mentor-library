# URL Structure Best Practices for Google Search

Source: https://developers.google.com/search/docs/crawling-indexing/url-structure

Google Search requires crawlable URL structures meeting specific standards. URLs that don't comply may result in inefficient crawling, excessive bandwidth consumption, or incomplete indexing.

## Requirements for Crawlable URLs

### Follow IETF STD 66

Google supports URLs as defined by the standard, requiring that reserved characters be "percent encoded."

### Avoid URL Fragments for Content Changes

Google generally doesn't support fragments like `#/potatoes` for changing page content. Use the History API for JavaScript-based content changes instead.

### Use Standard URL Parameter Encoding

- **Correct:** `https://example.com/category?category=dresses&sort=low-to-high`
- **Incorrect:** `https://example.com/category?[category:dresses][sort:price]`

## Best Practices for Understandable URLs

- **Use Descriptive Words**: Prefer readable terms over ID numbers (`/wiki/Aviation` vs `/index.php?topic=42&area=3a5ebc944f41daa6f`)
- **Match Your Audience's Language**: Incorporate audience language in URLs
- **Separate Words with Hyphens**: Use hyphens (`-`) rather than underscores (`_`) to separate words
- **Minimize Parameters**: Remove unnecessary parameters that don't affect content
- **Remember Case Sensitivity**: URLs are case-sensitive; standardize case to prevent treating identical content as separate pages
- **Structure Multi-Regional Sites Logically**: Use country-specific domains or subdirectories for easier geotargeting

## Common URL Structure Problems

Issues that create excessive crawlable URLs include:

- **Additive filtering** (combining multiple filters creates exponential URL variations)
- **Irrelevant parameters** (referral IDs, session IDs, sorting preferences)
- **Calendar functions** (infinite forward/backward date generation)
- **Broken relative links** (creating bogus URL chains)

## Solutions

Use `robots.txt` files to block problematic URLs, particularly dynamic search results and infinite calendar pages. For faceted navigation, manage crawling appropriately to prevent indexing excessive variations.
