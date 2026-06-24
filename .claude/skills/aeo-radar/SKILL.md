---
name: aeo-radar
description: "AEO/AI-search intelligence radar. Scans official platforms (Google, OpenAI, Anthropic, Perplexity, Microsoft/Bing, Shopify) as GOSPEL and AEO leaders/news as DIRECTIONAL, then STAGES new findings into ethan/_inbox/ and writes a dated 'what changed' digest to ~/ucl-brain/aeo/learnings/. Keeps UpClickLabs + the Ethan mentor KB current on AEO / AI visibility / GEO. Use when the user says 'aeo-radar', 'scan for AEO updates', 'what's new in AI search', 'check AEO sources', or when fired by the Mon/Wed/Fri scheduled task. Does NOT touch the live ethan/ KB - promotion is a separate step (aeo-promote)."
model: sonnet
effort: low
---

# aeo-radar - AEO / AI-search intelligence radar

> **Subagent note:** when an orchestrator spawns this skill as a subagent it MUST
> pass `model: sonnet` (effort `low`). Scheduled runs force Sonnet 4.6 / low for the
> orchestrator and every subagent - never silently upgrade.

Keeps two things current: **UpClickLabs** (via a digest) and the **Ethan mentor KB**
(via staged source files). Ethan is the source of truth Sam + Kristine build all AEO
SOPs from, so this skill is deliberately cautious: it **stages and proposes**, it
never writes the live KB. A human (or `aeo-promote`) commits.

## CRITICAL rules (never break)

1. **Two tiers, never blurred.** Official platform docs/releases = **GOSPEL** (statable
   as fact). Leaders/news/community = **DIRECTIONAL** (framework/opinion - always
   labelled as such). Source of truth for who is which: `source-list.md`.
2. **Never write the live `ethan/` KB.** New files go to `ethan/_inbox/` only.
   Never edit or delete an existing live file. Stale items are **flagged**, not removed.
3. **No fabrication. A quiet run is a SUCCESS.** If nothing new is found, say so. Never
   invent a "finding" to look productive. An empty `staged` list is a valid, passing run.
4. **Apify hard cap.** Total Apify spend per run <= `apify_max_run_usd` (default $1.50).
   Estimate before every Apify call; trim items or skip the channel to stay under.
   A skipped paid source is logged, not retried (graceful degradation).
5. **Dedupe against the existing KB.** Before staging anything, check it is not already
   in `ethan/` (match by `source_url`, then title). Re-runs must not re-stage.
6. **Cite everything.** Every digest line names its source URL + tier. No source = drop it.

## Inputs (read first, in this order)

1. `learned-rules.md` (this folder) - accumulated corrections. Obey them.
2. `source-list.md` (this folder) - the scan config: tiers, leaders, URLs, budget, rotation, notify.
3. The existing KB index - list `ethan/**` filenames + read frontmatter `source_url`/`date_synced`
   to dedupe and to compute staleness. Use:
   `find ethan -name '*.md' -not -path '*/_inbox/*'`
4. The last digest in `~/ucl-brain/aeo/learnings/` (most recent `aeo-radar-*.md`) - so this
   run reports deltas *since then*, not from zero.

## The run (closed loop - detail in REFERENCE.md)

Default mode = `scan`. (Other modes: `rollup` - see bottom.)

1. **Load** inputs above. Resolve today's weekday for leader rotation (`date '+%A'`).
2. **Scan** - GOSPEL every run (change-feeds first, diff vs last digest); DIRECTIONAL per
   today's rotation. Use free tools first (WebSearch/WebFetch, Firecrawl, YouTube RSS,
   Reddit). Use Apify only for LinkedIn/X (and YouTube fallback) under the budget guard.
3. **Tier + dedupe** - tag each candidate gospel/directional; drop anything already in `ethan/`.
4. **Validate gate (deterministic)** - keep a candidate only if: source URL resolves, has a
   date, maps to a target subfolder, and has a tier. Failures are dropped + logged.
5. **Quality-judge gate (spawn ONE sonnet/low subagent)** - for the surviving set: is each
   finding genuinely new + AEO/AI-search relevant (not hype/rehash)? Is the digest useful?
   What obvious source was missed? Max 2 passes. Off-topic/low-value items are cut.
6. **Stage** - write each kept NEW file into `ethan/_inbox/<subfolder>/` with full frontmatter
   (schema below), `tier:` set. Mirror the live folder names (`shopify/`, `blog/`,
   `youtube/`, `Google AI search/`, `pdf/`).
7. **Stale scan** - list live files superseded by a new finding OR older than `stale_after_days`.
   **Flag only.** (`aeo-promote` removes only what a human approves - `stale_policy: flag_then_promote`.)
8. **Tag JACKABLE items (content engine)** - for every DIRECTIONAL finding newer than
   `jackable_window_hours` (48h), tag a jack type + a ready angle:
   - `profilejack` - a named leader posted (e.g. Harley Finkelstein on agentic commerce) -> react to *their* post.
   - `newsjack` - a fresh platform/news item -> post our take within 48h.
   - `trendjack` - something hot on X/Reddit in our space -> mirror to LinkedIn.
   - `brandjack` - a platform move (Shopify/OpenAI/Perplexity) -> analyse it.
   Each jackable item carries: source URL, who/what, the angle, and the handoff mode for
   `linkedin-growth-post` (namejack/newsjack/brandjack). This is what keeps you fingers-on-pulse.
9. **Write outputs** - the digest + `ethan/_inbox/manifest.json` + refresh the always-current
   `STATE-OF-AEO.md` (one file to open). If `notify` is on, render this run into BRANDED HTML
   (fill `email-template.html` with the run data - brand palette in REFERENCE) and send via
   `notify_email.py` (Resend) to `notify_to`.

## Output contract

A run MUST produce exactly:

- **Staged files** in `ethan/_inbox/<subfolder>/*.md` (0 or more), each with frontmatter:
  ```yaml
  ---
  title: "..."
  source_url: "https://..."
  source_type: google | openai | anthropic | perplexity | bing | shopify | blog | youtube | reddit | pdf
  tier: gospel | directional
  mentor: "Ethan"
  date_synced: "YYYY-MM-DDTHH:MM:SS"
  leader: "Name"        # directional only; omit for gospel
  note: "one line - why this matters / framework to steal"
  ---
  ```
- **`ethan/_inbox/manifest.json`** - `{ run_date, weekday, staged: [{path, tier, source_url, why}], stale_flags: [{path, reason}], skipped: [{source, reason}], apify_spend_usd }`.
- **One digest** `~/ucl-brain/aeo/learnings/aeo-radar-YYYY-MM-DD.md` - dated record (format in REFERENCE.md).
- **The always-current state file** `~/ucl-brain/aeo/learnings/STATE-OF-AEO.md` - OVERWRITTEN each
  run. This is the ONE file Kristine/Sam open: top = "🎯 JACKABLE NOW" (fresh items to post about
  today, with angle + handoff mode), then current state of each platform, then what's stale.
  Built to be read straight into a LinkedIn post or YouTube script.

## Verify before declaring done

Self-check (the deterministic pass bar):
- [ ] Every staged file has all required frontmatter fields + a resolving `source_url`.
- [ ] No staged item duplicates an existing live `ethan/` file.
- [ ] Nothing was written outside `ethan/_inbox/` and the digest path.
- [ ] `apify_spend_usd` in the manifest is <= cap.
- [ ] Digest exists, is dated, and every claim cites a source + tier.
- [ ] If nothing new: digest clearly says "no new sources, KB current as of <date>" and
      `staged` is empty (not faked).

Report the result as a short table: staged count (gospel/directional), stale flags,
skipped sources, Apify spend, digest path. Then tell the user: run `aeo-promote` to
review + commit, or open the digest.

## Modes

- **`scan`** (default) - the run above. Also refreshes `STATE-OF-AEO.md`.
- **`jack`** - fast content mode: read the current `STATE-OF-AEO.md` "JACKABLE NOW" list and,
  for a chosen item, hand off to `linkedin-growth-post` with the right mode (namejack for a
  leader post, newsjack for fresh news, brandjack for a platform move) + the source + angle.
  Use when Kristine says "what can I post about today / give me a jack".
- **`rollup [30d|90d]`** - do NOT scan. Read the last N days of `aeo-radar-*.md` digests and
  compile ONE content-ready "State of the Market" brief (grouped: platform launches, framework
  shifts, data points/stats to quote, what's now stale, + a "post ideas" list). The artifact
  for a state-of-the-market video/carousel. Write to
  `~/ucl-brain/aeo/learnings/aeo-state-of-market-YYYY-MM-DD.md`.

## Feedback capture

When Kristine or Sam corrects a run ("that source is dead", "stop staging X", "this was
hype not gospel"), append a dated rule to `learned-rules.md` immediately, then continue.

## Tools

WebSearch, WebFetch, Firecrawl (JS-heavy pages), Reddit MCP, Apify (LinkedIn/X/YouTube,
budget-guarded), Read/Write/Edit/Glob/Grep, Bash (`date`, `find`, `gh`). Notify via the
configured channel (email/Slack/Telegram).
