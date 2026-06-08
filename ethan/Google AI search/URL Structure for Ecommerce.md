# Designing a URL structure for ecommerce websites

Source: https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites

## Why URL structure matters

Poor URL design creates three main problems:

**Content can be missed:** When Googlebot treats different URLs as duplicates, it may only crawl one version. For example, "/product/t-shirt#black" and "/product/t-shirt#white" appear identical to Google since fragment identifiers aren't used in indexing.

**Duplicate crawling:** When multiple URLs return the same content, Google wastes resources retrieving the page repeatedly.

**Infinite page scenarios:** URLs containing constantly-changing values (like timestamps) may appear as infinite unique pages to Google, delaying discovery of actual content.

## Good URL structure design best practices

### General URL recommendations

- Minimize alternative URLs returning identical content
- Standardize URL case if your server treats uppercase and lowercase identically
- Ensure paginated results have unique URLs
- Use descriptive words: prefer "/product/black-t-shirt-with-a-white-collar" over "/product/3243"

### URL query parameter recommendations

- Use "?key=value" format rather than "?value" for better clarity
- Avoid repeating parameters; use "?type=candy,sweet" instead of "?type=candy&type=sweet"
- Avoid session IDs, tracking codes, and time-based parameters in internal links

### Product variants

Structure variant URLs using either path segments ("/t-shirt/green") or query parameters ("/t-shirt?color=green"). When using optional parameters, designate the parameter-free version as the canonical URL to clarify variant relationships.

## Using URLs in your content

- Maintain consistent URLs across internal links, sitemaps, and canonical tags
- Include self-referencing canonical tags on all indexable pages
- Add canonical product URLs on all variant pages
- Use direct `<a href>` tags rather than JavaScript navigation
- Use meaningful anchor text describing linked content
- Apply `noindex` to empty categories or return 404 status codes
