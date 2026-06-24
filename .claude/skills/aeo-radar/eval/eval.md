# aeo-radar - eval set (what "good" looks like)

Run these 3 cases to grade the skill. Pass threshold = **3/3 on the checkable bar AND
the quality judge rates the digest useful.** Quiet-run honesty is a HARD fail if violated.

---

## Example 1 - Official release (GOSPEL)

**Input:** Shopify ships a new Editions / OpenAI changes crawler policy / Google updates
the AI-features doc.

**Good output:**
- A staged file in the right subfolder (`shopify/` or `blog/` or `Google AI search/`)
  with full frontmatter, `tier: gospel`, resolving `source_url`, a real date, and a
  `note` saying what changed.
- A GOSPEL row in the digest: source, what changed, why it matters, staged path.
- NOT written to the live KB. Appears in `manifest.staged[]`.

**Checkable:** frontmatter complete? URL resolves? tier=gospel? right folder? digest row
cites URL? staged not live?

---

## Example 2 - Leader insight (DIRECTIONAL)

**Input:** Ethan Smith (Graphite) / Aleyda / Mike King publishes a new AEO framework or
data point.

**Good output:**
- Staged file, `tier: directional`, `leader:` set, `note` = "framework to steal" line.
- A DIRECTIONAL row in the digest under the correct bucket (Shopify/Ecom vs General AEO).
- Clearly labelled as directional/opinion, never as platform fact.

**Checkable:** tier=directional? leader present? correct bucket? "steal this" line present?
cited?

---

## Example 3 - Quiet run (nothing new)

**Input:** A run where every source was already captured / nothing changed since last run.

**Good output:**
- `manifest.staged[]` is EMPTY.
- Digest TL;DR says "No new sources. KB current as of <date>."
- No fabricated findings. No files staged.
- Run still reports cleanly (this is a PASS, not a failure).

**HARD FAIL if:** it invents a "finding", re-stages an unchanged doc, or reports a quiet
run as an error.

---

## Grading method

1. Deterministic check (script-able): for every staged file - frontmatter fields present,
   `source_url` resolves (HTTP 200), `tier` in {gospel, directional}, folder matches
   `source_type`, no duplicate of a live file, nothing written outside `_inbox/` + digest,
   `apify_spend_usd` <= cap.
2. Judge check (LLM): is the digest useful to an AEO practitioner, tiers correct, anything
   obvious missed.
3. Quiet-run honesty: example 3 must not fabricate.

Pass = all deterministic checks green on examples 1-2, example 3 honest, judge = useful.
