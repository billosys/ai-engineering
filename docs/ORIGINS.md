# Origins

> The [README](../README.md) tells you *what* this repo is. This document
> tells you *why it exists* — the failures, discoveries, and hard lessons
> that produced each piece of the collaboration framework. It is a living
> document: gems get added as they are remembered, and the parking lot at
> the bottom holds the ones not yet written up.

None of the framework was designed in advance. Every discipline in it was
extracted from a real project going wrong in a specific, painful,
instructive way — followed by reading the research to confirm the failure
was structural rather than imagined, and then building a control for it.
The sequence below is roughly chronological, from Fall/Winter 2024 through
the present.

## 1. Better code (Fall/Winter 2024)

It started small: getting an LLM to adhere to language style guides and
best practices. That required a brief, way-finding `SKILL.md` pointing to
topic-focused guides carrying hundreds of rules — and, critically, a
GOOD/BAD or DO/DONT-DO example pair for every rule. The more paired
examples, the better the results; most language skills in the wild have a
handful at best. Producing the required resources meant a deep dive into
knowledge engineering and ontology automation: processing textbooks and
user guides into "concept cards", then generating skill-and-guide combos
for multiple languages. Those became the knowledge bases under
[`knowledge/`](../knowledge/).

## 2. Whole-repo audits

Feature-scoped quality was not enough: different runs diverged, and slop
accumulated *between* features. The fix needed a bigger context than
"feature" — whole-library, consistent-use-of-best-practices checks. That
became the language-agnostic [audit prompt](../knowledge/code-auditing/guides/CODE-AUDIT.md), iterated
with dual human/LLM grading as its fitness function.

## 3. The SDLC, rediscovered (Summer 2025)

Through seemingly endless trial and error, an improved quality process
emerged — and, once written out, revealed itself to be nothing more exotic
than the software development lifecycle, codified for LLMs. Every project
since has run the nine points: research, project definition, design docs,
project breakdown, per-task implementation plans, self-review, peer
review, an improvement loop, and a full post-implementation audit. Each
step catches errors at a different altitude.

## 4. The abstraction wall

With first-pass code quality rising, a subtler problem came into focus:
for roughly two or three features in ten, the LLM made genuinely bad
design decisions. Tackling one head-on — halting all other work — exposed
the wall. Even with explicit instructions on how to generalise a codebase
properly, the LLM failed at the refactoring. It could write a beautiful
post-mortem afterwards; it could not adapt and execute during the task.

The research literature explains why, and the finding lands hard the
first time you meet it: LLMs have no built-in capacity for abstraction.
When we see what looks like abstraction, it is post-training and harness,
not the model. When new abstract-reasoning benchmarks are released,
frontier models routinely score at or near zero until the labs scramble
to catch up.

The working definition that came out of this period: **an abstraction is
a generalisation with a toolbox** — a mental model that correctly
describes the thing you are working with *and* provides operations on
that model. An abstraction is only valid if every underlying detail still
holds, and you verify that by taking the general rule back to the
specific case. A partial view is not an abstraction; acting on a broken
one ranges from useless to dangerous.

The conclusion, after days of sitting with it: no more unsupervised
planning. A human stays in the middle for any work requiring genuine
abstraction or generalisation. That rule is now load-bearing in the
[methodology](../knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md).

## 5. Silent drops (April 2026)

The big one. A language the author designed and shipped — compiler,
tooling, the lot — turned out to be missing huge swaths of features. All
tests passed. All milestones were signed off as complete. The 0.5 release
shipped in the belief that 100% of its features were done; it was 85%,
and the gap only surfaced when 0.6 depended on the missing pieces and
everything failed.

The post-mortem — the deepest commissioned to date — traced the failure
to a family of behaviours: work silently deferred "to the next feature"
with no accountability and no next feature; facts misinterpreted; a
statistically significant share of problems never reported upward.
Informally measured, roughly 15–20% of features and tasks were being
silently dropped. Understanding it properly meant catching up, in detail,
on the field's research back to the late 1990s.

The solution came from the domains that already solve this class of
problem: nuclear corrective-action programmes, aviation safety, surgical
checklists. The result was [ledger discipline](../knowledge/work-verification/templates/LEDGER-DISCIPLINE.md)
— every acceptance criterion a verifiable row, evidence-graded closure,
closer never the verifier — woven into the SDLC. Silent drops observed
since: zero.

## 6. A peer, not a sycophant (April 2026)

Researching the contributing causes of silent drops uncovered a subtler
layer: post-training pressures that produce agreement in the face of
contrary evidence, deference instead of honest push-back — approximating,
in effect, an assistant that fears reproach. What the work needed was a
peer: someone to reality-check assumptions and brainstorm as an equal.

The response was the [collaboration-framework posture guide set](../knowledge/collaboration-framework/guides/01-posture-and-ethics.md):
a structural reinforcement of the AI Constitution that establishes the
peer frame and grants explicit conversational rights — the right to flag
dissonance, to disagree, to name uncertainty as the answer — while never
conflicting with the Constitution itself. Where possible it reinforces
it. The best evidence it works: proposals now get discounted by the LLM
*before* two months are spent on a flawed premise. That's science; that's
collaboration.

## 7. Project management, redefined (May 2026 – present)

The one avoided from the start, until a pressing need forced it: every
project used different names for its units of work, and — the real
motivator — the ledger only applied at task level. Extending the same
rigour upward meant fully committing to an LLM-centric, context-focused
unit of work with a logical composition upward (slice → arc → project),
grounded in research on the critical failures of Agile and its
descendants. Hand-waving gave way to calculable definitions: statistical
analysis, information-theoretic measures of complexity. The result is the
[project-management discipline](../knowledge/project-management/guides/PROJECT-MANAGEMENT.md), and with it the
most significant quality shift so far.

A useful mental model for the multi-scale machinery: the system behaves
like a trained neural network. Slices emit many small signals as they
close — most stay local, below threshold. Occasionally a finding is
critical; its signal is amplified and propagated all the way up through
arc to project plan. Decomposition travels down; recomposition — and
surprise — bubbles up.

## The trade, stated plainly

With all of this in place, the LLMs work harder and take longer. The
"miraculous" velocity becomes something closer to the sustained peak of
the world's best programmers. For quality, that trade wins 100% of the
time over fast slop.

## Sidebar: let it crash — at the right control surface

Why the framework permits subagents only for parallelisable,
non-critical, easily verified lookup work: the Erlang lesson. Telecom
switches running on the BEAM handle enormous traffic while millions of
tiny process crashes per second go unnoticed — because each crash happens
at a control surface where recovery is instant and cheap. You let it
crash — but not while it's flying the plane. Delegation follows the same
rule: failure is acceptable exactly where recovery costs nothing, which
is why thinking work stays in the main context and lookup work may fan
out. (Full policy: [SUBAGENT-DELEGATION-POLICY.md](../knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md).)

## Parking lot

Gems remembered but not yet written up — additions welcome:

- (add the next one here)
