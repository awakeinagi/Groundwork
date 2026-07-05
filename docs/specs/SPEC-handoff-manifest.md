# SPEC: Handoff Manifest

The machine-readable package Groundwork emits at its southern boundary: the
complete input an Implementation Swarm needs to build a set of approved
components in parallel ([DEC-0014](../decisions/DEC-0014-docs-are-the-product.md)).
This is an interface contract — swarm orchestration itself is out of scope.

## Format

One YAML file per handoff, generated (never hand-edited), pinned to a git ref
of the Canonical Store:

```yaml
manifest-version: 1
generated: 2026-09-01T14:00:00Z
canonical-ref: <git sha>              # all doc paths resolve at this ref
goal-context:
  goals: [BG-0001]                    # the intent everything traces to
  consolidations: [CON-0003]          # fresh consolidations for swarm use
components:
  - id: CMP-0004
    doc: docs/components/CMP-0004-ingestion.md
    status: approved
    approved-by: [j.chen]
    depends-on: [CMP-0002]            # build-order edges
    stories: [ST-0102, ST-0103]       # the work items being satisfied
build-order:                          # topological order over depends-on;
  - [CMP-0002]                        # components in the same tier may be
  - [CMP-0004, CMP-0005]              # built in parallel
```

## Rules

1. Only `approved` Component Docs may appear. Any `stale` ancestor of an
   included component invalidates the manifest.
2. `build-order` must be a valid topological sort of the `depends-on` graph;
   cycles are a generation error.
3. The manifest is reproducible: same `canonical-ref` → identical manifest.
4. Consumers must treat the manifest plus the docs at `canonical-ref` as the
   complete input. If an implementer needs information not reachable from
   there, that is a documentation defect to feed back into refinement — the
   iterative path toward fully self-contained component docs
   ([DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md)).
