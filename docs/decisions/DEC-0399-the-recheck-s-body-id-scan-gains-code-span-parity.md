---
id: DEC-0399
type: decision
title: "The recheck's body ID scan gains code-span parity with the checker"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0077 @ T12-T13"
overview: >-
  IDEA-0022's false-positive refusals, recorded at SES-0061, traced
  back to the recheck scanning raw body text for unresolved IDs
  while the full checker strips code spans and fences first. The
  recheck's body unresolved-ID scan now routes through the existing
  prose_lines code-stripping walker; the raw frontmatter scan is
  retained, which is correct enforcement on overviews under the
  sibling decision banning unresolvable overview-ID tokens. The full
  checker already conformed and is unchanged. The recheck and
  checker remain deliberately distinct passes per DEC-0315. Decided
  at SES-0077, paired with the overview-ID-ban decision.
links:
  derives-from: [SES-0077]
  relates-to: [DEC-0315, IDEA-0022, DEC-0398]
---
# DEC-0399: The recheck's body ID scan gains code-span parity with the checker

## Context

IDEA-0022's false-positive refusals, recorded at SES-0061, traced back to the recheck scanning raw body text for unresolved IDs while the full checker strips code spans and fenced blocks before scanning.

## Decision

The recheck's body unresolved-ID scan now routes through the existing `prose_lines` code-stripping walker. The raw frontmatter scan is retained, which under the sibling decision banning unresolvable overview-ID tokens is correct enforcement on that surface. The full checker already conforms to this behavior and is unchanged.

## Rationale

Not separately recorded at distillation; the rationale is carried by the Context and Decision above and by the source session's transcript at the recorded source span (skeleton restored at SES-0077).

## Alternatives Considered

No alternatives were separately recorded at distillation (skeleton restored at SES-0077).

## Implications

The recheck and the full checker remain deliberately distinct passes, per DEC-0315.
