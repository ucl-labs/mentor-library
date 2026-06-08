# Vacation Rental Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/vacation-rental

## Overview

Google Search Central provides guidance on implementing structured data for vacation rental listings to enable rich search results displaying property details like name, description, images, location, rating, and reviews.

## Key Requirements

### Before Starting

The feature is limited to sites meeting eligibility criteria. Interested parties should complete the "vacation rental interest form" to express interest in the Early Adopters Program, though completion doesn't guarantee acceptance.

### Implementation Steps

1. Add required properties to your structured data
2. Follow all guidelines
3. Validate using the Rich Results Test tool
4. Deploy test pages and use URL Inspection tool
5. Submit sitemaps for ongoing updates

## Required Properties

**Core fields** include:
- `containsPlace` (Accommodation object)
- `containsPlace.occupancy` (QuantitativeValue)
- `identifier` (must be stable and language-independent)
- `image` (minimum 8 photos showing bedroom, bathroom, common areas)
- `latitude` and `longitude` (5+ decimal places precision)
- `name`

## Recommended Properties

Enhanced data includes address details, aggregate ratings, brand information, check-in/check-out times, amenity features, bed configurations, floor size, bathroom/bedroom counts, descriptions, languages spoken, and guest reviews.

## Amenity Features

The system supports **boolean amenities** (ac, wifi, pool, wheelchair accessible, etc.) and **non-boolean values** (internetType, parkingType, poolType, licenseNum).

## Monitoring

Use Search Console to track structured data performance, monitor for invalid items after deployments, and analyze search traffic patterns through the Performance Report.
