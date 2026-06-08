# Course List Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/course

## Overview

This Google Search Central documentation explains how to implement course list structured data to help prospective students discover educational content through Google Search. The feature displays course information including name, provider, and description.

## Feature Availability

The course list rich result is "available in English in all regions where Google Search is available."

## Implementation Steps

1. Add required properties to structured data
2. Follow content and technical guidelines
3. Validate using Rich Results Test
4. Deploy and test with URL Inspection tool
5. Submit sitemaps for ongoing updates

## Required Properties

**For Course markup:**
- `name` (Text): Course title
- `description` (Text): Course overview, limited to 60 characters for display
- `provider` (Organization): Organization offering the course

**For ItemList markup:**
- `itemListElement` (ListItem): Individual course entries
- `position` (Integer): Ordinal placement
- `url` (URL): Unique canonical URL per course

## Content Guidelines

Courses must meet specific criteria: "A series or unit of curriculum that contains lectures, lessons, or modules in a particular subject and/or topic." Single videos or public events don't qualify.

## Technical Requirements

- Minimum of three courses required
- Carousel markup necessary on summary or all-in-one pages
- Each course needs valid name and provider properties
- No promotional language, pricing, or discount language in titles

## Implementation Approaches

Two approaches are documented:
- Single course detail pages paired with summary pages
- All-in-one pages containing list and course details together
