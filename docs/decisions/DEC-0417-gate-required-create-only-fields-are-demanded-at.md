---
id: DEC-0417
type: decision
title: "Gate-required create-only fields are demanded at artifact creation"
status: accepted
owner: awakeinagi
created: 2026-07-12
decided-by: awakeinagi (session SES-0081)
decided-on: 2026-07-12
overview: >-
  op_create now refuses any artifact type whose REQUIRED_AT_CREATE
  table row lists frontmatter fields not supplied via --field,
  generalizing the session-close field trap SES-0079 surfaced into a
  single declarative extension point (currently one row: session,
  listing the four SESSION_CLOSE_FIELDS). The refusal names the
  type, missing fields, and --field syntax, and runs after per-field
  value validation so value errors keep precedence. Session close's
  own field-presence check remains as a backstop, reading the same
  constant. Stakeholder awakeinagi approved the generalized design
  verbatim at SES-0081 after asking whether the session-only fix
  could be handled for all artifact types. Future trap-types are a
  one-line table row with automatic test coverage via the table-
  driven guard test.
links:
  derives-from: [SES-0081]
  relates-to: [DEC-0313, DEC-0402]
---

# DEC-0417: Gate-required create-only fields are demanded at artifact creation

## Context

SES-0079's close was refused because it lacked frontmatter that only the
create operation can write — participant, participant-role, facilitator,
and transcript-fidelity — and no post-creation write path existed to add
them retroactively, forcing an operator direct edit outside the typed API.
SES-0081's generalization audit walked every lifecycle gate in the write
path and found the general shape of this trap: a field is a creation trap
only when a later gate requires it and only create can write it. Applied
across the corpus, session close's four fields are the sole current trap —
accepted-in, approved-by/approved-on, superseded-by, and release are all
stamped or settable by set-status itself, and decided-by/source-span/
timebox/sponsor are demanded by no gate. Stakeholder awakeinagi asked
whether this could be handled more generally for all artifact types, with
required fields demanded at creation rather than caught later.

## Decision

`op_create` refuses to create any artifact whose type has a
`REQUIRED_AT_CREATE` table row listing fields not supplied via `--field`.
The table is the single extension point for this guard — currently one
row, sessions, listing the four `SESSION_CLOSE_FIELDS`
(participant, participant-role, facilitator, transcript-fidelity). The
refusal names the missing fields and the `--field` flag syntax needed to
supply them. The guard runs after per-field value validation, so an
existing bad-value error keeps precedence over a missing-field refusal.
Session close's own field-presence check remains in place as a backstop,
and both the create-time guard and the close-time check read the same
`SESSION_CLOSE_FIELDS` constant so they cannot drift apart.

## Rationale

An artifact born un-gateable does not fail loudly at the moment of the
mistake — it surfaces hours or sessions later as a refused close or a
refused approval, at which point the only route back into compliance is
an API-unreachable repair (IDEA-0042 class), an operator direct edit
outside the sole-sanctioned-write-path invariant (DEC-0312). Demanding
the fields at the door converts that delayed, confusing failure into an
immediate, self-explaining refusal at the exact moment the caller has all
the information needed to supply them.

## Alternatives Considered

A session-only hardcoded guard (checking only session-typed creates,
inline, with no table) was rejected: it would fix today's known trap but
rebuild the same blind spot for the next artifact type that grows a
create-only, gate-required field. A general post-creation `set-field`
operation, letting any artifact's frontmatter be edited after creation,
was rejected as reopening frontmatter-immutability questions the write
API deliberately closed (DEC-0312, DEC-0313) — it would trade one
narrow, well-scoped guard for a much larger new mutation surface.

## Implications

Future trap-types — an artifact type that grows a field required by some
later gate, writable only at create — are addressed with a one-line
`REQUIRED_AT_CREATE` table row, and the existing table-driven guard test
(`test_required_at_create_fields`) automatically covers the new row with
no new test code. Librarians must supply all four session close fields
via `--field` at every session `create` call going forward; there is no
retroactive path if they are omitted.
