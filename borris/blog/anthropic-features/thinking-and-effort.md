<!-- source: effort, adaptive-thinking, fast-mode docs — synced 2026-06-09 -->

# Effort, Adaptive Thinking & Fast Mode (one-model cost/quality dials)

## Effort parameter (`output_config: {effort: ...}`)
Controls how eagerly Claude spends tokens — affects text, tool calls, AND thinking. GA, no beta header. Supported on Opus 4.8/4.7/4.6/4.5, Sonnet 4.6.

| Level | Use for |
|---|---|
| `max` | Frontier problems, deepest reasoning. Expensive; often overkill. |
| `xhigh` | Long-horizon coding/agentic work (30+ min, millions of tokens). Opus 4.8/4.7 only. Recommended start for coding. |
| `high` | Default. Complex reasoning, hard coding, agentic tasks. (= omitting the param.) |
| `medium` | Balanced. **Recommended default for Sonnet 4.6** and most agentic/tool-heavy work. |
| `low` | Speed/cost. Simple classification, lookups, **subagents**, high volume. |

Replaces `budget_tokens` on 4.6+ for controlling thinking depth. Rule: **subagents/routine = low/medium; hard steps = high/xhigh.** Set a large `max_tokens` (start 64k) when using xhigh/max.

**ultracode (Claude Code):** not a new API level — it's `xhigh` effort + standing permission to launch multi-agent workflows (granted via mid-conversation system messages).

## Adaptive thinking (`thinking: {type: "adaptive"}`)
On Opus 4.8/4.7/4.6 and Sonnet 4.6, the model decides *when* to think and how much, based on each turn — so it skips wasted thinking on easy turns. Effort controls the depth. On Opus 4.8, manual `budget_tokens` is rejected (400 error); use adaptive + effort.

## Fast mode (`speed: "fast"`)
Significantly faster output token generation (up to ~2.5x) at premium pricing. Research preview on Opus 4.8/4.7. Claude Code Max-plan users default to fast mode on Opus 4.8.

**Advise like this:** "Run subagents at `effort: low`, the coordinator at `high`." "Turn on adaptive thinking so you only pay for thinking when a step needs it." "Use fast mode only when latency is the bottleneck and budget isn't."
