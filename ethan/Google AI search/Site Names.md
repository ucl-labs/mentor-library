# Provide a Site Name to Google Search

Source: https://developers.google.com/search/docs/appearance/site-names

When Google displays pages in search results, it shows the site name - distinct from individual page title links. The site name applies to the entire website rather than specific pages.

## Feature Availability

Site names display across all languages where Google Search operates, on both mobile and desktop devices. They work at domain and subdomain levels.

## How Google Creates Site Names

Google automates site name generation using content from a site's home page and web references. The primary method to indicate preference is adding `WebSite` structured data to your home page. Google also considers `og:site_name`, `<title>` tags, heading elements, and other home page text, though structured data takes priority.

## Guidelines for Choosing Site Names

- Select a unique, accurate name reflecting your site's identity while avoiding misleading descriptions
- Use concise, commonly recognized names (e.g., "Google" rather than "Google, Inc")
- Avoid generic names like location-based business descriptions
- Maintain consistency across your home page
- Provide alternative names for system consideration if your primary choice isn't available

## Technical Implementation

Add `WebSite` structured data to your home page's root URI (e.g., `https://example.com`), not subdirectories. Required properties:

- **name**: The website name
- **url**: The canonical home page URL

Optional: **alternateName** for acronyms or alternate versions.

## Troubleshooting

If your preferred name doesn't appear:
1. Verify structured data validity using schema validation tools
2. Confirm guidelines compliance
3. Check that other home page sources reference the same name
4. Ensure Googlebot can access your home page
5. Allow time for Google to recrawl and reprocess
6. Consider providing alternative names or domain names as fallback options
