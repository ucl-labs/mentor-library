# Add a Byline Date to Google Search Results

Source: https://developers.google.com/search/docs/appearance/publication-dates

A byline date represents Google's estimate of when a webpage was published or significantly updated. When Google can determine this date, it may display it in search results if deemed useful to users.

## How to Provide Date Information to Google

1. **Implement best practices** for influencing byline dates
2. **Add a visible date** prominently on the page with clear labeling such as:
   - "Posted Feb 4, 2019"
   - "Published February 4, 2019"
   - "Last updated: Feb 14, 2018"
   - "Updated Feb 14, 2019 8pm ET"

3. **Use structured data** by adding a `CreativeWork` subtype (such as `Article`, `BlogPosting`, or `VideoObject`) with `datePublished` and/or `dateModified` fields

## Best Practices for Byline Dates

- **Date is required; time is optional** - though timezone information enhances precision
- **Ensure consistency** between visible dates and structured data markup
- **Avoid future dates** or dates of events described on the page; use only publication/update dates
- **Minimize other dates** on the page to prevent confusion
- **Follow Google News guidelines** if targeting news search results

Google examines multiple factors rather than relying on single date indicators, as all sources can contain errors.
