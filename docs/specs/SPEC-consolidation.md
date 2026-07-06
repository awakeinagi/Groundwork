# SPEC: Consolidation (CON)

Curated, derived reference material summarizing a frequently traveled path of
the artifact graph — Groundwork's memory layer. Consolidations exist to keep
agent context windows lean: an agent reads one Consolidation instead of
crawling a dozen artifacts ([DEC-0017](../decisions/DEC-0017-consolidation-memory-layer.md)).

Extends [SPEC-artifact-common](SPEC-artifact-common.md).

## Frontmatter additions

```yaml
type: consolidation
status: fresh | stale                 # reduced lifecycle
sources:                              # every artifact this consolidation
  - id: BG-0001                       # summarizes, pinned to the git ref
    ref: <git sha>                    # it was built from
  - id: EP-0002
    ref: <git sha>
audience: session-agent | implementation-swarm | human-reviewer
```

## Required body sections

1. **Path Covered** — which graph traversal this consolidation replaces
   (e.g., "BG-0001 → EP-0002 → its decisions, for agents refining stories").
2. **Consolidated Content** — the summary itself. Faithful to sources; no new
   claims. Anything load-bearing carries its artifact citation so a reader
   can drop to the source.
3. **Omissions** — what was deliberately left out, so a reader knows when to
   go to the sources instead.

## Freshness rules

- A Consolidation is `fresh` only while every source's current git ref
  matches its pinned `ref`. Any source change flips it to `stale` —
  mechanically, no judgment involved.
- Stale Consolidations are never served to agents; they are regenerated (or
  retired) by the memory maintenance process.
- Any user may **flag** a Consolidation from the UI; a flag quarantines it
  immediately (treated as stale) pending disposition — regenerate, fix
  sources, or correct the faithfulness checker. Confirmed misses become
  evaluation-corpus regression cases
  ([DEC-0072](../decisions/DEC-0072-consolidation-review-flagging.md)).
- Consolidations are derived artifacts: they can always be deleted and
  rebuilt from sources. Nothing may cite a Consolidation as provenance —
  provenance citations go to Decisions and Sessions only.
