# Featured Snippets and Your Website

Source: https://developers.google.com/search/docs/appearance/featured-snippets

Featured snippets are special search result boxes that display descriptive information prominently, reversing the typical format of regular search results. They can also appear within related questions groups, commonly known as "People Also Ask" sections.

## How to Opt Out of Featured Snippets

### Block All Snippets

You can prevent both featured and regular snippets by adding the `nosnippet` rule to your page. The `data-nosnippet` HTML attribute also prevents text from appearing in either snippet type. If both rules are present, `nosnippet` takes priority.

### Block Featured Snippets Only

To keep regular snippets while excluding featured snippets, experiment with the `max-snippet` rule set to lower lengths. Featured snippets require sufficient text to be useful, so progressively reducing the value makes featured snippet inclusion less likely.

Google doesn't specify an exact minimum length for featured snippets, as requirements vary based on snippet content, language, and platform. A low `max-snippet` setting doesn't guarantee exclusion; for guaranteed prevention, use `nosnippet`.

## Can You Mark Your Page as a Featured Snippet?

No. Google's systems automatically determine which pages make suitable featured snippets for specific search queries and elevate them accordingly.

## User Behavior When Clicking Featured Snippets

Clicking a featured snippet directs users to the specific page section that appeared in the snippet, with automatic scrolling to that location. If browser technology doesn't support this or Google cannot determine the exact location confidently, the click directs to the page top.
