# Remove Your AMP Pages From Google Search

Source: https://developers.google.com/search/docs/crawling-indexing/amp/remove-amp

## Overview

This Google Search Central guide explains how web developers can remove AMP pages from Google Search results. The documentation distinguishes between two page setups:

- **Canonical AMP**: Single page version where the AMP page serves as the canonical version
- **Canonical Non-AMP**: Two versions including both AMP and non-AMP pages

## Three Removal Options

The guide presents three primary approaches for removing AMP content.

## Option 1: Remove All Page Versions

To eliminate both AMP and non-AMP versions entirely:

1. Delete both versions from your server or CMS
2. Use the "Remove outdated content" tool, entering URLs for both versions
3. Update the Google AMP Cache to clear cached content
4. Verify removal through Google Search or the AMP status report in Search Console

**Important caveat**: This method may display error messages to users during the removal period before Googlebot discovers the deletion.

## Option 2: Remove Only AMP Pages

To keep canonical non-AMP pages while removing AMP versions:

1. Remove the `rel="amphtml"` link from the non-AMP page's source code
2. Configure HTTP 301 or 302 redirect responses for removed AMP pages
3. Redirect the AMP page to the canonical non-AMP version
4. For complete removal from all platforms, send HTTP 404 responses and update the AMP Cache

**Critical warning**: Avoid simply deleting files, as empty documents are considered invalid and Google may continue serving older cached versions.

## Option 3: CMS-Based Removal

Most CMS platforms publish AMP and non-AMP versions simultaneously. Users can:

- Unpublish individual pages through the CMS interface
- Disable AMP entirely across the site (removes all AMP pages)
- Consult provider documentation for WordPress.com, Drupal, or Squarespace
