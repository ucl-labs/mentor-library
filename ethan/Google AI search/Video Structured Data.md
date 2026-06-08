# Video (VideoObject, Clip, BroadcastEvent) Schema Markup

Source: https://developers.google.com/search/docs/appearance/structured-data/video

Google Search helps videos appear in multiple locations including main results, Video mode, Google Images, and Google Discover. You can influence how your videos display by marking them up with `VideoObject` structured data.

## Video Features Available

**LIVE Badge**: Mark livestreams with `BroadcastEvent` to display a LIVE badge. Eligible content includes sporting events, awards shows, influencer videos, and live gaming streams.

**Key Moments**: Users can navigate video segments like book chapters. Google attempts automatic detection, but you can specify segments through:
- `Clip` structured data (all languages)
- `SeekToAction` structured data (multiple languages)
- YouTube description timestamps (all languages)

To opt out completely from key moments, use the `nosnippet` meta tag.

## Required VideoObject Properties

- **name**: Unique video title
- **thumbnailUrl**: URL to unique thumbnail image
- **uploadDate**: Publication date/time (ISO 8601 format with timezone recommended)

## Recommended VideoObject Properties

- **contentUrl**: Direct URL to video file (preferred over embedUrl)
- **description**: Unique video description (HTML tags ignored)
- **duration**: Length in ISO 8601 format (e.g., PT1M54S)
- **embedUrl**: URL to video player (if contentUrl unavailable)
- **expires**: When video becomes unavailable (ISO 8601)
- **hasPart**: Nest `Clip` properties for video segments
- **interactionStatistic**: View count and interaction type
- **regionsAllowed**: Countries where video is allowed (ISO 3166-1)

## Clip Properties (for Key Moments)

Required:
- **name**: Descriptive title for clip
- **startOffset**: Start time in seconds from beginning
- **url**: URL pointing to clip's start time

## YouTube Timestamp Best Practices

- Format: `[hour]:[minute]:[second]` (hour optional)
- Place label on same line as timestamp
- Each timestamp on new line
- Labels must contain at least one word
- List chronologically
