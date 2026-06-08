# Influencing Your Title Links in Search Results

Source: https://developers.google.com/search/docs/appearance/title-link

A **title link** is the clickable headline of a search result on Google Search and other Google properties. Google automatically determines title links from various sources, but you can influence them by following best practices.

## Best Practices for Influencing Title Links

**Every page needs a title:** Ensure each page includes a `<title>` element with descriptive, concise text. Avoid vague terms like "Home" or excessively long titles.

**Write clear, descriptive titles:** Avoid keyword stuffing or repeating phrases unnecessarily.

**Prevent boilerplate text:** Each page should have distinct title text. Avoid repetitive branding across all pages; consider placing your site name at the beginning or end, separated by punctuation.

**Make main titles stand out:** Ensure your primary title is visually distinctive and prominent - use larger fonts or place it in the first `<h1>` element.

**Match language and script:** Title text should match your page's primary language and writing system.

**Avoid flight pricing in titles:** Google typically omits flight prices from title links since pricing changes rapidly.

## How Google Creates Title Links

Google uses multiple sources to generate title links automatically:
- Content in `<title>` elements
- Main visual page titles
- Heading elements (`<h1>`, etc.)
- `og:title` meta tags
- Styled text and prominent content
- Anchor text and links pointing to the page
- `WebSite` structured data

Google may take several days to weeks to reflect changes after recrawling pages.

## Common Issues Google Addresses

**Half-empty titles:** Missing content like "|Site Name" alone - Google supplements with header text.

**Obsolete titles:** Year-old dates in titles when page content shows current information - Google uses visible dates instead.

**Inaccurate titles:** Titles not reflecting actual page content - Google may modify them for accuracy.

**Unclear main titles:** Multiple headings with equal prominence - Google may use the first heading as the title link.

**Language mismatches:** Titles in different languages than primary content - Google may select text in the correct language.

**Site name duplication:** Google may omit redundant site names already displayed elsewhere in results.
