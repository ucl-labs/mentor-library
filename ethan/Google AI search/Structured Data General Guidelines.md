# General Structured Data Guidelines

Source: https://developers.google.com/search/docs/appearance/structured-data/sd-policies

## Key Points

**No Guarantee of Display**: Even if your page is marked up correctly according to the Rich Results Test, structured data does not guarantee rich result display. The algorithm considers various factors including search history, location, and device type.

**Eligibility Requirements**: Structured data must comply with content policies and spam policies. A structured data manual action causes pages to lose rich result eligibility without affecting regular search ranking.

## Technical Guidelines

- Use one of three supported formats: JSON-LD (recommended), Microdata, or RDFa
- Don't block structured data pages using robots.txt or noindex
- Test using the Rich Results Test and URL Inspection tool

## Quality Guidelines

- Content must be visible to page readers; don't mark up hidden content
- Data must accurately represent page content (relevance requirement)
- Include all required properties for your specific rich result type
- Place structured data on the pages it describes
- Use most specific schema.org types available
- Ensure images are crawlable, indexable, and relevant

**Multiple Items**: Pages can contain multiple structured data types (nesting or individual items), helping Google understand diverse content like recipes with videos and reviews.
