# Event Structured Data Markup for Google Search

Source: https://developers.google.com/search/docs/appearance/structured-data/event

Google's event schema markup enables events to appear in enhanced search results, making them more discoverable to users. This feature provides "more interactive results" - one case study noted a "100% increase in typical year-over-year growth of traffic from Google Search."

## Three Implementation Paths

1. **Third-party platforms**: If posting through ticketing or social platforms already integrated with Google, no additional action is needed.
2. **CMS without HTML access**: WordPress and similar platforms may offer plugins, or the Data Highlighter tool can be used.
3. **Direct HTML editing**: Implement structured data manually using JSON-LD, Microdata, or RDFa formats.

## Key Requirements

**Required properties** include event name, location (with detailed address), and start date. The location address should be specific - "Bennelong Point, Sydney NSW 2000, Australia" works better than simply "Sydney."

Event names should highlight unique aspects without including venue names, prices, or promotional language.

## Content Guidelines

Events must be genuine public gatherings - not promotions, business hours, or virtual-only experiences. They require physical locations and must be accessible to the general public without advance membership requirements.

## Date and Time Best Practices

Use ISO-8601 format with UTC offsets (e.g., "2025-07-21T19:00-05:00"). For all-day or time-unknown events, specify only the date without granular hours.

## Regional Availability

Currently operates in: Australia, Brazil, Canada, Germany, India, Latin America, Spain, the United Kingdom, and the United States.
