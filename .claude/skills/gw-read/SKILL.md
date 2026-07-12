---
name: gw-read
description: Direct targeted reads of Groundwork corpus artifacts via the gw CLI's read-only families (DEC-0388, DEC-0389). Use whenever you need a bounded artifact lookup, even if Groundwork isn't named - what a DEC/EP/ST/SP/IDEA/SES/CMP says or decides, an artifact's status or overview, one section, who cites a decision, filtered listings (e.g. captured ideas), a single semantic search, or a single graph impact/provenance query. Read-only by charter - never the write family, never raw file reads of docs/. Delegate writes and open-ended synthesis (precedent hunts, surveys, recall audits, anything needing many chained calls) to the artifact-librarian agent.
---

# gw-read — direct targeted reads of the Groundwork corpus

Any agent may run these commands directly (DEC-0388's charter); this
skill is documentation only — the tooling lives in `artifact-interact`,
the single tooling home (DEC-0310, DEC-0316).

Entry point (define `GW` in the same shell invocation as the commands
that use it — each tool call runs a fresh shell):

```
GW="python3 .claude/skills/artifact-interact/scripts/gw.py --root ."
```

## Recipes

```
$GW read overview DEC-0388                        # one artifact's overview
$GW read overview --type idea --status captured   # filtered listing
$GW read outline SES-0076                         # section headings only
$GW read section EP-0009 "Derived Work"           # one section's body
$GW read citers DEC-0335                          # who cites this decision
$GW search search "write serialization"           # single semantic search
$GW graph impact DEC-0325                         # what a change would touch
$GW graph trace CMP-0009                          # provenance: why this exists
```

Search and graph hits include overviews (DEC-0290) — a hit list often
answers the question with zero further reads.

## Discipline (the charter's conditions — DEC-0388, DEC-0389)

- Overviews first; request a section or body only when an overview
  says the detail is there.
- Filters (`--type`, `--status`) over enumerating IDs.
- Bounded means bounded: a handful of reads, one search, one graph
  query, consumed as-is.
- The moment the task needs iterative exploration or cross-artifact
  synthesis — or you catch yourself chaining many calls — stop and
  spawn the `artifact-librarian` with a task-level intent instead.
- Never the `write` family; never raw Read/Grep/Glob of `docs/`
  files. Writes have exactly one path: a librarian write task
  (DEC-0312).
