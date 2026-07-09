---
id: DEC-0278
type: decision
title: The intake authority check lives in the guardrails story, and the CP source enum gains unauthorized-attempt
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0278 constrains the intake authority check to ST-0035 (guardrails
  and authority limits): at intake open, the engine resolves the
  proposer's decision rights through the governance-config lookup ST-0035
  AC3 defines; a failed check halts intake and writes a CP with new source
  unauthorized-attempt via the existing create-change-proposal operation.
  SPEC-change-proposal's source enum and ST-0039 AC1 gain the value. This
  reuses existing seams with no new machinery.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0052 @ T6-T7"
links:
  derives-from: [SES-0052]
  relates-to: [DEC-0054, DEC-0262]
---

# DEC-0278: Authority check in ST-0035; a new CP source

## Context

DEC-0255 step 4: an instruction outside the instructor's decision
rights proceeds no further — a CP captures the attempt verbatim
awaiting the authority holder(s) (DEC-0262). The application's CP
source enum (`jira-drift | ui-suggestion | implementation-feedback`)
has no such source, and two stories could plausibly own the check.

## Decision

ST-0035 (guardrails and authority limits) owns the intake authority
check: at intake open the engine resolves the proposer's decision
rights through the governance-config lookup ST-0035 AC3 already
defines; a failed check halts intake and writes a CP with new source
**`unauthorized-attempt`** via the existing `create-change-proposal`
typed operation. SPEC-change-proposal's source enum and ST-0039 AC1's
enumeration gain the value. CMP-0001's operation signatures do not
enumerate sources, so no component amendment is needed.

## Rationale

Reuses both existing seams — the rights lookup and the typed CP write —
with no new machinery. Splitting authority logic into ST-0032 would
duplicate ST-0035 AC3.

## Alternatives Considered

- **Engine-level check in ST-0032**: splits authority logic across two
  stories.
- **Log without capturing**: contradicts DEC-0262 — the attempt must
  be preserved verbatim awaiting the authority holders.

## Implications

ST-0035 gains the intake-check AC; ST-0039 AC1 and
SPEC-change-proposal carry the widened enum; the engine's open
sequence (DEC-0273) calls the check before any grilling.
