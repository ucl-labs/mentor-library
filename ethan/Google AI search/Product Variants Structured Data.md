# Product Variant Structured Data (ProductGroup)

Source: https://developers.google.com/search/docs/appearance/structured-data/product-variants

## Overview

This Google Search Central documentation explains how to implement structured data markup for product variants using `ProductGroup` and `Product` classes. The guidance helps e-commerce sites indicate which products are variations of the same parent item.

## Key Concepts

**Purpose**: According to the documentation, "To help Google better understand which products are variations of the same parent product, use the `ProductGroup` class" with associated properties like `variesBy`, `hasVariant`, and `productGroupID`.

**Benefit**: Adding this markup makes products eligible for display with variant information in merchant listing experiences while reducing information duplication.

## Implementation Approaches

The documentation describes two primary website design patterns:

1. **Single-page websites**: All variants selectable on one page using query parameters (e.g., `https://www.example.com/coat?size=small&color=green`)

2. **Multi-page websites**: Variants accessible on different pages requiring full markup on each variant page

## Required Properties

For `ProductGroup`:
- `name` (required): The product group name
- `variesBy`: Variant-identifying properties (color, size, material, pattern, etc.)
- `productGroupID`: Unique identifier for the product group

## Technical Requirements

Key guidelines include:
- Each variant must have a unique ID (SKU or GTIN)
- Single-page sites require one canonical URL for the overall product group
- Sites must support direct URL preselection of each variant
- Recommended: Include `Product` structured data alongside variant markup

## Validation Steps

1. Adding required properties
2. Following content guidelines
3. Testing with the Rich Results Test tool
4. Deploying test pages and using the URL Inspection tool
5. Allowing time for Google re-crawling and re-indexing
