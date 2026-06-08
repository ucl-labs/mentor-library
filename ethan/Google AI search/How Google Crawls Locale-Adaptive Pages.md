# How Google Crawls Locale-Adaptive Pages

Source: https://developers.google.com/search/docs/specialty/international/locale-adaptive-pages

## Overview

Google's documentation explains that websites with locale-adaptive pages - those returning different content based on visitor location or language - may face crawling and indexing challenges. This occurs because "the default IP addresses of the Googlebot crawler appear to be based in the USA" and the crawler doesn't set `Accept-Language` headers by default.

## Key Recommendation

Google strongly advises: "We recommend using separate locale URL configurations and annotating them with `rel="alternate"` hreflang annotations."

## Geo-Distributed Crawling

The search engine now operates crawlers from multiple geographic regions beyond the United States. Website administrators should apply consistent access rules across all locales when implementing the robots exclusion protocol.

## Important Considerations

- Googlebot maintains identical user agent strings regardless of crawl origin
- Administrators can verify geo-distributed crawls through reverse DNS lookups
- Robots meta tags and robots.txt files must enforce identical rules across all locale versions

## Practical Guidance

If your site blocks USA-based users but permits Australian visitors, treat Googlebot accordingly - block it when appearing from the USA and allow access when appearing from other regions.
