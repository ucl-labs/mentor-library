# Fact Check (ClaimReview) Markup for Search

Source: https://developers.google.com/search/docs/appearance/structured-data/factcheck

## Overview

Google is phasing out support for `ClaimReview` markup in Google Search, though the Factcheck Explorer Tool continues supporting it. Pages reviewing claims made elsewhere can include this structured data to display fact-check summaries in search results.

## How to Add Structured Data

The implementation process involves five steps:

1. **Add required properties** using the appropriate format and placement
2. **Follow guidelines** outlined in the documentation
3. **Validate code** using the Rich Results Test tool
4. **Test deployment** with the URL Inspection tool
5. **Submit sitemaps** to inform Google of ongoing changes

## Example Implementation

A fact-check page evaluating "the world is flat" would include JSON-LD structured data containing:
- `ClaimReview` type with the claim summary
- `Claim` object detailing the original claim's author and origin
- `Rating` object with truthfulness assessment

The rating scale maps numeric values to text: 1="False" through 5="True"

## Eligibility Requirements

Sites must meet multiple criteria including:

- **Content standards**: Several marked pages, clear claim attribution, traceable analysis with citations
- **Accountability**: Corrections policy, error reporting mechanism, no political entity affiliation
- **Technical**: Only one `ClaimReview` per page, matching structured data to visible content
- **Aggregation**: Publicly available list when combining fact-checks from multiple sources

## Structured Data Types

Three key components are required:

**ClaimReview**: Contains the reviewed claim URL, summary text, rating, and publisher information

**Claim**: Details the original claim's author, publication date, and sources where it appeared

**Rating**: Provides both numeric values (1-5) and human-readable text like "False" or "Mostly true"

## Monitoring with Search Console

Track performance through three phases:
- Initial deployment validation
- Monitoring after template updates
- Periodic traffic analysis using performance reports
