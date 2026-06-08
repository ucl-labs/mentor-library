# Merchant Return Policy Structured Data (MerchantReturnPolicy)

Source: https://developers.google.com/search/docs/appearance/structured-data/return-policy

## Overview

The `MerchantReturnPolicy` structured data type enables merchants to communicate return policies to Google Search. When implemented, this information can appear alongside products and in knowledge panels within search results.

According to Google's documentation, "When you add `MerchantReturnPolicy` structured data to your site, Google Search can use this information to display return policies alongside your products and in knowledge panels in Search results."

## Implementation Approaches

There are two primary ways to specify return policies:

1. **Organization-level**: A standard policy applicable to most or all products, specified using the `hasMerchantReturnPolicy` property nested under the `Organization` type

2. **Product-level**: Override policies for specific items, specified under the `Offer` type (supporting a limited property subset)

## Key Configuration Steps

- Adding required properties to your markup
- Following specific guidelines for your use case
- Validating code using Google's Rich Results Test
- Testing with the URL Inspection tool
- Submitting sitemaps for recrawl notification

## Essential Properties

**Required options** (select one):
- **Option A**: Specify `applicableCountry` and `returnPolicyCategory`
- **Option B**: Provide `merchantReturnLink` (URL to return policy page)

**For finite return windows**, the `merchantReturnDays` property becomes mandatory when using `MerchantReturnFiniteReturnWindow`.

## Return Policy Categories

Three enumeration values exist:
- `MerchantReturnFiniteReturnWindow`: Fixed return period
- `MerchantReturnNotPermitted`: No returns allowed
- `MerchantReturnUnlimitedWindow`: Indefinite return timeframe

## Additional Supported Details

Markup can specify:
- Return methods (mail, in-store, kiosk)
- Fee structures (free, customer responsibility, merchant-charged)
- Refund types (full monetary, store credit, exchange)
- Item condition acceptance (new, used, damaged, refurbished)
- Return label sourcing mechanisms
- Seasonal overrides for holiday periods

## Alternative Configuration Method

For complex or frequently-changing policies, merchants can configure return settings within Google Merchant Center or Search Console instead of markup. The platform uses a precedence hierarchy where Merchant Center settings override markup-based specifications.
