# Goal-Level Grilling Questions

The curated question bank for Business Goal (BG) refinement — Mode 2's
inception session and any later goal-level session. Organized by BG
template section (see [templates.md](templates.md)); every question is
tagged with a confidence tier.

## Confidence tiers

Goal-level answers are not all equally durable. Tag each as you record it:

- **[High]** — foundational; everything else hangs on it. Rarely revisited
  without a new session and a superseding decision. Treat as settled once
  confirmed.
- **[Medium]** — expected to sharpen as epics/stories refine it, but rarely
  reversed outright. Present to the approver as directionally firm.
- **[Low]** — provisional by nature: best-guess detail that genuine epic/
  story/spike work will very likely revise or replace. Never gate-block on
  precision here — capture what's known, flag what isn't, and move on.

Volatility runs High → Medium → Low as you get more concrete: the more
abstract the question, the more stable the answer. Say this plainly to the
approver at gate time (see the Diagrams and Gates note in
[refinement-process.md](refinement-process.md)) — they should know which
parts of what they're approving are load-bearing and which are illustrative
best-guesses that Epic/Story refinement will legitimately change.

Low-tier findings are **flagged, not resolved**, at goal level: carry them
into the corresponding Epic's Risks & Open Questions, or the relevant
Story's Acceptance Criteria, rather than trying to fully answer them here.
Forcing precision too early either stalls the goal gate or produces false
confidence that then gets contradicted downstream.

## Problem [High]

- What pain or opportunity motivates this, in the sponsor's own words? No
  solution language — describe the world, not the fix.
- Who hurts, and why does this matter now (vs. six months ago, vs. never)?

## Current State & Gap [High]

Distinct from Problem: Problem is the human/business pain; this is the
diagnostic — why the current landscape doesn't already cover it. Distinct
from System Context's build-vs-reuse question below: this is about the
*ambient* world before any decision to build something, not about the new
system's own internals.

- What exists today to address this — systems, manual workarounds, prior
  tooling, spreadsheets, tribal process — or is there genuinely nothing?
- What specifically is missing? Name the technology/capability gap that
  lets the problem persist despite whatever exists today.

## Intent [High]

- What does the business want to be true afterward?
- Why now — what changed, or what's the forcing function?

## System Context [High/Medium — tagged per sub-question]

Boundary-level only — the system as one opaque box, its actors, and what's
outside it. No internal mechanics, no architecture, no component
decomposition; that's Epic/Component territory. Answering these fully is
what feeds the epic-derivation deliverable-coverage pass (see the Epic
playbook) — every "container" named here needs an owning epic later,
including non-domain ones (a backend/API layer, a deployment shell) that
are easy to treat as ambient infrastructure instead of a real deliverable.

1. **[High]** What are we building? One or two sentences, plain language,
   boundary only.
2. **[High]** Who will use this, and how? Actors/personas/roles, plus the
   channels they expect (web, CLI, chat integration, API, mobile, etc.).
3. **[Medium]** Where will this live? Coarse hosting/deployment placement —
   internal tool, SaaS, on-prem, embedded in another product. Not
   infrastructure detail, just the general environment.
4. **[Medium]** What triggers this to act, and what tangible output or
   status exists when it's done? The system's black-box input/output
   contract — still no internals.
5. **[High]** Of the new system's own parts, what already exists vs. what
   must be designed and built from scratch? (Greenfield vs. brownfield for
   *this* system, as opposed to the ambient landscape covered above.)
6. **[Medium]** What existing internal systems or processes need to change
   to accommodate this?
7. **[Medium]** What external systems will it depend on? Name the
   entities Groundwork needs to talk to, not the protocol or payload shape
   — that's contract-level, decided at Component Doc time.

Render a **Context Diagram** (C4 Level 1, Mermaid) from questions 1–2 and
5–7 once they're answered — see
[refinement-process.md](refinement-process.md) for when and how. If enough
sequential detail comes out of question 4 (and the Illustrative Scenario
below), also render a **Process Flow** diagram; if not, skip it rather than
inventing steps.

## Illustrative Scenario [Medium (happy path) / Low (bad paths)]

Non-binding. This grounds shared understanding with a concrete example; it
is not a specification and never gates on completeness.

- **[Medium] Happy path.** Walk one flawless, standard transaction from
  trigger to output, in plain chronological bullets.
- **[Low, optional] Bad paths.** Only capture what the sponsor volunteers
  unprompted or near-unprompted — invalid input, a mid-transaction failure,
  a dependency going offline. Don't interrogate for edge cases at goal
  level; full enumeration is Epic (Risks & Open Questions) or Story
  (Acceptance Criteria) work. If nothing surfaces naturally, leave it out.

## Outcomes & Success Criteria [High]

- For each outcome: what's the observable result — and where possible,
  what metric moves, and by how much? ("Cuts manual processing time by
  50%" beats "processing gets faster.") Every outcome cites the decision
  that grounds it.

## Scope [High]

- What's explicitly out of scope for this phase — what are we
  intentionally deferring to guarantee a timely v1?
- If the work is release-scoped: what's the expected initial scale
  (users/records/volume)? If the timeline were cut in half, what's the
  first thing dropped? The answer to this *is* the release-1/release-2
  split — don't just record it as prose, let it shape the `Releases:`
  list.

## Constraints [High, with a required Low-tier check]

- Regulatory / technical / budget / timeline / organizational constraints?
- **Always ask explicitly** (never wait for it to surface): are there
  compliance, data-residency, or privacy boundaries — GDPR, HIPAA,
  PCI-DSS, or similar — that dictate how or where data is handled? Record
  "none identified" explicitly rather than leaving this silent.

## Stakeholders & Roles [High]

- Who sponsors this? Who approves what, at which gate?
- Who else participates in refinement (product owners, eng/DS leads,
  other stakeholders)?

## Conflicts & Tensions [High]

- Does this goal conflict or compete with an existing goal or in-flight
  work? Positions conflict more often than intents — dig for intent before
  concluding there's a real conflict.
