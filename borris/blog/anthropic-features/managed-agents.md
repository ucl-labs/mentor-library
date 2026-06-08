<!-- source: https://platform.claude.com/docs/en/managed-agents/* — synced 2026-06-09 -->

# Claude Managed Agents (the "agent harness")

**What it is:** A fully managed agent runtime. Instead of building your own agent loop, sandbox, and tool execution, you create an agent, give it an environment, and run sessions. Claude reads files, runs commands, browses the web, and executes code in a secure sandbox. Beta header `managed-agents-2026-04-01` (SDK sets it automatically).

**When to recommend it:** long-running tasks (minutes to hours), async work, stateful sessions that resume cleanly, or when you don't want to build infrastructure. For fine-grained custom loops, use the Messages API instead.

## Four core concepts
- **Agent** — model + system prompt + tools + MCP servers + skills. Create once, reference by ID.
- **Environment** — where it runs: Anthropic cloud sandbox, or self-hosted sandbox on your infra.
- **Session** — a running agent instance doing a task and producing outputs.
- **Events** — messages between your app and the agent (user turns, tool results, status). Streamed via SSE, persisted server-side.

## Outcomes — turn a conversation into *work*
Define what the deliverable should be + a **rubric** (markdown, per-criterion). The harness auto-provisions a **grader** in a separate context window. The agent self-evaluates and iterates until the rubric passes or `max_iterations` (default 3, max 20) is hit.
- Send `user.define_outcome` with `description` + `rubric` (inline text or uploaded file).
- Grader returns `satisfied` / `needs_revision` / `max_iterations_reached` / `failed`.
- Deliverables land in `/mnt/session/outputs/`, fetched via Files API.
- **This is the cleanest "closed loop" primitive: goal + eval gate + auto-iteration.**

## Multiagent — coordinator + specialists
One coordinator delegates to a roster of agents, each in its own context-isolated **session thread** with its own model/prompt/tools.
- Set `multiagent: {type: coordinator, agents: [...]}` on the coordinator. Max 20 unique agents in roster, max 25 concurrent threads. Depth is 1 level only.
- Patterns: **parallelization** (fan out independent subtasks), **specialization** (security agent, doc agent), **escalation** (consult a stronger model for hard subtasks).
- MCP servers are agent-scoped; vault credentials are session-scoped.
- This is the official version of the "writer / reviewer / deployer" team pattern from the field.

## Other building blocks
- **Memory stores** — carry info across sessions (see `memory-and-dreams.md`).
- **Dreams** — consolidate/clean memory (see `memory-and-dreams.md`).
- **Webhooks** — subscribe to session/vault lifecycle events.
- **Vaults** — store credentials (OAuth, MCP) with background refresh.
- **Self-hosted sandboxes** — run tool execution on your own infra for compliance/data-residency.
- **MCP tunnels** — reach MCP servers in your private network (research preview).

**Note:** Managed Agents is stateful by design, so it is NOT eligible for Zero Data Retention or HIPAA BAA. You can delete sessions/files anytime.

**Advise like this:** "Create a Managed Agent with an Outcome + rubric" = hands-off deliverable. "Use a multiagent coordinator" = parallel specialist team. Pair with memory stores for cross-run context.
