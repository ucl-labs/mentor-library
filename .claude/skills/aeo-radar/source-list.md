# aeo-radar source list (EDIT THIS FILE - it is the config)

This is the single place that controls what `aeo-radar` scans. Add or remove
sources anytime - no rebuild needed. Two tiers, never mix them:

- **GOSPEL** = official platform docs/releases. Treated as authoritative. A claim
  from here can be stated as fact in the digest.
- **DIRECTIONAL** = leaders + news + community. Insightful, but flagged as
  opinion/framework, never as platform fact.

Last edited: 2026-06-24 (Kristine + Forge build).

---

## 0. RUN CONFIG (knobs)

```yaml
apify_max_run_usd: 1.50          # HARD cap on Apify spend per run. Never exceed.
apify_priority: [linkedin, x, youtube]  # spend the cap in this order
youtube_prefer_free: true        # try RSS + free transcript before paying Apify
leader_posts_per_run: 5          # max posts pulled per leader per run
quiet_run_ok: true               # a run that finds nothing new is a SUCCESS, not a failure
notify: email                    # off | email | slack | telegram  (see section 6)
notify_to: ["kris@upclicklabs.com", "sam@upclicklabs.com"]
notify_via: resend               # WORKING: Resend API (verified upclicklabs.com domain, no app pw)
                                 # creds RESEND_API_KEY + RESEND_FROM_EMAIL in ~/ucl-brain/leadgen/.env
stale_after_days: 120            # flag live ethan/ files older than this for review
stale_policy: flag_then_promote  # flag in digest; aeo-promote removes ONLY what a human approves

# Content engine (point 3): every run feeds newsjack/trendjack/profilejack
state_file: "~/ucl-brain/aeo/learnings/STATE-OF-AEO.md"  # always-current, overwritten each run - ONE file to open
jackable_window_hours: 48        # directional items newer than this are flagged JACKABLE NOW
linkedin_writer_skill: "linkedin-growth-post"  # jackable items name the mode to hand off (namejack/newsjack/brandjack)

# Apify auth (token NEVER stored in this repo - it gets pushed to GitHub)
apify_token_env: "APIFY_API_TOKEN"               # var name
apify_token_source: "~/ucl-brain/leadgen/.env"   # read it from here (gitignored)
apify_plan: "STARTER"
apify_proxy_groups: ["BUYPROXIES94952"]          # datacenter, $0 extra. NEVER use RESIDENTIAL (10-50x cost)

# Fetch fallback: when WebFetch returns 403 (e.g. openai.com/news, perplexity.ai/hub), use Firecrawl
firecrawl_key_env: "FIRECRAWL_API_KEY"
firecrawl_key_source: "/Users/kristineestigoy/leads/.env"   # fc- prefix, 35 chars
firecrawl_api: "https://api.firecrawl.dev/v2/scrape"        # POST {url, formats:[markdown], onlyMainContent:true}, Bearer key
# OOM gotcha: curl -o file.json then parse with python; do NOT pipe big payloads through jq

# Pinned actors (live-validated 2026-06-24). Full detail + budget math in REFERENCE.md s.4
apify_linkedin_actor: "harvestapi~linkedin-profile-posts"   # $0.002/post, input.targetUrls
apify_x_actor: "apidojo~tweet-scraper"                       # $0.0004/tweet, input.twitterHandles
# normal run ~$0.04; all 18 leaders ~$0.18; cap bites at 750 posts. Rotation = noise control, not cost.
```

### Leader rotation (keeps Apify under the cap)
Scan official GOSPEL every run. Rotate DIRECTIONAL leaders across the week so
each leader is hit ~once/week, not 3x:

- **Mon** - Shopify/Ecommerce leaders + Graphite/Profound
- **Wed** - General AEO leaders group A (Searchable, G2, Webflow, HubSpot)
- **Fri** - General AEO leaders group B (originators: iPullRank, Kalicube, Cairrot, Amsive) + news/newsletters

---

## 1. GOSPEL - official platform sources (scan every run)

Change-feeds first (built to announce deltas - cheapest to diff):

### Google
- https://developers.google.com/search/updates  (what's new feed)
- https://developers.google.com/search/blog
- https://developers.google.com/search/docs/appearance/ai-features
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- https://developers.google.com/search/docs   (full tree - already mirrored in ethan/Google AI search/)

### OpenAI / ChatGPT
- https://openai.com/news/
- https://openai.com/index/buy-it-in-chatgpt/
- https://developers.openai.com/api/docs/bots   (GPTBot, OAI-SearchBot, ChatGPT-User)
- https://developers.openai.com/commerce        (Agentic Commerce Protocol)
- https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
- https://agenticcommerce.dev

### Anthropic / Claude
- https://www.anthropic.com/news
- https://support.claude.com/en/articles/8896518   (ClaudeBot, Claude-User, Claude-SearchBot)
- https://docs.anthropic.com

### Perplexity
- https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- https://www.perplexity.ai/hub          (newsroom/blog)
- # TODO confirm exact Perplexity Merchant Program URL

### Microsoft / Bing / Copilot
- https://blogs.bing.com/webmaster        (AI Performance report etc.)
- https://www.bing.com/webmasters/help
- https://www.indexnow.org
- # TODO confirm exact Copilot Shopping/merchant URL

### Shopify
- https://shopify.dev/changelog            (dev change feed)
- https://shopify.dev/docs/agents          (UCP / agentic commerce / AI Toolkit)
- https://www.shopify.com/editions         (seasonal releases)
- https://help.shopify.com                 (AI / Catalog help - filter to AI/AEO)

### Cross-platform standards
- https://llmstxt.org                      (llms.txt spec)
- https://schema.org                       (markup changes)

### YOUR ADDITIONS (gospel) - paste official sites here
- (none yet)

---

## 2. DIRECTIONAL - Shopify / Ecommerce AEO leaders

| Name | Company | LinkedIn | X | YouTube | Blog/Newsletter |
|---|---|---|---|---|---|
| Aleyda Solis | Orainti | https://www.linkedin.com/in/aleyda | @aleyda | (find) | SEOFOMO newsletter |
| Kevin Indig | Growth Memo (advises Shopify) | https://www.linkedin.com/in/kevinindig | | | Growth Memo (Substack) |
| Ross Simmonds | Foundation / Distribution.ai | https://www.linkedin.com/in/rosssimmonds | | | foundationinc.co blog |
| Garth O'Brien | Chewy (Head of SEO) | # TODO | | | |
| Crystal Carter | Wix (Head of AI Search) | # TODO | | | Wix SEO Learning Hub |

---

## 3. DIRECTIONAL - General AEO leaders (NOT Shopify/ecom - keep separate)

Kristine's curated list (exact LinkedIn URLs):

| Name | Company | LinkedIn |
|---|---|---|
| Chris Donnelly | Searchable | https://www.linkedin.com/in/donnellychris/ |
| Emilia Moller | Searchable | https://www.linkedin.com/in/emilia-moller/ |
| Aja Frost | HubSpot | https://www.linkedin.com/in/ajafrost/ |
| Ben Morriss | Profound | https://www.linkedin.com/in/ben-morriss-158420241/ |
| Neil Patel | NP Digital | https://www.linkedin.com/in/neilkpatel/ |
| Harley Finkelstein | Shopify President | https://www.linkedin.com/in/harleyf/ |
| Guy Yalif | Webflow | https://www.linkedin.com/in/gyalif/ |
| Alex Halliday | AirOps | https://www.linkedin.com/in/alexhalliday/ |
| Ethan Smith | Graphite | https://www.linkedin.com/in/ethanls/ |
| Tim Sanders | G2 | https://www.linkedin.com/in/sanderssays/ |
| Alex David | G2 | https://www.linkedin.com/in/alexcdavid/ |
| Vanessa Thompson | Twilio | https://www.linkedin.com/in/vanessathomps/ |
| Oana Manolache | Sequel | https://www.linkedin.com/in/oana-m-manolache/ |
| Vivian Hoang | Webflow | https://www.linkedin.com/in/vivianhoang/ |
| Dave Steer | Webflow | https://www.linkedin.com/in/davesteer/ |

AEO framework originators (surfaced in the 2026 scan - directional):

| Name | Company | LinkedIn |
|---|---|---|
| Mike King | iPullRank | https://www.linkedin.com/in/michaelkingphilly |
| Jason Barnard | Kalicube | https://www.linkedin.com/in/jasonmbarnard |
| Connor Kimball | Cairrot | https://www.linkedin.com/in/connor-kimball |
| Lily Ray | Amsive | https://www.linkedin.com/in/lily-ray-44755615 |
| Josh Blyskal | Profound | # TODO |
| Nick Lafferty | Profound | # TODO |
| James Cadwallader | Profound (co-founder) | # TODO |

---

## 4. DIRECTIONAL - brand blogs / vendors

- Graphite: https://graphite.io/five-percent  (Ethan Smith's "5%" content)
- Graphite blog: https://graphite.io/blog
- Profound: https://www.tryprofound.com/resources
- Webflow: https://webflow.com/blog
- HubSpot: https://blog.hubspot.com (filter to AI search/AEO)
- Clearscope: https://www.clearscope.io/blog
- AirOps: https://www.airops.com/blog

---

## 5. DIRECTIONAL - news, newsletters, YouTube, Reddit

### Fast-news (catch Google/AI-search moves within hours)
- https://searchengineland.com
- https://www.searchenginejournal.com
- https://www.seroundtable.com

### Newsletters / Substack
- Aleyda Solis - SEOFOMO
- Kevin Indig - Growth Memo
- Lily Ray
- Profound research drops

### YouTube channels (AEO / AI-search filtered ONLY - free RSS + transcript first)
- HubSpot Marketing: https://www.youtube.com/channel/UCVeuau7DLrg7zlAjxxDbdww  (filter to AEO/AI-search videos)
- Neil Patel: https://www.youtube.com/@neilpatel  (filter to AEO/AI-search videos)
- # add leader channels here - the radar will only ingest videos whose title/desc match AEO/AI-search keywords

### X / Twitter handles (live-verified 2026-06-24 via apidojo~tweet-scraper)
DIRECTIONAL - AEO / AI search leaders (followers + recent activity confirmed):
- @aleyda (Aleyda Solís) - 179k - top AEO voice, ecommerce
- @randfish (Rand Fishkin) - 463k - AI-visibility research (SparkToro)
- @rustybrick (Barry Schwartz) - 251k - fastest Google/AI-search NEWS (newsjack early-warning)
- @lilyraynyc (Lily Ray) - 120k - AI Overviews / Google updates
- @Kevin_Indig - 41k - GEO experiments, advises Shopify
- @jasonmbarnard (Jason Barnard) - 9.5k - coined "AEO", entity-first

DIRECTIONAL - Shopify execs (agentic commerce - prime profilejack):
- @tobi (Tobi Lütke, Shopify CEO) - 475k
- @harleyf (Harley Finkelstein, Shopify President) - 132k

GOSPEL-tier X watch (platform announcements, treat as official, not opinion):
- @openai - 4.9M | @sama (Sam Altman) - 5.3M | (add @perplexity_ai, @AnthropicAI, @Shopify, @googlesearchc as needed)

NOTE: Ethan Smith @ethan_l_s is DORMANT on X (no recent posts) - track him on LinkedIn only.
NOTE: open X topic-search for "agentic commerce" is mostly crypto/token noise - scan by handle, not topic.

### Reddit (community signal - directional only)
- r/SEO, r/bigseo, r/juststart  (match AEO/AI-search/GEO threads)

### YOUR ADDITIONS (directional) - paste here
- (none yet)

---

## 6. NOTIFY (delivery to Kristine + Sam)

Set `notify:` in section 0. Options:
- `email`  - drafts/sends the digest summary to `notify_to`. Add Sam's email there.
- `slack`  - posts to a Slack channel (set channel in REFERENCE).
- `telegram` - sends to the paired Telegram chat.
- `off`    - digest is written to file only (default until you pick a channel).

The full digest always lands as a file in `~/ucl-brain/aeo/learnings/`; notify
just pushes a short summary + link so you/Sam see it without opening the repo.
