---
id: DEC-0209
type: decision
title: Composition Root's story-level depends-on includes the new Queue Port and KV-store Port stories
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0039 @ T1-T2"
links:
  derives-from: [SES-0039]
  relates-to: [DEC-0201]
  supersedes: []
---

# DEC-0209: Composition Root Depends On the New Port Stories

## Context

DEC-0201 scoped
EP-0008's own
epic-level `depends-on` to EP-0001
only, not the full set of composed engines. Story derivation needed the
finer-grained build-order question: does the Composition Root story
itself need to wait on the two new Ports (Queue, KV-store) it also
wires, since — unlike the four pre-existing Ports — they don't exist
yet anywhere in the codebase.

## Decision

ST-0057 (Composition Root)
has `depends-on:
ST-0010,
ST-0060,
ST-0062]` — it cannot wire an
Adapter for a Port whose contract doesn't exist yet.

## Rationale

DEC-0201's epic-level
scoping was about which *epics* must be sequenced first, and correctly
left out EP-0004/EP-0007
because their Ports already exist (approved, built). The two new Ports
in this epic have no such existing implementation to wire against, so
the same "wiring needs the wired thing to exist" logic that motivated
naming EP-0001
applies to them at story grain.

## Alternatives Considered

- **No depends-on edge — build against contracts/stubs in parallel**:
  rejected — a stub can unblock coding, but the story's own Acceptance
  Criteria require binding *real* v1 adapters, which don't exist until
  ST-0060/ST-0062
  are built.

## Implications

None beyond ST-0057's
frontmatter `depends-on` list.
