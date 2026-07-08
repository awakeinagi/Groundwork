# Story-Slicing Seams

Guidance for slicing an approved epic into implementable stories (EP →
STs/SPs). Complements [epic-slicing-seams.md](epic-slicing-seams.md) one
level down: same vertical-vs-horizontal discipline, finer grain.

## Vertical slicing vs. horizontal (layer) slicing

Engineers decomposing an epic into stories often default to technical
layers instead: "Write SQL schema," "Create API endpoint," "Design UI
component." This is horizontal (layer) slicing, and it stagnates the
same way at story grain as it does at epic grain — a frontend component
can't be tested or deliver value without the database, and vice versa,
so nothing is demoable until every layer-story is done.

**Every story must be a thin, vertical slice through the entire
technical stack that delivers one tangible, testable result.** If a
candidate story's title names a technology or architectural layer rather
than a user-observable capability, re-slice it.

## No fixed number of stories

Same discipline as the epic seams: this catalog is a checklist of
candidate cuts, not a quota. Splitting exists to satisfy INVEST
(Independent, Negotiable, Valuable, Estimable, **Small**, Testable) — it
is a means, not an end in itself. The canonical warning applies directly:
**avoid inventing unnecessary splits without stakeholder demand**
(Story Splitting, Software and Cloud Architecture Design Practice
Repository). Split when a story's Acceptance Criteria can't stay a
tight, individually-testable list without ballooning, or its Component
Impact spans multiple CMPs with no single coherent deliverable — not
because a seam exists to apply for its own sake.

Splitting well pays for itself beyond scheduling: it's a design tool.
Well-sliced stories tend to expose candidate Component Doc boundaries
and contract items before you get to Component derivation — a story's
`Component Impact` field is exactly where slicing decisions surface into
CMP/Design Element shape later.

**Signals to split one candidate story into two:** the Acceptance
Criteria list keeps growing past what fits one coherent, individually
testable set; the story bundles more than one of the seams below (e.g.
a new data variation *and* a new workflow step); the
[coupling check](#cross-story-coupling-check-required-step) below shows
low coupling between the proposed halves once drafted.

**Signals to keep two candidate stories as one:** splitting would leave
one half with no independently observable value (INVEST's Valuable);
the coupling check shows persistent mutual coupling between the two that
never resolves — the same "same epic wearing two IDs" pattern as at the
epic level, just one grain down.

## Cross-story coupling check (required step)

Same tool as the epic-level check, generalized:

```bash
python3 <skill-dir>/scripts/groundwork_epic_coupling.py --root <project> check --type story ST-nnnn SP-nnnn ...
```

Run right after a draft story/spike set's impact edges are drawn, before
any of them is refined in depth. It groups siblings by their parent
epic and flags mutual (bidirectional) coupling the same way the epic
check does. INVEST's "Independent" criterion makes this signal matter
*more* at story grain than at epic grain — a mutual pair here is a
stronger hint the split should collapse back into one story.

## The seams

### 1. Data Seam — variations in data

Instead of building a form or handler that covers every data type or
option at once, build the simplest input variation first, then layer on
the others as separate stories.

**The Rule:** One story for the baseline data type; separate stories for
complex variations, formatting, or optional fields.

**Examples** (from a Subscription epic):
- Story 1: As a user, I can subscribe using a standard US credit card.
- Story 2: As a user, I can subscribe using Apple Pay.
- Story 3: As an international user, I can subscribe using a non-US
  billing address.

**Variant — different entry methods for the same data:** the same seam
also covers *how* the data arrives — a manual UI form vs. bulk CSV
import vs. a programmatic API call are separate stories delivering the
same underlying capability through different channels. Slice by channel
the same way, rather than building all entry methods in one story.

### 2. Chronological Seam — workflow steps

Break a complex user journey into single, discrete actions. A story
should represent exactly one user interaction and one system response.

**The Rule:** A story ends when control shifts back to the user or
pauses for a system event.

**Examples:**
- Story 1: As a user, I can click "Cancel Subscription" and see a
  confirmation prompt.
- Story 2: As a user, I can confirm the cancellation to update my status
  and view a success message.

### 3. Fidelity Seam — UI/UX sophistication

Never build the final, polished UI in the same story as the core
functional logic. Get it working with raw elements first, then make it
beautiful.

**The Rule:** Separate the mechanics of the feature from its polish and
interactive micro-copy.

**Examples:**
- Story 1: As a user, I can cancel my subscription via a basic text link
  and a standard browser confirmation dialog. (Functionality)
- Story 2: As a user, I can experience a smooth, branded cancellation
  workflow with feedback surveys. (Polish)

**Caveat — "basic" means unstyled, never sub-baseline.** `DEC-0188`
requires every v1 story's Acceptance Criteria to cite the shared
accessibility and responsive-conformance standard (WCAG 2.1 AA +
Tailwind's breakpoints) — that requirement applies to *every* story
this seam produces, including the "basic" one. A native browser
`confirm()` dialog clears this bar on its own (browsers handle its
accessibility automatically); a custom-built minimal modal in the same
story would not get a pass just because it's "just the mechanics" — it
still has to conform. Fidelity separates polish from function; it does
not separate compliant from non-compliant.

### 4. Logic Seam — business rule complexity

If a feature has multiple conditional paths based on business logic,
build the default path first. Treat every if/else branch as a potential
story boundary.

**The Rule:** Start with the default condition. Add complexity
iteratively.

**Examples:**
- Story 1: As a customer, I am charged the standard flat rate of
  $20/month when subscribing.
- Story 2: As a customer, the system applies a promo code discount to my
  subscription if one is provided.

### 5. Operational Seam — data freshness or processing mode

Don't build for real-time sync or high performance in the first story if
a slower or simpler method works.

**The Rule:** Build synchronous or manual processing first, then move to
asynchronous, queued, or automated processing.

**Examples:**
- Story 1: As an admin, I can manually click a button to refresh and
  view the active subscriber list.
- Story 2: As an admin, the active subscriber list automatically
  refreshes every hour in the background.

### 6. Operations Seam — CRUD and lifecycle operations

Separate stories by which operation on the core object they deliver —
create, read/query, update, delete/retire, search, archive, undo —
building the operation that unlocks the others first (Richard Lawrence
calls this "Operations Completion").

**The Rule:** One story per operation on the core object; build create
before the operations that act on what it created.

**Examples** (from Groundwork's own artifact lifecycle —
`groundwork-system.md`'s draft → gated → approved → stale/superseded):
- Story 1: As a facilitator, I can create a draft Business Goal from a
  closed session's decisions.
- Story 2: As an approver, I can gate and approve a drafted Business
  Goal.
- Story 3: As a facilitator, I can supersede an approved decision and
  walk the staleness cascade it triggers.

## Cross-reference: investigation is a Spike, not an undersized story

If a candidate story's real content is an unknown to investigate rather
than a known thing to build, it isn't a small story — it's a Spike. This
is Richard Lawrence's "Architectural Spike vs. Implementation" pattern,
and Groundwork already has first-class native support for it: the `SP-`
artifact type exists exactly for "a question that must be answered
before sibling work can be trusted" (`groundwork-system.md`). Don't
write a story whose Acceptance Criteria is secretly "figure out how X
works" — open a Spike, let its Findings become Decisions, then write the
implementation story against those decisions.

## See also

Mike Cohn's **SPIDR** (Spikes, Paths, Interfaces, Data, Rules) is a
five-letter mnemonic covering much of the same ground as the seams
above, useful as a quick memory aid: Spikes ↔ the cross-reference above,
Paths ↔ the Logic Seam, Interfaces ↔ the Data Seam's entry-method
variant, Data ↔ the Data Seam, Rules ↔ the Logic Seam.

Sources: Richard Lawrence, "Patterns for Splitting User Stories";
Mike Cohn, SPIDR; the Software and Cloud Architecture Design Practice
Repository's Story Splitting activity
(<https://socadk.github.io/design-practice-repository/activities/DPR-StorySplitting.html>).
