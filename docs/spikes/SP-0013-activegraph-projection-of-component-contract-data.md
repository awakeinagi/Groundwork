---
id: SP-0013
type: spike
title: "ActiveGraph projection of component contract data"
status: approved
approved-on: 2026-07-10
approved-by: awakeinagi@gmail.com
owner: awakeinagi@gmail.com
created: 2026-07-10
timebox: 1 session
overview: >-
  Question: does the existing component corpus project cleanly onto
  ActiveGraph typed objects and relations? Method: a throwaway
  script projects the 16 CMP docs -- typed design elements, element-
  scoped contract items (Element.K-n, C-n, IG-n), typed Uses: edges
  (interface/implementation/test), and per-item DEC citations --
  into an ActiveGraph run as typed objects/relations with
  provenance; validation is a round-trip count against the docs.
  Timebox: one session. Evaluation criteria: fraction of contract
  items projected cleanly, fraction of Uses edges with type
  qualifier preserved, per-item citation provenance preserved, and a
  concrete gap list of design information the docs carry that the
  projection cannot express -- descriptive, no pass/fail bar
  (DEC-0355). Data-source assumptions: the approved CMPs conform to
  SPEC-component/SPEC-design-elements; read-only direct parse of
  docs/ files is sanctioned for throwaway spike scope, to be
  confirmed at execution intake. Proceeds fully separate from
  SP-0007 per DEC-0357. Deliverable: findings report.
links:
  impacts: [SP-0014]
  derives-from: [EP-0009]
  relates-to: [SP-0007]
cites: [DEC-0354, DEC-0351, DEC-0357, DEC-0160, DEC-0335, DEC-0336, DEC-0337, DEC-0345, DEC-0355, DEC-0309, DEC-0299, DEC-0081, DEC-0087, DEC-0340]
---

> Guardrails (DEC-0351): this spike's outputs are strictly throwaway and are never deployed as part of the artifact interaction surface. Adoption of anything it surfaces happens only through the ordinary path -- a DEC-0337 option survey followed by DEC-0335 design intake -- never by this spike's findings alone.

## Question

Does the existing component corpus project cleanly onto ActiveGraph typed objects and relations? Concretely: can the 16 CMP docs' typed design elements, element-scoped contract items (`Element.K-n`, `C-n`, `IG-n`), typed `Uses:` edges (interface/implementation/test), and per-item DEC citations be projected into an ActiveGraph run as typed objects and relations with provenance, without losing information the docs carry?

## Why It Blocks

Blocks nothing today. It is the foundation the other four spikes build on: SP-0014 (SP-B)'s rules fire over this spike's projected graph, so its coverage stats gate what those rules can see. It is design input to whether the executable-design-knowledge approach (DEC-0354) is worth pursuing further.

## Method

A throwaway script projects the 16 CMP docs into an ActiveGraph run: typed design elements as typed objects, element-scoped contract items (`Element.K-n`, `C-n`, `IG-n`) as typed objects with provenance back to their source line, typed `Uses:` edges (interface/implementation/test) as typed relations, and per-item DEC citations as provenance edges. Validation: round-trip counts -- for each CMP, the number of elements/items/edges the parser found versus a hand count from the doc.

The projection implements DEC-0309's Uses-edges-source-of-truth / depends-on-projection contract: the docs remain the source of truth and the ActiveGraph run is a derived projection, never a second store. Edge typing follows DEC-0299's typed Uses vocabulary (interface/implementation/test). Contract-item nodes are keyed using DEC-0081's element-scoped contract-item IDs (`Element.K-n`, `C-n`, `IG-n`), and the parser's premise that elements are parseable body headings (DEC-0087) is what makes the whole extraction possible.

## Note on SP-0007

This spike proceeds fully separate from SP-0007 (the draft spike DEC-0160 deferred contract-item-level graph nodes to). The parse-scope overlap -- both spikes parse Component Doc contract items -- was identified at SES-0064 T10 and the duplication deliberately accepted by the stakeholder (DEC-0357). SP-0007 remains draft under its original EP-0004 scoping, unmodified; this spike's scope does not reference SP-0007's design or vice versa.

## Validation Note

This spike builds a throwaway executable; per DEC-0345, its validation approach (the round-trip / precision checks described above) is part of the reviewed spike design, not chosen ad hoc after the fact, and is sized minimally per DEC-0336's throwaway-scope yardstick.

## Evaluation Criteria
Descriptive measures, no pass/fail threshold (DEC-0355): the fraction of contract items projected cleanly; the fraction of `Uses:` edges with their type qualifier (interface/implementation/test) preserved; whether per-item citation provenance is preserved end to end; and a concrete gap list -- design information the docs carry that the projection cannot express.

## Data-Source Assumptions

The approved CMPs conform to SPEC-component and SPEC-design-elements (parseable element headings, Implements/Uses lines, per-item citation clauses). Read-only direct parse of `docs/` files is sanctioned for throwaway spike scope -- to be confirmed at execution intake, not assumed pre-authorized by this record alone.

DEC-0340's agent-contract profile is deliberately outside this projection's scope: the 16 CMPs carry no profiles until the EP-0009 backfill lands, so the projection does not attempt to model it. The read-only direct-parse-of-`docs/`-files assumption above is now CONFIRMED at execution intake by the operator's explicit instruction to execute this spike (SES-0064 T19).

## Findings

Pending — recorded at spike completion.


## Resulting Decisions

Pending — a completed spike produces at least one decision, even "assumption confirmed, no change."
