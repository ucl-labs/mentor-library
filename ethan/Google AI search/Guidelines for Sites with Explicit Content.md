# Guidelines for Sites with Explicit Content

Source: https://developers.google.com/search/docs/crawling-indexing/safesearch

## Overview

Google's documentation explains that many users prefer filtering explicit content from search results. Sites hosting adult material can help Google categorize content accurately by following specific guidelines.

## How Google Handles Explicit Content

### SafeSearch Function

SafeSearch filters results containing "explicit sexual content of any type, including pornography" and "nudity," along with related materials. The system uses machine learning to identify problematic content while attempting to preserve material with "educational, documentary, scientific, or artistic" value.

Google's systems work to prevent unwanted exposure regardless of SafeSearch settings through query understanding algorithms that detect when searches deliberately seek explicit material.

### Content Removal Policies

Google automatically removes child sexual abuse material (CSAM) and responds to removal requests for non-consensual explicit imagery. Sites receiving significant volumes of valid removal requests for such content face demotion in rankings.

## Recommended Best Practices

Five key recommendations:

1. Implement content moderation and publisher verification to prevent harmful user-generated material
2. Allow Googlebot to fetch video files for content analysis
3. Permit Googlebot crawling without triggering age gates or access restrictions
4. Separate explicit pages on distinct domains or subdomains from general content
5. Use metadata to tag explicit pages

## Metadata Implementation

Add rating metadata to explicitly mark pages:

```html
<meta name="rating" content="adult">
```

For video content, use the `<video:family_friendly>` tag set to `no` in video sitemaps to prevent inclusion when SafeSearch is enabled.
