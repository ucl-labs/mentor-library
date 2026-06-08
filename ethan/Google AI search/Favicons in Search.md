# Define a favicon to show in search results

Source: https://developers.google.com/search/docs/appearance/favicon-in-search

Google Search can display your site's favicon in search results if you implement it correctly. This feature applies to organic search results only.

## Implementation Steps

1. **Create a favicon** following the guidelines below
2. **Add a link tag** to your home page header:
   ```
   <link rel="icon" href="/path/to/favicon.ico">
   ```
3. **Allow time for processing** - Google needs to recrawl your home page, which can take days to weeks. You can request indexing using the URL Inspection tool.

## Supported Link Attributes

**rel attribute values:**
- `icon` - Standard favicon (also supports legacy `shortcut icon`)
- `apple-touch-icon` - iOS-friendly icon
- `apple-touch-icon-precomposed` - Earlier iOS versions

**href attribute:**
- Accepts relative paths (`/smile.ico`) or absolute URLs
- Can be hosted on a CDN, not necessarily your own server

## Guidelines for Eligibility

- **One favicon per hostname** - Subdomains can have different favicons, but subdirectories cannot
- **Crawler access required** - Both Googlebot and Googlebot-Image must be able to access the favicon and home page
- **Visual branding** - Should represent your site's brand identity
- **Size requirements** - Minimum 8x8px, but 48x48px or larger recommended
- **Stable URL** - Don't change the favicon URL frequently
- **Content restrictions** - Inappropriate imagery (pornography, hate symbols) will be replaced with a default icon

Note: Favicon appearance in search results is not guaranteed even when all guidelines are met.
