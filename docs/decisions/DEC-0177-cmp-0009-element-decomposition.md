---
id: DEC-0177
type: decision
title: CMP-0009 decomposes into a single GitHubConnector service element; no graduation at this time
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0032 @ T6"
links:
  derives-from: [SES-0032]
  relates-to: [DEC-0080, DEC-0129, DEC-0171]
---

# DEC-0177: [CMP-0009](../components/CMP-0009-github-connector.md) Element Decomposition

## Context

[CMP-0009](../components/CMP-0009-github-connector.md) needed a Design
Elements decomposition covering [ST-0031](../stories/ST-0031-github-connector.md)
before its contract could be drafted, plus — per
[DEC-0080](DEC-0080-hybrid-component-granularity.md)'s seam-graduation
rule — a graduation review of any candidate element. The specific
question: does webhook payload normalization (host JSON →
`HostEvent`) warrant its own element, separate from the rest of the
adapter's operations?

## Decision

[CMP-0009](../components/CMP-0009-github-connector.md) decomposes into
one element: `GitHubConnector` (service) — implementing the full
`CodeHostConnector` protocol from
[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)
(orchestration, review posting, check administration, branch/team
administration, allowlisted reads, webhook subscription) — mirroring
[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)'s
own one-big-protocol-with-lettered-operation-families pattern
([DEC-0129](DEC-0129-port-typed-operation-families.md)). Webhook
payload normalization is internal to `GitHubConnector`, not a separate
top-level element.

**Graduation review**: `GitHubConnector` is consumed by nothing but
the protocol it implements (no second component depends on it
directly — consumers depend on `CodeHostConnector`, already graduated
as [CMP-0005](../components/CMP-0005-code-host-connector-protocol.md))
and needs no independent versioned conformance beyond that protocol's
own suite. It does not meet the graduation rule; no further split
warranted.

## Rationale

[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)'s
`IG-2` already treats check-administration isolation as "a general
good practice," i.e. an internal adapter-boundary concern, not a sign
of an independently consumed seam — the same reasoning applies to
webhook translation. Splitting it out would add an element boundary
with no second consumer and no independent versioning need, pure
process overhead against the graduation rule's actual test.

## Alternatives Considered

- **Split: GitHubConnector + GitHubEventTranslator**: would allow
  independent testing/versioning of translation logic, but no
  component consumes translation separately from the rest of the
  connector, and versioning it independently serves no current
  requirement.

## Implications

[CMP-0009](../components/CMP-0009-github-connector.md)'s Design
Elements section carries a single `### GitHubConnector (service)`
heading with all operation-family contract items.
