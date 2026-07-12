---
id: DEC-0389
type: decision
title: "The direct-read surface is the existing gw CLI read, search, and graph families, chartered via AGENTS.md and a doc-only gw-read skill"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0076 @ T5-T9"
overview: >-
  Direct reads invoke gw.py's existing read/search/graph subcommand
  families rather than a new script or a second package. The charter
  is a standing AGENTS.md section plus a new doc-only gw-read skill:
  usage recipes and discipline (overviews first, filters over
  enumeration, never the write family, never raw file reads),
  pointing at the same gw.py. DEC-0310 (single tooling home) and
  DEC-0316 (one CLI) stand unmodified. Considered and rejected: a
  raw Read/Grep charter for all agents (loses partial-read economy,
  search/graph access, the audit line) and a standalone read package
  (re-fragments tooling, requires a build gate). Decided at
  SES-0076, elaborating DEC-0388.
links:
  derives-from: [SES-0076]
  relates-to: [DEC-0310, DEC-0316, DEC-0388, DEC-0390]
---
# DEC-0389: The direct-read surface is the existing gw CLI read, search, and graph families, chartered via AGENTS.md and a doc-only gw-read skill

## Context

With targeted reads de-mediated by DEC-0388, the surface and packaging for direct reads had to be chosen (skeleton restored at SES-0077).

## Decision

No new scripts and no second package: direct reads invoke `gw.py`'s existing `read`/`search`/`graph` subcommand families. The charter lives as a standing AGENTS.md section plus a new doc-only `gw-read` skill — a SKILL.md carrying usage recipes and the discipline of overviews first, filters over enumeration, never the write family, never raw file reads — pointing at the same `gw.py`. DEC-0310, the single tooling home, and DEC-0316, one CLI, stand unmodified.

## Rationale

Not separately recorded at distillation; the rationale is carried by the Context and Decision above and by the source session's transcript at the recorded source span (skeleton restored at SES-0077).

## Alternatives Considered

A raw Read/Grep charter for all agents, which loses partial-read economy, search/graph access, and the audit line. A standalone read package with wrapper scripts, which re-fragments the consolidated tooling and requires a build gate.

## Implications

No separate implications were recorded at distillation; the operative consequences are stated in the Decision (skeleton restored at SES-0077).
