---
id: DEC-0402
type: decision
title: "Typed frontmatter fields validate against a schema table at create, recheck, and checker"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0077 @ T10-T11"
overview: >-
  create had appended --field values verbatim with no validation,
  and session-close checked only field presence, not shape, how
  SES-0073 shipped off-spec values, IDEA-0044's spark. A
  FIELD_SCHEMA constant in gw_write.py now records per-type known
  fields with shapes and enums covering transcript-fidelity, scalar
  participant fields, ISO dates, source-span, timebox, and release.
  create refuses violations; the recheck enforces the same table
  under the DEC-0386 graceful-skip pattern; the checker gains a
  corpus-wide rule at WARN, duplicated into both check_links.py
  copies, with an in-session sweep deciding promotion to FAIL if the
  violation list is small. Unknown fields remain open for extension.
  Decided at SES-0077.
links:
  derives-from: [SES-0077]
  relates-to: [DEC-0386, DEC-0317, IDEA-0044, DEC-0315]
---
# DEC-0402: Typed frontmatter fields validate against a schema table at create, recheck, and checker

## Context

`create` had been appending `--field` values verbatim with no validation anywhere, and session-close checked only field presence, not shape — how SES-0073 shipped off-spec values, the spark for IDEA-0044.

## Decision

A `FIELD_SCHEMA` constant in `gw_write.py` records, per artifact type, the known fields and their shapes: transcript-fidelity's enum, scalar participant fields, ISO dates, source-span's format, timebox, and release. `create` refuses violations of this schema. The recheck enforces the same table under the DEC-0386 graceful-skip pattern. The checker gains a corpus-wide rule landing at WARN, duplicated into both `check_links.py` copies, with an in-session sweep deciding whether to promote it to FAIL if the violation list turns out small. Unknown fields remain open for future extension.

## Rationale

Not separately recorded at distillation; the rationale is carried by the Context and Decision above and by the source session's transcript at the recorded source span (skeleton restored at SES-0077).

## Alternatives Considered

No alternatives were separately recorded at distillation (skeleton restored at SES-0077).

## Implications

No separate implications were recorded at distillation; the operative consequences are stated in the Decision (skeleton restored at SES-0077).
