---
id: DEC-0245
type: decision
title: The doc viewer ships at docs/human_docs.html and is installed by project bootstrap
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Amends DEC-0244: the viewer lives at docs/human_docs.html (not
  tools/), with mount-relative fetch paths, and both tools
  (human_docs.html, serve_docs.py) are installed by groundwork-design-session
  bootstrap into new projects alongside check_links.py. This ensures
  bare-ID convention never ships without its human-navigability
  counterpart; agent-optimal storage and human-readable browsing land
  together.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0048 @ T1-T4"
links:
  derives-from: [SES-0048]
  relates-to: [DEC-0244]
---

# DEC-0245: Viewer at docs/human_docs.html, Installed at Bootstrap

## Context

DEC-0244 shipped the viewer as `tools/viewer.html`, serving this
repository only. The stakeholder directed two amendments: the human
surface belongs with the docs it renders, and every Groundwork
project should get it from day one.

## Decision

1. The viewer lives at `docs/human_docs.html` (amending DEC-0244's
   `tools/` placement). Its fetch paths are mount-relative — a base
   prefix derived from the page's own URL — so it works wherever the
   repository root is served.
2. The groundwork-design-session skill carries both tools
   (`assets/human_docs.html`, `scripts/serve_docs.py`) and Mode 1
   bootstrap installs them into new projects alongside
   `tools/check_links.py`. `serve_docs.py` resolves the skill scripts
   from the vendored `.agents` copy first, then the `~/.claude`
   install, so the API endpoints work in any project layout.

## Rationale

`docs/` is what the page renders; co-locating the surface with the
corpus makes it discoverable next to the artifacts and keeps `tools/`
for scripts. Bootstrap parity means the bare-ID convention (DEC-0242)
never ships without its human-navigability counterpart — a new
project gets agent-optimal storage and human-readable browsing in the
same commit.

## Alternatives Considered

- **Keep at `tools/viewer.html`** (DEC-0244's placement): groups the
  viewer with the scripts that serve it, but hides the human surface
  in a directory humans have no other reason to open.
- **Skill installs the viewer only on request**: smaller bootstrap
  footprint, but new projects would store bare-ID docs with no
  rendering surface until someone remembers to ask.

## Implications

SKILL.md Mode 1, the installed AGENTS.md asset, this repository's
AGENTS.md and README, and the vendored `.agents` copy are updated;
DEC-0244's design content (features, discovery, API surface) is
otherwise unchanged.
