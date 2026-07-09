# SPEC: Slice (SL)

A Slice is a first-class artifact (DEC-0302): a named, owned vertical
subset of work packages forming one end-to-end behavior (e.g. "gate an
artifact"), carrying the acceptance-criteria block that is the durable
home of end-to-end test expectations. Slices reference work packages
across components; they never regroup components (DEC-0307). The
Handoff Manifest references approved Slices in ordered sequence,
walking skeleton first (SPEC-handoff-manifest).

## Frontmatter additions

Beyond SPEC-artifact-common: standard lifecycle statuses
(`draft → gated → approved`), plus

```yaml
links:
  derives-from: [<SES or parent>]
  satisfies: [BG-....]              # the goal outcome the flow serves
  relates-to: [CMP-..., ST-...]     # components/stories the slice crosses
```

## Required body sections

- `## Behavior` — the end-to-end flow in prose: trigger, path through
  the system, observable output. One behavior per slice.
- `## Work Packages` — the ordered member list (element and integration
  work packages by manifest ID or component § element reference);
  within the slice, build-order topo-sorts lifted `implementation`
  edges (DEC-0309).
- `## Acceptance Criteria` — numbered `SL-<n>.AC-<m>` items, each
  testable against the assembled slice and each citing a `DEC-`
  (contract content like any other). These are what the Swarm
  Orchestrator (DEC-0308) executes and reports against.

## Rules

1. A slice is gated and approved like any artifact; only `approved`
   slices enter the manifest.
2. Every acceptance criterion cites at least one Decision.
3. Slice membership references work packages (dispatch-time), never
   raw element regrouping (design-time) — components remain the gate
   unit (DEC-0307, DEC-0298).
4. The first approved slice per release is the walking skeleton: the
   thinnest end-to-end path that runs (SES-0055 F9 disposition).
