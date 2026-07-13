---
id: DEC-0510
type: decision
title: "Three-way ownership split for the governance/ configuration files"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0094 @ T6–T9, T10–T11"
overview: >-
  The governance/ configuration files (roles.yaml, domains.yaml,
  gate-policies.yaml, people.yaml) sit at a three-epic junction with
  no single written owner-routing note. This decision records the
  three-way split that already follows from accepted decisions:
  schema and format belong to EP-0015 (DEC-0443); committed policy
  content belongs to EP-0014 (DEC-0484's tunable tables); evaluation
  machinery belongs to EP-0010 (DEC-0469). The files remain project-
  committed configuration the Engine reads, never Engine-defined
  schema, giving future intake on these files a written answer.
links:
  derives-from: [SES-0094]
  relates-to: [DEC-0443, DEC-0484, DEC-0469, DEC-0263]
---

# DEC-0510: Three-way ownership split for the governance/ configuration files

## Context

The governance/ files (roles.yaml, domains.yaml, gate-policies.yaml, people.yaml) sit at a three-epic junction, and a future change to them — for example adding a min-approvals field, versus setting its value in a project, versus teaching the checker to count approvals — had no single written owner-routing note, although each assignment follows from accepted decisions.

## Decision

EP-0014's body states the three-way ownership split: the files' schema and format belong to EP-0015 (DEC-0443); the committed policy content — the values the rule families consult — belongs to EP-0014 (DEC-0484's tunable tables); and the evaluation machinery belongs to EP-0010 (DEC-0469). The files remain project-committed configuration the Engine reads, never Engine-defined schema.

## Rationale

All three assignments already follow from accepted decisions; writing them in one findable place routes future intake without relitigating ownership.

## Alternatives Considered

Moving file-format ownership to EP-0010's artifact-model roster was rejected as contradicting DEC-0443 and dragging the approved Engine Core epic back into refinement. Leaving ownership unstated was rejected because the first file change would relitigate ownership under pressure.

## Implications

Intake classification for governance/ file changes has a written answer in EP-0014's body.
