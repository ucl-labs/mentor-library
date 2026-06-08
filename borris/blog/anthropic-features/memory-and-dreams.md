<!-- source: https://platform.claude.com/docs/en/managed-agents/memory + /dreams — synced 2026-06-09 -->

# Memory Stores & Dreams (cross-session memory)

## Memory stores
Each Managed Agent session starts fresh by default — when it ends, state is gone. A **memory store** lets the agent carry information across sessions: user prefs, project conventions, prior mistakes, domain context.

- A store is a workspace-scoped collection of text docs. Attached at session creation in `resources[]`, it mounts as a directory under `/mnt/memory/`. The agent reads/writes it with normal file tools (requires the agent toolset).
- Each memory addressed by path; every change creates an immutable **version** (audit trail + point-in-time recovery, 30-day retention).
- Limits: 100 kB (~25k tokens) per memory, 2,000 memories per store, **8 stores per session**.
- **Security:** defaults to `read_write`. If the agent ingests untrusted input, a prompt injection could poison memory that later sessions trust. Use `read_only` for reference material.
- Best practice: many small focused files, not few big ones. Use separate stores per user / shared knowledge / project.

## Dreams — the "dreaming agents" feature
This is the official version of the viral X post about agents that "dream" to consolidate memory. **It's real and documented.** Research preview; beta headers `managed-agents-2026-04-01` + `dreaming-2026-04-21`.

**What it does:** A dream is an async job that reads an existing memory store + 1–100 past session transcripts, then produces a **new, reorganized** store: duplicates merged, stale/contradicted entries replaced with the latest value, new insights surfaced. The input store is never modified — review the output and discard if you don't like it.

- Create with `inputs: [{memory_store}, {sessions: [...]}]`, a model (`opus-4-8`/`opus-4-7`/`sonnet-4-6`), and optional `instructions` to steer focus.
- Runs minutes to tens of minutes. Poll status: `pending → running → completed`. Output store ID appears in `outputs[]`.
- Billed at standard token rates; **cost scales with session count**, and much comes back cached (the post's "95% cached, near-zero cost" claim).
- Use it to keep stores under the 2,000-memory cap and to fold many sessions' learnings into clean memory.

**Advise like this:** "Attach a memory store" = remember across runs. "Run a dream nightly over the day's sessions" = self-improving, deduplicated memory without manual curation.
