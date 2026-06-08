# Dynamic Rendering as a Workaround

Source: https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering

## Overview

The documentation establishes that "Dynamic rendering was a workaround and not a long-term solution for problems with JavaScript-generated content in search engines." Google recommends adopting server-side rendering, static rendering, or hydration instead.

## Key Concepts

### Client-Side Rendering Context

Google's crawlers can detect JavaScript-loaded content, though some limitations exist. The document notes that "Other search engines may choose to ignore JavaScript and won't see JavaScript-generated content."

### What Dynamic Rendering Is

A dynamic rendering server identifies bot requests and routes them to a rendering service that generates static HTML versions, while users receive the client-side rendered version.

## Sites That Might Use Dynamic Rendering

Dynamic rendering applies to scenarios involving "indexable, public JavaScript-generated content that changes rapidly, or content that uses JavaScript features that aren't supported by the crawlers."

## How It Works

The system detects crawler user agents and serves appropriately formatted content. The documentation includes a diagram illustrating how servers route requests differently for browsers versus crawlers.

## Important Distinction: Not Cloaking

The guide clarifies that "Googlebot generally doesn't consider dynamic rendering as cloaking" when similar content is served. However, serving "completely different content to users and crawlers can be considered cloaking."
