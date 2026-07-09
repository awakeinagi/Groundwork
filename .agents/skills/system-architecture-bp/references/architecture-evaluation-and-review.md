# Architecture Evaluation and Review

**When to reach for this:** Use when acting as pre-gate reviewer of a draft (business goal, epic, story, or component doc), when a stakeholder asks "is this design sound?", or when a significant technology choice needs vetting. It covers the full ATAM method and a lightweight scenario-based adaptation, the review culture that makes evaluation constructive, technology-selection scrutiny, and diagram-level checks. The quality-attributes reference supplies the scenario substance; this one supplies the process and the reviewer's question bank.

Constructed: 2026-07-09

---

## 1. Why evaluate before building

- The economic argument: design review identifies problems "when changes remain inexpensive" — Google's design-doc culture exists precisely to catch issues at the document stage, build consensus, and ensure cross-cutting concerns (security, privacy, observability) are considered before code ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)).
- Evaluation is **constructive, not an audit**: AWS frames Well-Architected review as "a constructive review process — not an audit mechanism — to identify improvements" ([AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)). A reviewer who produces a verdict without improvement paths has done half the job.
- Formal evaluation (ATAM) yields early risk identification, improved stakeholder communication, clarified quality requirements, better documentation, and a recorded rationale ([SEI, ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)).

## 2. ATAM: the reference method

Purpose: evaluate an architecture "relative to quality attribute goals," exposing how decisions support business objectives and **how quality attributes interact and trade off against each other** ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)). Full form: 3–4 days, trained evaluators plus architect plus stakeholder representatives.

The nine steps ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)):

1. **Present the ATAM** — set method and expectations.
2. **Present business drivers** — organizational goals and primary architectural drivers (e.g., availability, time-to-market, security).
3. **Present architecture** — the architect shows how the design addresses the drivers.
4. **Identify architectural approaches** — list the approaches/patterns in play, *without analyzing yet*.
5. **Generate the quality attribute utility tree** — decompose "utility" into quality factors, specify them as stimulus/response scenarios, prioritize.
6. **Analyze architectural approaches** — probe the high-priority scenarios; record risks, sensitivity points, trade-off points.
7. **Brainstorm and prioritize scenarios** — stakeholders broaden the scenario set; group voting prioritizes.
8. **Analyze again** — repeat step 6 with the top-voted stakeholder scenarios as test cases.
9. **Present results** — findings back to all stakeholders.

Vocabulary a reviewer should use precisely ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)):

- **Risk**: a decision that may inhibit a business goal. **Non-risk**: a decision shown to support its goals (record these too — they are the review's positive assurance).
- **Sensitivity point**: an element where one quality attribute is significantly affected.
- **Trade-off point**: a decision affecting *multiple* qualities in opposite directions — the highest-value places to interrogate.
- **Risk themes**: synthesized patterns showing how the risks jointly threaten specific business drivers — the executive summary of the evaluation.

## 3. Lightweight ATAM for a refinement gate

The full ceremony rarely fits a documentation-first refinement loop, but the *shape* compresses well (structure per [SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)):

1. Restate the business drivers from the goal/epic docs (step 2 analog).
2. List the architectural approaches the draft commits to (step 4 analog).
3. Take the prioritized quality scenarios from the quality-requirements section — or force their creation if absent (step 5 analog; scenario anatomy per [arc42 Quality Model](https://quality.arc42.org/)).
4. Walk each top scenario through the design, recording risks / non-risks / sensitivity points / trade-off points (step 6 analog).
5. Add 2–3 adversarial scenarios the authors did not choose — growth, failure, and change cases (step 7 analog).
6. Synthesize risk themes and map each back to the business driver it threatens (step 9 analog).

Deliver findings as: risks (with the driver threatened), trade-off points needing a stakeholder decision, non-risks (assurance), and concrete improvement paths ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/); [AWS WAF](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)).

## 4. Review culture and mechanics (from Google's practice)

([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/))

- The doc under review should center on **trade-offs**: "absence of discussed trade-offs suggests no doc was needed" — or that the thinking hasn't happened. A design presenting one option is a proposal, not a design.
- Look for **goals and non-goals** and **alternatives considered with rejection reasons**; these two sections are where reviewers add most value.
- Review breadth scales with stakes: lightweight circulation for routine designs, formal review meetings for contentious/high-blast-radius ones.
- Docs should be **updated when reality diverges** during implementation (before shipping) — a gate reviewer should ask what will trigger doc updates post-approval.
- Don't demand a design doc (or heavy review) when the solution is obvious, trade-offs are minimal, or the doc would be an implementation manual — review effort is a budget; spend it where designs are ambiguous or contentious ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)).

## 5. Technology-selection review: spend innovation tokens deliberately

From McKinley's "Choose Boring Technology" ([boringtechnology.club](https://boringtechnology.club/)):

- A company has roughly **three innovation tokens**; novel technology choices spend them. Spend on the core business problem, not on infrastructure novelty.
- Mature technology has smaller sets of both known and unknown failure modes: "it's bad, but you know why it's bad." New technology maximizes **unknown unknowns** — the operational surprises no one can test for in advance.
- "Adding the technology is easy, living with it is hard": evaluate total cost of ownership (operations, on-call, expertise, migrations), not development-time convenience.
- Gatekeeping questions for any new-technology proposal:
  1. How would we solve this **without adding anything new**?
  2. Is the stated problem real, or is it "we want to use Technology X"?
  3. What are the awkward-but-workable solutions with existing tools, and how does their burden compare to *operating* the new thing?
  4. If adopted: is there a low-risk pilot, a commitment to **replace** (not duplicate) the old tool, and a reversion plan?
- Anti-pattern to name in review: fragmented stacks ("polyglot persistence is not the kind of freedom we are looking for") and abandoning tools during their inevitable early-difficulty phase, yielding N half-adopted systems ([boringtechnology.club](https://boringtechnology.club/)).
- Counterweight: technology diversity has genuine benefits (right tool per problem, gradual migration) in organizations that can afford the operational spread — keep the portfolio deliberately small rather than zero ([Fowler, Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html)).

## 6. Reviewing the diagrams themselves

Bad diagrams cause confident misreadings. The C4 review checklist checks three layers ([C4 Model, Review Checklist](https://c4model.com/diagrams/checklist)):

- **Diagram-level**: does it have a title, an identifiable type/abstraction level, a defined scope, and a key/legend for every notation used?
- **Element-level**: does every element have a name, a clear abstraction level, and a stated purpose/responsibility — with visual choices (color, shape, borders, size) that carry meaning explained in the key?
- **Relationship-level**: is every line labeled with the *intent* of the relationship, direction unambiguous, and technology/protocol annotated where it matters?

A useful gate rule: any unlabeled arrow in a submitted diagram is an unasked design question ([C4 checklist](https://c4model.com/diagrams/checklist)).

## 7. Cloud-workload review lens

For deployment-shaped epics/components, the Well-Architected pillar questions form a ready cross-cutting sweep — reliability, security, cost, operations, performance (and sustainability on AWS) — with per-pillar checklists and trade-off pages ([AWS WAF](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html); [Azure WAF Pillars](https://learn.microsoft.com/en-us/azure/well-architected/pillars)). See the cloud-well-architected reference for the distilled pillar-by-pillar questions.

## 8. Adversarial scenario prompts

ATAM's step 7 exists because architects' own scenarios cluster around the happy path; stakeholder brainstorming broadens the set ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)). Prompts a reviewer can inject:

- **Growth**: traffic 10x; data 10x; a new client type (mobile/third party — the gateway mismatch problem, [microservices.io, API Gateway](https://microservices.io/patterns/apigateway.html)); a new market with new compliance rules ([Thoughtworks, Fitness Functions](https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development)).
- **Failure**: a dependency is down for an hour; the network partitions between two data owners — what operations block, which proceed and get compensated? ([Brewer, CAP](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)); a deploy goes bad mid-rollout ([Azure WAF Operational Excellence](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/)).
- **Change**: the business renames/restructures a core concept — how many components move? (common closure, [microservices.io](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html)); a component must be replaced wholesale — is there a seam/gateway to strangle it behind? ([Fowler, StranglerFig](https://martinfowler.com/bliki/StranglerFigApplication.html); [Uber DOMA](https://www.uber.com/blog/microservice-architecture/)).
- **Security**: a credential leaks; an insider queries data outside their mandate; an upstream package is compromised (supply chain — [Azure WAF Operational Excellence](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/); [Azure WAF Security](https://learn.microsoft.com/en-us/azure/well-architected/security/)).
- **Consumers**: a consumer starts depending on an undocumented field — would we know? (the consumer-contract visibility problem, [Robinson](https://martinfowler.com/articles/consumerDrivenContracts.html)).

## 9. Evaluation output template

Structure findings the way ATAM structures its outputs ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)):

1. **Business drivers assumed** — restated, so a wrong assumption is visible and cheap to correct.
2. **Approaches identified** — the architectural bets the draft actually makes.
3. **Scenario analysis table** — scenario → verdict → evidence in the draft.
4. **Risks** — each phrased as decision → threatened driver → suggested improvement path (constructive posture per [AWS WAF](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)).
5. **Non-risks** — decisions positively confirmed; the assurance half of the review.
6. **Sensitivity and trade-off points** — flagged for explicit stakeholder ratification.
7. **Risk themes** — the few patterns that summarize what the risks jointly threaten.

## 10. Review anti-patterns

- **Audit posture**: pass/fail verdicts without improvement paths — the opposite of the framework's stated intent ([AWS WAF](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)).
- **Reviewing prose instead of decisions**: a doc with no trade-offs discussed either needed no review or hides its real decisions — dig for them ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)).
- **Style purity nitpicking**: enforcing a constraint the workload should rationally relax ([Azure Architecture Styles](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/)).
- **Heavyweight review of the obvious**: demanding full ceremony where the solution is clear and trade-offs minimal — review effort is a budget ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)).
- **Skipping the non-risks**: recording only problems robs the team of confirmed ground to build on ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)).

## 11. Pre-gate reviewer checklist (composite)

Run top to bottom against any draft:

1. **Drivers**: are business drivers and the top 3–5 quality goals stated and prioritized? ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/); [arc42](https://arc42.org/overview))
2. **Alternatives**: were at least two real alternatives considered, with reasons for rejection? ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/))
3. **Trade-offs**: does every major decision name what it sacrifices? Identify the trade-off points and check a stakeholder accepted each ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)).
4. **Scenarios**: walk the top quality scenarios through the design; record risks and non-risks explicitly ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)).
5. **Adversarial cases**: add failure, growth, and change scenarios the authors didn't pick ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)).
6. **Cross-cutting concerns**: security, privacy, observability, operability addressed — the classically forgotten sections ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)).
7. **Technology choices**: for each novel dependency, run the boring-technology questions; count the tokens ([boringtechnology.club](https://boringtechnology.club/)).
8. **Style/constraint conformance**: are the chosen style's constraints stated and honored, not just named? ([Azure Architecture Styles](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/))
9. **Diagrams**: apply the C4 checklist; unlabeled relationships and missing legends are findings ([C4 checklist](https://c4model.com/diagrams/checklist)).
10. **Decision record**: are the decisions this draft embodies captured as ADRs with context and consequences, so the rationale survives the review? ([Nygard, Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions))
11. **Deliver constructively**: findings as risks-with-improvement-paths and open questions, never a bare pass/fail ([AWS WAF](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)).

## 12. Choosing the review weight

- Full ATAM is a 3–4 day, multi-stakeholder engagement — reserve that weight for architectures whose failure is expensive ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)).
- Google scales review from lightweight email circulation to formal design-review meetings based on how contentious and high-stakes the design is ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)).
- Well-Architected-style reviews are designed to be repeatable and continuous (tooling-assisted), not one-time ceremonies ([AWS WAF](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html); [Azure WAF Pillars](https://learn.microsoft.com/en-us/azure/well-architected/pillars)).
- Default mapping for a gated refinement flow: lightweight scenario walk (section 3) at every gate; full utility-tree treatment when a draft fixes system-shaping decisions; skip ceremony where the solution is obvious and trade-offs minimal ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/); [SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)).

## 13. Related references in this corpus

- `quality-attributes-and-tradeoffs.md` — the scenario and utility-tree substance this review process consumes.
- `documentation-practices.md` — what a reviewable draft should contain (ADRs, goals/non-goals, alternatives).
- `architecture-styles.md` — style smells and constraint-conformance checks used in step 8 of the checklist.
- `decomposition-and-seams.md` — the seam checklist for reviewing decompositions.
- `cloud-well-architected.md` — pillar question banks for cloud-shaped drafts.
- `evolutionary-architecture.md` — converting review findings into fitness functions that persist after the gate.
