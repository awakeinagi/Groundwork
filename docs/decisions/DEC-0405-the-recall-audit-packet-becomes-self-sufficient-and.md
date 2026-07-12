---
id: DEC-0405
type: decision
title: "The recall-audit packet becomes self-sufficient and its output contract defended"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0077 @ T10-T13"
overview: >-
  IDEA-0027's judge-reported defects: packets omitted the audited
  artifact's content, candidate lists appeared mis-copied, stderr
  risked splicing into parsed JSON, and a stale-graph warning fired
  during generation; reconnaissance showed the mis-copy lives in
  orchestration, not generation. The packet now carries the audited
  artifact's id, title, overview, and full body; candidates carry
  overviews and rounded similarity scores; ordering is deterministic
  by descending score then ID. Third-party model-load chatter is
  redirected off stdout and an --output option writes the packet to
  a file; the stale-graph warning remains but reuses the refresh
  pass's mtimes; packet assembly is factored into a pure function
  for model-free testing; and the judge protocol gains an artifact-
  identity self-check making orchestration-layer packet swaps
  detectable. Decided at SES-0077.
links:
  derives-from: [SES-0077]
  relates-to: [IDEA-0027]
---
# DEC-0405: The recall-audit packet becomes self-sufficient and its output contract defended

## Context

IDEA-0027's judge-reported defects: packets omitted the audited artifact's own content, candidate lists appeared mis-copied, stderr risked splicing into the parsed JSON stream, and a stale-graph warning fired during packet generation. Reconnaissance showed the mis-copy defect actually lives in orchestration, not in packet generation itself.

## Decision

The packet now carries the audited artifact's id, title, overview, and full body; candidates carry their overviews and rounded similarity scores; ordering is deterministic by descending score then ID. Third-party model-load chatter is redirected off stdout, and an `--output` option writes the packet to a file. The stale-graph warning remains but now reuses the refresh pass's own mtimes rather than recomputing them. Packet assembly is factored into a pure function to allow model-free testing. The judge protocol gains an artifact-identity self-check, making orchestration-layer packet swaps detectable.

## Rationale

Not separately recorded at distillation; the rationale is carried by the Context and Decision above and by the source session's transcript at the recorded source span (skeleton restored at SES-0077).

## Alternatives Considered

No alternatives were separately recorded at distillation (skeleton restored at SES-0077).

## Implications

No separate implications were recorded at distillation; the operative consequences are stated in the Decision (skeleton restored at SES-0077).
