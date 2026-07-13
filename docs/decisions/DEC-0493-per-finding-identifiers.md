---
id: DEC-0493
type: decision
title: "Per-finding identifiers"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0092"
overview: >-
  Findings carry required identifiers Fn.m, where n is the round
  number and m is sequential within the round. The checker verifies
  identifier uniqueness and that each finding's round prefix matches
  the round section containing it. Cross-artifact prose references a
  specific finding as the artifact ID followed by the finding ID,
  for example "RSCH-0007 F2.3".
links:
  derives-from: [SES-0092]
  relates-to: [DEC-0453]
---

# DEC-0493: Per-finding identifiers

## Context

Cross-artifact prose and future stories need to reference a specific
finding precisely, not just "somewhere in RSCH-0007."

## Decision

Findings carry required identifiers Fn.m, where n is the round number
and m is sequential within the round. The checker verifies identifier
uniqueness and that each finding's round prefix matches the round
section containing it. Cross-artifact prose references a specific
finding as the artifact ID followed by the finding ID, for example
"RSCH-0007 F2.3".

## Rationale

A round-prefixed, sequential finding ID gives every finding a
permanent, collision-free address that is both human-readable (round
context is visible in the ID itself) and mechanically verifiable
(the round-prefix-matches-containing-section check catches
copy-paste errors when findings are edited or reordered).

## Alternatives Considered

A flat cross-round finding counter was considered and rejected: it
loses the round context in the ID itself and would not let the
checker verify placement against round structure.

## Implications

The checker enforces Fn.m uniqueness and round-prefix match;
cross-artifact citations of a finding use the two-token
"RSCH-nnnn Fn.m" form rather than a single combined identifier.
