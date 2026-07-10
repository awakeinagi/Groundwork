---
id: DEC-0344
type: decision
title: IDEA-0011 is taken up; its fix folds into BG-0002
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0059 @ T19"
overview: >-
  IDEA-0011 (ratified-but-unbuilt method tooling invisible to the
  status report) is taken up by SES-0059 and resolved structurally
  rather than by new tracking machinery: method work now lives in
  the artifact tree as ordinary Stories/Spikes/CMPs, so drafts,
  gated items, and underived approvals surface in the status report
  and frontier automatically; the residual guarantee — nothing
  ratified stays invisibly unbuilt — is BG-0002's outcome 4,
  verified at its gates. A future method obligation avoiding the
  tree is a DEC-0335 violation, not a tracking feature request.
links:
  derives-from: [SES-0059]
  relates-to: [IDEA-0011, DEC-0338, DEC-0335, BG-0002]
---

# DEC-0344: IDEA-0011 Taken Up — Visibility Folded into BG-0002

## Context

IDEA-0011 (captured at SES-0058) named the systemic gap: ratified
method-tooling build obligations were invisible to the status report
and work queue. This session's structural changes address most of it
natively.

## Decision

IDEA-0011 is taken up by SES-0059, and its fix is folded into BG-0002
rather than pursued as separate tooling work: method work now lives in
the artifact tree as ordinary Stories/Spikes/CMPs, so drafts, gated
items, and approved-but-underived work surface in the status report
and frontier automatically; the residual guarantee — nothing ratified
stays invisibly unbuilt — is BG-0002 outcome 4, verified at its gates.
No separate intake session is needed; IDEA-0011's status moves to
taken-up with its disposition pointing at SES-0059 and BG-0002.

## Rationale

The gap existed because method work lived outside the tree; putting it
inside the tree is the fix. A dedicated tracking mechanism would
duplicate what the status report already does for tree residents.

## Alternatives Considered

- **Separate intake session for IDEA-0011** — would re-derive this
  session's conclusion; rejected at T19.

## Implications

IDEA-0011: status → taken-up, disposition updated. BG-0002 carries the
residual criterion. If a future method obligation somehow avoids the
tree, that is a DEC-0335 violation, not a tracking feature request.
