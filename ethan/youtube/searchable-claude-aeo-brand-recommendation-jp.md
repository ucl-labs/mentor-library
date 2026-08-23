---
title: "How to Get Your Brand Recommended in Claude (Searchable webinar)"
source_type: youtube
source_format: webinar
mentor: "Ethan"
speaker: "JP - Head of SEO/AEO, Searchable (~13 years in search)"
publisher: "Searchable"
date_synced: "2026-08-23"
status: current
reliability: DIRECTIONAL
study_basis: "90,000+ Claude sources across 15 industries; ~1,000 unbranded buying questions; measured by driving the Claude UI with an agent and capturing outbound network requests, not API calls"
tags: [claude, per-engine-optimization, parametric-memory, brave, earned-media, entity, measurement]
---

# How to Get Your Brand Recommended in Claude

> **RELIABILITY (2026-08-23).** Single-vendor study by Searchable, unaudited and not peer-reviewed. The
> method is unusually transparent for a vendor deck - they drove the Claude UI with an agent and captured
> the outbound web-search requests rather than inferring from API responses - so the mechanism claims are
> credible, but every percentage here is **one company's measurement**. Use as a working model of how
> Claude behaves; re-verify before putting a number in a client report. The product pitch and the
> "AI Search Accelerator" upsell are stripped out. Speaker is **JP**, Searchable's SEO/AEO lead, **not
> Chris Donnelly**.

**One line:** Claude is an **earned-media engine, not an owned-media engine.** It answers from its own
training memory about half the time, cites your website roughly half as often as ChatGPT does, and when
it does search it leans on **Brave**, not Google.

---

## 1. Why Claude is a different game

Claude returns a short answer naming **three to four brands**. There is no page of ten blue links to
browse past. Being one of those three or four is close to binary.

### The memory split - the central finding

| | Answers from own memory | Performs a web search |
|---|---|---|
| **Claude** | ~52% | ~48% |
| **ChatGPT** | ~10% | ~90% (up to 95%) |

Claude's own memory is its **parametric memory** - the opinion baked in during training. When it is
confident, it never touches the web.

### By query type - where memory dominates

| Query type | Answered from pure memory |
|---|---|
| Advice ("what should I do about X") | up to **98%** |
| Comparison ("which is better X or Y") | **~89%** |
| Reviews / "is this brand any good" | **~85%+** |
| Purchase intent ("what should I buy") | ~27% |
| Local ("what's near me") | **~2%** |

For comparison queries, Claude is **more than 3x as likely as ChatGPT** to answer without searching.
That is the middle of the funnel, where most vendor shortlists get made.

### By industry - memory reliance

| Industry | Answers from memory |
|---|---|
| Software / SaaS | **66%** |
| Health | 63% |
| Home & Garden | (mid) |
| Finance | (mid) |
| Consumer tech | (lower) |
| Local services | **4%** |

**The logic:** the more static and consequential the decision, the more Claude trusts its trained
opinion. A CRM is a once-a-decade decision embedded in company process, so a stable memory is fine.
An iPhone recommendation needs current information. A plumber needs a live lookup (and Claude appends
geography to the query - "best plumber in Manchester" becomes "best plumber in Manchester UK").

Where it does search, memory acts as a **hypothesis that the search then confirms**, not a blank slate.

---

## 2. What Claude actually reads and cites

- When Claude searches, it **reads ~7 pages and quotes ~3** (~43% of what it reads).
- **It cites your own website ~32% of the time. ChatGPT cites it ~61%.** Roughly half.
- Quote rate by industry: Home & Garden 53%, Consumer tech 47%, Finance 43%, Software/SaaS 32%.
- **Query fan-out in Claude is far narrower than ChatGPT's.**

### Reddit - the finding that contradicts most AEO advice

**Claude almost never cites Reddit.** Separately, Reddit's robots.txt now blocks LLM crawlers, and there
has been a broad recent drop in Reddit citations across engines. In ChatGPT, Reddit remains roughly the
#2 source.

**So: Reddit is a ChatGPT/consumer play, not a Claude play.** See the engine-split note in SYMPTOM-MAP -
this does not cancel the Reddit material in the KB, it scopes it.

### YMYL - Claude is the more conservative engine

On "your money or your life" queries (finance, insurance, medical), the two engines invert:

| | Behaviour on health queries |
|---|---|
| **Claude** | Reads ~3 pages, often quotes fewer than one. Leans on trained opinion |
| **ChatGPT** | Searches 70-75% of the time, reads up to **16 pages** |

Trade-off: Claude's rigour means an error in training data can persist; ChatGPT's breadth means it is
more current. Neither is strictly safer.

---

## 3. Brave - the retrieval layer nobody optimises for

When Claude recommends a brand:

| Search engine | Brand appears in its top 10 |
|---|---|
| **Brave** | **63%** |
| Google | 34% |

Where the two lists disagree, Claude follows Brave roughly **6:1**.

**Position inside Brave's top 10 barely matters.** Claude appears to pull the top 10 as a *set* and then
re-shuffle by relevance to the prompt. This is the opposite of ChatGPT, AI Mode and AI Overviews, where
higher Google position raises your odds. So chasing Brave position 1 is not the play - **being anywhere
in Brave's top 10 is.**

Brave has its own index, its own algorithm, and a queryable API you can test against directly.

---

## 4. The shortlist forms before the search

From ~1,000 unbranded buying questions, inspecting the searches the model wrote **for itself**:

- **1 in 6 internal searches already named a specific brand** the user never mentioned.
- Random baseline for a brand appearing in a category it is not a leader in: **2.6%**.
- Examples: "road running shoes for comfort and recovery" -> Asics, Hoka, Brooks, New Balance. "Best
  payroll software" -> Gusto, QuickBooks, ADP. "Ergonomic chairs" -> Herman Miller, Steelcase, Secretlab.

Claude holds an opinion about who the category leaders are before any retrieval runs.

### Who gets missed by parametric memory

1. **New entrants** launched since the last training cut. Testable: search a new company and watch whether
   Claude fires a web search. Search an incumbent and watch it not.
2. **Rebrands and renames** - the model still remembers the old label.
3. **Challengers to a famous incumbent**, including brands sharing a name.
4. **Fast movers** - new products, pivots, new lines not yet absorbed.

This is a gap you can close before the next training round, not a permanent state. Memory refreshes with
model releases; timing is not published.

### What the study can and cannot claim

| Can say | Cannot say |
|---|---|
| The shortlist often forms in memory before any search | That being in memory guarantees you appear in the answer, or appear first |
| You can measure whether you are in it (run prompts, watch whether a web search fires) | That any one tactic reliably puts you there |
| You can shape what the model learns about you | That you can do it overnight |

---

## 5. What to actually do

### The one-line takeaway

> **Your first move is not to write. It is to be written about.**
> On Google you earn a ranking. On Claude you earn a reputation.

A page on your own domain is worth roughly **half** what a mention on a site Claude trusts is worth. That
reweights the entire plan away from publishing more of your own pages and toward brand presence,
partnerships, digital PR, affiliate and merchandising placements, and press.

**The counterweight - be the custodian of your own brand.** Earned sources can only describe you
accurately if you have given them something consistent to learn from. Own media does not win the citation
directly, it feeds the loop that does. Repeat one claim everywhere: *"We are an X platform for Y that does
Z."* Calling yourself a platform here and a tool there blurs the entity.

### Entity hygiene

Strong entity recognition is the mechanism. Consistent NAP (name, address, phone), Wikidata, Wikipedia
where warranted, clean redirects on any rebrand, and the same descriptor across every surface.

### Find the sources Claude uses in your category

1. Run your unbranded prompts.
2. Exclude your own brand from the source set and see what is actually driving the answers.
3. Compare against the source list for your competitors and target the gap. This is the earned-media brief.

### Where to earn placement, by industry

| Industry | Target sources | The move |
|---|---|---|
| Software / SaaS | G2, Capterra | Get into the listicles and roundups |
| Consumer tech | Tom's Guide and similar review sites | Get your product tested - these sites accept testing requests |
| Finance | NerdWallet, Forbes | Editorial and comparison placement |
| Home & Garden | Category review sites, merchandising | Review placement and merchandising |

### Technical - if it cannot be read, it cannot be cited

This fails **silently**. No alarm, no rank drop, you just never appear, or worse, Claude hallucinates
about you.

- **ClaudeBot respects robots.txt.** Check yours.
- **CDN bot rules** (Cloudflare and similar) can block on a prefetch rule with zero signal to you.
- **Heavy client-side JavaScript will not be read.** Use server-side rendering. Gemini/AI Mode is the
  notable exception that renders JS.
- **The test:** ask Claude to read your page. It will often say yes. Then ask it to **fetch the H1 from
  the source and quote it back.** If it cannot, you are blocked.

### What to deprioritise for Claude

- **Reddit** - blocked and barely cited here. Keep it for ChatGPT.
- **Chasing position 1** in Google or Brave for Claude's sake. Top 10 in Brave is the threshold.
- **Over-investing in owned media** as a Claude tactic specifically. It is a ChatGPT tactic (61% vs 32%).
- **Treating local as a web game.** Claude goes to a map surface, not your landing pages.

### Proof that it moves

Searchable restructured one section of their own site into question-shaped pages. First Claude citations
landed **within 4 days**; three weeks later citations were up **as much as 26x** on some prompts.
**[DIRECTIONAL - self-reported]**

---

## 6. Measurement - citation tracking is the wrong metric for Claude

**If about half of answers involve no search at all, there is nothing to cite.** A flat citation count in
Claude may mean you are winning from memory.

**Measure brand recall instead:**
- Ask **unbranded** category questions the way a customer would phrase them.
- Count how often your name comes back.
- **One run is not enough** - answers shuffle. Run each prompt many times (the manual version is ~40 runs
  per question) and measure frequency.
- Recommended prompt split: **90% unbranded, 10% branded.** Branded prompts will always return your brand,
  so they measure nothing.
- Also watch whether a web search fires at all - that tells you if you are in memory or being retrieved.

---

## How UpClickLabs uses this

- **This is the file to read whenever a client's ICP is B2B/enterprise.** Claude behaves so differently
  that a generic AEO deliverable actively misleads.
- **Brave is an unclaimed lever.** Almost nobody is optimising for it. Worth a standalone check in the
  technical audit: are we in Brave's top 10 for our head prompts?
- **The robots.txt / CDN / JS-render check belongs in the Pillar 3 technical audit** with the H1-fetch test
  as the verification step, because it fails silently.
- **The measurement reframe protects the retainer.** If a Claude-focused client is judged on citation
  count, the programme looks dead when it is working. Report unbranded brand recall.
- **"Your first move is not to write, it is to be written about"** is the same argument as
  `frameworks/six-pillar-reputation-system.md` (backlinks 1.9/5, third-party citations and expert
  authorship win) arrived at from completely independent data. That convergence is worth citing in a pitch.
- Pairs with `youtube/searchable-state-of-ai-search-2026.md` (the per-engine overview this drills into) and
  `pdf/the-ai-discovery-playbook-webflow-hubspot.md` (the four-pillar maturity grid).
