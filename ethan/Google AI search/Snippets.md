# Control your snippets in search results

Source: https://developers.google.com/search/docs/appearance/snippet

A snippet represents the description or summary displayed in Google Search results. Google automatically generates snippets primarily from page content, though it may use meta description elements when they better represent the page.

## How snippets are created

Snippets are automatically generated from page content to emphasize and preview the most relevant portions for a user's specific search query. Different searches may produce different snippets for the same page. While Google primarily uses on-page content, it sometimes relies on meta description HTML elements if they provide a more accurate description.

## Preventing or adjusting snippet length

Control snippet display through HTML meta tags:
- Use `nosnippet` to prevent snippets entirely
- Use `max-snippet:[number]` to specify maximum length
- Use `data-nosnippet` attribute to exclude specific page sections

## Best practices for meta descriptions

### Create unique descriptions for each page

Identical descriptions across multiple pages reduce effectiveness. Prioritize creating descriptions for critical URLs like homepages and popular pages.

### Include relevant content information

Meta descriptions can incorporate structured information beyond sentences. News articles might include "author, date of publication, or byline information." Product pages can feature key details like price, age, or manufacturer.

### Generate descriptions programmatically

For database-driven sites, programmatic generation is appropriate and encouraged. Descriptions should remain human-readable and diverse, using page-specific data rather than long keyword strings.

### Use quality descriptions

High-quality descriptions improve search traffic quality and quantity.

**Poor:** "Sewing supplies, yarn, colored pencils, sewing machines, threads, bobbins, needles"

**Better:** "Get everything you need to sew your next garment. Open Monday-Friday 8-5pm, located in the Fashion District."

## Best practices for "Read more" deep links

Deep links within snippets guide users to specific page sections. To increase their likelihood:
- Ensure content is immediately visible, not hidden behind expandable sections
- Avoid JavaScript controlling scroll position on page load
- Preserve hash fragments in History API or location.hash modifications
