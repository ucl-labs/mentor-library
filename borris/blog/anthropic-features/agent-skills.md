<!-- source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview — synced 2026-06-09 -->

# Agent Skills

**What it is:** Reusable, filesystem-based packages of domain expertise — instructions, scripts, and resources — that turn a general agent into a specialist. Claude loads them on-demand, so you stop re-explaining the same guidance every conversation. Launched Oct 2026 (`skills-2025-10-02`).

**When to recommend it:** any time Kristine keeps re-pasting the same "here's how we do X" (brand voice, report format, DM style, a workflow). Build it once as a Skill; Claude auto-triggers it when relevant.

## Progressive disclosure — why Skills are token-cheap
Three loading levels:
1. **Metadata (always loaded):** `name` + `description` in YAML frontmatter. ~100 tokens per skill. Install many skills with no real context penalty.
2. **Instructions (loaded when triggered):** the `SKILL.md` body. Under ~5k tokens. Read via bash only when the request matches.
3. **Resources & code (loaded as needed):** bundled files (REFERENCE.md, schemas, scripts). Scripts run via bash and only their *output* enters context — the code never does. Effectively unlimited bundled content at zero idle cost.

## Structure
```
my-skill/
├── SKILL.md        # required: YAML frontmatter (name, description) + instructions
├── REFERENCE.md    # optional deep reference
└── scripts/run.py  # optional executable
```
- `name`: ≤64 chars, lowercase/numbers/hyphens, no "anthropic"/"claude".
- `description`: ≤1024 chars — say **what it does AND when to use it** (this is what drives auto-triggering).

## Where Skills work
- **Claude API** — pre-built (pptx, xlsx, docx, pdf) + custom via `/v1/skills`. Needs code execution. No network/package install at runtime.
- **Claude Code** — custom only, filesystem-based (`~/.claude/skills/` or `.claude/skills/`). Full network access. Shareable via plugins. **(This is how all of Kristine's mentor skills work.)**
- **claude.ai** — pre-built + custom (zip upload, per-user).
- Skills do NOT sync across surfaces; upload separately.

**Security:** only use skills from trusted sources — a malicious skill can direct Claude to misuse tools. Audit bundled scripts.

**Advise like this:** "Create a skill to..." whenever the task is repeatable expertise. It's the lowest-token way to specialize Claude.
