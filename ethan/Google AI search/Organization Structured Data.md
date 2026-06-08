# Organization Schema Markup

Source: https://developers.google.com/search/docs/appearance/structured-data/organization

Adding Organization structured data to your home page enables Google to:
- Better understand administrative details
- Disambiguate your organization from others
- Influence visual search elements like logos and knowledge panels
- Enhance merchant knowledge panels and brand profiles (for merchants)

## Recommended Properties (30+ available)

- `name` and `alternateName`
- `url` and `logo`
- `address` (with postal details)
- `contactPoint`, `telephone`, `email`
- `description`
- Business identifiers (`iso6523Code`, `vatID`, `taxID`)
- `foundingDate`
- `hasMerchantReturnPolicy` and `hasShippingService`

## Implementation Guidelines

- Place on home page or about page
- Use most specific schema.org subtype (e.g., OnlineStore, LocalBusiness)
- Follow image requirements for logos (minimum 112x112px)
- Ensure crawlability and proper formatting

## Code Examples

JSON-LD examples available for:
- Basic Organization markup
- OnlineStore subtype with shipping and return policies
