# Subscription and Paywalled Content Markup

Source: https://developers.google.com/search/docs/appearance/structured-data/paywalled-content

Use schema.org JSON-LD structured data to mark paywalled content, helping Google distinguish it from cloaking practices that violate spam policies.

## Key Requirements

**Required Property:**
- `isAccessibleForFree`: Set to `false` to indicate paywalled sections

**Recommended Properties:**
- `hasPart.cssSelector`: References the CSS class marking paywalled content
- `hasPart.@type`: Should be set to `WebPageElement`
- `hasPart.isAccessibleForFree`: Set to `false` for paywalled sections

## Implementation Steps

1. Add class names to HTML elements containing paywalled content
2. Include `NewsArticle` or other `CreativeWork` structured data
3. Add `isAccessibleForFree: false` and `hasPart` properties with CSS selectors
4. Validate using Google's Rich Results Test

## Supported Content Types

Works with `CreativeWork` and specific subtypes including: Article, NewsArticle, Blog, Course, HowTo, Review, and WebPage.

## Important Guidelines

- Only `.class` selectors are permitted for `cssSelector`
- Don't nest content sections
- Ensure Googlebot can access paywalled content if indexing is desired
- Use `data-nosnippet` to exclude sections from snippets

## AMP Considerations

Publishers should use `amp-subscriptions` where appropriate and ensure consistent bot access policies between AMP and non-AMP versions.
