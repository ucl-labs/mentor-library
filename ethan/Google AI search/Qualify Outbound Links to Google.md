# Qualify Your Outbound Links to Google

Source: https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links

## Overview

Google Search Central provides guidance on using `rel` attribute values in anchor tags to communicate the nature of links on your website. This helps Google understand your relationship with linked pages.

## Key rel Attribute Values

### rel="sponsored"

This marks paid links and advertisements. Google states: "Mark links that are advertisements or paid placements (commonly called paid links) with the sponsored value." The documentation notes that `nofollow` was previously recommended for this purpose but `sponsored` is now preferred.

### rel="ugc"

User-generated content links (comments, forum posts) should use this value. The guidance suggests: "you might remove this attribute from links posted by members or users who have consistently made high-quality contributions over time."

### rel="nofollow"

Use when other values don't apply and you prefer Google not follow the link. The documentation clarifies this applies to external links; for internal site restrictions, use `robots.txt` instead.

## Multiple Values

You can combine values as space or comma-separated lists:
- `rel="ugc nofollow"`
- `rel="ugc,nofollow"`

## Important Notes

Links marked with these attributes generally won't be followed by Google, though pages may still be discovered through other means like sitemaps. These attributes work only in crawlable `<a>` elements.
