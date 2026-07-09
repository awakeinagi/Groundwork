---
id: DEC-0170
type: decision
title: Allowlist filtering is a behavior clause on the connector's read-operation family, not a separate element
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0030 @ T2"
links:
  derives-from: [SES-0030]
  relates-to: [DEC-0049]
---

# DEC-0170: Allowlist Filter as a Read-Operation Behavior Clause

## Context

ST-0023's Component
Impact says CMP-0005
supplies "the read-operation and allowlist-filter contract sections" —
leaving open whether `governance/repos.yaml` filtering and path
excludes (DEC-0049)
deserve their own design element or belong inside the read operations
themselves.

## Decision

Allowlist enforcement is not a separate element. It is a contract
obligation directly on `CodeHostConnector.A-9`'s (browse/search/read)
items: a repository absent from `governance/repos.yaml` is
indistinguishable from one that doesn't exist (`not-found`, not
`permission-denied`), per-repository path excludes never surface in
listings/search/reads, and every returned result carries a repo+ref
citation.

## Rationale

Every adapter must apply this filter identically and it has no
independent lifecycle, state, or API surface of its own — it is a
predicate the read operations evaluate before returning, not a thing
with identity. A separate value/service element would model a
cross-cutting concern as if it were a first-class capability, adding
element bookkeeping (an `Implements:` line, a graduation check) without
a corresponding design payoff. Keeping the seam small also matches
CMP-0002/CMP-0003's
pattern of one element per genuinely distinct capability.

## Alternatives Considered

- **Separate `AllowlistFilter` value/service element** — more explicit
  and independently testable, but over-models a rule every adapter must
  apply uniformly as part of read correctness, not as an optional or
  swappable capability.

## Implications

`CodeHostConnector.A-9`'s contract items state the allowlist and
path-exclude behavior directly, citing
DEC-0049; the
conformance suite tests it as part of the read-operation family, not as
a standalone test target.
