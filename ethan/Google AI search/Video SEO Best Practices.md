# Video SEO Best Practices

Source: https://developers.google.com/search/docs/appearance/video

## Help Google Find Your Videos

Use standard HTML elements like `<video>`, `<embed>`, `<iframe>`, or `<object>` for embedding. Avoid fragment identifiers and ensure videos appear in rendered HTML. Google supports structured data, video sitemaps, and Open Graph protocol metadata.

## Ensure Videos Can Be Indexed

Videos must meet several requirements:
- The watch page must be indexed and performing well
- Videos can't be hidden behind paywalls (unless paywall structured data is provided)
- Each video needs a valid thumbnail at a stable URL

Supported file types include MP4, WebM, MOV, and others.

## Create Dedicated Watch Pages

Videos should have dedicated pages where the video is the main content. Each watch page needs "unique page title and description that are unique to that video."

## Enable Specific Features

- Video previews require allowing Google to fetch video files
- Key moments can use Clip or SeekToAction structured data
- Live Badge uses BroadcastEvent structured data

## Video Thumbnail Requirements

- Minimum 60x30 pixels
- Supported formats: JPEG, PNG
- Must be accessible by Googlebot
- "At least 80% of the thumbnail's pixels must have an alpha (transparency) value greater than 250"

## Monitoring and Troubleshooting

Search Console provides video indexing reports, rich result reports, and performance tracking tools to monitor video content performance.
