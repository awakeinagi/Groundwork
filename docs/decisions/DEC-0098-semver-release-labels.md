---
id: DEC-0098
type: decision
title: release frontmatter field with SemVer-prefix values plus reserved backlog
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0016 @ T3-T5, T9-T11"
links:
  derives-from: [SES-0016]
  relates-to: [DEC-0097, DEC-0099]
---

# DEC-0098: `release:` Frontmatter Field with SemVer-Prefix Values plus Reserved `backlog`

## Context

`status: deferred` ([DEC-0097](DEC-0097-deferred-status.md)) says *that*
an artifact is parked, not *for which release*. The discovery
requirement — bring parked items back when the time is right — needs a
target, in a controlled vocabulary that tooling can validate and sort.

## Decision

Stories and epics may carry a `release:` frontmatter field. Its value is
either the reserved label `backlog` ("wanted, no target release yet") or
a prefix of a Semantic Versioning 2.0.0 version core: `MAJOR` (`1`),
`MAJOR.MINOR` (`1.2`), or `MAJOR.MINOR.PATCH` (`1.2.3`). The major
component is mandatory; minor and patch are optional. Each specified
component is a numeric identifier with no leading zeroes (SemVer rule 2
per component). No `v` prefix; no pre-release or build metadata.

Semantics:

- **A partial value is a scope, not a version**: `release: 1` means
  "somewhere in the 1.x.x line"; `1.2` narrows it; `1.2.3` pins it.
  Narrowing an existing label as planning firms up is a mechanical edit;
  *moving* an item between releases cites a decision per
  [DEC-0100](DEC-0100-scope-moves-cite-decisions.md).
- **Absence of the field means the current release** — existing
  artifacts need no migration.
- An epic's `release:` is the default for stories deriving from it; a
  story may override with its own value.
- An artifact whose `release:` names anything other than a current
  release must be `deferred`; a `deferred` artifact must carry a
  `release:` (else its parking is unexplained).
- Reporting sorts by SemVer precedence (spec §11) over the numeric
  components, `backlog` always last.

## Rationale

Status and build intent are two independent facts; this field carries
the second. SemVer gives an unambiguous, widely understood grammar and a
deterministic sort order, fetched from the official specification
rather than invented. The spec's FAQ is explicit that `v1.2.3` is not a
semantic version — `v` belongs to git tag names — so labels are bare.
Pre-release and build metadata identify build artifacts, not planning
scopes, and are excluded. Absence-as-default keeps the common case
(current work) zero-ceremony.

## Alternatives Considered

- **Binary deferred flag**: rejected — distinguishing "next release"
  from "someday" was the immediate, stated need.
- **Free-form tags**: rejected — label drift defeats validation and
  violates glossary discipline.
- **Full SemVer versions only (`X.Y.Z` mandatory)**: rejected — planning
  rarely knows minor/patch up front; the participant amended labels to
  prefix scopes.
- **Allowing pre-release/build metadata in labels**: excluded now; a
  future decision can admit them if pre-release planning ever needs its
  own scope.

## Implications

[SPEC-story](../specs/SPEC-story.md) and
[SPEC-epic](../specs/SPEC-epic.md) gain the field. The checker
validates format, exact membership in the declared release set per
[DEC-0099](DEC-0099-releases-declared-in-goal-scope.md), and the
deferred/release consistency rules. YAML users should quote values
(`release: "1.2"`) so they parse as strings, not floats.
