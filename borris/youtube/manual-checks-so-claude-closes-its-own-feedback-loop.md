---
title: "Manual Checks: How Claude Closes Its Own Feedback Loop"
source_url: ""
source_type: youtube
mentor: "Borris"
date_synced: "2026-06-12T00:00:00Z"
note: "Cleaned from an auto-generated transcript. Obvious speech-to-text errors corrected (Claude / Claude Code / dev server / Core Web Vitals / CI / GitHub / PR); substance preserved, nothing added."
---

# Manual Checks: How Claude Closes Its Own Feedback Loop

In most sessions you follow a loop. You ask for a change, the agent gathers context, takes action, and responds. You check the result, ask for another change, and so on. It's like a turn-based game where every turn waits on you - sometimes you go back and forth several times until you get what you wanted.

Like humans, agents produce better work when they receive feedback. But the feedback doesn't always have to come from you. As models get better at coding and reasoning, they're also getting better at verifying their own work by observing the signals around them - type checkers, tests, and runtime errors. Often, just having these in your codebase is enough for Claude to understand what commands to run and how to fix the code.

However, those checks are deterministic - pass or fail. The code works or it doesn't. What Claude can't always infer are the steps **you** take to manually verify a new feature or change. Those steps aren't in the codebase. So the more of those verification steps you can encode for Claude, the closer its first response will land to what you had in mind. You'll spend less time babysitting, fewer tokens on back-and-forth, and free yourself up to work on something else while Claude iterates.

## Encode the verification loop

A good place to start is to write down a best-practices version of what you already do.

- **Web/front-end:** run the dev server, open the browser, click around as if you were the user, check the console for errors.
- **Backend:** hit the endpoint, check the status and the response.

Every domain has its own version of this, but the shape is similar.

For each of those, there's usually a tool Claude can already drive in your place:

- **Front-end:** the Claude Code Chrome extension, the desktop preview, and the Chrome DevTools MCP. Claude can open pages, navigate, take screenshots, read the console, and check Core Web Vitals.
- **Backend:** Claude can call the endpoint and read the response.
- **Mobile and desktop apps:** computer use, plus the iOS and Android Simulator MCPs.

Whatever your manual check looks like, there's usually a way to hand it off to Claude.

## Turn it into a skill

Once you've clarified your current workflow, encode it as a **skill** by invoking the skill-creator and asking Claude to interview you. If you're struggling to articulate it, ask Claude to help draft the best practices and show you what an end-to-end verification flow might look like.

Looking at a draft skill Claude created, it decided to verify changes via browser automation: capture visual evidence, watch the console, and check for regressions.

**Example.** Here's a page with a known layout-shift issue I hadn't gotten around to fixing. I asked Claude to work on something completely unrelated - adding a like button. Claude adds the button, checks it, and because it's a UI change, runs the verification pass on its own: the dev server starts, the preview opens, Claude clicks the like button (works), and takes a screenshot. The skill also tells it to capture a performance trace through the Chrome DevTools MCP. So Claude reports back: the like button works, **but** there's layout shift on this page. That wasn't part of the task, but the skill caught it - because checking Core Web Vitals is part of the verification we encoded. As you encode more of your workflow, Claude's coverage grows.

## Get a second pair of eyes (another agent)

Before you ship, it's worth a second review - from another agent. A second agent won't share the biases of the agent that wrote the code. It has its own context and isn't influenced by previous conversations. That isolation makes reviews more honest and catches things the first agent missed.

Options for code review:

- **The code-review plugin** spins up several subagents in parallel, each looking at the change from a different angle, scores the findings for confidence, and posts the result back on the PR.
- **The managed cloud code-review feature** runs automatically on every PR to GitHub (Team and Enterprise plans).

Whichever you pick, it's helpful to have a last line of defense before merging.

## Roll it into one shipping workflow

At this point you have two layers: the verification layer that runs while Claude is building your application, and a second review before you merge, run by agents that didn't write the code. Both are part of the same overarching development cycle.

Think about how things go right now: you make a change, you verify it works, you commit, open a PR, get it reviewed, and keep an eye on CI. You can roll these steps into one workflow by writing a skill that calls all these skills. For example, the Claude Code team has a skill they run whenever they're shipping a feature. It calls:

- the build/simplify skill to clean up the diff,
- custom verify skills to confirm the change works end-to-end,
- a design check if the diff touched the UI,
- a step to open and subscribe to a PR, and
- one that watches CI and fixes failures as they come in.

Your workflow might look different. The point is to hand off as much as possible so Claude can verify its own work end-to-end.
