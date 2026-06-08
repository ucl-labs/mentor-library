# Mobile Site and Mobile-First Indexing Best Practices

Source: https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing

Google indexes and ranks websites using the mobile version of content, a practice called "mobile-first indexing." While having a mobile version isn't required for inclusion in search results, it's strongly recommended to follow best practices.

## Create a Mobile-Friendly Site

Three configuration options exist:

**Responsive Design** (Google's recommendation): Serves identical HTML on the same URL across all devices but adjusts display based on screen size. This is the easiest pattern to implement and maintain.

**Dynamic Serving**: Uses the same URL but serves different HTML versions based on user-agent detection and the `Vary: user-agent` HTTP header.

**Separate URLs**: Different URLs serve different HTML versions for each device type, also relying on user-agent and Vary headers.

## Ensure Google Can Access and Render Content

- Apply identical robots meta tags to both mobile and desktop versions
- Avoid lazy-loading primary content that requires user interaction
- Don't block resources with robots.txt disallow rules if you want Google to crawl them

## Maintain Content Parity Between Desktop and Mobile

Equivalent content across both versions allows ranking for identical keywords. Preserve primary content through design adjustments like accordions or tabs rather than removing it. Use consistent, clear headings on both versions.

## Structured Data Requirements

Ensure matching structured data across versions. Prioritize `Breadcrumb`, `Product`, and `VideoObject` markup. Update URLs in structured data to match mobile URLs.

## Metadata Consistency

Title elements and meta descriptions should be equivalent across both versions of your site.

## Advertisement and Visual Content Standards

Follow the "Better Ads Standard" when displaying mobile ads. High-quality images should use supported formats. Maintain identical alt text across versions. Videos should use supported formats and tags like `<video>`, `<embed>`, or `<object>`.

## Separate URL-Specific Practices

For m-dot configurations:
- Match error page status across versions
- Avoid URL fragments (content after `#`)
- Ensure desktop pages with distinct content have mobile equivalents
- Verify both versions in Search Console
- Link mobile hreflang tags to mobile URLs and desktop tags to desktop URLs
- Ensure sufficient server capacity for increased crawl rates
- Apply consistent robots.txt rules across versions
- Use proper `rel=canonical` (pointing to desktop) and `rel=alternate` tags

## Common Troubleshooting Issues

**Missing Elements**: Verify structured data, images, titles, and meta descriptions exist on both versions.

**Indexing Blocks**: Remove `noindex` tags, ensure robots.txt doesn't block important resources.

**Content Quality**: Follow Better Ads Standards, maintain equivalent primary content.

**Technical Issues**: Ensure proper video formatting and placement, avoid lazy-loading primary content.
