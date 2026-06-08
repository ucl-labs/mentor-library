# Keep Redacted Information out of Google Search

Source: https://developers.google.com/search/docs/crawling-indexing/keep-redacted-information-out

## Overview

This Google Search Central documentation addresses how unintended information can be published alongside intentionally redacted content. The page explains that "information that you might not see, or that was intended to be redacted, might be included in some document formats."

Search engines index publicly available material, including images. Technologies like optical character recognition (OCR) and screen readers can make seemingly hidden content discoverable. Visual concealment methods - such as tiny fonts, matching text color to backgrounds, or covering text with images - do not prevent search engine indexing.

## Key Problems Identified

Document formats often retain:
- Change history showing redacted or altered text
- Full versions of cropped or redacted images
- Metadata listing file access and editor information

This information persists even after format conversion or export.

## Best Practices for Redaction

### Edit Images Before Embedding

- Crop unwanted information before adding images to documents
- Remove or obscure text and non-public image portions (OCR can make image text searchable)
- Eliminate undesired metadata
- Export as flattened formats like PNG or WEBP to prevent unintended inclusions

### Remove Text Before Publishing

- Use proper document redaction tools rather than black rectangles
- Verify document metadata in public files
- Follow format-specific redaction best practices
- Consider information in URLs and filenames - use hashes instead of emails or names
- Implement authentication with `noindex` robots meta tags
- Verify the website in Google Search Console for quick removal if needed

## Recovery Steps

If improperly redacted documents are indexed:

1. Remove the live document from its hosting location
2. Use the Removals tool in Search Console to remove indexed versions (typically under one day)
3. Host properly redacted documents at new URLs and update links
4. Contact other sites hosting the same documents
5. Allow removal requests to expire after 6 months or upon index updates
