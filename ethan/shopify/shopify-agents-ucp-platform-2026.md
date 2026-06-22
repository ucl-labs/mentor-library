---
title: "Shopify Agents Platform & Universal Commerce Protocol (UCP) 2026"
source_url: "https://shopify.dev/docs/agents"
source_type: shopify
mentor: "Ethan"
date_synced: "2026-06-22T00:00:00"
note: "Full page via firecrawl. Dev docs - the protocol layer behind agentic commerce."
---

# Shopify Agents Platform & Universal Commerce Protocol (UCP) 2026

**Source:** shopify.dev (official developer docs)

Build unified agentic experiences that securely act on behalf of buyers with the **Universal Commerce Protocol (UCP)** (ucp.dev) and Shopify's UCP-compliant **MCP servers**. Agents authenticate with Shopify, search the Catalog, build carts and checkouts, and monitor orders.

## Get started (Shopify AI Toolkit + UCP CLI)
- Requires **Node.js 18+**.
- Install the **UCP CLI** globally: `npm install -g @shopify/ucp-cli`.
- Install the **Shopify AI Toolkit** plugin for your AI tool. Supported on **any agent that supports the skills format**. The toolkit's `ucp` skill applies UCP best practices against each merchant's live schema.
- Per-tool install: **Claude Code** (plugin system), **Cursor** (`/add-plugin shopify`), **Gemini CLI** (GitHub extension), **VS Code** (plugin from source).

## The four-stage buyer journey (Shopify's MCP tools implement UCP at each step)
1. **Negotiate & authenticate** - agent presents a profile (hosted at a well-known URL, referenced on every UCP request) so Shopify verifies it and applies rate limits + tool access. **Higher trust tiers** unlock broader access, including **direct checkout completion**.
2. **Discover products** - **Global Catalog** (search products across **every Shopify merchant** from one endpoint) or **Storefront Catalog** (scoped to a single merchant). Fetch variant details to build a cart or hand off to a checkout permalink.
3. **Carts & checkout** - **Cart MCP** builds/iterates carts (line items, localization, totals across turns). **Checkout MCP** converts carts to checkouts; trusted agents complete purchases directly, others hand off to the merchant storefront for payment.
4. **Monitor orders** - **Order MCP** + **order webhooks** (UCP-shaped) track fulfillment, refunds, returns, exchanges, cancellations. `get_order` fetches fresh state on demand ("Where's my order?").

## Universal Cart (early access)
"One Cart, every brand." The **Universal Cart API** lets agents collect items from **any merchant, on or off Shopify**, into a single unified cart, all via UCP.

## MCP server map
- **Catalog MCP** (Global + Storefront) - discovery, image search, product lookup (up to 50 IDs/request).
- **Cart MCP** - build/iterate carts.
- **Checkout MCP** - convert carts → checkouts; direct completion for trusted agents.
- **Order MCP** + **order webhooks** - lifecycle monitoring.

## AEO takeaway
This is the plumbing under "agentic shopping." For UpClick offers it underpins **Agentic Checkout / UCP readiness** (variants, availability, checkout, profile) and the agent-facing files (extend llms.txt/agents.md awareness with the UCP profile concept). Building/managing on this is Claude Code + Shopify-API/CLI work.
