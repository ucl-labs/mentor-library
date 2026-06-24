---
name: aeo-promote
description: "Review and commit the AEO findings that aeo-radar staged. Reads ethan/_inbox/manifest.json, shows the staged files + stale flags, and on approval moves staged files into the LIVE ethan/ KB, updates SYMPTOM-MAP.md, then git commits AND pushes to mentor-library. Use when the user says 'aeo-promote', 'promote the AEO findings', 'commit the staged sources', 'approve the radar', or after reading an aeo-radar digest. This is the ONLY path from staging into the live Ethan KB - it requires explicit human approval (Kristine or Sam)."
model: sonnet
effort: low
---

# aeo-promote - commit staged AEO findings into the live Ethan KB

> **Subagent note:** if spawned as a subagent, the orchestrator MUST pass `model: sonnet`
> (effort `low`).

`aeo-radar` only stages. This skill is the human-gated gate that moves approved staged
files into the live `ethan/` KB that Sam + Kristine build SOPs from. **Nothing moves
without explicit approval.**

## CRITICAL rules

1. **Require explicit approval before any move.** Show the staged set first. Move only
   what Kristine or Sam approves (all, or a named subset). No silent promotion.
2. **Additive only.** Move/copy staged files into live folders. NEVER delete a live file
   here either - stale flags are shown for the human to action manually, not auto-deleted.
3. **Preserve frontmatter.** Keep `source_url`, `tier`, `date_synced`, `leader`, `note`.
   Drop nothing. (The `_inbox/` location is the only thing that changes.)
4. **Update the map.** After moving, add the new files as rows in `ethan/SYMPTOM-MAP.md`
   under the right symptom section, and refresh its `Last built:` date.
5. **Commit + push only after approval.** Per Kristine's setting: once she or Sam approve,
   `git add` the moved files + map, commit with a dated message, and `git push`. Report the
   commit hash + pushed branch.

## Steps

1. Read `ethan/_inbox/manifest.json` and list staged files (grouped gospel/directional),
   stale flags, and skipped sources. If `_inbox` is empty, say so and stop.
2. For each staged file, show: title, tier, source_url, target live folder, one-line note.
3. **Ask for approval** - "promote all / promote these / cancel". Wait.
4. For approved files: move `ethan/_inbox/<sub>/<file>` -> `ethan/<sub>/<file>`. If a name
   collides with a live file, stop and ask (do not overwrite).
5. Update `ethan/SYMPTOM-MAP.md`: add rows for new files under the matching symptom(s);
   bump `Last built:` to today (`date '+%Y-%m-%d'`).
6. Show the stale-flag list and ask whether to action any (manual - you only edit/delete a
   live file if the human explicitly says so in this step).
7. `git add` moved files + SYMPTOM-MAP, `git commit -m "aeo-radar: promote N sources (YYYY-MM-DD)"`,
   `git push`. Report hash + branch.
8. Clear the promoted entries from `_inbox/` and update/remove `manifest.json`.

## Verify

- [ ] Only approved files moved; collisions surfaced, not overwritten.
- [ ] Frontmatter intact on every moved file.
- [ ] SYMPTOM-MAP has a row per new file + refreshed date.
- [ ] Commit created AND pushed; hash reported.
- [ ] No live file deleted unless the human explicitly approved it this run.

## Tools
Read/Write/Edit/Glob/Grep, Bash (`mv`, `git`, `date`).
