---
id: ST-0028
type: story
title: Additional code-host connectors — Bitbucket Cloud, GitLab
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0019]
cites: [DEC-0045, DEC-0100, DEC-0156, DEC-0172]
---

# ST-0028: Additional Code-Host Connectors

> Deferred to `backlog` at creation (per
> DEC-0156,
> the deferral citation per
> DEC-0100).
> Subscribed to trigger TRG-0007 — a deployment requiring a code host
> other than GitHub revives it. GitHub itself moved from this bucket to
> v1 (ST-0031); Bitbucket Data Center
> moved the other direction, into its own dedicated deferred story
> (ST-0020, trigger
> `TRG-0010`) rather than this generic bucket, since it already had a
> fully-scoped story of its own
> (per DEC-0172).

## Summary

Connectors for hosts beyond the v1 GitHub reference — Bitbucket Cloud,
GitLab — each a new adapter plus capability manifest against the
existing protocol, never a core change.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. Each new connector passes the protocol conformance suite from
   ST-0019 and declares an
   honest capability manifest (per DEC-0045,
   DEC-0172).
2. Richer host features (e.g. GitLab's approval rules) surface through
   the manifest for the gate compiler to exploit, and no host lands
   host-specific logic in core
   (per DEC-0045).

## Component Impact

None yet — one component per connector, stubbed at revival against
CMP-0005.

## Out of Scope

The protocol and manifest schema
(ST-0019); the GitHub
reference (ST-0031); the deferred
Bitbucket Data Center reference
(ST-0020).
