# Maintaining your website's SEO

Source: https://developers.google.com/search/docs/fundamentals/get-started

If your site is on Google and you're familiar with the fundamentals of SEO, there are more things you can do to improve how your site appears on Google. This guide covers more in-depth SEO tasks, such as preparing for a site move or managing a multi-lingual site.

## Control how Google crawls and indexes your site

Read our guide to understand how Google Search works; if you don't understand the crawl/index/serving pipeline well, it will be difficult to debug issues or anticipate Search behavior on your site.

### Duplicate content

Be sure that you understand what canonical pages are, and how they affect crawling and indexing of your site.

### Resources

Be sure that any resources (images, CSS files, and so on) or pages that Google is meant to crawl are accessible to Google; that is, they are not blocked by any robots.txt rules and are accessible to an anonymous user. Inaccessible pages will not appear in the Page Indexing report, and the URL Inspection tool will show them as not crawled.

### Robots.txt

Use robots.txt rules to prevent crawling, and sitemaps to encourage crawling. Block crawling of duplicate content on your site, or unimportant resources that might overload your server with requests. Don't use robots.txt as a mechanism to prevent indexing; use the `noindex` tag or login requirements for that.

### Sitemaps

Sitemaps are a very important way to tell Google which pages are important to your site, and also provide additional information (such as update frequency), and are very important for crawling non-textual content (such as images or video). Although Google won't limit crawling to pages listed in your sitemaps, it will prioritize crawling these pages. This is especially important for sites with rapidly changing content, or with pages that might not be discovered through links.

### Internationalized or multi-lingual sites

If your site includes multiple languages, or is targeted at users in specific locales:
- Read about multi-regional and multi-lingual sites for high-level advice
- Use hreflang to tell Google about different language variations of pages on your site
- If your site adapts content based on locale, read how this can affect Google's crawl

### Migrating a page or a site

#### Migrating a single URL

If you move a page permanently to another location, implement `301` redirects. If the move is only temporary, return `302` instead to tell Google to continue to crawl your page.

When a user requests a page that has been removed, create a custom `404` page. Be sure that when a user requests a page that is no longer there, you return a true `404` error, not a soft 404.

#### Migrating a site

If you're migrating an entire site, implement all the `301` and sitemap changes you need, then tell Google about the move so that we can start crawling the new site.

### Follow crawling and indexing best practices

- **Make your links crawlable.**
- **Use `rel=nofollow`** for paid links, links that require login, or untrusted content
- **Managing your crawl budget**: If your site is particularly large, Google might not be able to crawl your entire site as often as you'd like, so point Google to the most important pages via sitemaps
- **JavaScript usage**: Follow Google's recommendations for JavaScript on websites
- **Multi-page articles**: Ensure prominent next and previous links for users to click
- **Infinite scroll pages**: Provide a paginated version if you want the page to be crawled
- **Block access to URLs that change state**, such as posting comments, creating accounts, adding items to a cart
- If your site is still HTTP, migrate to HTTPS for users' security

## Help Google understand your site

Put key information in text, not graphics, on the site. Although Google can parse and index many file types, text is still the safest bet. If you use non-text content, add structured data to your pages to help Google understand your content.

## Follow our guidelines

Be sure to follow our Search Essentials. Some of these are recommendations and best practices; others can lead to a site being removed from the Google index if you do not follow them.

### Content-specific guidelines

- **Video**: Follow video best practices to enable Google to find, crawl, and show results for videos
- **Images**: Follow image best practices to get your images to appear in Search
- **For children**: Tag your pages or site as child-directed to comply with COPPA
- **Adult sites**: Consider tagging adult-only content, which will filter it in SafeSearch results
- **News**: Create a News sitemap, prevent abuse, and consider flexible sampling for paywalled content

## Manage the user experience

Providing a good user experience should be your site's top goal, and a good user experience is a ranking factor. Key elements include:
- Use HTTPS rather than HTTP
- Fast page load speed
- Mobile-friendly design

## Control your search appearance

Google provides many kinds of search result features including review stars and special result types. Consider implementing relevant features and providing a favicon to show in search results.

## Using Search Console

Search Console offers a broad range of reports to help you monitor and optimize your site performance on Google Search.
