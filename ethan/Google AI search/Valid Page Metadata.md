# Valid Page Metadata for Google Search

Source: https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata

"Using valid HTML for page metadata ensures that Google can use the metadata as documented."

While Google attempts to interpret invalid or inconsistent HTML, markup errors can negatively impact how metadata appears in Google Search.

## Valid Elements in `<head>`

According to HTML standards, the `<head>` element should contain only these valid elements:

- `title`
- `meta`
- `link`
- `script`
- `style`
- `base`
- `noscript`
- `template`

## Invalid Elements to Avoid

The documentation specifically warns against placing these elements in `<head>`:

- `iframe`
- `img`

**Important Note:** "Once Google detects one of these invalid elements, it assumes the end of the `<head>` element and stops reading any further elements."

This means invalid elements not only cause problems themselves but can prevent Google from reading subsequent valid metadata tags.

## Recommendation

If invalid elements must be used, place them after all desired metadata to minimize negative impact on Google's parsing.
