# Loyalty Program (MemberProgram) Structured Data

Source: https://developers.google.com/search/docs/appearance/structured-data/loyalty-program

## Overview

This Google Search Central documentation explains how merchants can implement `MemberProgram` structured data to display loyalty benefits in search results. The feature allows businesses to showcase membership tiers, benefits, and requirements directly in Google Search.

## Key Information

**Feature Availability:** Loyalty program information displays in Australia, Brazil, Canada, France, Germany, Mexico, the UK, and the US across desktop and mobile.

**Core Purpose:** When you add `MemberProgram` structured data to your site, "Google Search can use this information to display loyalty benefits with your products" in search results and knowledge panels.

## Implementation Steps

1. Add required properties following the appropriate format
2. Follow guidelines for structured data
3. Validate using Rich Results Test
4. Deploy and test with URL Inspection tool
5. Submit sitemap for ongoing updates

## Structured Data Components

### MemberProgram (Required Properties)

- **description:** Text explaining primary member benefits
- **hasTiers:** At least one tier required
- **name:** Program name

### MemberProgramTier (Required Properties)

- **hasTierBenefit:** Specifies benefits (loyalty points or member pricing)
- **name:** Tier name (e.g., "silver," "gold")

### Optional Features

Tiers can include requirements (credit cards, minimum spending, fees) and earn rates for loyalty points.

## Key Requirement

Nest `MemberProgram` markup under the `Organization` structured data type on pages containing business administrative details and policies.

## Alternative Approach

Merchants with Google Merchant Center accounts can configure loyalty programs directly through that platform instead of using markup.
