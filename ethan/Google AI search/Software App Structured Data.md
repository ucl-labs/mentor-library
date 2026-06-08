# Software App (SoftwareApplication) Schema

Source: https://developers.google.com/search/docs/appearance/structured-data/software-app

Structured data for software applications enhances their appearance in Google Search results through rich results display.

## Required Properties

The `SoftwareApplication` type requires:
- `name`: The application title
- `offers.price`: Pricing information (set to 0 for free apps)
- Either `aggregateRating` or `review`: User ratings or review content

## Recommended Properties

- `applicationCategory`: Type of app from a supported list (GameApplication, BusinessApplication, EducationalApplication, etc.)
- `operatingSystem`: Required OS specification

## Supported App Types (24 categories)

Games, social networking, travel, shopping, sports, lifestyle, business, design, development, and utilities applications.

## Extended Properties

Mobile and web applications can use specialized subtypes (`MobileApplication`, `WebApplication`). VideoGame types must be combined with another type to qualify for rich results.

## Implementation Steps

1. Add required properties
2. Follow guidelines
3. Validate code with the Rich Results Test
4. Deploy pages and use the URL Inspection tool
5. Submit sitemaps for ongoing updates
