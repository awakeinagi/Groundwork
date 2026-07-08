---
id: ST-0028
type: story
title: Additional code-host connectors — GitHub, Bitbucket Cloud, GitLab
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0019]
cites: [DEC-0045, DEC-0050, DEC-0156]
---

# ST-0028: Additional Code-Host Connectors

> Deferred to `backlog` at creation (per
> [DEC-0156](../decisions/DEC-0156-future-connector-families-deferred.md),
> the deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)).
> Subscribed to trigger TRG-0007 — a deployment requiring a code host
> other than Bitbucket Data Center revives it.

## Summary

Connectors for hosts beyond the v1 Bitbucket Data Center reference —
GitHub, Bitbucket Cloud, GitLab — each a new adapter plus capability
manifest against the existing protocol, never a core change.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. Each new connector passes the protocol conformance suite from
   [ST-0019](ST-0019-code-host-connector-protocol.md) and declares an
   honest capability manifest (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md),
   [DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md)).
2. Richer host features (e.g. GitHub's path-scoped review rules)
   surface through the manifest for the gate compiler to exploit, and
   no host lands host-specific logic in core
   (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).

## Component Impact

None yet — one component per connector, stubbed at revival against
[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md).

## Out of Scope

The protocol and manifest schema
([ST-0019](ST-0019-code-host-connector-protocol.md)); the BBDC
reference ([ST-0020](ST-0020-bitbucket-data-center-connector.md)).
