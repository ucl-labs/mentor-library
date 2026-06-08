# Q&A (QAPage) Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/qapage

## Overview

This Google Search Central documentation covers the QAPage schema for marking up question-and-answer content to enable rich results in search.

## Key Purpose

According to the page, "Q&A pages are web pages that contain data in a question and answer format, which is one question followed by its answers." Properly marked pages become eligible for enhanced search result displays.

## Implementation Steps

1. Add required properties using schema.org markup
2. Follow content guidelines
3. Validate with Rich Results Test
4. Deploy and test with URL Inspection tool
5. Submit sitemaps for ongoing updates

## Critical Guidelines

The page specifies several restrictions on QAPage usage:

- "Only use the `QAPage` markup if your page has information in a question and answer format, which is one question followed by its answers."
- Users must be able to submit answers (distinguishing it from FAQ pages)
- Invalid uses include product pages with multiple Q&As and single-answer content
- Content cannot be obscene, sexually explicit, graphically violent, or promote illegal activities

## Required Properties

**For QAPage:**
- `mainEntity`: Must contain exactly one Question

**For Question:**
- `answerCount`: Total number of answers
- At least one `acceptedAnswer` or `suggestedAnswer`
- `name`: The question text

**For Answer:**
- `text`: Complete answer content

## Monitoring

Use Search Console to track rich result performance and troubleshoot implementation issues.
