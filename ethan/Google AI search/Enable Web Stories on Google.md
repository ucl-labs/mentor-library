# Enable Web Stories on Google

Source: https://developers.google.com/search/docs/appearance/enable-web-stories

Web Stories are a dynamic visual format combining "video, audio, images, animation and text" that users can explore at their own pace.

## Feature Availability

Web Stories can appear as single results on Google Search across all regions and languages. In the Discover feed, they appear as tappable cards, with highest visibility in the United States, India, and Brazil.

## Five-Step Process

1. **Create the Web Story** - Use story editor tools (no coding required) or build with AMP if you have engineering resources
2. **Validate AMP compliance** - Ensure adherence to AMP specifications using the Web Stories Google Test Tool, URL Inspection Tool, or AMP Linter
3. **Verify metadata** - Supply required fields: `publisher-logo-src`, `poster-portrait-src`, `title`, and `publisher`
4. **Check indexing status** - Use the URL Inspection Tool or Page Indexing report to confirm Google has indexed your story
5. **Follow content policies** - Adhere to Web Story Content Policies

## Indexing Requirements

- Link to Web Stories from your site or include URLs in your sitemap
- Ensure each story has a self-referential `link rel="canonical"` tag
- For multilingual versions, use hreflang tags to indicate localized versions
- Verify Web Story URLs aren't blocked via robots.txt or noindex tags
