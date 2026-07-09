# Architecture Documentation Practices: ADRs, arc42, C4, Design Docs

**When to reach for this:** Use when advising how a design should be *recorded* — which decisions deserve an ADR, what a component or system doc should contain, which diagram belongs at which abstraction level and audience, and how to keep documentation from rotting. In a documentation-first method the docs are the product of refinement, so this reference also serves as a quality bar for the artifacts themselves.

Constructed: 2026-07-09

---

## 1. Principles that recur across all four practices

- **Document decisions and rationale, not just structure.** New team members otherwise face code without "why"; decisions unrecorded get blindly changed or fearfully preserved ([Nygard, Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)). Google's design docs likewise emphasize "explaining *why* rather than implementation details" ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)).
- **Small, modular documents beat large specifications** — they stay current and stay read; ADRs deliberately keep each record to a page or two ([Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)); Google's sweet spot is 10–20 pages for large projects and 1–3 page mini-docs for incremental work ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)).
- **Fixed abstraction levels prevent the classic diagram failures** — mixed abstraction levels, inconsistent notation, unclear relationships are exactly what C4's leveled model exists to eliminate ([C4 Introduction](https://c4model.com/introduction)).
- **Don't hand-write what can be generated**: formal interface specs in prose "get outdated quickly" ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)); C4 recommends automating component-diagram generation to keep them current ([C4 Component Diagram](https://c4model.com/diagrams/component)); Stripe generates changelogs and per-user docs from first-class version metadata ([Stripe, API Versioning](https://stripe.com/blog/api-versioning)).

## 2. Architecture Decision Records (ADRs)

Nygard's format — the industry default ([Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)):

| Section | Content | Discipline |
|---|---|---|
| Title | Short noun phrase, numbered sequentially | Numbers are never reused |
| Context | The forces at play — technological, political, social, project-local — described **value-neutrally** | Facts, not advocacy |
| Decision | The response, stated in **active voice** ("We will …") | One decision per record |
| Status | Proposed / accepted / deprecated / superseded | Superseded records stay visible with a pointer forward |
| Consequences | **All** resulting outcomes — positive, negative, and neutral | The most-skipped, most-valuable section |

Practices around the format ([Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)):

- Record decisions that are **architecturally significant** — those affecting structure, non-functional characteristics, dependencies, interfaces, or construction techniques.
- Records are **immutable in intent**: don't rewrite history; supersede with a new record so the reasoning trail survives.
- Keep them **in the repository** with the code they govern, so they travel with checkouts and diffs.
- The audience is the future team: "a new team member can read through the decision log and understand how the system got to where it is."
- arc42 reserves its section 9 for exactly these records — "important, expensive, or risky decisions with rationales" ([arc42 Overview](https://arc42.org/overview)).

**Advisory check:** if a refinement session made a choice between real alternatives and no decision record exists, the session's output is incomplete ([Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)).

## 3. arc42: the system-level table of contents

The 12 sections and what each carries ([arc42 Overview](https://arc42.org/overview)):

1. **Introduction & Goals** — driving requirements, top 3–5 prioritized quality goals, stakeholder table with expectations.
2. **Constraints** — organizational, regulatory, technical limits on the solution space.
3. **Context & Scope** — system boundary and external interfaces, business perspective first.
4. **Solution Strategy** — the handful of fundamental decisions: technology choices, top-level decomposition, quality-goal approaches.
5. **Building Block View** — static decomposition, hierarchical white-box/black-box refinement.
6. **Runtime View** — behavior of building blocks in key scenarios, including error/operations cases.
7. **Deployment View** — infrastructure, environments, mapping of software to hardware.
8. **Crosscutting Concepts** — domain model, patterns, rules applied across components.
9. **Architectural Decisions** — the ADR log.
10. **Quality Requirements** — quality tree and scenarios, expanding section 1's goals.
11. **Risks & Technical Debt** — known problems, stated honestly.
12. **Glossary** — the ubiquitous language, term by term.

Usage guidance: arc42 is explicitly pragmatic — fill sections as needed rather than exhaustively ([arc42 Overview](https://arc42.org/overview)). Mapping note for goal→docs pipelines: sections 1–3 correspond to business-goal/epic material; 4–8 to component-level structure and behavior; 9–11 are cross-stage ledgers that grow continuously ([arc42 Overview](https://arc42.org/overview)).

The two frameworks compose naturally: arc42 answers *what to write down* (the table of contents), C4 answers *how to draw the structural parts* — a context diagram serves section 3 (context & scope) and container/component diagrams serve section 5 (building block view), since both frameworks fix scope-per-level in the same way ([arc42 Overview](https://arc42.org/overview); [C4 Introduction](https://c4model.com/introduction)).

## 4. C4: diagrams at four fixed zoom levels

The model: four hierarchical levels — **System Context, Container, Component, Code** — navigable like map zooming, each with a defined scope and audience ([C4 Introduction](https://c4model.com/introduction)). Uses: team communication, onboarding, architecture reviews, risk/threat identification ([C4 Introduction](https://c4model.com/introduction)).

| Level | Shows | Audience | Guidance |
|---|---|---|---|
| 1. System Context | The system centered among users and neighboring systems; no technology detail | Everyone, including non-technical | "Recommended for all teams"; the entry-point diagram ([C4 System Context](https://c4model.com/diagrams/system-context)) |
| 2. Container | Applications and data stores, technology decisions, responsibility distribution | Technical: architects, developers, ops | Also recommended standard practice; deliberately excludes deployment concerns (clustering, failover) as separate ([C4 Container](https://c4model.com/diagrams/container)) |
| 3. Component | Inside one container: components, responsibilities, technologies | Architects and developers | Automate generation rather than hand-maintain ([C4 Component](https://c4model.com/diagrams/component)) |
| 4. Code | Class-level detail | Developers, on demand | Rarely worth drawing manually ([C4 Introduction](https://c4model.com/introduction)) |

Every diagram, at any level, should pass the C4 review checklist: title, scope, key/legend; named elements with purposes; labeled, directed relationships with technology annotations ([C4 Review Checklist](https://c4model.com/diagrams/checklist)).

**Fit with artifact trees:** context diagram ≈ business-goal/epic scope; container diagram ≈ epic/story-level decomposition; component diagram ≈ component-doc internals ([C4 Introduction](https://c4model.com/introduction); [C4 Container](https://c4model.com/diagrams/container)).

## 5. Design docs: the exploratory front-end

Where arc42/C4 record the *resulting* architecture, a design doc captures the *exploration*. Google's anatomy ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)):

- Sections: context and scope (succinct, objective); **goals and non-goals**; the design itself (where trade-offs live); **alternatives considered** (with rejection reasons); **cross-cutting concerns** (security, privacy, observability).
- Include: system-context diagrams, API *sketches* (design-relevant parts only), high-level data storage approach. Exclude: formal interface specs, full schemas, code listings — they rot.
- Lifecycle: rapid collaborative iteration → wider review → **update during implementation when reality diverges** (before shipping) → serve as institutional memory.
- Write one when 3+ of: design approach uncertain; senior input valuable beyond code review; ambiguous/contentious problem; team forgets cross-cutting concerns; legacy thinking needs recording. Skip when the solution is obvious or the doc would be an implementation manual ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)).

## 6. Anti-rot practices

- **Update-before-ship**: divergence between doc and implementation is corrected as part of delivery, not as later cleanup ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)).
- **Supersede, don't edit history**: changed decisions get new ADRs pointing back ([Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)).
- **Generate what you can**: component diagrams, changelogs, API reference ([C4 Component](https://c4model.com/diagrams/component); [Stripe](https://stripe.com/blog/api-versioning)).
- **Keep docs next to code** in version control so they branch, review, and travel together ([Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)).
- **Glossary discipline**: maintain the term list per bounded context — the glossary is where model boundaries become visible ([arc42 Overview](https://arc42.org/overview); [Fowler, BoundedContext](https://martinfowler.com/bliki/BoundedContext.html)).
- **Retrospective evaluation**: authors should return to a design doc later and assess what the design got right and wrong — the maintenance-and-learning phase of the lifecycle ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)).

## 7. Choosing the artifact: what goes where

| Need | Artifact | Why this one |
|---|---|---|
| Explore an open design problem, weigh alternatives | Design doc | Built around trade-offs, goals/non-goals, alternatives; catches flaws while cheap ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)) |
| Record a choice between real alternatives | ADR | Small, immutable, sequential; context + decision + consequences survive the people ([Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)) |
| Maintain the durable reference picture of a system | arc42-structured doc set | Stable table of contents from goals through risks; fill pragmatically ([arc42 Overview](https://arc42.org/overview)) |
| Communicate structure to a given audience | C4 diagram at the matching level | Fixed abstraction levels prevent mixed-level confusion ([C4 Introduction](https://c4model.com/introduction)) |
| Specify a component's external surface | Contract spec (API-first, e.g. OpenAPI) | Machine-checkable, reviewable before implementation ([Zalando Guidelines](https://opensource.zalando.com/restful-api-guidelines/)) |
| Capture quality requirements | Scenario catalog / quality tree | Measurable stimulus-response form ([arc42 Quality Model](https://quality.arc42.org/)) |

Sequencing in a refinement flow: design-doc-style exploration happens *during* grilling; ADRs precipitate out of each session's choices; arc42 sections and C4 diagrams accumulate as the durable record; contract specs are the component-gate deliverable ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/); [Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions); [arc42 Overview](https://arc42.org/overview)).

## 8. ADR skeleton

Per Nygard's format ([Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)):

```markdown
# ADR-0042: <short noun phrase>

## Status
Accepted   <!-- proposed | accepted | deprecated | superseded by ADR-00NN -->

## Context
<The forces at play — technical, political, social, project-local.
 Value-neutral: describe tensions as facts, not as advocacy.>

## Decision
We will <active-voice statement of the response to these forces>.

## Consequences
<ALL outcomes: positive, negative, neutral. What becomes easier,
 what becomes harder, what new decisions this forces later.>
```

Discipline notes: one decision per record; numbers never reused; superseded records remain in place pointing forward; keep in the repository with the code ([Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)).

## 9. Review checklist: documentation quality

1. Does every significant decision have an ADR with value-neutral context and *all* consequences, including negative ones? ([Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions))
2. Are goals and **non-goals** stated? Scope creep hides in missing non-goals ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)).
3. Are alternatives-considered present with honest rejection reasons? ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/))
4. Do diagrams declare their abstraction level, and does each stay on it (no containers inside context diagrams)? ([C4 Introduction](https://c4model.com/introduction))
5. Does each diagram pass the C4 checklist (title, key, named elements, labeled directed relationships)? ([C4 Review Checklist](https://c4model.com/diagrams/checklist))
6. Are quality goals (≤5, prioritized) and their scenario expansions present in the appropriate sections? ([arc42 Overview](https://arc42.org/overview))
7. Are risks and technical debt recorded honestly rather than omitted? ([arc42 Overview](https://arc42.org/overview))
8. Is there a glossary, and is it consistent with the bounded contexts' ubiquitous language? ([arc42](https://arc42.org/overview); [Fowler, BoundedContext](https://martinfowler.com/bliki/BoundedContext.html))
9. Is anything hand-maintained that could be generated — and therefore already stale? ([C4 Component](https://c4model.com/diagrams/component))
10. Would a newcomer reading only the docs understand *why* the system is shaped this way? That is the stated purpose of the decision log ([Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)).
11. Is the documentation effort proportionate — full ceremony where designs are contentious, mini-docs or nothing where the solution is obvious? ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/))

## 10. Related references in this corpus

- `architecture-evaluation-and-review.md` — the review process these documents feed; what reviewers look for.
- `quality-attributes-and-tradeoffs.md` — the scenario form for arc42 section 10 quality requirements.
- `interface-and-contract-design.md` — the contract-spec artifact in detail (API-first, completeness skeleton).
- `decomposition-and-seams.md` — the building-block content C4 container/component diagrams should reflect.
- `architecture-styles.md` — solution-strategy (arc42 section 4) substance: style choice and its constraints.
- `evolutionary-architecture.md` — superseding decisions and keeping records honest as the system changes.
