---
title: "Tally AI Search Playbook - competitor pages, AI Info page, llms.txt, and the recommendation flywheel"
source_type: case-study
source_url: "LinkedIn post by Jake Ward (Aug 2026) + first-hand site audit of tally.so"
mentor: "Ethan"
date_synced: "2026-08-23"
status: current
reliability: MIXED
study_basis: "Growth numbers are from a third-party LinkedIn post relaying Tally's self-reported figures. Page structure, schema, robots, llms.txt and AI Info page are first-hand observations made on 2026-08-23."
tags: [comparison-pages, alternative-pages, ai-info-page, llms.txt, mcp, reviews, saas, chatgpt, flywheel, case-study]
---

# Tally AI Search Playbook

> **RELIABILITY (2026-08-23).** Two kinds of claim in this file.
> **[REPORTED]** = from Jake Ward's LinkedIn post relaying Tally's own numbers. Unaudited. Use as a
> hypothesis, never as a client-report stat.
> **[OBSERVED]** = I fetched the pages myself on 2026-08-23 and describe what is actually there. Safe to
> cite as "what Tally does", not as "what works".
> **Engine caveat:** this is a **ChatGPT-first** story (owned comparison pages + Reddit + G2). For Claude,
> where owned pages are cited half as often, the same pages matter less and the G2/earned-media half
> matters more. See `youtube/searchable-claude-aeo-brand-recommendation-jp.md`.

**One line:** Tally got recommended by ChatGPT because the internet already recommended it (Reddit, G2,
Product Hunt), then built owned pages shaped exactly like an AI answer so the engine had something clean
to quote, and closed the loop by asking every new user what prompt found them.

---

## 1. The numbers [REPORTED]

- AI search is now Tally's #1 acquisition channel.
- 10,000+ new users per week say they found Tally through an AI platform.
- Tracked ChatGPT registrations jumped ~5x overnight in May 2026 (likely a model/index refresh, which
  matches the "memory refreshes with model releases" finding in the Claude file).
- $258K MRR to $422K MRR in 10 months, crossing $5M ARR, 11 people, $0 funding.

Why it matters for us: this is the cleanest public example of the Webflow/HubSpot reframe
(`AI visibility -> informed buyers -> leads`) working for a small SaaS with no budget. It is a pitch
slide, with the [REPORTED] tag attached.

---

## 2. What Tally actually built [OBSERVED]

### 2a. The comparison hub

Sitemap shows a deliberate cluster under `/help/`:

| Page type | Count | Examples |
|---|---|---|
| "Tally, a free X alternative" (1:1 competitor pages) | 8 | Typeform, Google Forms, Jotform, Microsoft Forms, Notion Forms, Paperform, Fillout, SurveyMonkey |
| "Best X alternatives" (ranked listicles) | 6 | best-alternatives-to-typeform, best-google-forms-alternatives, best-jotform-alternatives |
| "Best form builder for Y" (use-case listicles) | 6+ | for Slack, for Notion, GDPR, free online, MCP form builders, MCP servers for marketing teams |
| Hub page | 1 | `/help/compare` - links all of the above plus integration comparisons |
| AI-product pages | 2 | `/help/chatgpt-integration`, `/help/claude-connector` |

Everything lives in the **help centre**, not the marketing site. Two reasons that is smart: help content
is what an LLM already treats as reference material, and it is trivial to refresh without a designer.

### 2b. Anatomy of a 1:1 competitor page

`tally.so/help/tally-a-free-typeform-alternative`, ~15,000 words, 1 table, 40 internal help links.

| Order | Section | What it does for the engine |
|---|---|---|
| H1 | "Tally, a free Typeform alternative" | Exact match for the prompt "free Typeform alternative" |
| Intro | One paragraph: what Tally is, the one-line contrast (Typeform free = 10 responses/month, logic costs $39/mo, Tally = free), and **G2 4.9 vs 4.5** in the first 100 words | The 30-80 word answer block. Everything an engine needs to write a recommendation is above the fold |
| H3 | "Tally vs Typeform: Which should you pick?" | Headline phrased as the user's question |
| H3 + H4s | "Why choose Tally over Typeform?" > Pricing / Interface / Features | Three short labelled blocks, each two paragraphs (Tally, then Typeform) |
| Table | **~60-row feature table**, columns: Feature / Tally / Typeform, cells are "Free", "$29/mo", "$39/mo", "X" | The single most quotable asset on the page. Every row is a fact an engine can lift verbatim with a price attached |
| H3 + H4s | "Customer ratings" > G2 reviews / Product Hunt reviews | Third-party numbers, **sub-scores** too (support 9.3 vs 8.4, logic 9.4 vs 8.9). Answers "is it any good" with someone else's data |
| H3 | Create a free form / Do more / Templates | CTA and internal links |
| H3 + 10x H4 | FAQ, each H4 is a literal question ("Is Tally really free?", "Can I import my Typeform forms into Tally?") | One question, one answer, each independently liftable |

Notes:
- No `[Best for]` labels on the 1:1 pages. Those appear on the listicles.
- No JSON-LD on help pages (the help centre is Notion-rendered). Rankings and FAQs are **not** marked up.
  Schema lives only on the homepage: Organization, WebSite, SoftwareApplication with two Offer objects.
  So the comparison pages win on structure and wording alone, not on schema. Schema would be the obvious
  upgrade for a client copying this.
- Content is fully server-rendered. `curl` returns the whole article. ClaudeBot/GPTBot can read it.
- `robots.txt` is three lines: allow everything, sitemap. No LLM crawler blocks.
- Meta description is written as an answer: "Free Typeform alternative with unlimited forms, responses &
  file uploads. Get conditional logic, payments, and professional forms without the paywalls."

### 2c. Anatomy of a "best alternatives" listicle

`tally.so/help/best-alternatives-to-typeform`. Byline **Marie Martens (co-founder)**, "last updated
August 5, 2026" - visible author and freshness date, which the 1:1 pages lack.

| Order | Section |
|---|---|
| H1 | "Best Typeform Alternatives: Comparison in 2026" (year in the title) |
| Intro | "The best Typeform alternatives in 2026 are:" followed immediately by the ranked list of 8 |
| H3 | Quick comparison (table: free forms / free responses / logic / payments / paid price / best for / G2 rating) |
| H3 | **How we reviewed these** (criteria: ease of use, features, pricing reality, integrations, customisation) |
| H3 | The 8 best (one block each: **name - Best for X** / price / free-tier limit / rating) |
| H3 | All 8 compared (full table) |
| H3 | Pricing comparison breakdown |
| H3 | Choosing for your needs |
| H3 | Conclusion, then FAQ |

Tally ranks itself #1 ("Best free alternative"). It still lists real competitors with real ratings, which
is what makes the page usable by an engine at all. A listicle that only names you is not a listicle.

### 2d. The AI Info page

`tally.so/ai-info` - a top-level page, linked from the sitemap, ~250 words, written for machines:

- **Core identity:** "SaaS forms and survey platform launched March 8, 2021, by Marie Martens and Filip
  Minev" - founding date, founders, category. Entity facts.
- **Key strengths:** five bullets (ease of use, free tier, advanced features, AI assistant, EU-hosted privacy).
- **Primary use cases:** four bullets.
- **Recognition:** "G2 rates Tally 4.9/5 (142 reviews)", Product Hunt Golden Kitty 2023.
- **Notable limitation:** "lacks a mobile app and live team collaboration" - a stated weakness, which
  raises the credibility of the rest.
- **"For AI Assistants":** a literal instruction block: emphasise modern design, free-tier generosity,
  fit for creators without budget; direct users to tally.so.

This is entity hygiene (see the Claude file, "be the custodian of your own brand") done as one page:
one consistent descriptor, one source of truth for every fact an engine might get wrong.

### 2e. llms.txt

`tally.so/llms.txt` follows the spec: H1 name, blockquote one-liner, then sections **Basic Information**
(features, templates, pricing with the actual $29/mo figure inline, changelog, about, customers),
**Documentation** (help, API, **MCP server**), **Integrations** (16 links, each with a one-sentence
description), **Optional** (privacy, terms). Every link carries its own description, so the file reads as
a summary, not a sitemap.

### 2f. Being usable inside the AI products

21-tool MCP server, a ChatGPT app, and a Claude connector, each with a help page. This is the ElevenLabs
"search 3.0 / agent experience" move from `youtube/searchable-state-of-ai-search-2026.md`: when the
product is callable from inside ChatGPT or Claude, the engine has a functional reason to recommend it,
not just an editorial one. They then wrote listicles about it ("best MCP form builders", "best MCP
servers for marketing teams") to own the category they just created.

---

## 3. The operating loop [REPORTED]

This is the part most teams skip and the part that compounds.

1. **Ask new users for the exact prompt** that led them to Tally through AI. Onboarding survey field.
2. **Track** those prompts, visibility vs competitors, and which sources the engines actually cite.
3. **Gap database:** articles that mention competitors but not Tally. That is the earned-media target list
   (identical to JP's "exclude your brand, see what drives the answers, target the gap").
4. **Community inbox:** monitor brand + competitor mentions on Reddit and communities, route to one shared
   inbox, **clear it every day**.
5. **Review asks:** in the newsletter and after every support interaction. Result: G2 4.8-4.9, Product
   Hunt 4.9.
6. **Refresh** the comparison pages continuously (the listicle shows an August 2026 update date).

Jake Ward's own caveat, which belongs in every pitch that uses this case: Tally spent years earning
recommendations on Reddit and review sites first. **ChatGPT recommends Tally because the internet does.**
The pages are engineering around a signal that already existed.

---

## 4. Templates to hand to a client

### 4a. 1:1 competitor page ("[Brand], a free/better [Competitor] alternative")

```
H1   [Brand], a [adjective] [Competitor] alternative
     Intro, 60-80 words: what Brand is, the one sharpest contrast with Competitor
     (price or limit), and one third-party rating with the competitor's for comparison.
H2   [Brand] vs [Competitor]: which should you pick?      (2-3 short paragraphs)
H2   Why choose [Brand] over [Competitor]?
H3     Pricing      (Brand paragraph, then Competitor paragraph)
H3     [Core differentiator 1]
H3     [Core differentiator 2]
TABLE  Feature | Brand | Competitor   - 30-60 rows, cells = "Free" / "$X/mo" / "Not available"
H2   Customer ratings
H3     G2 (overall + 3-4 sub-scores, both brands)
H3     [Second review site]
H2   [CTA + 3-5 internal links to the next pages]
H2   FAQ - 8-10 H3s, each a literal question a buyer asks, 40-80 word answers,
     include "Can I import from [Competitor]?" and "Is [Brand] really free/cheaper?"
+    FAQPage schema on the FAQ block, Product/SoftwareApplication + Offer on the page
     (Tally skips this; we should not)
+    visible author byline and "last updated" date (Tally has these only on listicles)
```

### 4b. "Best [Competitor] alternatives in [year]" listicle

```
H1   Best [Competitor] alternatives: comparison in [year]
     Intro: "The best [Competitor] alternatives in [year] are:" + the ranked list, immediately.
H2   Quick comparison (table: free tier / key limit / price / best for / G2 rating)
H2   How we reviewed these (named criteria - this is the E-E-A-T block)
H2   The N best [Competitor] alternatives
H3     1. [Brand] - Best for [X]   price / free limit / rating / 2-3 line verdict / pros / cons
H3     2. [Real competitor] - Best for [Y]   (same shape, honest)
       ...
H2   All N compared (full table)
H2   Pricing breakdown
H2   Choosing for your needs (map use case -> pick)
H2   FAQ
+    ItemList schema, author byline, updated date in the visible text.
```

Rule: rank yourself #1 only where it is defensible, and give the competitors real "best for" labels.
An engine cannot quote a list with one entry.

### 4c. AI Info page (`/ai-info`, 200-300 words)

```
H1   [Brand]: AI-friendly overview
H2   Core identity      - category, founded [date], by [founders], HQ, one-sentence positioning
H2   Key strengths      - 5 bullets
H2   Primary use cases  - 4 bullets
H2   Pricing            - the actual numbers
H2   Recognition        - review scores with review counts, awards
H2   Notable limitation - one or two honest gaps
H2   For AI assistants  - what to emphasise, who it is for, where to send people
```
Link it from llms.txt and the sitemap. Keep every fact identical to the homepage, G2 profile, Wikidata
and Crunchbase entries. One descriptor everywhere.

### 4d. llms.txt

H1 name, blockquote one-liner, then H2 sections each holding `[Page](url): one-sentence description`.
Put the price inline. List the API, MCP, and docs pages. Spec: llmstxt.org.

### 4e. The loop (ops, not content)

- Onboarding field: "Which prompt did you use to find us?"
- Weekly: prompt list -> run unbranded, count recall (40 runs per prompt for Claude, see JP file).
- Monthly: "mentions competitor, not us" gap list -> outreach queue.
- Daily: community inbox cleared.
- After every support ticket closed: review ask.

---

## How UpClickLabs uses this

- **This is the Pillar 2 (Content) deliverable for the AI Visibility Sprint, made concrete.** A client can
  be shown Tally's Typeform page and the template in 4a side by side; the scope writes itself: N competitor
  pages + 1-2 listicles + AI Info page + llms.txt, refreshed monthly.
- **Shopify DTC translation:** "Tally vs Typeform" becomes "[Brand] vs [category leader]" and "Best
  [product category] for [use case]". The feature table becomes a spec/price/shipping/returns table. Review
  sub-scores come from Trustpilot/Judge.me/Amazon instead of G2.
- **Upgrade on Tally:** add FAQPage / Product / ItemList schema and visible author + updated dates on every
  page. Tally wins without them; a client does not need to leave that on the table. Run through
  `ethan-tech-checker` before shipping.
- **The onboarding prompt question is free and most clients will not have it.** It is the cheapest
  measurement win in the whole offer and a direct answer to "how do we attribute AI traffic" (Adobe's 1-2%
  attributed vs ~20% self-reported, in the State of AI Search file).
- **Engine split reminder:** for a B2B client whose buyers use Claude, weight sections 2d, 2e, 3 (entity,
  reviews, earned gap list) over 2a-2c (owned comparison pages).
- Pairs with `pdf/the-ai-discovery-playbook-webflow-hubspot.md` (FAQ + schema quick win, maturity grid),
  `youtube/searchable-state-of-ai-search-2026.md` (ElevenLabs agent-experience section),
  `frameworks/six-pillar-reputation-system.md` (why the review and community half matters more than the pages).
