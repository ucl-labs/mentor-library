# Translated Results in Google Search

Source: https://developers.google.com/search/docs/appearance/translated-results

## Feature Availability

Google may translate search results into 21 languages including Arabic, Bengali, English, French, German, and others. The feature is available on both mobile and desktop platforms.

## How Translated Results Work

When users click a translated title link, they access a machine-translated version of the page. Users can switch back to view the original content. Google doesn't host translated pages; this functions similarly to using Google Translate or Chrome's built-in translation tool.

## Performance Monitoring

The Search Appearance filter in Search Console's Performance report allows publishers to track clicks and impressions for translated results.

## Opting Out

Translated results apply across all pages by default - no opt-in required. To opt out, use the `notranslate` rule via meta tag:

```html
<meta name="googlebot" content="notranslate">
```

Or as an HTTP response header:

```
X-Robots-Tag: notranslate
```
