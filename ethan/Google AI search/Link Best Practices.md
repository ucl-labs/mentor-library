# Link Best Practices for Google

Source: https://developers.google.com/search/docs/crawling-indexing/links-crawlable

Google uses links as signals for relevancy and page discovery. This guide covers making links crawlable and optimizing anchor text for both users and search engines.

## Make Your Links Crawlable

Google can parse links in `<a>` HTML elements with `href` attributes. Most other link formats aren't reliably extracted by crawlers.

**Recommended examples Google can parse:**
- `<a href="https://example.com">`
- `<a href="/products/category/shoes">`
- `<a href="./products/category/shoes">`
- Links with onclick or class attributes

**Not recommended (may not parse reliably):**
- `<a routerLink="products/category">`
- `<span href="https://example.com">`
- `<a onclick="goto('https://example.com')">`

URLs must resolve to actual web addresses that crawlers can request.

## Anchor Text Placement

Anchor text (link text) communicates page topics to users and Google. Place it between crawlable `<a>` elements.

For empty links, Google uses the `title` attribute as fallback. For image links, use descriptive `alt` text on the `img` element.

Use the URL Inspection Tool to verify JavaScript-inserted anchor text appears in rendered HTML.

## Write Good Anchor Text

Effective anchor text is descriptive, concise, and relevant to both source and target pages.

**Avoid:** Generic phrases like "Click here," "Read more," or "website"

**Better approach:** Descriptive phrases that provide context, such as "list of cheese types"

Write naturally without keyword stuffing (which violates spam policies). Space links apart rather than chaining them consecutively.

## Internal Links

Link to related content on your site using contextual anchor text. Every important page should have at least one internal link. No magical ideal link count exists, but avoid excessive linking.

## External Links

Linking to other sites establishes trustworthiness and credibility. Use `nofollow` only for untrusted sources, not all external links. Qualify paid links with `sponsored` or `nofollow`, and user-generated links with `ugc` or `nofollow`.
