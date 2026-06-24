# aeo-radar - learned rules

Read ALL rules before every run. Append a dated rule whenever Kristine or Sam corrects
a run. Keep it tight - one rule per line, newest at the bottom of its section.

## Seeded rules (build-time, 2026-06-24)

- GOSPEL = official platform docs/releases only (Google, OpenAI, Anthropic, Perplexity,
  Microsoft/Bing, Shopify, llms.txt, schema.org). Everything else is DIRECTIONAL.
- NEVER write, edit, or delete a live `ethan/` file. Stage to `ethan/_inbox/` only.
- A quiet run (nothing new) is a SUCCESS. Never fabricate findings to look busy.
- Dedupe before staging: match `source_url` first, then title, against existing `ethan/**`.
  Do not re-stage docs that have not changed.
- Apify spend per run is hard-capped at `apify_max_run_usd` (default $1.50). Estimate
  first, trim or skip to stay under. Skipped paid source = log + continue, never retry.
- Prefer free channels first (WebSearch/WebFetch, Firecrawl, YouTube RSS+transcript,
  Reddit). Apify is last resort, LinkedIn > X > YouTube.
- YouTube: ingest only videos whose title/description match AEO/AI-search/GEO keywords.
  HubSpot Marketing + Neil Patel channels are general - filter hard.
- Change-feeds are the cheapest signal: diff `search/updates`, `shopify.dev/changelog`,
  `openai.com/news`, `anthropic.com/news`, `blogs.bing.com/webmaster` against last run.
- Every digest line cites a source URL + tier. No source = drop the line.
- Keep the two leader buckets separate in the digest: Shopify/Ecommerce vs General AEO.
- Apify token: read `APIFY_API_TOKEN` from `~/ucl-brain/leadgen/.env`. NEVER write it into
  mentor-library (the repo is pushed to GitHub). Empty token = skip Apify gracefully.
- Apify proxy: ALWAYS `BUYPROXIES94952` (datacenter, $0). NEVER `RESIDENTIAL` (10-50x, blows cap).
- JACKABLE only if newer than `jackable_window_hours` (48h). A stale jack flops - do not flag it.
- Content handoff target is `linkedin-growth-post` (modes: namejack/newsjack/brandjack). Confirm
  it exists before promising a handoff.
- `STATE-OF-AEO.md` is overwritten every run and must lead with "JACKABLE NOW" - it is the
  one file Kristine/Sam open for content. Keep it scannable.
- Depth: a MAJOR item (new doc, policy change, new capability, big framework) ALWAYS gets a
  full DETAILS block in the digest - source link + 3-8 bullet summary of what changed + why +
  SOP impact + link to the full staged capture. Only minor items stay a one-line table row.
  The full lengthy capture always lives in the staged ethan/ source file.
- X scanning: scan by KNOWN HANDLE + platform accounts, NOT open topic search. A raw X search
  for "agentic commerce"/"AI" is dominated by crypto/token hype - apply a relevance filter
  (must mention AEO/AI-search/Shopify/ecommerce; drop crypto/token/web3 terms) before staging.
- Before adding any leader's X, VERIFY they are active (recent posts) + >1000 followers via the
  tweet-scraper. Ethan Smith (@ethan_l_s) is dormant on X -> LinkedIn only. Verify, don't assume.
- @openai / @sama / @AnthropicAI / @perplexity_ai / @Shopify on X = GOSPEL-tier (platform
  announcements), not directional opinion.

## Run corrections (append below, dated)

- 2026-06-24: X "Latest" pull STARVES low-volume leaders - prolific accounts (rustybrick, tobi)
  eat the maxItems cap. Fix: pull X per-handle (or tiny groups), or use sort=Top, not one big
  Latest batch.
- 2026-06-24: @tobi (Tobi Lutke) X is mostly Canadian politics / Le Mans, NOT AEO. Down-rank his
  X; rely on Shopify announcements + his LinkedIn. Low signal-to-noise.
- 2026-06-24: EMAIL must be BRANDED HTML, not plain text. Use email-template.html (cream/tan
  tables #e4d9c2, brown headers #5b4a2e/#6b5a36, green accent #2f7d32, italic angles #8a8170) -
  matches Kristine's client proposal emails. Pass the filled HTML as notify_email.py's 3rd arg.
- 2026-06-24 [RESOLVED]: EMAIL works via Resend (not Gmail SMTP). Key reused from the
  upclicklabs.com app, stored as RESEND_API_KEY in ~/ucl-brain/leadgen/.env; verified domain
  upclicklabs.com so no Gmail app password needed. Send with notify_email.py (uses curl - Resend
  is behind Cloudflare which 403s python-urllib's default UA). The GSC routine uses this same
  Resend backend via the website's /api/gsc/health endpoint.
- 2026-06-24 [RESOLVED]: openai.com/news + perplexity.ai/hub 403 on WebFetch. FIX BAKED IN:
  fall back to Firecrawl v2 (key in /Users/kristineestigoy/leads/.env, see REFERENCE s.10b).
  Validated working - OpenAI 3k chars, Perplexity 35k chars. Never log these as "no news"
  without trying Firecrawl first. (Perplexity "Shopping That Puts You First" = Nov 2025, not new.)
- 2026-06-24: env gotchas - `timeout` is not on macOS (use curl `--max-time`); pass JSON parsers
  as files, not inline python -c with escaped quotes (f-string backslash error).
- 2026-06-24: LinkedIn (harvestapi) batches cleanly - pass all profile URLs in ONE call with
  targetUrls + maxPosts + postedLimit:"month". 15 leaders x 3 posts ran fine (~$0.09).
