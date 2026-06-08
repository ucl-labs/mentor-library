# Movie Carousel Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/movie

## Overview

This guide explains how to mark up movie lists with structured data so they can appear as rich results in Google Search, specifically in carousel format on mobile devices.

## Key Features

- **Available on**: Mobile devices only
- **Purpose**: Enable users to explore movies on Google Search in new ways
- **Displayable information**: Movie titles, directors, images

## How to Add Structured Data

The implementation process involves five main steps:

1. **Add required properties** using JSON-LD format
2. **Follow guidelines** specific to carousel and movies
3. **Validate** using the Rich Results Test tool
4. **Test deployment** using URL Inspection tool
5. **Submit sitemap** for ongoing updates

## Two Implementation Approaches

### Approach 1: Summary + Details Pages

A summary page lists movies briefly, linking to individual detail pages focused on one movie each.

### Approach 2: All-in-One Page

A single page contains complete information about all listed movies.

## Required Properties

For the `Movie` type, the following are mandatory:

- **`image`**: URL or ImageObject (must be .jpg, .png, or .gif; 6:9 aspect ratio required)
- **`name`**: Text field containing the movie title

## Recommended Properties

- **`aggregateRating`**: AggregateRating object for average review scores
- **`dateCreated`**: Movie release date
- **`director`**: Person object with director's name
- **`review`**: Nested Review object with review details

## Important Guidelines

According to the documentation, "If Google detects that some of the markup on your pages may be using techniques that are outside our structured data guidelines, your site may receive a manual action."
