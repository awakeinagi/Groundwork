---
id: DEC-0294
type: decision
title: The system-architect knowledge corpus lives in a dedicated system-architecture-bp companion skill — curated cited distillation plus vendored arc42 and awesome-software-architecture; free-to-read canon summarized, never vendored
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0054 @ T7-T12"
overview: >-
  The system-architect agent's preloaded knowledge lives in a
  dedicated companion skill, system-architecture-bp, which the agent
  definition loads — mirroring the overview-writer/groundwork-overview
  precedent (agent = who, skill = what it knows). Contents: a curated,
  cited best-practices distillation; a vendored copy of the arc42
  template and guidance (CC-BY-SA 4.0, ShareAlike preserved on copies
  and adaptations); and a vendored copy of the
  awesome-software-architecture curated index (CC0). Free-to-read
  canon — c4model.com, martinfowler.com catalogs, microservices.io,
  AWS and Azure Well-Architected — is summarized with citations, never
  vendored; the Google Cloud Well-Architected Framework (CC BY 4.0)
  may be derived from with attribution. Sourcing grounded in the
  licensing research at SES-0054 T4.
links:
  derives-from: [SES-0054]
  relates-to: [DEC-0292, DEC-0295]
---

# DEC-0294: The `system-architecture-bp` Companion Skill

## Context

IDEA-0003 specifies a context "preloaded with best practices". The
licensing research (SES-0054 T4) found the canon splits three ways:
permissively licensed texts (arc42 CC-BY-SA 4.0, Google Cloud
Well-Architected Framework CC BY 4.0, awesome-software-architecture
CC0), free-to-read but unlicensed-for-reuse pages (c4model.com,
martinfowler.com, microservices.io, AWS/Azure Well-Architected), and
copyrighted material unavailable for preloading (ISO/IEC/IEEE
42010/42020/42030, canonical books).

## Decision

The knowledge corpus lives in a **dedicated companion skill,
`system-architecture-bp`**, loaded by the system-architect agent
definition — the overview-writer/groundwork-overview precedent:
agent = who, skill = what it knows. Contents:

- a **curated, cited distillation** of architecture and design best
  practices (constructed per DEC-0295);
- **vendored arc42** template + guidance, with CC-BY-SA 4.0 preserved
  on our copies and any adaptations, attributed;
- the **vendored awesome-software-architecture index** (CC0) as a
  public-domain map of the wider literature.

Free-to-read canon is **summarized with citations, never vendored**.
The Google Cloud Well-Architected Framework (CC BY 4.0) may be
derived from with attribution rather than vendored wholesale.
Copyrighted standards and books are cited as pointers only.

## Rationale

A dedicated skill keeps the facilitator's skill lean, is reusable
across projects, and syncs to the vendored .agents copy like the rest
of the method. Vendoring only permissively licensed texts keeps the
corpus license-clean, offline, and auditable; summarize-with-citation
captures the unlicensed canon's substance without reuse risk. The
content-named skill (`system-architecture-bp` rather than the
groundwork-* family convention) was the stakeholder's naming call
(SES-0054 T12).

## Alternatives Considered

- **Inside the groundwork-design-session skill** — rejected: bloats
  the facilitator's skill with content only the specialist needs.
- **In the project docs/ tree** — rejected: method knowledge, not
  project design; would need re-seeding into every future project.
- **Live fetch at invocation** — rejected: slow, costly,
  network-dependent, non-reproducible grounding.
- **Model-internal knowledge only** — rejected: unauditable and not
  "preloaded" as IDEA-0003 states.

## Implications

A new skill directory (`system-architecture-bp`) joins the method
surface and the project's vendored .agents skill copy, carrying
third-party licensed material for the first time — CC-BY-SA
attribution and ShareAlike obligations attach to the arc42 files and
any adaptation of them, and a license notice must travel with the
vendored texts. The system-architect agent definition (DEC-0292)
loads this skill; corpus content changes only via the DEC-0295
pipeline and its ratification rule.
