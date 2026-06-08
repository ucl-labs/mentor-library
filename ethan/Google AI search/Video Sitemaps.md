# Video Sitemaps and Alternatives

Source: https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps

A video sitemap is a specialized sitemap format that includes additional metadata about videos hosted on web pages. "Creating a video sitemap is a good way to help Google find and understand the video content on your site, especially content that was recently added or that we might not otherwise discover."

Google recommends video sitemaps as the primary approach, though alternative formats like mRSS feeds are also supported.

## Key Best Practices

- Videos must be relevant to their host page content
- All referenced files must be accessible to Googlebot without authentication
- URLs cannot be disallowed by robots.txt
- Only HTTP and FTP protocols are supported (not streaming protocols)
- Content must be verifiable as Googlebot if access is restricted

## Required Elements

Every video entry requires:

- **Thumbnail location** (`<video:thumbnail_loc>`) - pointing to an image file
- **Title** - matching the on-page video title
- **Description** - up to 2,048 characters
- **Either content location OR player location** - pointing to actual video file or player embed

## Optional Elements

Enhanced metadata includes duration, expiration date, ratings, view counts, publication dates, family-friendly status, geographic/platform restrictions, subscription requirements, uploader information, livestream status, and tags (maximum 32 per video).

## Alternative: mRSS Feeds

mRSS (Media RSS) is an RSS 2.0 extension supporting multimedia syndication, offering similar functionality to video sitemaps with comparable metadata fields.
