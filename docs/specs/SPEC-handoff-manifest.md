# SPEC: Handoff Manifest

The machine-readable package Groundwork emits at its southern boundary:
the complete input the Swarm Orchestrator (DEC-0308) needs to dispatch
an Implementation Swarm over a set of approved components in parallel.
Generated, validated, and written by the Artifact Store (EP-0001);
topology supplied by the Graph Index (EP-0004); triggered via the
Inbound API (EP-0008) (DEC-0305). This spec supersedes the
component-list schema per DEC-0300/DEC-0302 (SES-0056).

## Format

One YAML file per handoff, generated (never hand-edited), pinned to a git
ref of the Canonical Store:

```yaml
manifest-version: 2
generated: 2026-09-01T14:00:00Z
canonical-ref: <git sha>              # all doc paths and bundles resolve at this ref
goal-context:
  goals: [BG-0001]                    # the intent everything traces to
  consolidations: [CON-0003]          # fresh consolidations for swarm use
shared-preamble: bundles/preamble.md  # single generated cross-cutting context
                                      # (reference stack, error model, repo
                                      # conventions) — DEC-0300
slices:                               # ordered; walking skeleton first (DEC-0302)
  - id: SL-0001
    doc: docs/slices/SL-0001-walking-skeleton.md
    status: approved
    work-packages: [WP-CMP-0001-storage, WP-CMP-0001-integration, ...]
work-packages:
  - id: WP-CMP-0001-storage           # element work package (DEC-0300)
    kind: element
    component: CMP-0001
    elements: [StorageService, Artifact]   # batched by the standalone criterion
    bundle: bundles/WP-CMP-0001-storage.md # generated projection
    stories: [ST-0002, ST-0001]
    depends-on:                        # typed edges (DEC-0299/DEC-0309)
      - {package: WP-CMP-0003-port, type: implementation}
      - {package: WP-CMP-0001-validator, type: interface}
  - id: WP-CMP-0001-integration        # integration work package (DEC-0301)
    kind: integration
    component: CMP-0001
    charter: [C-1, C-2, C-3, C-4, acceptance]
    depends-on:                        # all member element packages
      - {package: WP-CMP-0001-storage, type: implementation}
build-order:                           # topological tiers over implementation
  - [WP-CMP-0003-port]                 # edges ONLY; interface/test edges never
  - [WP-CMP-0001-storage, ...]         # serialize (DEC-0309)
```

## Rules

1. Only `approved` Component Docs and `approved` Slices may appear. Any
   `stale` ancestor of an included component invalidates the manifest.
2. `build-order` must be a valid topological sort over `implementation`
   edges; cycles are a generation error. `interface` and `test` edges
   constrain bundle contents, never ordering (DEC-0299, DEC-0309).
3. The manifest, bundles, and preamble are reproducible: same
   `canonical-ref` → identical output (DEC-0300).
4. Consumers must treat the manifest plus the docs at `canonical-ref` as
   the complete input. An implementing agent starts with its
   work-package bundle plus the Shared Preamble — empty conversational
   context; crawl of the pinned corpus sanctioned (DEC-0304). If an
   implementer needs information reachable neither in its bundle nor by
   crawl, that is a documentation defect to feed back into refinement
   (DEC-0011).
5. Work-package batching follows the standalone criterion (DEC-0300):
   an element is standalone iff it carries self-contained implementable
   A/B items; otherwise it rides with its enforcing/consuming element;
   protocols always standalone. Batching is generator logic — never
   hand-tagged.
6. Every component contributes exactly one integration work package
   (DEC-0301) depending on all its element work packages; its charter
   is the component's invariants and Acceptance & Test Expectations.
7. Bundle closure: every reference inside a generated bundle must
   resolve inside the bundle (DEC-0303); closure is checked at
   component gate time and again at generation.
