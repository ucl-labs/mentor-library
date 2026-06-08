# Mark Up FAQs with Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/faqpage

**Important update:** As of May 7, 2026, FAQ rich results are no longer appearing in Google Search.

## Key Points (Historical Reference)

**Availability**: FAQ rich results were previously limited to "well-known, authoritative websites that are government-focused or health-focused" on desktop and mobile.

**Content Structure**: Pages must use three main schema types:
- `FAQPage` (one per page)
- `Question` (required property: `name` and `acceptedAnswer`)
- `Answer` (required property: `text`)

**Usage Guidelines**: Valid uses included FAQ pages "written by the health site itself, with no way for users to submit alternative answers." Invalid uses included forum pages or product support pages where users can submit competing answers.

**HTML Support**: Answer text can contain specific HTML tags including headings, lists, links, paragraphs, bold, strong, italic, and emphasis tags.

## Monitoring

Use Search Console's Rich Results Status Report to monitor structured data after deployment and track changes over time.
