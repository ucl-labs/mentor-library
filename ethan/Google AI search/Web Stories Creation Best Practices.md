> **HISTORICAL - do not recommend (flagged 2026-08-23).** Google has wound down Web Stories
> support in Search and Discover, and the format has no relevance to Shopify DTC / AEO client
> work. Kept for reference only. Do not cite this in a client audit or deliverable.

# Best Practices for Creating Web Stories

Source: https://developers.google.com/search/docs/appearance/web-stories-creation-best-practices

## Overview

Google recommends focusing on critical tasks first, then implementing additional recommended best practices for Web Stories to maintain reader engagement.

## Storytelling

**Critical Practices:**
- **Video first**: "Video is more engaging than text or images. Use as much video as possible, and supplement with images and text."

**Recommended Practices:**
- Share personal perspective beyond facts
- Develop narrative arc with suspense and context
- Deliver satisfying conclusions

## Design

**Critical Practices:**
- Reduce character count to approximately 280 characters per page
- Prevent text from being blocked by other content
- Keep all text visible and avoid overflow issues
- Use animations purposefully without repetitive or distracting elements

**Recommended Practices:**
- Remove platform-specific calls-to-action when adapting from Instagram/Snapchat/YouTube
- Include full bleed videos and images for immersion
- Maintain high-quality, non-distorted visuals
- Add high-resolution brand logo to cover page
- Keep individual videos under 15 seconds (maximum 60 seconds)
- Include quality audio (minimum 5 seconds, balanced volume)
- Consider auto-advance for video-only stories

## SEO

**Critical Practices:**
- Provide high-quality, useful content
- Keep titles under 90 characters (ideally under 70)
- Avoid `noindex` attributes
- Add Web Stories to sitemap
- Ensure self-canonical structure: `<link rel="canonical" href="https://www.example.com/url/to/webstory.html">`
- Include AMP story metadata, title tags, meta descriptions, structured data, OGP, and Twitter cards

**Recommended Practices:**
- Incorporate structured data markup
- Include image alt text
- Integrate stories into website navigation
- Use consistent URL structure with other content
- Implement AMP story page attachments for additional context
- Add video captions/subtitles
- Use semantic HTML markup
- Enable landscape display support

## Technical

**Critical Practices:**
- Validate AMP compliance using AMP Validator tool
- Avoid text within poster images
- Ensure poster image minimum size: 640x853px (3:4 aspect ratio)
- Ensure logo minimum size: 96x96px (1:1 aspect ratio)

**Recommended Practices:**
- Include `og:image` meta tags for discoverability
