---
id: IDEA-0047
type: idea
title: "Add a remove-cite operation to the write API"
status: taken-up
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi@gmail.com
overview: >-
  Surfaced during SES-0076's DEC-0267 cascade: the write API has no
  sanctioned way to remove a cites: entry, so a citer whose body
  legitimately stops mentioning a superseded decision would leave a
  dead-cite violation (DEC-0247's bidirectional rule) with no repair
  path. The cascade worked around it by retaining one body mention
  per artifact in the SPEC's superseding-citation convention. A
  remove-cite operation with appropriate guardrails would close this
  API-unreachable surface.
links:
  derives-from: [SES-0076]
  relates-to: [IDEA-0042, DEC-0247]
---

# IDEA-0047: Add a remove-cite operation to the write API

## The Idea

Add a `remove-cite` operation to the write API, with appropriate guardrails, so a citer can drop a `cites:` entry when its body legitimately stops mentioning a superseded decision.

## Spark Context

Surfaced during SES-0076's DEC-0267 cascade: the write API has no sanctioned way to remove a `cites:` entry, so a citer whose body legitimately stops mentioning a superseded decision would leave a dead-cite violation (DEC-0247's bidirectional rule) with no repair path. The cascade worked around it by retaining one body mention per artifact, per the SPEC's superseding-citation convention.

## Disposition

Taken up via SES-0077. DEC-0403 adds a `remove-cite` operation to the write API's operation set, following the DEC-0377 extension precedent, with the refusal conditions and `--amend` requirements this idea's spark called for.

