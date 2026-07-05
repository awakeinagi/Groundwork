# SPEC: Epic (EP)

A coherent body of work derived from an approved Business Goal, refined with
Product Owners and Engineering/Data-Science Leads, and projected to Jira.

Extends [SPEC-artifact-common](SPEC-artifact-common.md).

## Frontmatter additions

```yaml
type: epic
jira-key: PROJ-123        # set once projected; absent before first sync
links:
  derives-from: [BG-....]
  satisfies: [BG-....]
```

## Required body sections

1. **Summary** — what this epic delivers and for whom; the text projected to
   Jira ([DEC-0013](../decisions/DEC-0013-jira-summary-plus-link.md)).
2. **Why (Goal Alignment)** — how this epic advances each linked Business
   Goal; the argument a reviewer checks at the gate.
3. **Scope** — in and out, at epic granularity.
4. **Domain Context** — the bounded context(s) this epic touches; new or
   sharpened glossary terms it introduced (with links to CONTEXT.md entries).
5. **Interfaces & Contracts to Define** — the API/data/behavior contracts the
   epic's stories and components will pin down.
6. **Risks & Open Questions** — including candidate Spikes.
7. **Derived Work** — Stories and Spikes derived from this epic (maintained
   as they are created).

## Rules

- Derivable only from an `approved` Business Goal; must be `approved` before
  Stories/Spikes are derived.
- Jira carries title, Summary, status, and a link back to this doc plus the
  ID in a custom field — never the full body
  ([DEC-0013](../decisions/DEC-0013-jira-summary-plus-link.md)). Drift
  detected in Jira is reconciled toward this doc
  ([DEC-0002](../decisions/DEC-0002-doc-store-canonical.md)).
