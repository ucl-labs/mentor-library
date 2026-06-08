# SEO Guide for Web Developers

Source: https://developers.google.com/search/docs/fundamentals/get-started-developers

## Get started with Search: a developer's guide

Making your content search-friendly matters because it's how you get more relevant users viewing your content. This is called search engine optimization (SEO), which can result in more interested users coming to your site. If Google Search has trouble understanding your page, you're possibly missing out on an important source of traffic.

This guide covers what developers can do to make sure that their sites work well with Google Search.

## Find out how Google sees your site

To get started, test your site in the URL inspection tool or Rich Results Test to see how Google sees your site. Googlebot is Google's web crawling bot that discovers new and updated pages for the Google index.

You may be surprised to find that Google doesn't always see everything that you see in the browser. For example, Google may not see images if the page uses a JavaScript feature that isn't supported by Google.

## Check your links

Googlebot navigates from URL to URL by fetching and parsing links, sitemaps, and redirects. Googlebot treats every URL as if it's the first and only URL it has seen from your site. To make sure that Googlebot can find all the URLs on your site:

- Use `<a>` elements that Google can crawl. Ensure that all pages on the site can be reached by a link from another findable page. Make sure the referring link includes either text or, for images, an alt attribute, that is relevant to the target page.
- Build and submit a sitemap to help Googlebot more intelligently crawl your site.
- For JavaScript apps that have only one HTML page, make sure that each screen or piece of individual content has a URL.

## Check how you're using JavaScript

While Google does run JavaScript, there are some differences and limitations that you need to account for when designing your pages and applications. Learn more about the basics of JavaScript SEO or how to fix Search-related JavaScript problems.

## Keep Google updated when content changes

To make sure that Google finds your new or updated pages quickly:
- Submit sitemaps
- Ask Google to recrawl your URLs

If you're still having trouble getting your page indexed, check your server logs for errors.

## Don't forget about the words on the page

Googlebot can only find content that is textually visible. To make sure that Google Search understands what your page is about:

- **Make sure that your visual content is expressed in text form.** A product category page should include some textual explanation for each image.
- **Make sure that every page has a descriptive title and meta description.** Unique titles and meta descriptions help Google show how your pages are relevant to users.
- **Use semantic HTML.** While Google indexes HTML, PDF content, images, and videos, it doesn't index content that requires plugins or content rendered in a canvas.
- **Make sure your text content is accessible in the DOM.** Content added via the CSS `content` property is not part of the DOM and Google Search ignores it.

## Tell Google about other versions of your content

Google doesn't automatically know that there are multiple versions of your site or content. To make sure that Google serves the right version to users:
- Consolidate duplicate URLs
- Tell Google about localized versions of your site
- Make your AMP pages discoverable

## Control what content Google sees

There are several ways to block Googlebot:
- To block Google from finding your page, restrict access to logged-in users
- To block Googlebot from crawling your page, create a robots.txt
- To block Google from indexing your page but still allow crawling, add a `noindex` tag

A robots.txt is not a mechanism for keeping a web page out of Google. Use the `noindex` robots rules, or password-protect your page for that purpose.

If your content isn't showing up in Google Search and you want it to show up:
- Check if Googlebot can access the page with the URL inspection tool
- Test your robots.txt file to see if you're unintentionally blocking Googlebot
- Check your HTML for `noindex` rules in `meta` tags

## Enable rich results for your site

A rich result can include styling, images, or other interactive features that can help your site stand out more in Search results. You can help Google understand your page better and show rich results for it in Search by providing explicit clues about the meaning of a page with structured data on the page.
