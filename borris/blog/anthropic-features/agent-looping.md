<!-- source: field patterns (X) cross-referenced with official Workflows/Managed Agents docs — synced 2026-06-09 -->

# Agent Looping — open vs closed (mental model + official mapping)

This is the practitioner framing for what the docs call Workflows, Managed Agent sessions, Outcomes, and multiagent. Use it to *explain* the architecture; use the official briefs for the *mechanics*.

## The loop
Every agent (single or in a fleet) runs the same cycle:
**Discovery → Planning → Execution → Verification → Iteration**, looping until the goal is met, then hands off or ships.

## Single-agent loop
One agent works on itself: researches, drafts, checks the draft against a goal, fixes weak spots, repeats until it clears the requirements. You stop prompting each step.
→ Official: a Managed Agent **session** with an **Outcome + rubric** (the rubric is the verification gate; the grader runs in a separate context).

## Fleet loop
An **orchestrator owns the goal**, breaks it into pieces, hands each to a **specialist**, who hands narrow work to **subagents**. The whole tree loops.
→ Official: **multiagent** coordinator + roster (Managed Agents), or **subagents/Workflows** in Claude Code.
- Orchestrator owns the goal · specialists own the steps · subagents do narrow work · **an eval gate keeps it from being slop.**

## Open vs closed (the key decision)
- **CLOSED loop** — human designs the path first: clear goal, defined steps, an eval at each step, a stop/handback point that feeds performance data back. Cheap, repeatable, gets better every run, runs on a normal budget. The standard is what keeps it honest. **Recommend this for ~90% of work.**
- **OPEN loop** — wide exploratory space; the agent discovers and builds things you didn't spec. Powerful but burns an insane amount of tokens — only runnable on an unlimited budget, and with a loose standard it becomes a fast slop machine.

## The "specialist team" pattern (writer / reviewer / deployer)
Split one job across agents with separate system prompts so each has a different incentive: writer optimizes for speed, reviewer for correctness (no incentive to approve), deployer for safety (only ships what passed review). They communicate via shared files or a coordinator. This is the official **multiagent** pattern; in Claude Code it's **subagents** with separate definitions.

**Advise like this:** start by asking "is the path known?" Known path → closed loop (Workflow / Outcome+rubric). Unknown, exploratory, unlimited budget → open loop. Then map roles to a coordinator + specialists + an eval gate.
