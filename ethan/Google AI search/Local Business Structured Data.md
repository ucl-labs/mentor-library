# Local Business (LocalBusiness) Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/local-business

LocalBusiness structured data helps Google understand business information for search results and Maps displays. Businesses can use structured data to display details in Google Search knowledge panels and carousels.

## Required Properties

For basic LocalBusiness markup:
- **address** (PostalAddress with street, locality, region, postal code, country)
- **name** (business name)

## Recommended Properties

- Opening hours specifications
- Geographic coordinates (latitude/longitude with 5+ decimal precision)
- Phone numbers
- Price ranges
- Restaurant cuisine types
- Reviews and ratings
- Department information

## Business Hours Format

- Standard weekday/weekend hours
- Late night hours (crossing midnight)
- All-day operations (00:00-23:59)
- Seasonal closures (with validFrom/validThrough dates)

## Departments

Businesses with multiple departments can markup each separately with distinct properties like different phone numbers or hours.

## Restaurant Carousel

A limited-access feature allows restaurants meeting specific criteria to appear in carousels, requiring images and cuisine information.
