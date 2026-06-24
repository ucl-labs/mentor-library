---
title: "OpenAI - Agentic Commerce Protocol & Instant Checkout (Buy it in ChatGPT)"
source_url: "https://developers.openai.com/commerce"
source_type: openai
tier: gospel
mentor: "Ethan"
date_synced: "2026-06-24T15:00:00"
note: "Official OpenAI spec for selling inside ChatGPT - product feeds + agentic checkout + Stripe. Gospel for AI commerce; directly relevant to Shopify DTC AEO."
---

# OpenAI - Agentic Commerce Protocol (ACP) & Instant Checkout

**Source:** developers.openai.com/commerce + openai.com/index/buy-it-in-chatgpt/ (official OpenAI)
**Staged by:** aeo-radar 2026-06-24 (GOSPEL). Reason staged: not previously in KB; official AI-commerce standard.

## What it is
The **Agentic Commerce Protocol (ACP)** is OpenAI's open standard letting AI agents,
people, and businesses complete purchases together. It powers **Instant Checkout** -
buying directly inside ChatGPT. OpenAI has open-sourced the protocol (see
`agenticcommerce.dev` + GitHub) so any merchant/developer can integrate.

## The three flows a merchant must implement
1. **Product feeds** - merchant shares structured product data (CSV/JSON: identifiers,
   descriptions, pricing, inventory, media, fulfillment) so ChatGPT can surface products
   accurately in search + shopping.
2. **Agentic Checkout Spec** - ChatGPT acts as the buyer's agent and renders checkout
   embedded in ChatGPT's UI; it calls the merchant's ACP endpoints to create/update a
   checkout session and share buyer/fulfillment/payment info.
3. **Payment handling** - merchants already on **Stripe** can enable agentic payments in
   roughly one line of code (Stripe co-developed ACP with OpenAI).

## Why it matters for AEO / Shopify DTC
- Appearing in ChatGPT shopping now has an explicit, documented technical contract -
  not just "write good content." Product feed quality + ACP endpoints decide eligibility.
- Pairs with the crawler story (allow **OAI-SearchBot** for ChatGPT search citations;
  `developers.openai.com/api/docs/bots`).
- Complements Shopify's own UCP / agentic-commerce work (`shopify.dev/docs/agents`) -
  cross-reference for Shopify merchants.

## Key official URLs
- Spec + guides: https://developers.openai.com/commerce
- Checkout spec: https://developers.openai.com/commerce/specs/checkout
- Announcement: https://openai.com/index/buy-it-in-chatgpt/
- Open protocol: https://agenticcommerce.dev
- Crawlers (OAI-SearchBot/GPTBot/ChatGPT-User): https://developers.openai.com/api/docs/bots
