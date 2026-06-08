# Discussion Forum (DiscussionForumPosting) Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/discussion-forum

## Overview

This documentation explains how to implement structured data markup for forum-style websites using the `DiscussionForumPosting` schema type. According to Google, this markup helps "Google Search better identify online discussions across the web" and enables features like Discussions and Forums.

## Key Use Cases

The markup applies to "any forum-style site where people collectively share first-hand perspectives." However, if your forum primarily follows a Q&A pattern, the documentation recommends using Q&A markup instead.

## Implementation Approaches

### Threaded Forums

For forums with nested reply structures, comments should nest under related posts in a tree format, with child comments containing their own comment arrays.

### Linear Forums

For sequential reply structures, all comments nest under the original post. Multi-page forums should include the original post URL across all pages.

### Single Post Pages

Use `mainEntity` or `mainEntityOfPage` to identify the primary `DiscussionForumPosting` when a URL focuses on one post.

## Required Properties

**For DiscussionForumPosting:**
- `author` (Person or Organization with name required)
- `datePublished` (ISO 8601 format)
- At least one of: `text`, `image`, or `video`

**For Comments:**
- `author` (Person or Organization)
- `datePublished` (ISO 8601 format)
- At least one of: `text`, `image`, or `video`

## Content Guidelines

Valid uses include community forums, generic forum platforms, and social media where users post and reply. Invalid uses include publisher-authored articles with comments or product reviews.

The documentation states: "Only use `DiscussionForumPosting` markup to describe a user-generated post on a website."

## Technical Guidelines

Google recommends Microdata or RDFa formats to avoid duplicating large text blocks, though JSON-LD remains fully supported.

## Monitoring & Validation

Use Search Console's Rich Result status report to monitor deployment, the Rich Results Test to validate markup, and the URL Inspection tool to verify Google's interpretation of pages.
