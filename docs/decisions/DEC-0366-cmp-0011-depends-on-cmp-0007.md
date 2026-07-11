---
id: DEC-0366
type: decision
title: "CMP-0011 depends on CMP-0007"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-11
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-11
source-span: "SES-0066 @ T20-T21"
overview: >-
  ApiApplication.B-1 requires an authenticated Participant resolved
  on every route; that capability exists as CMP-0007's
  IdentityService (A-1 resolve(auth_subject) -> person_id), so the
  element edge (ApiApplication -> IdentityService, interface), the
  depends-on entry, and the phrasing correction were applied.
  Surfaced by the DEC-0157-motivated stale-phrase spot-check during
  SES-0066's consistency dispositions; same defect shape as
  DEC-0361.
links:
  derives-from: [SES-0066]
  relates-to: [DEC-0132, DEC-0361]
---

## Context

During SES-0066's close-out consistency dispositions (T20), the DEC-0157-motivated stale-phrase spot-check found that `CMP-0011`'s Dependencies section still described the identity-provider contract from `ST-0022` (owned by `CMP-0007`) as forward-declared per `DEC-0132` — the same stale defect shape DEC-0361 corrected for `CMP-0001`/`CMP-0005`. `CMP-0007` is approved, and its `IdentityService.A-1` (`resolve(auth_subject) → person_id`) is exactly the capability `ApiApplication.B-1` requires: an authenticated Participant resolved on every route.

## Decision

`CMP-0011` depends on `CMP-0007`. The element edge (`ApiApplication` → `IdentityService`, `(interface)`) was added to `ApiApplication`'s `Uses:` line, `CMP-0007` was added to `CMP-0011`'s `depends-on` frontmatter link, and the stale "forward-declared" Dependencies-section phrasing for the identity-provider contract was corrected to describe `CMP-0007` as a standing, consumed dependency (`IdentityService.A-1`).

## Rationale

`CMP-0007` has been approved since EP-0004 refinement completed; recording its identity-resolution surface as still forward-declared understates a structural edge `ApiApplication.B-1`'s own contract prose already asserts, and leaves the corpus's typed `Uses:`/`depends-on` graph incomplete for this route.

## Alternatives Considered

Leaving `CMP-0011`'s Dependencies note as a forward declaration was rejected: `DEC-0132` itself anticipated this edge becoming a standing dependency once the owning CMP existed, and it now does — the same reasoning DEC-0361 applied to CMP-0001's analogous stale note.

## Implications

`CMP-0011`'s `depends-on` now includes `CMP-0007`; DEC-0309's both-directions projection check (enforced by checker rule 20) requires this. No other artifacts needed correction as a consequence.
