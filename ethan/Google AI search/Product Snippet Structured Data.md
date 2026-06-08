# Product Snippet Structured Data Guide

Source: https://developers.google.com/search/docs/appearance/structured-data/product-snippet

## Overview

This Google Search Central documentation explains how to implement Product structured data markup to enable product snippets in search results. A product snippet is a text result that displays "additional product information such as ratings, review information, price, and availability."

## Key Implementation Steps

1. **Add required properties** using JSON-LD, RDFa, or Microdata formats
2. **Follow guidelines** for technical and content compliance
3. **Validate using Rich Results Test** to identify critical errors
4. **Deploy and test** with the URL Inspection tool
5. **Submit sitemap** for ongoing updates

## Required Properties

The `Product` type requires:
- **name** (Text): The product's title
- **At least one of**: review, aggregateRating, or offers

## Recommended Properties

- `aggregateRating` (AggregateRating): Overall product ratings
- `offers` (Offer or AggregateOffer): Pricing and availability details
- `review` (Review): Individual product reviews with optional pros/cons

## Technical Requirements

- Focus markup on single products, not product lists
- Use distinct URLs per currency offering
- Include `Car` and `Product` types together for vehicle products
- Avoid `AggregateOffer` for product variants
- For JavaScript-generated markup, ensure adequate server resources

## Content Restrictions

"Content that promotes widely prohibited or regulated goods" is prohibited, including firearms, recreational drugs, tobacco, and gambling products.

## Monitoring

Use Search Console's Product Snippets Report to track performance and identify issues. Allow several days for recrawling and indexing after publishing updates.
