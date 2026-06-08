# Tell Google About Localized Versions of Your Page

Source: https://developers.google.com/search/docs/specialty/international/localized-versions

When you have multiple versions of a page for different languages or regions, inform Google about these variations. This helps Google Search direct users to the most appropriate version based on their language or region preferences.

## When to Indicate Alternate Pages

- Your main content stays in one language while only the template (navigation, footer) is translated
- Your content has small regional variations with similar content in a single language (e.g., English versions for the US, GB, and Ireland)
- Your site content is fully translated into multiple languages

## Three Methods for Indicating Alternate Pages

HTML tags, HTTP headers, or XML sitemaps - all three are equivalent from Google's perspective.

### Guidelines for All Methods

- Each language version must list itself plus all other language versions
- Use fully-qualified URLs including the protocol: `https://example.com/foo`
- Alternate URLs don't need to be on the same domain
- For multiple locales with the same language, provide a catchall URL for geographically unspecified users
- Both pages must point to each other bidirectionally, or the tags will be ignored
- Consider adding a fallback page using the `x-default` value for unmatched languages

### HTML Tags Method

Add `<link rel="alternate" hreflang="lang_code"... >` elements to your page's `<head>` section.

**Syntax:**
```html
<link rel="alternate" hreflang="[lang_code]" href="url_of_page" />
```

**Example for USA, UK, Germany, and default:**
```html
<head>
  <link rel="alternate" hreflang="en-gb" href="https://en-gb.example.com/page.html" />
  <link rel="alternate" hreflang="en-us" href="https://en-us.example.com/page.html" />
  <link rel="alternate" hreflang="en" href="https://en.example.com/page.html" />
  <link rel="alternate" hreflang="de" href="https://de.example.com/page.html" />
  <link rel="alternate" hreflang="x-default" href="https://www.example.com/" />
</head>
```

### HTTP Headers Method

Return an HTTP header with your page's GET response. Useful for non-HTML files like PDFs.

**Syntax:**
```
Link: <url1>; rel="alternate"; hreflang="[lang_code_1]", <url2>; rel="alternate"; hreflang="[lang_code_2]", ...
```

### Sitemap Method

Use an XML sitemap with `<xhtml:link rel="alternate" hreflang="...">` child elements for each URL variant.

## Supported Language and Region Codes

`hreflang` attribute value consists of:
- **First code:** Language code in ISO 639-1 format
- **Second code (optional):** Region code in ISO 3166-1 Alpha 2 format

Only specify language codes (not just country codes). For Belgium: `de-be`, `nl-be`, or `fr-be` (not `be`).

## Using x-default for Unmatched Languages

The reserved `x-default` value specifies the fallback page for users whose language settings don't match any localized version. Useful for language selector pages and auto-redirecting home pages.

## Common Mistakes

**Missing return links:** If page X links to page Y, page Y must link back to page X.

**Incorrect language codes:** Ensure all language codes identify the language (ISO 639-1 format) and optionally the region (ISO 3166-1 Alpha 2 format).

**Incorrect region codes:** Use officially assigned codes. Reserved codes like `EU`, `UN`, or `UK` are ignored by Google Search.
