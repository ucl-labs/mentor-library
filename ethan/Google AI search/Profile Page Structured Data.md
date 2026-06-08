# Profile Page (ProfilePage) Schema Markup

Source: https://developers.google.com/search/docs/appearance/structured-data/profile-page

`ProfilePage` structured data helps Google Search understand creators in online communities. This markup is "designed for any site where creators (either people or organizations) share first-hand perspectives," supporting features like Discussions and Forums in search results.

## Required Properties

**ProfilePage** requires:
- **mainEntity**: Must be either a `Person` or `Organization` type representing the profile's subject

**Person/Organization** requires:
- **name**: The primary identifier (real name recommended, with `alternateName` for handles)

## Recommended Properties

- `dateCreated` and `dateModified`: Profile timeline metadata
- `alternateName`: Social media handles or alternate identifiers
- `description`: User byline or credentials
- `image`: Profile photograph (must be crawlable and in supported formats)
- `interactionStatistic`: Engagement metrics (followers, likes)
- `agentInteractionStatistic`: Creator activity metrics (posts, shares)
- `sameAs`: Links to external profiles or homepages

## Valid Use Cases

- User profiles on forums
- Author pages on news sites
- "About Me" pages on blogs
- Employee pages on company websites

## Invalid Uses

Store homepages or organization review sites.
