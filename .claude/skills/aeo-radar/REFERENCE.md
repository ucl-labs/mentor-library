# aeo-radar - REFERENCE (deep detail)

Read this when you need the exact mechanics. SKILL.md is the runbook; this is the how.

## Contents
1. Folder routing (where a finding gets staged)
2. Frontmatter schema + examples
3. Change-feed diffing (how to detect "new")
4. Apify budget guard (the $1.50 math)
5. Quality-judge gate (the prompt + bound)
6. Stale detection
7. Digest format (the human + video artifact)
8. manifest.json schema
9. Notify
10. Graceful degradation

---

## 1. Folder routing

Stage into `ethan/_inbox/<subfolder>/` mirroring live folders:

| Finding | Subfolder |
|---|---|
| Google Search Central doc/blog/update | `Google AI search/` |
| Shopify (editions, dev, help, catalog) | `shopify/` |
| OpenAI / Anthropic / Perplexity / Bing platform doc or release | `blog/` (prefix filename with platform, e.g. `openai-...`) |
| Leader article / vendor blog / newsletter | `blog/` |
| YouTube video (transcript) | `youtube/` |
| PDF / whitepaper / report | `pdf/` |

Filename: kebab-case slug of the title, e.g. `openai-agentic-commerce-instant-checkout-2026.md`.
Keep it descriptive and dated where the source is a release.

## 2. Frontmatter schema + examples

Match the existing KB exactly, plus `tier`. Gospel example:

```yaml
---
title: "OpenAI - Agentic Commerce Protocol & Instant Checkout"
source_url: "https://developers.openai.com/commerce"
source_type: openai
tier: gospel
mentor: "Ethan"
date_synced: "2026-06-24T10:00:00"
note: "Official ACP spec - product feeds + agentic checkout + Stripe. Gospel for AI commerce."
---
```

Directional example (note `leader:`):

```yaml
---
title: "Graphite - The 5% That Matters in AEO"
source_url: "https://graphite.io/five-percent"
source_type: blog
tier: directional
mentor: "Ethan"
leader: "Ethan Smith"
date_synced: "2026-06-24T10:00:00"
note: "Directional - Ethan Smith's high-impact framework. Adopt as a lens, not gospel."
---
```

Body: a clean markdown capture of the source (scope to the AEO/AI-search relevant parts,
like the Spring '26 file does). Lead with `**Source:** <url> (<what it is>)`.

## 3. Change-feed diffing (detect "new")

The cheap path. For each GOSPEL change-feed:
- Google: `developers.google.com/search/updates` + `/blog`
- Shopify: `shopify.dev/changelog` + `shopify.com/editions`
- OpenAI: `openai.com/news`
- Anthropic: `anthropic.com/news`
- Bing: `blogs.bing.com/webmaster`

Steps:
1. Read the feed, extract dated entries.
2. Compare to the last digest's "as of" date AND to existing `ethan/` `source_url`s.
3. Anything dated after the last run AND not already in the KB = a candidate. Fetch the
   linked page for the full capture only if it survives tiering + dedupe.

For static doc pages (no feed), only re-capture if the page clearly changed since the
matching live file's `date_synced` (e.g. a new section, a changed policy). Do NOT
re-stage unchanged docs - that is noise and a dedupe failure.

## 4. Apify budget guard (the $1.50 math)

**Auth:** read the token from the env var named in `apify_token_env` (`APIFY_API_TOKEN`),
sourced from `apify_token_source` (`~/ucl-brain/leadgen/.env`). The token is NEVER written
into mentor-library (the repo is pushed to GitHub). If the var is empty, ALL Apify channels
skip gracefully and the run continues on free channels.

**Plan + proxy (from leadgen/scale-engine notes):** account is on **STARTER**. Always pass
`proxy: {useApifyProxy: true, apifyProxyGroups: ["BUYPROXIES94952"]}` (datacenter, $0 extra).
**Never use `RESIDENTIAL`** - it costs 10-50x and will blow the $1.50 cap instantly. Use
`fastMode` / 512MB memory where the actor supports it (cheaper, as in the joylo Reddit run).

Apify is the only paid tool. Hard rule: total spend per run <= `apify_max_run_usd`.

Pre-flight, before ANY Apify call:
```
remaining = apify_max_run_usd - spent_so_far
planned_items = leaders_due_today * leader_posts_per_run   # e.g. 3 * 5 = 15
projected = planned_items * actor_unit_price_usd           # unit price stored per actor
```
- If `projected <= remaining`: proceed.
- If `projected > remaining`: trim `planned_items` to `floor(remaining / unit_price)`.
- If even 1 item > remaining: SKIP the channel, log `{source, reason: "budget"}`.

Spend the budget in `apify_priority` order (linkedin -> x -> youtube). Because
`youtube_prefer_free: true`, always try YouTube RSS + free transcript first; only spend
Apify on YouTube if the free fetch failed AND budget remains.

Record actual `apify_spend_usd` in the manifest. When wiring a specific Apify actor,
store its actor id + `unit_price_usd` next to this section so the estimate is real:

```yaml
# Apify actors - PINNED + live-validated 2026-06-24 (account quakier_frog, STARTER)
linkedin_actor:
  id: "harvestapi~linkedin-profile-posts"   # 9.5M runs, no cookies
  unit_price_usd: 0.002                       # per post (+ $0.00005 actor start, negligible)
  unit: "post"
  input: { targetUrls: ["<profile-url>"], maxPosts: 5, postedLimit: "month" }  # postedLimit/postedLimitDate = recency filter
  date_field: "date"                          # ISO date on each post -> use for 48h jackable window
x_actor:
  id: "apidojo~tweet-scraper"                # 149M runs - "Tweet Scraper V2"
  unit_price_usd: 0.0004                       # per tweet (BRONZE/STARTER tier)
  unit: "tweet"
  input: { twitterHandles: ["<handle>"], maxItems: 5, sort: "Latest" }
  date_field: "createdAt"
youtube_actor:
  id: "free: RSS + transcript"               # do NOT pay Apify for YouTube; free path first
  unit_price_usd: 0.00
```

### Budget reality (real prices, cap $1.50/run)
- LinkedIn $0.002/post, X $0.0004/tweet. A normal rotated run (~3 leaders x 5 items each):
  LinkedIn 15 posts = **$0.03**, X 15 tweets = **$0.006** -> ~**$0.04/run**. ~37x under the cap.
- Even scanning ALL ~18 leaders x 5 posts = 90 LinkedIn posts = **$0.18**. So the cap is very safe.
- Hard ceiling check: $1.50 / $0.002 = **750 LinkedIn posts** before the cap bites. Rotation is now
  for freshness/noise, NOT cost - you could scan everyone every run for under $0.25 if you wanted.
- Call actors via REST: `POST https://api.apify.com/v2/acts/{id}/run-sync-get-dataset-items?token=$APIFY_API_TOKEN`
  with `proxy: {useApifyProxy:true, apifyProxyGroups:["BUYPROXIES94952"]}` where supported.

If Apify is not connected/authenticated, ALL Apify channels skip gracefully (logged),
and the run still completes on the free channels.

## 5. Quality-judge gate

After validation, spawn ONE subagent (`model: sonnet`, effort `low`) with the surviving
candidate set + the digest draft. Prompt it to act as a skeptical AEO editor:

> You are grading an AEO intelligence run for an agency whose KB feeds all client SOPs.
> For each candidate: is it genuinely NEW and relevant to AEO / AI-search / GEO (not hype,
> not a rehash of something already known)? Is the tier correct (official=gospel,
> leader=directional)? For the digest: is it useful to a practitioner, and what obvious
> source/release did it MISS? Return: keep[], cut[] (with reason), tier_fixes[], missed[].

Apply keep/cut/tier_fixes. If `missed[]` names a concrete source, do ONE more targeted
fetch for it (this is the only loop-back; max 2 passes total). Then finalize.

## 6. Stale detection

A live file is stale if EITHER:
- a newly staged finding supersedes it (same topic, newer official guidance), OR
- its `date_synced` is older than `stale_after_days` (default 120) AND the topic is
  fast-moving (platform behavior, crawler rules, catalog requirements).

Never delete. Add to `manifest.stale_flags[]` and to the digest's "Review for staleness"
section with the reason. `aeo-promote` is where a human decides.

## 7. Digest format

Write `~/ucl-brain/aeo/learnings/aeo-radar-YYYY-MM-DD.md`:

```markdown
# AEO Radar - {Weekday} {YYYY-MM-DD}

**As of:** {date}  |  **Prev run:** {date of last digest}  |  **Apify spend:** ${x}

## TL;DR (what changed)
- {1-5 bullets: the headline deltas. If none: "No new sources. KB current."}

## GOSPEL - official platform changes
| Source | What changed (1 line) | Why it matters | Staged file |
|---|---|---|---|
(only verified official deltas; each row cites a URL. The table is the scan; the
DETAILS section below carries the depth.)

## DIRECTIONAL - leader & news insights
| Leader/Source | Insight / framework | Steal this | Staged file |
|---|---|---|---|

## DETAILS (depth for every significant item)
For each item that is more than minor, write a full block - this is where "a massive
Google update" gets summarised properly, not in a table cell:

```markdown
### {Platform/Leader} - {title}
- **Source:** {full clickable URL}  ({official doc | release | leader post})
- **Tier:** gospel | directional
- **What changed:**
  - {bullet}  - the actual substance, 3-8 bullets for a big update
  - {bullet}
- **Why it matters for us / clients:** {1-3 lines, Shopify-DTC angle}
- **Action / SOP impact:** {what to change in our process, if any}
- **Full capture:** {staged file path}   ← the lengthy version lives here
```

Rule: a "minor" item (typo fix, unrelated deprecation) stays a single table row. A
"major" item (new doc, policy change, new capability, big framework) gets a full DETAILS
block with multi-bullet summary + source link. When unsure, write the block - more
context is better here.

## Review for staleness (human decides - nothing deleted)
- {live file} - {why it may be stale}

## Skipped (graceful degradation)
- {source} - {reason: budget / blocked / auth}

## Next step
Run `aeo-promote` to review + commit staged files, or open ethan/_inbox/.
```

This file IS the answer to "how do we know what's new" and the raw material for a
"state of the market" video (use `rollup` to compile several).

## 7b. STATE-OF-AEO.md (the one file to open) + content jacking

Overwrite `~/ucl-brain/aeo/learnings/STATE-OF-AEO.md` every run. Built for speed: Kristine
or Sam open ONE file and immediately know what to post. Structure:

```markdown
# State of AEO - updated {YYYY-MM-DD HH:MM}

## 🎯 JACKABLE NOW (post about these today)
| Jack | Who/What | The angle (your take) | Source | Hand off to |
|---|---|---|---|---|
| profilejack | Harley Finkelstein posted on agentic commerce | React: what this signals for DTC AEO | <linkedin url> | linkedin-growth-post namejack |
| newsjack | OpenAI shipped X (within 48h) | Our hot take + what merchants do now | <url> | linkedin-growth-post newsjack |
| trendjack | Hot X/Reddit thread in our space | Mirror to LinkedIn with a POV | <url> | linkedin-growth-post |
| brandjack | Shopify/Perplexity platform move | Analyse the move | <url> | linkedin-growth-post brandjack |

## Current state by platform (gospel)
- Google / OpenAI / Anthropic / Perplexity / Bing / Shopify: 1-2 lines each, latest known.

## Stats & data points to quote (for posts/video)
- {stat} - {source}

## Now stale / changed (don't repeat the old line)
- {old claim} -> {new reality} ({source})
```

Jack types map to `linkedin-growth-post` modes: **profilejack -> namejack** (hijack a named
voice's post), **newsjack -> newsjack** (react to fresh news <48h), **brandjack -> brandjack**
(analyse a platform move), **trendjack -> namejack/newsjack** depending on the source. Only
flag an item JACKABLE if it is newer than `jackable_window_hours` (48h) - stale jacks flop.
The `jack` mode reads this file and triggers the handoff for a chosen item.

## 8. manifest.json schema

```json
{
  "run_date": "2026-06-24",
  "weekday": "Wednesday",
  "prev_digest": "2026-06-22",
  "staged": [{"path": "ethan/_inbox/shopify/...md", "tier": "gospel", "source_url": "...", "why": "..."}],
  "stale_flags": [{"path": "ethan/shopify/...md", "reason": "superseded by ..."}],
  "skipped": [{"source": "linkedin:aleyda", "reason": "budget"}],
  "apify_spend_usd": 0.00
}
```

## 9. Notify

Each run, render the digest into BRANDED HTML (see palette below) by filling
`email-template.html` with this run's data, save it (e.g. /tmp/aeo-email.html), then:
`python3 notify_email.py <digest_path> "kris@upclicklabs.com,sam@upclicklabs.com" /tmp/aeo-email.html "<subject>"`
The 3rd arg = HTML file (sent as the rich `html` body); plain digest is the text fallback.

### Brand palette (matches Kristine's client emails - keep consistent)
- Body: Arial/Helvetica, color `#3a3a3a`, 15px, line-height 1.55, max-width 720px.
- Tables: `border:1px solid #e4d9c2; border-radius:8px; overflow:hidden; border-collapse:collapse`.
- Section header rows (colspan): bold, 11px, `letter-spacing:1.5px`, color `#6b5a36`.
- Column headers `th`: color `#5b4a2e`, `border-bottom:1px solid #e4d9c2`.
- Row borders: `border-bottom:1px solid #efe7d6`. Italic sub-text/angles: `#8a8170` 12px italic.
- GREEN accent (jack-type, NEW, gospel, links, highlights): `#2f7d32`. Muted/dash: `#c2b79e`.
  Small note text: `#7a715d`. Stale flag: amber `#c2730f`.
- No gradients/shadows. `email-template.html` in this folder is the canonical worked example.

If `notify` != off, after writing the digest run:
`python3 notify_email.py <digest_or_state_path> "kris@upclicklabs.com,sam@upclicklabs.com"`

- **PRIMARY: Resend** (validated working 2026-06-24, exit 0). Same provider the upclicklabs.com
  app uses, on the verified `upclicklabs.com` domain - NO Gmail app password needed. Key =
  `RESEND_API_KEY` + `RESEND_FROM_EMAIL` in `~/ucl-brain/leadgen/.env`.
  GOTCHA: Resend is behind Cloudflare which 403s the default `python-urllib` user-agent -
  the script sends via `curl` (subprocess), not urllib. Don't "fix" it back to urllib.
- FALLBACK: Gmail SMTP if `GMAIL_APP_PASSWORD` set; else Gmail MCP draft; else exit 2 (log+skip).
- `slack` / `telegram` - post the summary instead, if chosen.

The full digest is always the file; notify is just the ping so Kristine + Sam see it.

## 10b. Fetch fallback - 403/blocked sources via Firecrawl (REQUIRED, not optional)

Some gospel sources block plain WebFetch with 403 (confirmed: `openai.com/news`,
`perplexity.ai/hub`). Do NOT record these as "no news" - they are blocked, not empty.
Fallback chain for any gospel URL: **WebFetch -> (on 403/empty) Firecrawl v2 -> (still fails) log skip.**

Firecrawl call (validated 2026-06-24):
```bash
FCKEY=$(grep -E '^FIRECRAWL_API_KEY' /Users/kristineestigoy/leads/.env | cut -d= -f2 | tr -d '"'"' ")
curl -s --max-time 150 -o /tmp/fc.json -X POST "https://api.firecrawl.dev/v2/scrape" \
  -H "Authorization: Bearer $FCKEY" -H "Content-Type: application/json" \
  -d '{"url":"<URL>","formats":["markdown"],"onlyMainContent":true}'
# then parse /tmp/fc.json with python (data.markdown). OOM: never pipe big payloads through jq.
```
To enumerate a feed then drill into a post: scrape the index, regex the post URLs from the
markdown, scrape the chosen post for the full capture + metadata.title/publishedTime.

## 10. Graceful degradation (scheduled-run default)

Any failed source (timeout, block, auth, budget) = log to `skipped[]` and CONTINUE.
A source is only "skipped" AFTER the WebFetch->Firecrawl fallback also fails.
Never retry in a loop, never escalate, never abort the whole run for one dead source.
A partial run that writes a digest is a success.
