# SPEC: Spike (SP)

A research unit derived from an Epic: a question that must be answered before
sibling Stories or Component Docs can be trusted. A spike's product is not
code — it is Decision records.

Extends [SPEC-artifact-common](SPEC-artifact-common.md).

## Frontmatter additions

```yaml
type: spike
jira-key: PROJ-789
timebox: 3d                 # agreed effort bound
release: backlog            # optional target release; absent = current release
links:
  derives-from: [EP-....]   # or [BG-....] for cross-cutting, process-level
                            # spikes that exist before any epic is approved
                            # (per DEC-0027)
  satisfies: [BG-....]
  relates-to: [ST-....]     # sibling work whose assumptions are at stake
```

## Required body sections

1. **Question** — the specific uncertainty to resolve, phrased so that an
   answer is recognizable.
2. **Why It Blocks** — which assumptions in which artifacts hinge on the
   answer.
3. **Method** — how the question will be investigated (prototype, data audit,
   vendor eval, literature).
4. **Findings** — filled at completion: what was learned, with evidence.
5. **Resulting Decisions** — the `DEC` records distilled from the findings
   ([DEC-0023](../decisions/DEC-0023-spike-findings-become-decisions.md)).

## Rules

- A completed spike must produce at least one Decision record (its
  `derives-from` pointing at this spike) — even "assumption confirmed, no
  change" is a Decision worth recording.
- Publishing a spike-sourced Decision triggers Impact Analysis; affected
  siblings are marked `stale` automatically
  ([DEC-0007](../decisions/DEC-0007-impact-analysis-stale-marks.md)).
- **Release scoping** (see
  [SPEC-artifact-common](SPEC-artifact-common.md) § Release scoping): a
  spike whose question matters later, not now, is `deferred` with a
  `release:` label
  ([DEC-0104](../decisions/DEC-0104-deferred-extends-to-spikes.md)); its
  parent epic's label is the default. A deferred spike blocks nothing
  and its "Why It Blocks" section says so. Revival conditions belong in
  the [trigger registry](../TRIGGERS.md)
  ([DEC-0106](../decisions/DEC-0106-trigger-registry.md)); deferral and
  revival each cite a Decision
  ([DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)).
