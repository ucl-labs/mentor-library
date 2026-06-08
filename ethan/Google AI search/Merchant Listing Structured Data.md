# Merchant Listing Structured Data Guide

Source: https://developers.google.com/search/docs/appearance/structured-data/merchant-listing

## Overview

Google's documentation explains how to implement `Product` and `Offer` structured data to make items eligible for merchant listing experiences, including shopping knowledge panels and product snippets.

## Key Implementation Steps

The process involves five stages: adding required properties, following guidelines, validating code through the Rich Results Test, deploying pages, and submitting sitemaps for crawling.

## Required Product Properties

Every product must include:
- **name**: The product's title
- **image**: Multiple high-resolution photos (minimum 50K pixels) in 16x9, 4x3, and 1x1 aspect ratios
- **offers**: An `Offer` object for selling the product

## Offer Requirements

The `Offer` object demands either `price` or `priceSpecification.price` (greater than zero for merchant listings) plus `priceCurrency` using ISO 4217 format.

## Pricing Options

Google recognizes three price types:
- **Active prices**: Current sale prices (no special marking)
- **Strikethrough prices**: Original prices marked with `priceType: StrikethroughPrice`
- **Member prices**: Loyalty program pricing using `validForMemberTier` property

## Additional Features

Merchants can include shipping details through `OfferShippingDetails`, return policies via `MerchantReturnPolicy`, certifications like energy ratings, and 3D models in glTF format.

## Content Restrictions

Products promoting "widely prohibited or regulated goods" including firearms, recreational drugs, tobacco, and gambling-related items are not permitted.
