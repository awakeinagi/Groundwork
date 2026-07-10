---
id: DEC-0352
type: decision
title: "Install-script contract scope call deferred to backfill take-up"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi
decided-on: 2026-07-10
source-span: "SES-0065 @ T9-T10"
overview: >-
  The recurring question of whether install.sh is a contracted
  deliverable of the Artifact Interaction Surface epic (vs the
  future distribution/packaging epic DEC-0339 already defers to
  IDEA-0010's take-up) is deliberately deferred a third time
  (previously punted at DEC-0339, then at SES-0060 without
  resolution). Rather than lapsing by omission, SES-0065 (T9-T10)
  records the deferral explicitly and carries it as a named open
  question through EP-0009's gate, to be settled at the backfill
  fold-in Idea's take-up once the two Component Docs' actual
  contract shape is known.
links:
  derives-from: [SES-0065]
  relates-to: [DEC-0339, DEC-0334]
---

## Context

Whether `install.sh` (the DEC-0319 install script) is a contracted
deliverable of this epic, or belongs to the future distribution/
packaging epic DEC-0339 already defers to IDEA-0010's take-up, has now
been raised and left open twice before (per DEC-0339, and again at
SES-0060 where it was one of two items explicitly deferred rather than
resolved). Grilling round 1 (T9) raised it a third time; the
stakeholder's answer (T10) was to defer again rather than settle it
here.

## Decision

The install-script contract scope call is deliberately deferred a
third time. It is not silently dropped: it is carried as an explicit
open question through EP-0009's gate (named in Risks & Open
Questions) and is to be settled at the backfill fold-in Idea's
take-up, alongside that take-up's other open questions.

## Rationale

The stakeholder had a live choice between settling it now and
deferring again, and chose deferral (T10) — the call depends on
backfill-take-up context (what the two CMPs actually contract) that
does not yet exist. Recording the deferral explicitly, rather than
letting it lapse a third time by omission, is what distinguishes this
from the DEC-0334/DEC-0339 pattern of implicit, undocumented
punting.

## Alternatives Considered

- **Settle it now**: install.sh in scope — rejected, T10.
- **Settle it now**: install.sh out of scope, reserved for the
  distribution epic — rejected, T10; the stakeholder chose deferral
  over either resolution.

## Implications

The fold-in Idea created this session names this open question
explicitly as one it carries forward, so the deferral is traceable
and does not require re-discovery at the next take-up.
