# SPEC: Session (SES)

The append-only record of one 1:1 refinement conversation between the agent
and one participant ([DEC-0021](../decisions/DEC-0021-one-on-one-sessions.md)).
Sessions are the raw material of provenance: Decisions cite spans of them
([DEC-0015](../decisions/DEC-0015-transcript-decision-citation-chain.md)).

Extends [SPEC-artifact-common](SPEC-artifact-common.md).

## Frontmatter additions

```yaml
type: session
participant: <named person>
participant-role: stakeholder | product-owner | eng-lead | ds-lead | arbiter
facilitator: <agent identity + model version>
transcript-fidelity: verbatim | reconstructed
links:
  relates-to: [BG-....]       # artifact(s) the session refined; may be empty
                              # for inception sessions that create the artifact
```

## Lifecycle

Sessions use a reduced lifecycle: `open → closed`. A closed session is
immutable. Follow-up conversation is a new Session linking
`relates-to` the same artifacts.

## Required body sections

1. **Purpose** — what the session set out to refine.
2. **Transcript** — the conversation, turn-numbered (`T1`, `T2`, …) so
   Decisions can cite spans (`SES-0042 @ T31–T38`). `verbatim` fidelity is
   the standard once the application hosts sessions; `reconstructed` is
   permitted only for pre-application bootstrap records and must say so.
3. **Decisions Produced** — the `DEC` records distilled from this session
   (maintained by the distillation step).
4. **Conflicts Raised** — `CFL` records opened during the session, if any.

## Rules

- Append-only: turns are never edited or deleted after the fact. Corrections
  happen in later turns or later sessions.
- Every Decision distilled from a session must cite a turn span that actually
  supports it.
- Multi-stakeholder input is achieved by Synthesis across separate 1:1
  sessions, not shared sessions ([DEC-0021](../decisions/DEC-0021-one-on-one-sessions.md)).
