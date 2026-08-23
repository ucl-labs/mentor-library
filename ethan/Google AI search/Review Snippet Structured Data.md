> **CAUTION - partial (flagged 2026-08-23).** This doc does not mention Google's self-serving review
> restriction: Google ignores `review` / `aggregateRating` markup that a business writes about
> **itself** on `LocalBusiness` and `Organization` entities, so those stars will never render.
> Only mark up reviews of **products, services, and other reviewable entities**, sourced from real
> customers. Validate any recommendation against the live Search Central page before shipping it.

# Review Snippet (Review, AggregateRating) Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/review-snippet

Review snippets display short excerpts from reviews or ratings, typically averaging scores from multiple reviewers. Google may show these as rich snippets with stars and summary information when valid markup is detected.

## Eligible Content Types

- Book
- Course list
- Event
- Local business
- Movie
- Product
- Recipe
- Software App

Also supports: CreativeWorkSeason, CreativeWorkSeries, Episode, Game, MediaObject, MusicPlaylist, MusicRecording, and Organization types.

## Key Guidelines

- Use `AggregateRating` for evaluations by multiple people
- Nest reviews within relevant schema.org types or use `itemReviewed` property
- Make review content immediately visible to users on the page
- Provide ratings with review comments and author names when possible
- Review specific items, not categories
- Don't aggregate reviews from other websites
- For local businesses: reviews must come directly from users, not the business itself

## Required Properties

**For Review:**
- `author` (Person or Organization)
- `itemReviewed` (valid schema.org type)
- `reviewRating` (Rating object)

**For AggregateRating:**
- `itemReviewed` (valid schema.org type)
- `ratingValue` (numerical rating)
- At least one of: `ratingCount` or `reviewCount`
