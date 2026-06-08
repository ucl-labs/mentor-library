# Image Metadata for Google Images

Source: https://developers.google.com/search/docs/appearance/structured-data/image-license-metadata

## Overview

Google Images can display enhanced details about images when you provide metadata, including creator information, usage rights, and licensing details. This documentation explains how to add image metadata so your images may qualify for features like the Licensable badge.

## Feature Availability

This feature works across all mobile and desktop platforms where Google Search operates globally.

## Preparation Requirements

Before implementing image metadata, ensure:

- Pages containing images are publicly accessible without login requirements
- Googlebot can crawl your image pages (check the Page Indexing report or URL Inspection tool)
- Your content follows Search Essentials guidelines
- You've implemented image SEO best practices
- You submit a sitemap to keep Google informed of updates

## Two Metadata Approaches

You can add image information through either method - only one is necessary:

**Structured Data**: Page-level markup using Schema.org that associates metadata with specific image instances. Required for each page where an image appears.

**IPTC Photo Metadata**: Information embedded directly within image files that persists across pages. Add once per image file.

When both exist, structured data takes precedence if information conflicts.

## Implementation Steps

1. Add required properties to your markup
2. Follow general structured data guidelines
3. Validate using the Rich Results Test tool
4. Deploy test pages and use URL Inspection
5. Request recrawling after verification
6. Submit sitemaps for ongoing updates

## Structured Data Requirements

### Required Properties

**contentUrl** (URL): Points to the actual image file - Google uses this to match metadata to images.

**At least one of**:
- `creator`: Image maker (person or organization)
- `creditText`: Published credit attribution
- `copyrightNotice`: Copyright claim
- `license`: Usage rights page URL

### Recommended Properties

- `acquireLicensePage`: Where users find licensing information
- `creator.name`: Creator's name
- `copyrightNotice`: Copyright holder identification
- `license`: URL describing usage terms

For the Licensable badge specifically, the `license` property is mandatory.

## Code Example (JSON-LD Format)

```json
{
  "@context": "https://schema.org/",
  "@type": "ImageObject",
  "contentUrl": "https://example.com/photos/black-labrador.jpg",
  "license": "https://example.com/license",
  "acquireLicensePage": "https://example.com/licensing",
  "creditText": "Photo Lab",
  "creator": {
    "@type": "Person",
    "name": "Jane Smith"
  },
  "copyrightNotice": "John Doe"
}
```

## IPTC Metadata Fields

Google extracts these embedded image properties:

- **Copyright Notice**: Ownership identification
- **Creator**: Photographer or organization name
- **Credit Line**: Published attribution
- **Digital Source Type**: Creation method (algorithmic, synthetic, composite, trained algorithmic)
- **Licensor URL**: Where licensing information is found
- **Web Statement of Rights**: Usage rights page URL

The Web Statement of Rights field is required for Licensable badge eligibility.

## C2PA Metadata Support

Images containing C2PA version 2.1+ metadata signed by certified authorities may display creation and editing information in the "About this image" feature within search results.

## Common Troubleshooting

- Verify structured data syntax using the Rich Results Test
- Check for manual action penalties in Search Console
- Confirm compliance with structured data guidelines
- Allow several days for recrawling and reindexing
