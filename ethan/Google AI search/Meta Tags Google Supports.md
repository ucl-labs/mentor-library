# Meta Tags and Attributes that Google Supports

Source: https://developers.google.com/search/docs/crawling-indexing/special-tags

Meta tags are HTML elements providing additional page information to search engines. They're placed in the `<head>` section and appear as `<meta>` tags with name and content attributes.

## Supported Meta Tags

**description**
Provides a brief page summary that may appear in search result snippets.

**robots and googlebot**
Control crawling and indexing behavior. The robots tag applies universally, while googlebot is Google-specific. When conflicting directives exist, "the more restrictive tag applies."

**notranslate**
Prevents Google from providing translated versions of your page in search results.

**nopagereadaloud**
Blocks Google's text-to-speech services from reading pages aloud.

**google-site-verification**
Used to verify site ownership in Search Console.

**Content-Type and charset**
Define page content type and character encoding (UTF-8 recommended).

**refresh**
Redirects users after a delay, though "server-side 301 redirect" is recommended instead.

**viewport**
Indicates mobile-friendliness to Google by configuring mobile rendering.

**rating**
Labels pages containing adult content for SafeSearch filtering.

## HTML Attributes Google Supports

Attributes like `src` and `href` help discover resources. Google also recognizes `rel` attributes for qualifying outbound links and the `data-nosnippet` attribute for excluding content from snippets.

## Important Notes

- Google reads both HTML and XHTML-style tags
- Letter case is generally unimportant except for google-site-verification
- JavaScript injection of meta tags should be avoided
- Use the URL Inspection Tool to verify page meta tags

## Unsupported Elements

Google ignores meta-keywords tags, `lang` attributes, `next`/`prev` rel values, and the nositelinkssearchbox directive.
