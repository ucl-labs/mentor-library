# Employer Aggregate Rating (EmployerAggregateRating) Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/employer-rating

## Overview

The `EmployerAggregateRating` structured data helps sites publishing user-generated employer ratings provide job seekers with organizational evaluations. According to the documentation, this markup enables "prominent brand placement in the enriched job search experience on Google."

## Key Purpose

Sites hosting user ratings about hiring organizations can implement this structured data to display aggregate employer scores in search results, helping job seekers make informed decisions about potential employers.

## Required Properties

The implementation requires three essential fields:

- **itemReviewed**: An Organization object representing the rated company
- **ratingValue**: A numerical quality rating (default 5-point scale)
- **ratingCount or reviewCount**: Total count of user ratings or reviews provided

## Additional Configuration

Implementers can specify custom rating scales using `bestRating` and `worstRating` properties. The documentation notes that "if `bestRating` is omitted, 5 is assumed" and "if `worstRating` is omitted, 1 is assumed."

## Implementation Guidelines

The page emphasizes that "users must be able to post their own ratings on your site and your site must host those user ratings." Additionally, rating counts must reflect actual user submissions, and aggregate scores must accurately derive from provided ratings.

## Migration Note

Google recommends transitioning from review snippet structured data to `EmployerAggregateRating` structured data.
