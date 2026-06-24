# AI Features and Your Website

Source: https://developers.google.com/search/docs/appearance/ai-features

Google's documentation explains that AI features like AI Overviews and AI Mode are integrated into Google Search. The key message: "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary."

## How AI Features Work

**AI Overviews** help users quickly understand complicated topics and provide links for deeper exploration. They appear when Google's systems determine they add value beyond traditional search results.

**AI Mode** serves queries requiring "further exploration, reasoning, or complex comparisons." Both features may use "query fan-out" techniques - issuing multiple related searches - to surface "a wider and more diverse set of helpful links" than classical search.

## Requirements for Appearing in AI Features

To be eligible for inclusion, pages must:

- Meet standard Google Search technical requirements
- Be indexed and eligible for snippets in traditional search
- Follow existing Search policies
- Focus on creating helpful, reliable content

The documentation emphasizes that "specific optimization isn't required for AI Overviews and AI Mode."

## Content Control

Site owners can use existing controls like `nosnippet`, `data-nosnippet`, `max-snippet`, and `noindex` to limit content appearing in AI features. These work through standard robots.txt directives for Googlebot.

## Performance Measurement

Traffic from AI features appears in Search Console's Performance report under the "Web" search type, alongside traditional search results data.

## Update 2026-06-24 - dedicated Generative AI report in Search Console

Beyond the "Web" search type, Search Console now has a **dedicated Generative AI performance report** (2026-06-03) showing impressions/pages in AI Overviews, AI Mode, and Discover. Site owners also get a **toggle to opt out of AI features** (Google states opting out is not used as a ranking signal for core web search).

- Detail: `Generative AI Performance Reports in Search Console.md`
- Source: https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports
