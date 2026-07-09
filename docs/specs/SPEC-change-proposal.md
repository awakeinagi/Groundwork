# SPEC: Change Proposal (CP)

A lightweight artifact capturing a change someone proposed from *outside*
the refinement pipeline — a direct Jira edit, a UI suggestion, or (future)
implementation-swarm feedback — so the intent survives redirection into the
proper flow and every proposal has a durable triage record
(DEC-0047).

Extends [SPEC-artifact-common](SPEC-artifact-common.md).

## Frontmatter additions

```yaml
type: change-proposal
source: jira-drift | ui-suggestion | implementation-feedback
proposed-by: <person-id>
triage: pending | mechanical | session | rejected
links:
  relates-to: [EP-....]      # the target artifact(s) the change concerns
```

## Lifecycle

CPs use the `triage` field, not the common status lifecycle: created
`pending`; the session agent triages to `mechanical` (trivial — a
mechanical-fix PR is opened citing the CP), `session` (substantive — a
refinement session is opened with the CP as input, and the proposer is
invited), or `rejected` (with rationale). Terminal states persist; CPs are
never deleted.

## Required body sections

1. **Proposed Change** — the captured diff or suggestion, verbatim.
2. **Context** — where and how the proposal arose (e.g., the Jira issue and
   field, the drift event).
3. **Triage Outcome** — filled at triage: the classification, rationale,
   and links to the resulting PR, session, or rejection reasoning.

## Rules

- CPs are created by connectors and the UI via typed operations
  (DEC-0033); they never
  modify their target artifact directly — the mechanical-fix PR or
  refinement session does, citing the CP.
- A Decision produced by a CP-triggered session cites the session normally;
  the session's record links `relates-to` the CP, preserving the chain
  proposer → CP → session → Decision.
