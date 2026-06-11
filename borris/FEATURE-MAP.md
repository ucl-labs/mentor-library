<!-- This is Borris's DECISION BRAIN. Read this FIRST, every time, before answering a "how should I build this" question. It is intentionally short so it costs almost nothing to load. Drill into blog/anthropic-features/<file>.md or blog/_reference/ only when a specific primitive is in play. Last synced from official Anthropic docs: 2026-06-09. -->

# Borris Feature Map — Pick the Right Claude Primitive

Use this to answer: **"Here's what I'm shipping. What's the best way to build it without burning tokens?"**

Read the user's goal, match it to a row below, recommend the primitive, then cite the matching brief in `blog/anthropic-features/`.

---

## The 30-second decision tree

1. **Is it a one-shot task or short chat?** → Plain **Messages API** call. Pick the model by cost/intelligence (see model table). Don't reach for agents.
2. **Repeatable expertise you keep re-explaining?** → Build a **Skill**. (e.g. "always format reports this way", "here's how we write cold DMs".)
3. **A fixed multi-step pipeline you want to run hands-off?** → **Closed loop**: Claude Code **Workflow**, or a **Managed Agent** with a defined **Outcome + rubric**.
4. **A long-running job that should work on its own for minutes/hours?** → **Managed Agent session** (sandbox, tools, streaming, resumable).
5. **One coordinator splitting work across specialists?** → **Multiagent** (Managed Agents) or **subagents** (Claude Code).
6. **Needs to remember across sessions?** → **Memory tool / Memory stores**, and **Dreams** to clean memory up.
7. **Quality matters but you want to run a cheaper model?** → **Advisor tool** (cheap executor + smart advisor) or **effort** tuning.
8. **Conversation/task too long for the context window?** → **Compaction** + **context editing** + **prompt caching**.
9. **Lots of tools (10+)?** → **Tool search tool** + `defer_loading`.
10. **Needs live data / the web?** → **Web search** + **web fetch** tools.

---

## Match table: "I want to..." → primitive

| You're shipping... | Use this | Brief |
|---|---|---|
| A bot that answers from my docs | Messages API + **search results / citations** (RAG) | `search-and-rag.md` |
| Reusable domain expertise ("do X our way") | **Agent Skill** (`SKILL.md`, progressive disclosure) | `agent-skills.md` |
| A fixed pipeline: discovery→plan→build→check→ship | **Closed loop** via Workflows / Outcome+rubric | `agent-looping.md`, `managed-agents.md` |
| Hands-off long task (research run, code change, report) | **Managed Agent session** | `managed-agents.md` |
| Define a deliverable + how it's graded, let it iterate | **Outcomes** (auto grader, self-iterates) | `managed-agents.md` |
| One lead agent delegating to specialists in parallel | **Multiagent** (coordinator + roster) | `managed-agents.md` |
| Writer / reviewer / deployer split | **Multiagent** or **subagents**, separate system prompts | `agent-looping.md` |
| Remember user prefs / project context across runs | **Memory stores** (attach to session) | `memory-and-dreams.md` |
| Clean up bloated/contradictory memory (the "dreaming agents" post) | **Dreams** (merge dupes, drop stale, 1–100 sessions) | `memory-and-dreams.md` |
| Higher quality at lower cost | **Advisor tool** (Opus advises a Sonnet/Haiku executor) | `advisor-tool.md` |
| Trade quality vs cost/speed on one model | **Effort** param (`low`→`max`, `xhigh` for long agentic) | `thinking-and-effort.md` |
| Let the model think only when needed | **Adaptive thinking** (Opus 4.8/4.7, Sonnet 4.6) | `thinking-and-effort.md` |
| Much faster output, willing to pay premium | **Fast mode** (`speed: "fast"`) | `thinking-and-effort.md` |
| Effectively infinite conversation | **Compaction** (server-side summarization) | `context-management.md` |
| Cut repeat input cost up to 90% | **Prompt caching** (auto + manual breakpoints) | `context-management.md` |
| Drop stale tool results / thinking to save context | **Context editing** | `context-management.md` |
| 10+ tools / big MCP setup eating context | **Tool search tool** + `defer_loading` | `tools-overview.md` |
| Claude runs Python/Bash, makes files | **Code execution tool** (free w/ web search/fetch) | `tools-overview.md` |
| Reduce latency/tokens across many tool calls | **Programmatic tool calling** (Claude calls tools in code) | `tools-overview.md` |
| Live web data with citations | **Web search** + **web fetch** | `tools-overview.md` |
| Guaranteed JSON / schema-conformant output | **Structured outputs** (GA) | `structured-outputs.md` |
| Connect external tools (CRM, GitHub, Slack…) | **MCP** (connector, remote servers, tunnels) | `mcp.md` |
| Cap total spend on a long agent run | **Task budgets** / compaction counter | `context-management.md` |
| Make the agent verify its own work / stop babysitting | **Encode manual checks as a verify skill** + 2nd-agent code review | `youtube/manual-checks-so-claude-closes-its-own-feedback-loop.md` |
| Process huge volume cheaply, async | **Message Batches API** (50% off) | `tools-overview.md` |
| Analyze images / PDFs / charts | **Vision** + **PDF support** | (see `_reference/`) |

---

## Model pick (current as of 2026-06-09)

| Model | API ID | $/MTok in·out | Use for |
|---|---|---|---|
| **Opus 4.8** | `claude-opus-4-8` | $5 / $25 | Most capable. Complex reasoning, long-horizon agentic coding, coordinators, advisors. 1M context, adaptive thinking, effort defaults `high`. |
| **Sonnet 4.6** | `claude-sonnet-4-6` | $3 / $15 | Best speed+intelligence balance. Default workhorse, executors, tool-heavy workflows. 1M context. Set `effort: medium`. |
| **Haiku 4.5** | `claude-haiku-4-5` | $1 / $5 | Fastest, cheapest. High-volume, real-time, simple subagents. 200k context. |

Rule of thumb: **coordinator/advisor = Opus, workers/executors = Sonnet or Haiku.** Pair a cheap executor with an Opus **advisor** to get near-Opus quality at a fraction of the cost.

---

## Token-economy cheat sheet (the "without burning tokens" goal)

- **Skills** cost ~100 tokens until triggered (progressive disclosure). Install many freely.
- **Tool search** cuts tool-definition context by 85%+ when you have many tools.
- **Prompt caching** cuts repeat input cost up to 90%. Cache system prompts separately.
- **Advisor tool** generates the bulk of output at the cheap executor's rate; only the short plan is at Opus rates.
- **Dreams** rebuild memory ~free because ~95% of tokens come back cached.
- **Effort `low`/`medium`** on subagents and routine work; reserve `xhigh`/`max` for genuinely hard steps.
- **Compaction** keeps long runs under the limit instead of paying for a bloated context every turn.

---

## Open vs Closed looping (mental model from the field)

- **Closed loop** = human designs the path: clear goal, defined steps, an eval gate at each step, a stop point. Cheap, repeatable, improves every run. **This is what to recommend for ~90% of marketing/business work.** Maps to Workflows + Outcomes + rubrics.
- **Open loop** = wide exploratory space, agent discovers its own path. Powerful but burns huge tokens; only viable on unlimited budgets and with a tight standard, or it becomes a slop machine.

When advising Kristine: **default to closed.** Orchestrator owns the goal → specialists own the steps → subagents do narrow work → an eval gate keeps it honest.
