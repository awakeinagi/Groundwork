---
id: DEC-0364
type: decision
title: "CMP-0014's port contract carries no runtime dependency"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-10
source-span: "SES-0066 @ T16-T17"
overview: >-
  The doc's own disclaimer is honored: KvStorePort gets Uses: none
  and depends-on stays empty; the v1 adapter's JobRuntime.A-1
  registration remains adapter-level coupling outside the port
  contract.
links:
  derives-from: [SES-0066]
  relates-to: [DEC-0222]
---

## Context

During the Uses: backfill's extraction and classification pass (SES-0066 T16), the facilitator found that CMP-0014's v1 default Adapter registers its expiry-sweep handler via `JobRuntime.A-1` at its own startup (per DEC-0222), but CMP-0014's own Notes section explicitly disclaims that "this port's own contract does not depend on that runtime" — raising the question of whether the port contract itself should carry a Uses: edge to CMP-0013.

## Decision

CMP-0014's port contract carries no runtime dependency. The `KvStorePort` element gets `Uses: none`, and CMP-0014's `depends-on` frontmatter link stays empty. The v1 adapter's `JobRuntime.A-1` registration remains adapter-level coupling, outside the port contract itself, exactly as CMP-0014's own Notes section (per DEC-0222) already disclaims.

## Rationale

The port/adapter seam is the point of this component: `KvStorePort` is the contract consumers build against, and consumers never see or depend on the sweep-job registration, which is purely an implementation detail of the v1 default Adapter. Honoring the doc's own disclaimer keeps the Uses: backfill consistent with a distinction the component had already made deliberately, rather than overriding it during a mechanical backfill pass.

## Alternatives Considered

Adding a `(implementation)` Uses: edge from `KvStorePort` to `JobRuntime.A-1` was considered, since the v1 adapter genuinely registers with it. It was rejected: the edge would belong to the adapter, not the port element the backfill is scoped to, and would contradict CMP-0014's own Notes-section disclaimer without a session decision to change that boundary.

## Implications

No depends-on or Uses: edge changes result for CMP-0014 from this backfill. The adapter-level JobRuntime coupling remains undocumented as a typed edge, consistent with the port/adapter contract boundary CMP-0014 already draws (per DEC-0222).
