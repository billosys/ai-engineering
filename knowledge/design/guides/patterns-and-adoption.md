# Patterns and contextual adoption

Use this route when a pattern from another system looks useful for a real task.
The goal is a supported local decision, not a catalogue of borrowed ideas.
Start with the supplied brief, content, identity and working behavior; a source
page can inform the decision but cannot establish that your adaptation works.

## Make a bounded decision

1. **Name the task and candidate.** State what the person needs to do, where
   the candidate pattern would help, and what must remain intact. Use the
   existing brief and evidence distinctions in [From a Brief to a Revised
   Design](design-workflow.md); do not turn this route into a new questionnaire.
2. **Check what already exists.** Inspect the current flow and the smallest
   relevant part of the candidate source. Note its intended users, setting,
   evidence, dependencies and contribution or adoption conditions. Look for a
   local equivalent and a credible alternative before proposing a new pattern.
3. **Separate the claims.** Keep upstream evidence about the source pattern
   distinct from local inspection or technical checks, participant research,
   and service-owner decisions. Record what each observation supports and what
   remains unknown. Do not transfer a study result or conformance claim to a
   changed implementation.
4. **Choose adopt, adapt or decline.** Adopt when task, content, setting and
   constraints fit the pattern as supplied. Adapt when its useful principle
   transfers but details need to change; name those changes. Decline when an
   existing route works better or the pattern's assumptions do not fit. State
   the reason and one context where the other choice might be appropriate.
5. **Make the first use reversible.** Identify the smallest route or state to
   try, what a credible failure would look like, who owns the next check, and
   how to back out or revise. Check the actual task before widening adoption.
   Name a participant, service, privacy, accessibility or platform review only
   when that decision needs it; do not claim the review happened in advance.

The note can be a few sentences in an existing design brief or handoff. This
method does not require an evidence schema, committee, source inventory or
government contribution workflow. Read the cited source when it can change a
consequential choice; the decision and its limits should still be clear to a
designer who does not need to study a source catalogue first.

When the adoption changes an existing semantic token contract across owners or
implementations, use [Migrate a Semantic Design System Between Owners](system-migration.md)
for the role map, compatibility, mode propagation, implementation projection
and rollback. The [LFE semantic mode handoff](examples/lfe-system-handoff.md)
shows one bounded case. This route does not add a required evidence schema or
change the adopt/adapt/decline decision above.

## What the source comparisons support

The [GOV.UK Design System contribution criteria](https://design-system.service.gov.uk/community/contribution-criteria/)
ask whether a proposed pattern is useful and unique, then whether a contribution
is usable, consistent and versatile in that system's publication context. Its
examples point to reuse across services and testing in stated contexts. These
are useful questions about alternatives, evidence and fit. GOV.UK's own research,
style, frontend and publication criteria govern its system; they do not certify
this skill's examples or make its identity and standards universal.
**Decision:** adapt its usefulness, uniqueness and context questions for a local
choice; decline its system-specific publication, style and frontend rules as
general acceptance criteria.

The [USWDS maturity model](https://designsystem.digital.gov/maturity-model/)
separates integrating principles, following UX guidance and using USWDS code.
Its incremental route shows that a team can use a relevant principle or inspect
UX guidance without installing its stylesheet or replacing every component.
The levels describe adoption of USWDS; adapting one idea does not make a project
USWDS-compliant or establish a maturity level. A code import needs its own
implementation and contextual checks.
**Decision:** use the principles/guidance/code distinction to choose a local
adoption depth; decline importing USWDS code or claiming its maturity from that
comparison alone.

The [Design Council Framework for Innovation](https://www.designcouncil.org.uk/resources/framework-for-innovation/)
describes divergent and convergent exploration, alternatives, small tests and
iteration, alongside people-first and collaborative principles. That supports
the existing small brief, meaningful alternatives and revision in the workflow
guide. Keep those activities proportionate to the decision; this comparison
does not add mandatory phases or authorize a separate research program.
**Decision:** adapt the iterative alternatives-and-checks idea to the existing
workflow; decline a fixed four-phase gate for every task.

## Worked decision: the library visit form

The [form and language text cases](using-the-skill.md#forms-and-recovery) are
fictional examples for the
four required fields Name, Email, Visit time and Visitors. The task is a short
request with a possible interruption. The form already has visible labels,
instructions, a linked error summary, retained valid values, and separate
explicit Save, Restore and Clear actions. Restore warns that it replaces all
four current fields. Completion is a local simulation; nothing is sent or
reserved. A representative fictional entry is Sam Reader,
`reader@example.com`, Morning (`AM-101`) and 2 visitors. See the [form and
recovery guide](forms-and-recovery.md) for the full state sequence.

**Decision — adapt the recovery pattern for this example.** The upstream
comparisons make reuse and evidence scope worth checking; they do not provide
research about this library service. Explicit recovery can be useful when a
person is interrupted while completing a transaction. Here, session storage is
limited to this tab and same-origin scripts can read it; the person chooses
when to save, restore, or clear. The no-clobber behavior for missing, invalid,
expired or unavailable drafts is a local choice, as are its 24-hour restore
window and fictional data. A real service must decide whether this storage,
retention, data handling, recovery and completion contract fits its users and
deployment. Do not copy this pattern into a service without that review.

A credible failure would be a person mistaking Save for submission, losing
current edits when Restore replaces them, or believing an example confirmation
means the service received a request. The current instructions and local-only
confirmation make those cases visible in the specimen; they do not show how a
real service or its participants would respond.

The existing independent Chromium checks exercised named English and Arabic
routes, linked errors, partial save/reload/restore, malformed and expired draft
handling, storage-failure messaging and completion at the recorded widths and
inputs. Those observations apply to the tested engine and states. The Arabic
form's actual labels, errors, draft instructions/messages and completion also
received the Operator's wording verdict, “Reviewed: suitable for this example.”
That approval is for the unchanged illustrative wording. These separate
observations do not establish real-service behavior, data or privacy policy,
participant research, native Arabic input, assistive-technology quality, native
zoom, other browser engines, or accessibility conformance.

**First use and handoff.** For a real service, first map the existing task and
failure policy with its service and privacy owners. Trial the explicit recovery
flow on one representative route with fictional or safely controlled data;
check that Save is deliberate, Restore replacement is understood, failures
preserve current entries, and Clear affects only the service's own draft. The
service owner decides whether to keep, adapt or remove recovery after suitable
participant and technical review. Before retiring it, the owner chooses and
communicates what happens to drafts already saved: preserve a recovery and clear
route, or provide an agreed migration, expiry or disposal path and explain the
transition to affected people. Keep ordinary submission, error and retry
working, and change only the service's own recovery path. This fictional example
does not implement a rollout, migration, retention rule or browser-level
deletion guarantee. Its checks are starting questions, not a live rollout
result.

## Counterexample: editorial reading and exploration

The supplied [LFE reading-desk text case](using-the-skill.md#dense-comparison)
and its [workflow case](examples/lfe-workflow.md) support browsing, searching and reading
editorial material. That task does not become a short transaction merely
because the form has useful labels or recovery. Do not add required personal
details, a visit request or draft persistence without a task and evidence that
call for them. Keep LFE's supplied identity and working reading/search behavior;
use its own navigation and content structure for an editorial change. The
method transfers as a decision process, not as a visual skin or interaction
template.
