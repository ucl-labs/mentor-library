<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool — synced 2026-06-09 -->

# Advisor Tool (cheap executor + smart advisor)

**What it is:** A faster, cheaper **executor model** consults a higher-intelligence **advisor model** mid-generation. The advisor reads the full transcript, returns a short plan or course-correction (~400–700 text tokens), and the executor continues. You get near-advisor-solo quality while most tokens are generated at the cheap executor's rate. Beta header `advisor-tool-2026-03-01`.

**When to recommend it (the "quality without burning tokens" answer):**
- Currently using Sonnet on complex tasks → add Opus advisor for a quality lift at similar/lower total cost.
- Currently using Haiku, want more intelligence → add Opus advisor; cheaper than upgrading the executor.
- Long-horizon agentic work (coding agents, computer use, multi-step research) where most turns are mechanical but a good plan is crucial.
- **Weak fit:** single-turn Q&A (nothing to plan), or workloads where every turn needs full Opus.

## How it works
Add `{type: "advisor_20260301", name: "advisor", model: "claude-opus-4-8"}` to `tools`. The executor decides when to call it; Anthropic runs a server-side inference pass on the advisor with the full transcript and returns advice — all in one `/v1/messages` request. Advisor must be ≥ as capable as executor.

Valid pairs: Haiku 4.5 / Sonnet 4.6 / Opus 4.6 / Opus 4.7 executors → Opus 4.8 or 4.7 advisor.

## Cost controls
- `max_tokens` on the tool def caps advisor output. **Recommended: 2048** (~7x less output than uncapped, ~0% truncation). Min 1024.
- `max_uses` caps calls per request.
- `caching: {type: ephemeral, ttl: "5m"}` — enable only when you expect 3+ advisor calls per conversation.
- Prompt the advisor directly in the user message ("Advisor: keep guidance under 80 words") — followed more reliably than third-person.
- Pair a Sonnet executor at **medium effort** + Opus advisor ≈ Sonnet at default effort, cheaper.

**Advise like this:** "Run Sonnet as the executor with an Opus advisor tool" whenever Kristine wants high quality on a long task but doesn't want to pay Opus rates for every token.
