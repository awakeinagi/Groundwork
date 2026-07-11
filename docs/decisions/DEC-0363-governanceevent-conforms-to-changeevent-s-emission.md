---
id: DEC-0363
type: decision
title: "GovernanceEvent conforms to ChangeEvent's emission contract"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-10
source-span: "SES-0066 @ T16-T17"
overview: >-
  The 'consistent with CMP-0002's emission semantics' prose is a
  real conformance dependency, recorded as the element edge
  GovernanceEvent -> ChangeEvent.B-1 (interface), keeping CMP-0002
  supported in CMP-0004's depends-on.
links:
  derives-from: [SES-0066]
---

## Context

During the Uses: backfill's extraction and classification pass (SES-0066 T16), the facilitator found that CMP-0004's `depends-on` frontmatter link already lists CMP-0002, but the only element-level evidence supporting it was `GovernanceEvent`'s prose describing itself as "consistent with CMP-0002's emission semantics" — a conformance relationship that had never been recorded as a typed element edge.

## Decision

`GovernanceEvent` conforms to `ChangeEvent`'s emission contract. The "consistent with CMP-0002's emission semantics" prose is recorded as a real conformance dependency: the element edge `GovernanceEvent` → `ChangeEvent.B-1` (`(interface)`) was added, keeping CMP-0002 supported in CMP-0004's `depends-on` frontmatter link under DEC-0309's both-directions projection requirement.

## Rationale

The prose relationship is a genuine conformance dependency, not incidental phrasing: `GovernanceEvent` is designed to match `ChangeEvent`'s emission semantics (delivery guarantees, ordering) as published in `ChangeEvent.B-1`, which is exactly the kind of build-against-contract-alone relationship the ratified `(interface)` classification test targets.

## Alternatives Considered

Dropping CMP-0002 from CMP-0004's `depends-on` for lack of element-level support was considered, since DEC-0309 requires depends-on to equal the exact projection of typed edges. It was rejected in favor of recording the underlying element edge, since the dependency the frontmatter link asserts is real and independently evidenced in the contract prose — the correct fix was to make the typed edge explicit, not to remove the accurate frontmatter link.

## Implications

CMP-0004's depends-on retains CMP-0002, now backed by an explicit typed element edge as DEC-0309 requires.
