# Generate Structured Data with JavaScript

Source: https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript

## Overview

This Google Search Central guide addresses how to implement structured data using JavaScript on modern websites. According to the documentation, "there are a few things you need to look out for when using JavaScript to generate structured data."

## Two Primary Methods

The guide identifies two common approaches:

1. **Google Tag Manager** - A no-code platform solution
2. **Custom JavaScript** - Direct implementation in your codebase

## Key Implementation Strategies

### Google Tag Manager Approach

The process involves:
- Setting up GTM on your site
- Creating a Custom HTML tag
- Adding supported structured data blocks
- Publishing the container

The documentation emphasizes using variables to extract data from the page rather than duplicating information, noting this "increases the risk of having a mismatch between page content and the structured data."

### Custom JavaScript Method

Developers can generate structured data by:
- Fetching data from APIs
- Creating script elements with type `application/ld+json`
- Appending markup to the DOM

### Server-Side Rendering Alternative

For frameworks supporting server-side rendering, structured data can be included directly in rendered output.

## Testing Requirements

Google provides the Rich Results Test tool to validate implementation. Success means the message "Page is eligible for rich results" appears after testing.

## Important Warning

For Product markup specifically, the guide cautions that dynamic generation "can make Shopping crawls less frequent and less reliable," potentially affecting fast-changing content like pricing.
