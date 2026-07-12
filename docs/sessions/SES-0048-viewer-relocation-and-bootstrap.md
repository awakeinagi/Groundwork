---
id: SES-0048
type: session
title: Viewer relocation to docs/ and bootstrap inclusion
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Short follow-up to SES-0047 on two stakeholder directives for the doc
  viewer. Relocated single-page webapp from tools/ to docs/human_docs.html;
  made all fetch paths mount-relative so viewer works wherever repo is
  served. Added notes to README. Integrated into agent skill bootstrap:
  skill installs docs/human_docs.html and tools/serve_docs.py alongside
  check_links.py. Server resolves skill scripts from vendored .agents copy
  first, falling back to ~/.claude install, so bootstrapped tool works in
  any Groundwork project. Produced DEC-0245.
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [SES-0047, DEC-0244, DEC-0245]
---

# SES-0048: Viewer Relocation and Bootstrap Inclusion

Short follow-up to SES-0047: two stakeholder directives on the doc
viewer, arriving immediately after DEC-0244 was committed.

## Purpose

Short follow-up to SES-0047 executing two stakeholder directives for the doc viewer: relocate it from tools/ to docs/human_docs.html and include it in the agent-skill bootstrap. (skeleton restored at SES-0078)

## Transcript

### T1 — Stakeholder

Include the single-page webapp for human-readable docs at
`docs/human_docs.html`, and add notes to the README on how to use it.

### T2 — Facilitator

Noted that DEC-0244's accepted text places both tools in `tools/`, so
the relocation is recorded by an amending decision rather than an
edit. Implementation: moved the file, made all fetch paths
mount-relative (a `BASE` prefix derived from the page's own location,
so the viewer works wherever the repo root is served), updated the
server banner and README.

### T3 — Stakeholder

The agent skill should also include this webapp as part of project
bootstrapping.

### T4 — Facilitator

Implemented at method level: the skill gains `assets/human_docs.html`
and `scripts/serve_docs.py`; SKILL.md's Mode 1 skeleton now installs
`docs/human_docs.html` and `tools/serve_docs.py` alongside
`tools/check_links.py`; the installed AGENTS.md asset names the
browsing surface. `serve_docs.py` resolves the skill scripts from the
vendored `.agents` copy first, falling back to the `~/.claude`
install, so the bootstrapped tool works in any Groundwork project.
Read back as DEC-0245; stakeholder direction constitutes the
confirmation.

## Consistency Checks

`sweep DEC-0245`: DEC-0244 has no ratified citers — clear. `terms
DEC-0245`: two unlinked co-occurrences on the generic path token
`docs/` (DEC-0091, DEC-0113) — noise, neither touches viewer
placement; no links added.

## Decisions Produced

- DEC-0245 — the viewer ships at `docs/human_docs.html` and is
  installed by project bootstrap

## Conflicts Raised

None raised during this session. (skeleton restored at SES-0078)
