---
id: DEC-0362
type: decision
title: "CMP-0010 depends on CMP-0015"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-10
source-span: "SES-0066 @ T16-T17"
overview: >-
  The Composition Root loads the master key at startup (IG-3) and
  hands it to the Secret Store, corroborated by CMP-0015's own IG-2;
  the edge (CompositionRoot -> SecretStore, interface), the depends-
  on entry, and a Dependencies-section entry were added.
links:
  derives-from: [SES-0066]
  relates-to: [DEC-0232]
---

## Context

During the Uses: backfill's extraction and classification pass (SES-0066 T16), the facilitator found that the Composition Root loads the master key at startup and hands it to the Secret Store (CMP-0010's own `IG-3`), corroborated by CMP-0015's `IG-2` — a real cross-component dependency that CMP-0010's `depends-on` frontmatter link did not record.

## Decision

CMP-0010 depends on CMP-0015. The element edge (`CompositionRoot` → `SecretStore`, `(interface)`), a `CMP-0015` entry in CMP-0010's `depends-on` frontmatter link, and a corresponding Dependencies-section entry describing the master-key hand-off (per DEC-0232, ST-0022) were added.

## Rationale

Both components' own contract items (CMP-0010's IG-3 and CMP-0015's IG-2) independently describe the same master-key hand-off; the dependency is real and mutually corroborated, not a one-sided inference, so recording it makes the depends-on graph match the contracts it is derived from.

## Alternatives Considered

Treating the master-key hand-off as out-of-scope startup wiring rather than a structural dependency was rejected: DEC-0309 treats element-grain Uses: edges as the source of truth for component depends-on, and this edge meets the interface-dependency test (CompositionRoot can be built against SecretStore's published contract alone).

## Implications

CMP-0010's depends-on now includes CMP-0015; DEC-0309's both-directions projection check (enforced by rule 20, decision 2) requires this.
