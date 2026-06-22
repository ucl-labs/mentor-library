---
title: "Shopify Catalog Mapping (Default Listing / Data Sources) 2026"
source_url: "https://help.shopify.com/en/manual/promoting-marketing/seo/shopify-catalog/default-listing"
source_type: shopify
mentor: "Ethan"
date_synced: "2026-06-22T00:00:00"
note: "Full page via firecrawl. Replaces stale snippet 'shopify-catalog-default-listing.md'."
---

# Shopify Catalog Mapping (Default Listing / Data Sources) 2026

**Source:** Shopify Help Center (official)

You can map your Shopify Catalog product data to preferred sources and influence how products are represented on **AI-driven sales channels**. Shopify Catalog structures product data by: using categories, identifying product attributes, consolidating variants, and grouping identical items - so customers see relevant, unique results with live pricing and stock.

- The **Shopify Catalog Mapping tool** may show **suggested default options**, based on analysis of your store's unique product data.
- **All stores can map**, but most won't need changes. Mapping matters most when a store uses **custom data / grouping logic**: metafields, metaobjects, tag prefixes, or separators/delimiters in product titles.
- Mapping changes how products display on AI platforms **without affecting** the underlying store product structure or data.

## Where it lives
Shopify admin → **Sales channels → Agentic** → **Sources** section → "Review how your product data is sent to the Shopify Catalog for Agentic Channels."

## 1. Set product field mappings
In **Product fields**, set a different **Source** for each (choose from **product attributes, product metafields, or metaobject references**):
- **Product title** → drop-down → select source
- **Product description** → drop-down → select source
- **Product category** → drop-down → select source
Use **Change** in **Product summary** to preview different products, then **Save**.

## 2. Set custom variant grouping
- Default grouping uses your **Shopify Combined Listings** configuration.
- Activate **Custom variant grouping** and pick a **Grouping method**:
  - **Product title** → choose a **Delimiter** (default no-space delimiter; "Other" + custom value if titles use spaces around the delimiter; "None" if no delimiter).
  - **Product metafield** → choose the grouping metafield.
  - **Product tag** → enter the tag prefix in "Tag starts with."
- Grouping with unstructured metafields → no preview results for "Additional products in this group."

## 3. Set product option values
If Custom variant grouping is on, in **Product options** → **Add variant selector**:
- Pick the **Option** (drop-down).
- Confirm/adjust the **Display name** shown to customers.
- Repeat for additional options. Preview, then **Save**.

## AEO takeaway
This is the successor to the old "Catalog Mapping setup" idea. Ingestion is automatic, but **mapping the right sources + grouping logic** is real, defensible work for stores with custom data (metafields/metaobjects/tag-prefix/delimiter titles). Connection is in-admin; the data prep behind it is Admin-API automatable.
