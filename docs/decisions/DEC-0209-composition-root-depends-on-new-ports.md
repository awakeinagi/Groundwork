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

[DEC-0201](../decisions/DEC-0201-composition-root-split.md) scoped
[EP-0008](../epics/EP-0008-backend-application-platform.md)'s own
epic-level `depends-on` to [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md)
only, not the full set of composed engines. Story derivation needed the
finer-grained build-order question: does the Composition Root story
itself need to wait on the two new Ports (Queue, KV-store) it also
wires, since — unlike the four pre-existing Ports — they don't exist
yet anywhere in the codebase.

## Decision

[ST-0057](../stories/ST-0057-composition-root.md) (Composition Root)
has `depends-on:
[ST-0010](../stories/ST-0010-app-database-port.md),
[ST-0060](../stories/ST-0060-queue-port.md),
[ST-0062](../stories/ST-0062-kv-store-port.md)]` — it cannot wire an
Adapter for a Port whose contract doesn't exist yet.

## Rationale

[DEC-0201](../decisions/DEC-0201-composition-root-split.md)'s epic-level
scoping was about which *epics* must be sequenced first, and correctly
left out [EP-0004](../epics/EP-0004-graph-index.md)/[EP-0007](../epics/EP-0007-consolidation-memory-layer.md)
because their Ports already exist (approved, built). The two new Ports
in this epic have no such existing implementation to wire against, so
the same "wiring needs the wired thing to exist" logic that motivated
naming [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md)
applies to them at story grain.

## Alternatives Considered

- **No depends-on edge — build against contracts/stubs in parallel**:
  rejected — a stub can unblock coding, but the story's own Acceptance
  Criteria require binding *real* v1 adapters, which don't exist until
  [ST-0060](../stories/ST-0060-queue-port.md)/[ST-0062](../stories/ST-0062-kv-store-port.md)
  are built.

## Implications

None beyond [ST-0057](../stories/ST-0057-composition-root.md)'s
frontmatter `depends-on` list.
