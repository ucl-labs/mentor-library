# Speakable (BETA) Schema Markup

Source: https://developers.google.com/search/docs/appearance/structured-data/speakable

## Overview

The `speakable` schema.org property identifies sections of articles or webpages suitable for text-to-speech audio playback. This markup enables search engines and applications to distribute content through audio channels on Google Assistant-enabled devices.

## Key Functionality

According to the documentation, "The Google Assistant uses `speakable` structured data to answer topical news queries on smart speaker devices." When users request news on specific topics, the Assistant can return up to three articles with audio playback support for marked sections.

## Availability

Currently, this feature works for "users in the U.S. that have Google Home devices set to English, and publishers that publish content in English."

## Implementation Requirements

### Required Properties

Two locator methods are available:

- **cssSelector**: Uses CSS class attributes to address content
- **xPath**: Uses XML path notation to locate specific elements

Publishers must select one method; combining both is not permitted.

### Content Guidelines

The documentation recommends "around 20-30 seconds of content per section of `speakable` structured data, or roughly two to three sentences." Publishers should avoid marking datelines, photo captions, or attribution text.

## Technical Constraints

Content marked with `speakable` "must have concise headlines and/or summaries that provide users with comprehensible and useful information." Additionally, exclude elements that may confuse audio-only listeners.
