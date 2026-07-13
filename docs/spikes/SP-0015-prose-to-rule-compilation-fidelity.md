---
id: SP-0015
type: spike
title: "Prose-to-rule compilation fidelity"
status: approved
approved-on: 2026-07-12
approved-by: awakeinagi
owner: awakeinagi@gmail.com
created: 2026-07-10
timebox: 1 session
overview: >-
  Question: can prose best-practice knowledge compile into checkable
  rules without corruption? Method: one bounded curated source (an
  arc42 section from system-architecture-bp, or a chapter extracted
  via a book-to-skill-style pipeline); an agent compiles it into
  candidate rules, each citing its source passage; stakeholder
  reviews rule-vs-passage side by side. Independent of
  SP-0013/SP-0014. Evaluation criteria: ratifiable-as-is rate;
  catalog of compilation failure modes (over-generalization, lost
  applicability conditions, invented specificity) -- explicitly no
  kill bar (DEC-0355). Data-source assumptions: source is
  curated/licensed content already in the corpus or explicitly
  provided; passage-level citations are resolvable. Deliverable:
  fidelity report. Re-affirmed approved under DEC-0441 (approved-by
  awakeinagi, approved-on 2026-07-12) after the SES-0085 staleness
  walk found it clean of the old charter.
links:
  derives-from: [EP-0009]
cites: [DEC-0354, DEC-0351, DEC-0335, DEC-0337, DEC-0355, DEC-0345, DEC-0336, DEC-0294]
---

> Guardrails (DEC-0351): this spike's outputs are strictly throwaway and are never deployed as part of the artifact interaction surface. Adoption of anything it surfaces happens only through the ordinary path -- a DEC-0337 option survey followed by DEC-0335 design intake -- never by this spike's findings alone.

## Question

Can prose best-practice knowledge compile into checkable rules without corruption? Concretely: when an agent compiles one bounded curated source into candidate rules, each citing its source passage, how often is the result ratifiable as-is, and what does it get wrong?

## Why It Blocks

Blocks nothing today. It is independent evidence for the compilation half of the executable-design-knowledge idea (DEC-0354) -- separate from SP-0014's hand-compiled rules, this spike tests whether an agent can do the compilation step itself faithfully, which matters for the approach scaling beyond a handful of hand-written rules.

## Method

Select one bounded curated source: an arc42 section from system-architecture-bp, or a chapter extracted via a book-to-skill-style pipeline. An agent compiles it into candidate rules, each citing the specific source passage it was compiled from. The stakeholder reviews each candidate rule against its cited passage, side by side.

This spike builds a throwaway executable; per DEC-0345, its validation approach (the checks described above) is part of the reviewed spike design, not chosen ad hoc after the fact, and is sized minimally per DEC-0336's throwaway-scope yardstick.

The system-architecture-bp corpus itself is the direct precedent for this compilation exercise: DEC-0294 established it as a curated, cited best-practice corpus, and it is this spike's source material.

**Source selected (SES-0064 T22).** The stakeholder selected the arc42-section route over the book-to-skill extraction alternative as this spike's bounded curated source, and selected a gate-approve-launch disposition path for this spike.

## Evaluation Criteria
Descriptive measures, no pass/fail threshold (DEC-0355): the ratifiable-as-is rate (fraction of candidate rules the stakeholder accepts without edits); a catalog of compilation failure modes observed (over-generalization, lost applicability conditions, invented specificity not present in the source).

## Data-Source Assumptions
The source passage is curated/licensed content already present in the corpus (e.g. system-architecture-bp's vendored arc42 material) or explicitly provided for this spike; passage-level citations are resolvable back to a specific location in the source so the stakeholder's side-by-side review is possible.

## Findings

**Source.** arc42 Section 5, Building Block View (lines 340-546 of the vendored arc42 template in the system-architecture-bp skill), chosen as the densest single section covering both decomposition and interface-contract guidance; compiled in full, not cherry-picked.

**Output.** 14 candidate rules -- roughly 3 structural-presence rules, 3 judgment-class rules, 5 guarded heuristics, 3 meta-constraints -- each with a verbatim passage, line citation, applicability conditions, and a compiler self-flagged confidence level. 9 further pieces of source content were correctly judged uncompilable rather than force-fitted into a rule shape. The full candidate-rule table is retained as throwaway evidence in the session scratchpad per DEC-0351, not committed to the corpus.

**Stakeholder side-by-side review** (the spike's measurement, rule vs. cited passage): 12 of 14 ratified in compiled form. R1, R3, R4, R5, R6, R13 ratified as-is. R7, R8, R11 ratified in their guarded compiled forms -- R8's guard fires only on author-flagged complex interfaces, with the finding phrased as "confirm a signature isn't sufficient" rather than a stronger claim; R11's guard restricts to author-supplied importance metadata only, explicitly rejecting graph-derived importance proxies. R2 and R9 were ratified but downgraded to advisory severity: both are definition-derived or source-optional content that should never fire as a violation. R14 was ratified as an LLM-judgment rule. R10 and R12 were reclassified as meta-guards on the ruleset itself rather than firing rules. Zero corrupted compiles were ratified.

**Failure-mode catalog** -- the spike's key deliverable, extending the three anticipated modes (over-generalization, lost applicability conditions, invented specificity):
(a) definition-to-imperative conversion (R2) -- a definitional sentence compiled into an imperative rule;
(b) benefit-to-imperative elevation from Motivation prose (R14) -- a stated benefit of a practice compiled as if it were a mandate;
(c) invented trigger criteria where the source prose delegates to human judgment (R8, R11) -- the compiler had to invent a firing condition the source never specified, caught only by guarding it;
(d) optional-content elevation (R9) -- source content marked as optional compiled as if mandatory;
(e) NOVEL -- contradiction-generating rule pairs: faithful compiles of R3 (completeness) and R11 (selectivity) conflict with each other unless the otherwise-uncompilable meta-principle R12 ("relevance over completeness") rides along as a guard on both;
(f) NOVEL -- template-vs-invariant genre effect: a documentation-template source (arc42) compiles mostly into presence checks rather than design-correctness invariants, so the checkable fraction of a source depends on its genre, not just its density.

**Bottom line.** Prose-to-rule compilation is viable only as a citation-preserving pipeline with stakeholder ratification in the loop -- the compiler's verbatim-passage discipline and its self-flagged interpretation points are precisely what made every guard catchable during review.

## Resulting Decisions

This spike's findings -- the ratifiable-as-is rate (12 of 14 candidate rules ratified, most as-is or in guarded/downgraded form), the failure-mode catalog, and the stakeholder's side-by-side rule-vs-passage review -- were recorded and ratified at SES-0064 (T22 disposition, gate-approve-launch path selected). No rule-adoption decision has actually been made: this spike is throwaway per its own guardrails (DEC-0351), and adopting anything it surfaces requires the ordinary DEC-0337 option survey followed by DEC-0335 design intake -- not this spike's findings alone. Rule-adoption decisions are deferred to SP-0016 preparation, per DEC-0354 (the governing program decision establishing this five-spike evaluation and the adoption path that follows it).

