# Create a News Sitemap

Source: https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap

News sitemaps allow news publishers to inform Google about articles and their metadata. Publishers can extend existing sitemaps with news-specific tags or create dedicated news sitemaps.

## News Sitemap Best Practices

- Update sitemaps with fresh articles as published rather than creating new sitemaps for each update
- Include only recent URLs for articles created within the last two days
- Remove URLs older than two days or strip their `<news:news>` metadata
- Understand that sitemaps may temporarily become empty without causing indexing issues
- Follow all general sitemap best practices

## Required News Sitemap Tags

News tags use the namespace: `http://www.google.com/schemas/sitemap-news/0.9`

Essential required tags:

- `<news:news>` - Parent tag for news-specific content; maximum 1,000 per sitemap
- `<news:publication>` - Parent for publication name and language
- `<news:name>` - Publication name exactly matching news.google.com appearance
- `<news:language>` - ISO 639 language code (with zh-cn/zh-tw exceptions for Chinese)
- `<news:publication_date>` - Original article publication date in W3C format
- `<news:title>` - Article headline without author, publication name, or date
