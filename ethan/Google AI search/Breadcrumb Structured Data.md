# Breadcrumb (BreadcrumbList) Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/breadcrumb

Breadcrumb trails indicate a page's position within site hierarchy, helping users understand and navigate a website effectively. Users can move up the hierarchy one level at a time through the breadcrumb trail.

## Feature Availability

Available on desktop across all regions and languages where Google Search operates.

## Key Implementation Details

**BreadcrumbList** requires an `itemListElement` property containing at least two `ListItem` objects. Each `ListItem` must include:

- `position`: Integer indicating order in the trail
- `name`: The breadcrumb title displayed to users
- `item`: URL of the breadcrumb page (optional for final item)

## Guidelines

- Provide breadcrumbs representing typical user navigation paths rather than URL structure
- Include at least two items in the list
- Don't include the domain/homepage or current page as required items
- Follow general structured data and Search Essentials guidelines
