# SPEC: Decision (DEC)

The unit of provenance: a distilled, attributable decision extracted from a
Session (or produced by a Spike's findings). Contracts, requirements, and
acceptance criteria cite Decisions; Decisions cite their source
(DEC-0015).

Extends [SPEC-artifact-common](SPEC-artifact-common.md).

## Frontmatter additions

```yaml
type: decision
status: proposed | accepted | superseded     # reduced lifecycle
decided-by: <named person>                   # whose authority the decision carries
decided-on: 2026-07-05
source-span: "SES-0001 @ T12-T14"            # turns supporting the decision;
                                             # "SP-0003 findings" for spikes
links:
  derives-from: [SES-....]                   # or [SP-....]
  supersedes: []                             # earlier decision(s) replaced
```

## Required body sections

1. **Context** — the question that had to be answered, and why it arose.
2. **Decision** — one unambiguous statement. If it takes more than a short
   paragraph, it is probably several decisions.
3. **Rationale** — why this option, in the decider's terms.
4. **Alternatives Considered** — what was rejected and why (brief).
5. **Implications** — known consequences for other artifacts, if any.

## Rules

- Decisions are immutable once `accepted`. Changing course means a new
  Decision with `supersedes` set; Impact Analysis then walks everything that
  `cites` the superseded Decision and marks it `stale`.
- ADR discipline applies to significance: record decisions that are hard to
  reverse, surprising without context, or genuine trade-offs. Routine
  clarifications live in the artifact body, not as DEC records.
- One decision per record. Compound decisions defeat citation granularity.
