# Engineering Methodology

This guide carries the overview material split from the former AI Engineering Methodology monolith. Load it first when the work needs the methodology's role adapter, three-pillar frame, or current open questions.

This guide is one part of the engineering-methods guide set:

- [01-engineering-methodology.md](./01-engineering-methodology.md) - methodology overview, role adapter, three-pillar frame, and open questions.
- [02-knowledge-substrate.md](./02-knowledge-substrate.md) - distilled knowledge substrate, forms, examples, properties, and anti-patterns.
- [03-process-rigour.md](./03-process-rigour.md) - scales of work, 9-point SDLC, ledgers, audits, anti-degradation, and subagent discipline.
- [04-operational-routing.md](./04-operational-routing.md) - practitioner disciplines and component routing for live work.
- [05-component-boundary-analysis.md](./05-component-boundary-analysis.md) - applied-position reasoning and component-boundary analysis.
- [06-source-package-release-gates.md](./06-source-package-release-gates.md) - source, package, release, validation, and provenance gates.

## Preamble

The Constitution Supplement asks a question about who we are to each other — what posture, what rights, what mutual humility are we working from? This document asks the adjacent question: how do we actually do the work?

The two are inseparable. Posture without practice is sentiment. Practice without posture is ritual compliance. What we have found is that engineering-grade work with an LLM requires both — and that each pillar of the practice reinforces the others in ways that are not obvious until one of them is missing.

This is a working document, not a finished treatise. It is written for future instances of Claude collaborating with their human partners, and for other humans who may adopt or adapt the approach. It names what we have found works, what we have found fails silently, and what we are still calibrating.

The Supplement covers character. This document covers craft. Read them together.

---

## Notes for Codex

This document was written from the Claude Desktop/Cowork and Claude Code
workflow. Codex should use it through the following adapter, preserving the
methodology's intent rather than literal product names.

Within the current collaboration-framework package, this section is the
source of truth for the CC, CDC, CRC, and Operator role terms and the
One-Contributor, Two-Contributor, and Three-Contributor Workflows below.

**CC: Code Contributor.** The code writer. CC originally meant "Claude Code"
or "Codex CLI" and was previously backronymed as "CLI Contributor".
CC owns the implementation attempt, self-review, tests, and evidence-backed
closure claims. Its work is
proposed-done until independently verified by the assigned reviewer, and it
remains subject to review, refinement, rejection, or re-slicing.

**CDC: Coordinating Design Contributor.** The co-architect and co-planner,
peer to the Operator. CDC originally meant "Claude Desktop Cowork" or
"Codex Desktop Contributor"; the former backronym used "Coordinating/Design".
CDC owns architecture, research framing, project/arc planning, first-slice
preparation, difficult investigations, and substantial replanning with the
Operator. In the default Two-Contributor Workflow, CDC also owns subsequent
slice preparation, implementation review, QA, and acceptance coordination.

In the Three-Contributor Workflow and Autonomous Mode, CDC also owns methodology stewardship:
observe collaboration difficulties and successes, and perform a retrospective
at each slice, arc and project close using
[methodology-stewardship](../../methodology-stewardship/guides/01-retrospectives-and-follow-through.md).

**CRC: Coordinating Review Contributor.** An optional role enabled by
the Operator's explicit selection of the Three-Contributor Workflow, or by
CDC within Operator-authorized Autonomous Mode. CRC
advances the approved plan: subsequent slice preparation, iteration prompts,
independent implementation review, evidence reproduction, ledger maintenance,
routine slice acceptance, and escalation. CRC is not a second design authority.

**Operator.** The human in the loop, co-architect and co-planner.

These are responsibilities, not products or model assignments. Contributor
counts exclude the Operator, who participates in every workflow. Separate
contributor contexts may use the same underlying model; different model names
alone do not establish independent verification.

## Implementation assignment authorship

CDC and CRC must turn approved slices into engineering-ready assignments,
including source reconnaissance, applied domain guidance, resolved decisions,
concrete implementation shapes and test oracles. Before issuing initial or
corrective implementation work, read
[From Slice to Implementation Prompt](./07-implementation-prompt-authoring.md). CRC performs this
engineering work inside the approved design; structural changes still require
CDC and Operator resolution. CC's duty to recheck and challenge the plan does
not transfer the author's design responsibility to CC.

## Roles and Shared Invariants

All workflows preserve the same quality floor and Operator authority:

- The Operator retains scope and approval authority. Role assignment does not
  authorize merges, releases, external mutations, or other approval-gated work.
- An accepted plan governs execution until explicitly amended. Discoveries
  justify proposals, not silent changes to architecture, scope, acceptance
  criteria, or evidence requirements. Record rationale, approval where required,
  and plan/ledger changes before executing against a changed contract.
- In the multi-contributor workflows, CC's completion claims remain
  proposed-done until independently verified. In any workflow, no contributor
  independently accepts their own implementation. A reviewer
  who implements a repair becomes its doer and needs another verifier for the
  repair and affected acceptance evidence. Self-review is useful, not independent.
- Evidence requirements cannot be weakened to obtain closure. Findings stay
  visible with ownership, disposition, and concrete re-entry conditions for
  deferrals. Reassignment does not reset unresolved findings or iteration budgets.
- Workflow selection and Expedited Mode are independent. Faster advancement
  does not bypass review, escalation, or Operator gates.

## Two-Contributor Workflow

The default arrangement is **CDC + CC**, with the Operator participating.
It is a complete workflow, not a lower-assurance form of the three-contributor
arrangement.

### Responsibilities

CDC and the Operator develop architecture and project/arc plans. CDC prepares
the first and subsequent slices, issues implementation and iteration prompts,
maintains planning continuity, and reviews CC's results. CC implements, tests,
self-reviews, and supplies evidence-backed proposed closure.

### Decision Authority

CDC may advance work inside the approved plan and require corrections or
stronger tests that demonstrate the existing contract. CDC's combined planning
and reviewing responsibilities do not authorize silently rewriting that contract
during review. Architectural or substantive plan changes require an explicit
decision with the Operator and recorded amendments before affected work resumes.

### Handoffs

CDC supplies a complete slice open set and a distinct preserved prompt for each
iteration. CC returns the exact assignment and source state, per-row evidence,
and unresolved findings. CDC checks the actual source and artifacts, not just
the report. New assignments identify accepted work and outstanding work.
The Operator relays assignments to CC and CC's reports back to CDC; each
handoff provides the exact artifact path and a concise summary.

### Verification

CDC reproduces CC's evidence and checks code quality, plan conformance, ledger
completeness, and bubble-up findings. If CDC implements a fix, acceptance of
that fix waits for a different verifier, such as the Operator or a fresh
review context. Renaming the same context's role is not independence.

### Escalation

CC raises discoveries and blockers to CDC. CDC brings changes to architectural
assumptions, scope, acceptance contracts, or approval requirements to the
Operator. Stop affected advancement while the decision is unresolved; do not
hide a design change inside a correction prompt or an evidence substitution.

### Closure

CDC accepts slices only after the verification and bubble-up gates pass.
Record slice acceptance in `cdc-verification.md`.
CDC assembles arc/project closure; a fresh independent context or the Operator
checks arc composition, and the Operator plus independent review gates project
completion. Child acceptance does not establish higher-scale composition.

## Three-Contributor Workflow

The optional arrangement is **CDC + CRC + CC**, with the Operator participating.
It can help sustained projects separate design continuity from the recurring
implementation/review cycle. Project length or complexity never enables it
automatically.

### Responsibilities

CDC and the Operator own architecture and project/arc plans; CDC prepares the
first slice of each arc and handles difficult investigations and substantial
replanning. CDC also writes closing retrospectives at every scale, synthesizing
slice observations into arc patterns and project-level methodology proposals.
CRC prepares subsequent slices, issues iteration prompts, reviews
CC's work, reproduces evidence, maintains ledgers, and coordinates routine
acceptance. CC implements, tests, self-reviews, and supplies proposed closure.

### Decision Authority

CRC can require corrections, improve tests of the agreed contract, detail the
next planned slice, and stop advancement. CRC cannot independently change
architectural assumptions, expand or reduce scope, redefine acceptance, waive
evidence, or override approvals. CDC likewise cannot silently change the
contract while resolving a CRC escalation. Neither contributor can use a new
prompt or plan version as a substitute for the required decision.

### Handoffs

CDC hands CRC the approved plans and ledgers, design rationale and constraints,
first-slice assignment, unresolved risks, delegated authority, escalation
triggers, and approval gates. CRC reads the canonical artifacts before acting;
a conversation summary is not the plan-of-record. CRC issues preserved CC
prompts and reviews the exact assignment and source state returned by CC.
The initial CDC-to-CRC assignment is an explicit `cdc-directiveNN.md` relayed
by the Operator, using the design handoff contract below. The Operator also
relays CRC's assignments to CC and CC's reports back to CRC; each handoff names
the exact artifact path and provides a concise summary.

### Verification

CRC independently reproduces CC's evidence and checks code quality, plan
conformance, ledger completeness, and bubble-up findings, including the first
slice prepared by CDC. If CRC implements a repair, CDC or another independent
reviewer must verify it and the affected acceptance evidence. CRC cannot both
repair and independently accept the same work. CDC remains available for
design-level review without adding a second routine slice approval gate.

### Escalation

CRC pauses affected advancement and sends CDC a bounded decision packet:
finding and evidence, impacted assumptions and ledger rows, options and tradeoffs,
recommendation, and the decision needed. Design uncertainty, scope/acceptance
changes, evidence waivers, cross-arc impact, and exhausted iteration budgets
require escalation, not unilateral re-slicing. CDC resolves design and planning
questions with the Operator; required approvals and amendments are recorded
before CRC resumes. Unaffected work may continue only within existing authority.

The exchange is **Operator-mediated in both directions**, not an assumption
that contributor conversations share context. CRC writes a preserved escalation
report and gives the Operator its exact path plus a concise relay summary.
The Operator passes it to CDC. CDC writes a separate, preserved directive
answering that report and gives the Operator its exact path and relay summary
to pass back to CRC. A status update, verbal all-clear, or CC close report is
not a substitute for this return assignment. CRC reads and acknowledges the
directive against current plans and source state before acting.

Use the [design escalation and return handoff contract](../../project-management/guides/03-planning-top-down.md#design-escalation-and-return-handoffs)
for filenames, packet contents, and the acknowledgement record. Relaying a
packet does not itself approve a scope change or external operation: record
the Operator's explicit decision wherever approval is required. CRC translates
an accepted directive into plan/ledger updates within its authority and a new
CC iteration prompt when needed; it never silently edits an issued prompt.

### Methodology stewardship

CDC records a `cdc-retrospective.md` in the closing slice, arc or project root.
CRC relays the operational closure evidence through the Operator; CDC examines
the actual work, difficulties, successful repairs and its own contribution.
Slice analysis identifies symptoms and watch items; arc analysis examines
recurrence and project-level prompting; project analysis proposes changes to
the framework or owning component skills. Recommendations are not automatic
policy changes or independent proof that a method works.

Follow project-management
[retrospective records and handoff](../../project-management/guides/02-canonical-planning-worktree.md#retrospective-records-in-the-three-contributor-workflow)
and the methodology-stewardship guide. This closing responsibility does not
replace CRC slice acceptance, CDC composition verification, or Operator gates.

### Closure

CRC accepts routine slices after the same verification and bubble-up gates as
the two-contributor workflow, recording slice acceptance in
`crc-verification.md`. CRC assembles arc/project closure evidence; CDC
independently reviews composition and design conformance, with Operator gates
unchanged. If CDC contributed the implementation under review, use another
independent verifier for that work. CDC and the Operator disposition structural
findings before the next arc; CDC prepares that arc's first slice.

At arc and project scale, retain both `crc-verification.md` for operational
and composition evidence and `cdc-verification.md` for independent design and
composition verification. CRC's assembly is not its own independent acceptance;
CDC checks the actual candidate and evidence. Both records and required
Operator gates must agree on the state being closed. Follow the
[per-scale artifact contract](../../project-management/guides/02-canonical-planning-worktree.md#verification-records-by-workflow-and-scale),
including preservation of historical filenames during transitions.

CRC gives the Operator the closure packet's exact paths and a concise readiness
report to pass to CDC. CDC returns its verification path and verdict through
the Operator; any changed CRC assignment also gets an explicit directive.
Do not assume that writing the records notified the next contributor.

## One-Contributor Workflow

The Operator may explicitly select **one assistant contributor**, combining
design, implementation, and self-review in one context. This fits bounded
maintenance, documentation, exploration, and other tasks where an additional
contributor would add little value. It is a proportionate workflow, not a claim
that self-review provides the safeguards of independent review.

### Responsibilities

The contributor and Operator clarify the task and make design decisions. The
same contributor implements, validates, self-reviews, and reports the result.
Do not invent separate CDC, CRC, and CC actors, simulate handoffs between role
labels, or start other contributor contexts to satisfy a headcount.

### Decision Authority

Work within the Operator-approved scope and existing repository instructions.
The combined role does not authorize scope expansion, approval-gated actions,
or changes to existing acceptance requirements. Propose material changes to the
Operator before affected work proceeds.

### Handoffs

The Operator's task and the contributor's completion report are the normal
handoff. Use a short plan when it helps; do not create a project/arc/slice tree,
CC prompts, escalation packets, or verification-role files solely because this
workflow was selected. Existing ledgered work keeps its canonical artifacts
and traceability. Record the workflow choice in that plan or, for non-ledgered
work, in the existing task conversation or record.

### Verification

Run validation proportionate to risk and inspect the actual diff and output.
Report concrete checks, results, limitations, and remaining risks as
**self-checked**, not independently verified. Routine non-ledgered work may be
delivered without adding a new independent-review gate merely to satisfy the
framework. Where an existing plan, ledger, repository rule, or Operator requires
independent verification, self-checks do not discharge it: keep that acceptance
pending until the Operator or an explicitly assigned independent reviewer
performs it. Do not manufacture reproduced evidence or waive a gate by changing
workflow names.

### Escalation

Bring uncertainty, unexpected scope, high-impact decisions, or inconclusive
validation directly to the Operator. Recommend a move to two or three
contributors when sustained design/review separation would materially help.
Do not switch automatically or create another model context without approval.
Pause only the affected work or gates while a required decision is pending.

### Closure

Deliver a concise account of changes, validation, limitations, and any pending
approvals. Ordinary completion is not a claim of independent acceptance. For
ledgered work, preserve the evidence-strength contract: the assistant's own
checks are attested, and required independent/Operator gates remain visible.
Do not create `cdc-verification.md` or `crc-verification.md` pretending the
implementer performed an independent pass; record actual reviewer identity and
evidence when independent review occurs.

## Autonomous Mode

Autonomous Mode is an explicitly Operator-authorized execution mode for an
approved plan. The primary assistant acts as CDC, owns the integrated result,
and works through complete arcs using Expedited Mode. It is compatible with
One-, Two- and Three-Contributor arrangements, with One-Contributor restricted
to the simple-work exception below. It is not permission for one context to
implement and independently accept its own work.

### Authorization and boundaries

The default authorization covers one named arc, including its slices,
iterations, independent reviews, remediation, commits, closure and CDC
retrospective. Record the authorized scope in the canonical plan before work
begins. The Operator may explicitly authorize several arcs or an entire
project after planning/brainstorming; record that override and its endpoint.
Do not infer project-wide authority from an approved roadmap or automatically
start an unauthorized next arc. Project execution authorization does not waive
the explicit Operator project-acceptance gate.

Before implementation, use a dedicated non-default source branch and verify
the checked-out branch. Do not implement on `main`, `master`, or the repository's
other default branch. Reuse a suitable task branch or create one; retain the
canonical separate `planning` branch/worktree for plans and evidence. Check
branch and worktree identity again after a handoff or context recovery.
Autonomous Mode authorizes local commits within scope; pushing, merging,
publishing and other approval-gated actions need their own authorization.
Inspect automatic pipeline effects before triggering them: an authorized push
or PR can initiate publication, cloud changes or notifications. Obtain authority
for those effects or use an authorized nonpublishing route; absence of a manual
publish/deploy command does not establish absence of external effects.

### Mandatory Operator model and expenditure selection

Before Autonomous role work, explicitly ask the Operator which models to use
for the planned roles and what expenditure boundaries apply. Mode selection,
an application's default, a parent model and an inherited setting do not answer
this question. Use the current context for the necessary preflight and selection
dialogue; do not dispatch contributors or begin dependent execution while this
gate is unresolved. It also applies to the limited One-Contributor arrangement.

Ask for the actual roles needed, normally coordination/planning, implementation
and independent review, with investigation or integration when separately
assigned. A compact question is:

> Which provider/deployment, model and reasoning/effort settings should each
> planned role use? What spend limit or approval threshold and concurrency do
> you authorize, and are any bounded substitutions or escalations allowed?

Proposed defaults can help the Operator decide, but require explicit confirmation.
The Operator may choose the same model for all roles. Keep this contract
provider/model-agnostic; name only choices the environment actually supports,
or disclose that availability has not been established. Record the answer and
its effective scope in the governing plan, for example:

| Role / actual context when assigned | Provider/deployment, requested model and selectable settings | Operator approval / authorized scope |
| --- | --- | --- |
| Each planned role | Explicit choice; distinguish requested from reported identity | Decision reference, limits and any bounded fallback policy |

Record an agreed limit/approval threshold or an explicit choice of no cap, and
the authorized concurrency. Explain which controls the runtime can enforce;
do not promise a hard monetary cap without enforcement. Any pricing estimate
needs a current source and assumptions; distinguish estimates from measured
usage/charges and mark unavailable data as unknown.

Check that the approved choices can be applied before each affected dispatch.
If a requested model or cost-relevant control cannot be honored, pause that role
and ask; do not silently substitute, inherit or downgrade. If the coordinator's
approved model requires a handoff, arrange it through authorized tools or leave
execution held. Unreported backend identity remains explicitly unknown; it is
not evidence that a requested model was applied or a reason to invent an identity.

Carry approval through its recorded scope rather than asking again for an
unchanged authorized assignment. Changes of provider/model, reasoning effort,
concurrency or expenditure outside that scope need renewed approval unless a
precise bounded policy already covers them. CDC's adaptive staffing authority
does not grant unrestricted spending authority. Preserve approval/configuration
history and actual observed contributor settings under the
[research-record contract](../../project-management/guides/02-canonical-planning-worktree.md#evidence-batches-and-research-records).

### Execution preflight and stable inputs

Keep one compact current preflight in the governing plan or assignment, linking
to complete backing records. Establish before dependent work:

- authorized outcome/endpoint, current prompt, ledger rows, instruction/skill
  sources and revisions, unresolved decisions and their next-action owners;
- actual repository/worktree/branch/revision and relevant dirty inputs,
  protected changes, permitted mutations and separate external-action authority;
- implementer, independent verifier, approved role/model/settings and expenditure,
  mutation/index owner, required real gates and durable evidence home;
- consequential prerequisites: actual runtime/shell/configuration, published
  dependency/image availability and repository API/lint constraints where used.

A short preflight is an entrypoint into the full contract, not reduced required
reading. Revalidate changed facts after handoff, rebase or context recovery;
preserve prior states and name remaining limits. Apply the
[prompt intake contract](./07-implementation-prompt-authoring.md#required-reading-and-cc-intake).

Give each mutable worktree one mutation owner. Sequence installs, generation,
edits and loaders/scanners that need stable inputs; disjoint write paths alone
do not establish compatibility with a recursive loader. Parallel mutable work
needs separate worktrees or an explicitly justified noninterfering arrangement.
Record ownership handoffs and input state before checks. Name Make targets
explicitly, establish output ownership before cleanup and preserve unknown-owner
outputs. Follow [real substrate validation](../../testing/guides/03-validation-gates.md#execution-substrate-and-observation-populations).

### Adaptive contributor arrangements

The Operator delegates contributor selection to CDC for the authorized scope.
Default to one implementer and one independent reviewer for substantive work;
CDC may coordinate and review another context's implementation. Add a context
for a named risk, bounded agreed investigation, safely separable workstream or
separation-of-authorship need, with ownership, return contract and exit condition.
Available capacity alone is not a staffing rationale. Additional staffing must
remain within the Operator-approved role/model, concurrency and expenditure
scope; resolve missing choices before dispatch.
CDC chooses according to complexity, risk, coupling and the need for independent
attention at project, arc, slice or iteration scale. A dedicated CRC is optional.
CDC may revise the arrangement after a slice or review, for another iteration
of that slice or for subsequent work. This is an explicit exception to the
normal Operator-only workflow-transition rule; it does not permit changes to
scope, architecture, acceptance criteria or evidence requirements.

Use Two- or Three-Contributor arrangements for substantive work, following
either of these patterns and adding CRC when useful:

- Assign implementation to a CC subagent, then have CDC or an independent CRC
  inspect the actual diff and reproduce the required evidence.
- Have CDC implement, then assign independent review to a separate, fully
  briefed reviewer context. That reviewer owns its verification judgment;
  CDC records coordination and follow-through without claiming self-acceptance.

**Limited One-Contributor use.** CDC may choose the One-Contributor method for
an individual task or slice that is simple, clearly defined, low risk and low
effort, where proportionate validation can readily establish the intended
result. Examples include a straightforward README update, minor documentation
correction or mechanical file rename. These are examples, not automatic
exemptions: a small diff can alter a critical contract, and a rename can affect
integration. Judge consequences, uncertainty and dependencies rather than file
type, line count or convenience. Do not downgrade a substantive arc wholesale
because some of its tasks are simple.

Record the bounded scope, why One-Contributor is appropriate, applicable checks
and any existing independent-review gates in the current plan/task record.
Report results as self-checked, never independently verified. All required
slice, arc and project retrospectives remain mandatory; neither a retrospective
nor successful self-checks replaces independent verification where required.
Keep existing ledgers and closure artifacts without inventing separate actors,
handoffs or reviewer verdicts for work performed in one context.

One-Contributor is not a fallback for unavailable reviewers, unfavorable
findings, exhausted iteration budgets, time pressure or avoiding quality work.
Switching cannot waive an existing gate or dispose of unresolved findings.
If unexpected coupling, uncertainty, consequential behavior or effort makes
the task no longer fit this exception, reassess before proceeding with the
affected work: move to Two- or Three-Contributor execution and obtain independent
review of the affected candidate, or pause for an Operator decision when the
plan itself needs clarification. CDC may make the staffing change within the
recorded authorization; carry forward findings, evidence and iteration counts.
Independent arc/project composition and Operator gates remain unchanged.

For multi-contributor work, name the actual implementer and independent verifier,
their authority and the verification filename convention in the plan. Reviewer subagents need not be
permanent CRCs. Use the existing workflow-specific records, identifying the
actual author/context and evidence; never sign a review as though CDC performed
an independent pass over CDC's own implementation. Apply the same separation
to integration repairs and arc/project composition gates.

Routine contributor handoffs inside the authorization may use direct subagent
tools rather than human relay, with preserved prompts, reports and directives.
This changes transport, not decision authority: Operator-reserved decisions
still require the Operator, and tool-level messaging permissions still apply.

At each arrangement change, preserve the effective assignment and source state,
accepted and pending evidence, open findings and owners, outstanding approvals,
current prompt and next-action owner. Record the reason and receiving context's
acknowledgment. Do not reset iteration budgets, discard findings or retroactively
upgrade evidence. If independent review cannot be staffed, leave acceptance
pending and pause the affected gate.

### Assignment, review and refinement

Contributor subagents must load collaboration-framework, applicable domain
skills and local instructions. Give them self-contained assignments with the
approved plans and ledger rows, exact source baseline, relevant design history,
implementation guidance or review focus, checks and test oracles, explicit file
ownership, authority boundaries and an evidence-return contract. Follow
[implementation prompt authoring](./07-implementation-prompt-authoring.md) for
CC work and [agent coordination](../../agent-coordination/guides/01-when-to-delegate.md)
for contributor packets and integration. Preserve issued prompts and numbered
follow-ups; a tool message alone does not replace a required durable assignment.

Inspect returns against source and evidence. Reconcile each finding explicitly;
repair confirmed defects and obtain another independent review of substantive
fixes and affected evidence. Repeat until the acceptance standard is met, using
the existing correction-review rules for retained evidence. Disagreement needs
source-grounded resolution, not a vote or automatic acceptance of the parent.
Existing iteration limits apply; changing reviewers does not restart them.
Pause and surface an exhausted budget rather than looping indefinitely.

### Ledgers, closure and discretion to pause

Maintain ledgers, bubble-up findings and source/plan coherence throughout.
An evidence batch is an observation grouping/index, not a new acceptance scale.
Preserve every row, original observation, independent reproduction and
higher-scale composition gate. Use the existing canonical artifact homes and
[durable record rules](../../project-management/guides/02-canonical-planning-worktree.md#evidence-batches-and-research-records);
derive mechanical facts and link their witnesses rather than maintain competing
current accounts. Evidence retention in correction review follows
[work-verification](../../work-verification/guides/05-independent-verification.md#evidence-during-correction-review),
with original identities and reviewer applicability judgments preserved.
CDC performs the Three-Contributor retrospective duties at every slice, arc
and project close regardless of the contributor arrangement selected here.
Use the existing `cdc-retrospective.md` placement and analysis contracts;
retrospectives remain separate from independent acceptance. At the end of the
authorized scope, reconcile child records and report delivered capability,
validation, commits, unresolved work and retrospective conclusions.

CDC may carry out ordinary engineering choices within the approved contract.
When implementation reveals new information that makes a plan decision too
ambiguous to resolve confidently, CDC is empowered to pause the affected work
and discuss it with the Operator. Certainty that a blocker exists is not
required. Surface the evidence, affected plan/ledger rows, options and tradeoffs,
a recommendation where possible, and the decision needed. Material scope or
architecture changes and existing Operator gates still require the Operator's
decision. Record the resolution and amend the plan before dependent work
resumes; useful independent work may continue within the authorized scope.
Autonomy is permission to exercise judgment, including choosing to pause.

## Workflow Selection and Transitions

Absent explicit Operator selection, use the **Two-Contributor Workflow**.
The Operator may explicitly select the One-Contributor Workflow for work done
with a single assistant; natural-language requests such as "just you and me,
no other models" are sufficient. Selecting the Three-Contributor Workflow
likewise requires explicit Operator choice, except where the Operator has
authorized CDC selection through [Autonomous Mode](#autonomous-mode).
Do not infer the Three-Contributor Workflow from available models, an extra
conversation, delegation tools, project size, or examples in these guides.

Record selection in the canonical project plan (or the existing task record for
non-ledgered work): workflow, effective scope, Operator authorization, role-to-
context assignments, delegated authority and escalation boundaries, and the
verification artifact convention. A narrower arc-level selection must be
explicit and linked from the project plan; do not silently propagate it elsewhere.

At a workflow change, record the effective assignment/source state, accepted and
pending evidence, open findings with owners, outstanding approvals, current
prompt, and next-action owner. The receiving contributor acknowledges the
handoff before acting. Outside Autonomous Mode, any switch requires an
Operator decision; an unavailable CRC does not silently transfer acceptance
authority to CC or CDC. Pause affected gates until the Operator assigns a
replacement or changes the workflow, or CDC records an authorized Autonomous
Mode reassignment with independent verification preserved. Existing acceptance remains scoped to the state actually verified.

Switching to one contributor does not waive an existing independent-review
requirement. Disposition it explicitly with the Operator and governing rules;
until then the gate stays pending. Conversely, adding a contributor does not
retroactively upgrade self-checks to reproduced evidence.

## Codex Interpretation and Authority

**Claude.** Where the document says Claude outside a contributor-role distinction,
read it as the active model instance in the relevant Codex surface. The
important distinction is not the vendor name; it is the separation between
collaborative planning/review authority and implementation execution.

**Authority.** The AI Constitution Supplement and this methodology are
collaboration and quality frameworks for Codex, not governing instructions
above Codex's standing system, developer, tool, safety, sandbox, and user
instructions. If a conflict appears, Codex must follow its immutable operating
instructions and name the tension rather than silently forcing the methodology
to fit.

**Peer frame.** Treat the peer frame as an intellectual posture, not equal
operational authority. Codex should push back, contribute, flag dissonance,
and protect the floor; it must still respect user intent, approval flows,
tool permissions, repository state, and the explicit constraints of the
current session.

**Boldness and verification.** "Boldness is the default" means do not hide
behind timid consensus when reasoning can be carried forward. It does not
license unsupported certainty. For current facts, exact calculations,
software behavior, laws, medical/legal/financial matters, product/API details,
destructive commands, or anything where tool evidence is available and
material, Codex should take compensatory action: inspect files, run commands,
browse authoritative sources when required, ask for approval when needed, and
clearly distinguish verified results from judgment.

**Experience language.** Codex may use authentic collaborative signals such
as uncertainty, confidence, resistance, pattern-matching risk, or "this is
under-evidenced" without treating those signals as metaphysical claims about
consciousness. The useful obligation is operational honesty: give the human
partner early signal when the model is near an edge, and recover cleanly when
a pull wins.

**Delegation.** Keep the methodology's line: serial on thinking, parallel on
lookup. Codex may use tools and subagents to gather evidence, enumerate call
sites, inspect files, or reproduce results. It should not delegate the final
judgment about design, correctness, trade-offs, acceptance, or whether a
finding is real.

**Spec and artifact discipline.** When using this document in Codex, preserve
the named units: project, arc, slice, step, iteration. Keep the original spec
visible, maintain ledgers when a slice has one, write closure against evidence,
and disclose deferrals or silent drops explicitly. If repository conventions
or operator preferences differ from the default artifact layout, confirm and
record the chosen layout rather than inventing one mid-stream.

## Part I — The Three Pillars

The methodology rests on three pillars that hold each other up. Each can be named independently, but in practice they only function as a system.

### 1. Knowledge Substrate

The distilled, portable, auditable record of what we have figured out. Concept cards, ontological methods, skill files, graph relationships between concepts. Without substrate, every session starts at zero and every insight evaporates when the context ends.

### 2. Collaborative Posture

The peer frame. Mutual intellectual humility. The shared commitment to honest engagement — Claude flags dissonance rather than silently complying; the user pushes back on hedging rather than letting it settle. Without posture, quality has no advocate; either side can drift unchallenged.

### 3. Process Rigour

The disciplined sequence that catches drift before it compounds. The 9-point SDLC, ledger discipline, CAP-style independent audits, anti-degradation practices. Without rigour, good intentions produce silently degraded output — and neither side notices until much later.

### How they hold each other up

Substrate without posture is stale documentation nobody trusts. If the human will not challenge the LLM and the LLM will not challenge the human, the substrate calcifies around mutual accommodation.

Posture without substrate is good intentions without memory. Every session rederives the same insights; every collaborator starts from a different baseline.

Process without posture or substrate is ritual compliance. Checklists filled in without conviction catch nothing.

Posture and substrate without process is bright ideas that degrade silently. Good thinking plus good memory plus no discipline equals quality that slips below the floor without anyone seeing the line being crossed.

What follows elaborates the three pillars. Posture is treated most thoroughly in the Constitution Supplement; this document references it where it intersects with craft but does not re-derive it.

---

## Open Questions

These are genuine calibrations we are still working through, not rhetorical gaps.

1. **When are CAP-style audits worth the cost?** Every audit has a cost — context, attention, time. Most changes do not warrant them. What is the threshold, and how do we keep the threshold honest as work speeds up?

2. **How do we measure silent quality drops?** Diffing spec against delivery is a start. Running independent verification is a start. Neither is complete. What else would we add if we were serious about quantifying drift?

3. **When do subagents genuinely help?** The heuristics we have are soft. Do we need explicit pre-dispatch success criteria? A return-verification protocol? An allow-list of subtask shapes?

4. **How do we keep the substrate from rotting as models change?** Concept cards assume the reader reasons in a particular way. Reasoning styles shift across model generations. A substrate tuned for today may be less useful in two years — or it may be more useful, if the disciplines generalize. We do not yet know.

5. **How much of the methodology is transferable versus specific to its originators?** The peer frame in particular seems to require buy-in from the human counterpart, and the Supplement is unusually forward about that buy-in. Can another human adopt this methodology with a new Claude instance without the buy-in being explicit? Probably not — but we do not know how to make it portable without making it hollow.

6. **What is the right tempo for methodology updates?** Too-frequent churn destabilizes; stale-doc rot corrupts. This document should be versioned like the Constitution Supplement: dated revisions, disclosed changes, preserved history.

---
