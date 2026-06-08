<!-- source: compaction, context-editing, prompt-caching, task-budgets docs — synced 2026-06-09 -->

# Context Management (long runs without blowing tokens)

When a conversation or agent task gets long, three tools keep it cheap and focused.

## Compaction (server-side, recommended for long runs)
Beta `compact-2026-01-12`. Auto-summarizes older context when input tokens cross a threshold (default 150k, min 50k). The API emits a `compaction` block; on the next request all blocks before it are dropped and the run continues from the summary. Effectively infinite conversations. Supported on Opus 4.8/4.7/4.6, Sonnet 4.6.
- `pause_after_compaction: true` lets you preserve recent messages verbatim before continuing.
- Combine with a compaction counter to enforce a total token budget and gracefully wrap up.
- Cache the system prompt separately so compaction doesn't invalidate it.

## Context editing
Automatically clears stale content as you approach limits:
- `clear_tool_uses` — drop old tool results/calls.
- `clear_thinking` — drop old thinking blocks.

## Prompt caching (cut repeat input cost up to 90%)
- **Automatic caching:** add one `cache_control` field; the system caches the last cacheable block and moves the point forward as the conversation grows. No manual breakpoint management.
- Manual breakpoints still available for fine control. 1-hour cache TTL is GA.
- On Opus 4.8 the minimum cacheable prompt is 1,024 tokens.
- Always cache long system prompts separately from the conversation.

## Task budgets
Cap total token spend on a long agentic run (supported on Opus 4.8). Pair with compaction's counter pattern for hard ceilings.

**Advise like this:** "Enable compaction with a 100k trigger and cache your system prompt" for any long-running agent. This is the difference between a run that costs a little and one that re-pays for a bloated context every single turn.
