# Temporarily Pause or Disable a Website

Source: https://developers.google.com/search/docs/crawling-indexing/pause-online-business

## Overview

This Google Search Central documentation page addresses how to safely pause an online business if unable to fulfill orders or manage inventory. The key principle is preserving search visibility during temporary closures.

## Recommended Approach: Limit Site Functionality

Google advises keeping your site online while restricting capabilities. Key recommendations include:

- **Disable checkout**: "Disabling the cart functionality is the simplest approach, and doesn't change anything for your site's visibility in Search."
- **Add notifications**: Display banners explaining status, delays, and delivery options using the `data-nosnippet` attribute to prevent snippet inclusion
- **Update structured data**: Modify Product, Event, or Local Business schema to reflect current availability and hours
- **Sync Merchant Center**: Ensure availability attributes match current inventory
- **Request recrawling**: Use Search Console to prompt re-indexing of updated pages

## Not Recommended: Full Site Disablement

Complete removal from search results carries significant consequences:

- Customers lose access to business information
- Knowledge Panels lose data (phone numbers, logos)
- Search Console verification fails
- Recovery timeline is uncertain and prolonged

If temporary disablement is necessary (maximum 1-2 days):
- Return a `503` HTTP status code with informational content
- Allow robots.txt crawling to continue
- Include retry-after headers and clear reopening dates
- Avoid `403`, `404`, `410` codes or `noindex` tags

## FAQs

The page addresses common questions about duration, regional blocking, and out-of-stock product handling, emphasizing that functionality limitation outweighs complete removal strategies.
