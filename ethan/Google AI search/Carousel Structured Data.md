# Carousel (ItemList) Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/carousel

## Overview

Carousels are list-like rich results allowing users to swipe through multiple cards from the same website on mobile devices. To qualify, add `ItemList` structured data combined with supported content types: Course list, Movie, Recipe, or Restaurant.

## Implementation Approaches

### Summary Page and Multiple Detail Pages

This model uses a summary page containing brief item descriptions that link to individual detail pages.

**Summary Page Structure:**
The summary page defines an `ItemList` where each `ListItem` contains three properties: `@type` (ListItem), `position` (1-based ordering), and `url` (link to detail page).

**Detail Pages:**
Each detail page includes specific structured data for the content type (Recipe, Movie, Course, or Restaurant).

### Single All-in-One-Page List

A single page containing complete carousel information for all items, including full content without external linking. All items display on one page with anchor links.

## Required Properties

### ItemList Container

- **itemListElement**: Array containing minimum two `ListItem` elements of identical type

### ListItem Properties

**For Summary Pages:**
- `position`: Integer (1-based)
- `url`: Canonical URL of detail page on same domain

**For All-in-One Pages:**
- `position`: Integer (1-based)
- `item`: Object containing:
  - `item.name`: Display title
  - `item.url`: Current page URL with anchor
  - Content-type-specific required properties

## Guidelines

- "All items in the list must be of the same type" (e.g., all recipes, no mixing)
- Carousel structure must match visible page content
- Items display in `position` order
- All items listed on page must appear in structured data

## Validation Steps

1. Use Rich Results Test for validation
2. For summary pages, verify: minimum two ListItems, uniform type, valid detail page URLs
3. Deploy test pages and use URL Inspection tool
4. Confirm Google accessibility (no robots.txt blocking, noindex tags, or login walls)
5. Submit sitemap to inform Google of updates
