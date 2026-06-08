# Get Started with Signed Exchanges on Google Search

Source: https://developers.google.com/search/docs/appearance/signed-exchange

## Overview

Signed exchanges (SXG) represent a privacy-preserving prefetching technology that allows Google Search to load resources before users click results. As the documentation explains, "this means that both AMP and non-AMP results shown on Google Search may prefetch a few key resources (such as HTML, JavaScript, CSS, images, or fonts) in a privacy-preserving manner."

The primary benefit involves improved page performance metrics. When visitors ultimately access the content, rendering begins faster since critical assets are already cached, potentially lowering Largest Contentful Paint scores and enhancing overall page experience.

## Implementation Steps

The guide directs developers to follow web.dev's comprehensive implementation guide first. For AMP-specific pages, amp.dev provides dedicated documentation. After setup, developers should reference Chrome's optimization guide for Largest Contentful Paint improvements.

### Key Requirements for Google Search

Several technical considerations apply specifically to Google's systems:

**Cache and Expiration Management**: Google maintains an SXG cache for content prefetching. The documentation specifies that "the expiration date is less than both of these dates: The cache expiration determined by your HTTP headers" and either 1 day ahead (for JavaScript-containing pages) or 7 days ahead.

**Cross-Device Compatibility**: Developers should implement responsive design patterns or serve device-specific URLs separately. The guide recommends moving personalized elements like shopping carts into lazy-loaded sections outside the SXG wrapper, or applying the `Vary: Cookie` header.

## Monitoring and Troubleshooting

Several debugging tools exist for validation. The SXG Validator Chrome extension helps verify cache compatibility. Alternatively, developers can query the Google SXG cache directly using a specific subdomain transformation algorithm.

If Googlebot encounters parsing issues, it automatically attempts retrieval without the `application/signed-exchange;v=b3` Accept header to fetch HTML variants instead.

## Community and Updates

Staying current requires subscribing to the webpackaging-announce mailing list for announcements regarding cache capability changes and Web Packager tool updates.
