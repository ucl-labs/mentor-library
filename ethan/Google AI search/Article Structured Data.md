# Article Schema Markup Documentation

Source: https://developers.google.com/search/docs/appearance/structured-data/article

Adding `Article` structured data to news, blog, and sports article pages helps Google better understand content and display improved title text, images, and date information in search results across Google Search, Google News, and Google Assistant.

## Key Structured Data Types

Supports three schema.org types:
- `Article`
- `NewsArticle`
- `BlogPosting`

## Recommended Properties

- `headline`: "The title of the article" (keep concise as lengthy titles may truncate)
- `image`: Multiple high-resolution images with 16x9, 4x3, and 1x1 aspect ratios recommended
- `datePublished`: "The date and time the article was first published, in ISO 8601 format"
- `dateModified`: Publication modification date in ISO 8601 format
- `author`: Person or Organization with name and URL properties

## Implementation Steps

1. Add applicable properties (no required fields exist)
2. Follow all guidelines before deployment
3. Test with Google's Rich Results Test tool
4. Use the URL Inspection tool to verify Google accessibility
5. Submit sitemaps for ongoing updates

## Author Markup Best Practices

- Include all credited authors separately in individual `author` fields
- Use `Person` type for individuals and `Organization` for entities
- Include author URLs or `sameAs` properties for disambiguation
- Reserve `author.name` for names only - use separate properties for job titles, honorifics, or publisher information
