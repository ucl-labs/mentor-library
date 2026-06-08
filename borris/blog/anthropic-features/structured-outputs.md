<!-- source: build-with-claude/structured-outputs — synced 2026-06-09 -->

# Structured Outputs (guaranteed schema conformance)

**What it is:** Force Claude's output to match a schema you define. GA on the Claude API for Sonnet 4.5/4.6, Opus 4.5+, Haiku 4.5. No beta header. Two modes:
- **JSON outputs** — the response body conforms to your JSON Schema.
- **Strict tool use** — tool-call inputs are validated against the tool's schema (no malformed args).

Config moved to `output_config.format`.

**When to recommend it:** any pipeline step that feeds another system — extraction, classification, data enrichment, anything where you parse Claude's output downstream. Eliminates "the model returned slightly wrong JSON" bugs.

**In workflows/multi-agent:** when one agent's output is another's input, give it a schema so the handoff never breaks. (This is exactly what the Workflow `schema` option does — the agent is forced to return validated structured data.)

**Advise like this:** "Define a schema and turn on structured outputs" whenever the output is consumed by code or a next agent, not read by a human.
