# Using Search Console and Google Analytics Data for SEO

Source: https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console

Search Console reveals "how your website is performing in Google Search results," while Google Analytics shows "visitors' interactions with your website."

## Key Distinctions Between Tools

**Search Console** tracks pre-arrival metrics like impressions, clicks from search results, and search queries that bring users to your site.

**Google Analytics** measures post-arrival behavior including page visits, session duration, and user actions, plus traffic source attribution.

## Looker Studio Dashboard

Using a Looker Studio dashboard template to visualize both data sources simultaneously:
- Orange for Analytics data
- Blue for Search Console data
- Filters organic Google traffic specifically
- Controls for country, device, and date range selection

## Five Key Metrics

The recommended dashboard displays:
- Sessions
- Engagement rate
- Returning users
- Clicks
- Click-through rate (CTR)

## Data Discrepancies

Clicks and sessions won't match exactly due to different calculation methods. Common reasons include Analytics implementation gaps, timezone differences, attribution model variations, and bot traffic filtering differences.

## Additional Resources

- Connecting Search Console to Analytics
- WordPress Site Kit plugin
- BigQuery exports for detailed analysis
