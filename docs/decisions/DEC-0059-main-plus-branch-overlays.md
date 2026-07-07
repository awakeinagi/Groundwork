---
id: DEC-0059
type: decision
title: The index maintains main as base plus an overlay per open item branch
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0007 @ T2-T3"
links:
  derives-from: [SES-0007]
---

# DEC-0059: Main + branch overlays

## Context

Under fork-pull ([DEC-0028](DEC-0028-fork-pull-pr-gating.md)) drafts live
on item branches; mid-session agents need graph queries over their drafts
in the context of approved reality, while impact analysis and manifests
must see only ratified truth.

## Decision

The index maintains main as the base view plus a lightweight overlay per
open item branch (the branch's additions/changes layered over main). Every
query names its view: session agents query their item-branch overlay;
impact analysis, Handoff Manifests, and Jira sync query main-only. Results
tag each node with ref and status so drafts cannot be mistaken for
approved artifacts.

## Rationale

One base graph with thin overlays gives both consumer classes the reality
they need without ambiguity — a flattened multi-branch graph makes every
traversal silently filter-dependent.

## Alternatives Considered

- **Main-only index**: context recipes ([DEC-0056](DEC-0056-context-recipes-in-packs.md))
  lose graph queries exactly when the agent is building new links.
- **Flattened multi-branch**: same artifact differing across branches makes
  answers ambiguous.

## Implications

Overlay lifecycle tracks item-branch lifecycle (created on branch open,
dropped on merge/abandon); overlay support is an [SP-0002](../spikes/SP-0002-graph-engine-selection.md) engine criterion.
