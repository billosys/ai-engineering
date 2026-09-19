---
project: project08-concept-card-metadata
status: active
depends-on: [project05-concept-card-skill]
blocks: []
related: [project03-concept-card-method, CompCogNeuro/book, ai-music-theory]
version: "1.37"
---

# Concept Card Metadata

Deliver concept cards that retain the early method's useful teaching bodies and
directly queryable concept relationships, generalize across source types, and
preserve the current evidence and lifecycle distinctions. Implement and exercise
the resulting skills against real sources until repeated extraction meets the
operator's quality bar. Metadata is the initial focus; card bodies and extraction
guidance are explicitly in scope throughout the project.

Project05 is formally closed in its recorded history. Subsequent use exposed
gaps that its package and bounded UAT evidence did not settle. This project owns
those gaps and their resolution. It does not inherit a presumption that the
current profile, its field names, or its body structure are sufficient.

## Basis And Design Status

The operator accepted this project name, the five-arc starting hypothesis, and
room for a potentially long Arc04 on 2026-09-12. The source checkout was clean at
`e763c661`; concept-cards reports `metadata.version: "4.8.1"`. The teaching-profile
changes are already in that baseline, not an uncommitted prototype. Historical
workbench reports retain their original 1.8.x labels; do not rewrite provenance
or infer an exact instruction match from a relabeled version alone.

The initial design hypothesis is recorded in
[the planning brief](./arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/planning-brief.md).
It combines directly usable discovery/graph metadata with scoped evidence and
lifecycle records. Exact fields, nesting, authorities and migration rules remain
research/design decisions. Arc02 will supply the accepted architecture artifact.

## Schema And Specification Discussion Gate

Operator addition, 2026-09-14: before finalizing or formalizing the metadata
design, review schemas together and discuss creation of a specification.
This makes the existing Arc02 schema/validator decision an explicit operator
checkpoint, not an implied approval from inventory or template conformance.
See [the discussion agenda](./artifacts/schema-and-spec-discussion-agenda.md).

Arc06 Slice11 must carry the evidence, alternatives and unresolved decisions
into that discussion. Arc02 owns the resulting design and any specification/
schema deliverables agreed there. Do not accept a normative profile, choose its
final schema form, or start implementing it as the accepted contract before
recording the operator discussion and decision. Exploratory comparisons and
clearly provisional drafts remain possible; they are not adoption.

Review the semantic model, human-readable specification, machine-checkable
constraints and representative body/metadata records together. Discuss scope,
authority, requiredness, extensions, versioning, migration and test coverage;
do not silently choose a schema language, file location or spec publication
format. Record what will be delivered and how it will be verified.
Project ledger P-15 carries this gate independently of final output-quality
acceptance. Later material design changes from Arc04 must return for discussion
before being promoted to the normative contract.

Slice12 evidence remediation and original Slice01 recomposition closed on
2026-09-15. They fixed historical interpretation and a replay error path,
not the future schema or specification. The P-15 discussion gate remains open.

## Required Outcomes

- A complete historical/current metadata inventory and capability crosswalk,
  including values, types, meaning, query behavior and migration consequences.
  The operator's named fields are examples, not an exhaustive requirement list.
- A researched, readable metadata profile covering books, research papers,
  white papers, blog posts, and wiki/encyclopedia articles, with source identity
  distinct from format, edition/snapshot, location and extraction provenance.
- Directly machine-readable typed relationships and competency-question data
  that support useful traversal without parsing narrative prose. Preserve
  identity, direction, support, uncertainty and revision applicability.
- Flexible discovery/classification without imposing category/subcategory/tier
  on every domain, while preserving historical classification information.
- Explicit semantics for lifecycle summaries and evidence/result references,
  including unknown, unassessed, missing, conflicting and stale data. No false
  implication that a whole card inherits one claim's evidence or admission.
- Implemented concept-cards guidance, templates, examples, reference material,
  and the document-extraction handoff changes the evidence shows are needed.
  Preserve sibling support directories and single-purpose guides.
- Real, repeated CC extraction of body and metadata; comparison against the
  historical Complete Musician/Erlang cards and the same CompCogNeuro subset;
  source-type diversity checks; and evidence-driven refinements as needed.
- A same-chapter Complete Musician trial using the operator's prepared Markdown
  and actual pre-skill cards, with predeclared measures, independent fresh
  extractions, bias-controlled review and explicit historical confounds.
- Full-book CompCogNeuro extraction after subset quality acceptance, with
  coverage and dependency reconciliation. The conditional gate is not a quiet
  deferral: failure returns to refinement; success opens the full-book slices.
- Fresh package/version/install checks and independent composition review,
  plus explicit operator acceptance of output quality before project closure.

## Current Direction: Semantic Families And Capabilities

Operator decision, 2026-09-14, following Arc01 Slice09 and the progress review:
adopt [the preserved assessment](./artifacts/semantic-family-processing-assessment.md).
The operator regards all prior work as well spent, explicitly retains the
rigorous bounded-packet approach when warranted, and prefers semantic
organization consistent with the work's ontological roots.

This is a modest execution pivot, not a reduction in scope or a schema decision.
Preserve all 115 transition-accepted contextual pairs and all original criteria.
The initial remainder was 440. After Slice12 repair and original Slice01
recomposition, 150 were accepted and 405 remained. Slice02's independent
closure added 30 CQ pairs, reaching 180 accepted / 375 remaining. Slice13's
independent closure adds eight actor-identity pairs; Slice14's independent
CRC closure adds twelve more; Slice15's independent CRC closure adds eight
bounded mode/role pairs, followed by Slice16's twelve independently accepted
pairs. CRC independently closed Slice17 after one focused repair, accepting its
eighteen extraction-run operation/input/method/time pairs, then completed fresh
readiness for Slice18. Live accounting is 238 accepted / 317 remaining / 22
assigned / 295 outside. Slice18 owns only run scope/worker/output Set B; the
other three approved provenance units remain unopened and 248 further pairs
retain their evidence/lifecycle-family owners.
Use the
[current coverage register](./artifacts/semantic-coverage-current.json).
The transition snapshot stays immutable. Process the remainder by family, retaining
exact field-path/record-kind accounting plus finer corpus/role distinctions.
Shared rules need explicit applicability, member roles and exceptions; repeated
field spelling, shape or lifecycle words never establish semantic equivalence.

Distinguish documented rules, populated observations, contradictions and
unspecified behavior. A bounded, evidenced unknown is an acceptable inventory
finding, not permission to silently omit the information or invent a rule.
Each family must explain concrete reader/extractor/query/migration consequences.

Reuse registered evidence and a common validation route where justified. Keep
small sequential correction packets for difficult or ambiguous areas.
Repairs remain implementation work subject to independent review. Under the
current framework, a reviewer who implements any repair needs another verifier
for that repair and its affected evidence. Earlier attributed CDC completions
remain historical records; they are not precedent for self-acceptance.

## Contributor Workflow (2026-09-17)

Operator authorization: "adopt the 3-Collab Workflow" and "Expedited Mode";
this existing session takes CDC, the Operator will create a separate CRC
session, and fresh CC sessions continue implementation. Effective scope is
remaining Project08 work from Arc06 Slice14 onward, not other projects or
retroactive changes to closed evidence. Was: Two-Contributor CDC + CC.

- CDC: this continuing design context; project/arc design, difficult
  investigations, structural replanning, first slice of each new arc, and
  independent arc/project composition review.
- CRC: separate Operator-created review context, with recorded acknowledgement of
  [cdc-directive01.md](./cdc-directive01.md); routine CC review, corrections,
  subsequent slice preparation within approved boundaries, ledger/coverage
  maintenance and closure assembly.
- CC: fresh independent implementing context for each issued assignment;
  tests and reports proposed-done to CRC through the Operator.
- Operator: relays CDC/CRC directives and escalations, CC prompts/reports,
  and retains all scope, schema/spec and output-quality approval gates.

CRC may close routine slices without a second CDC slice approval once the
agreed verification and bubble-up gates pass. It must escalate architectural,
scope/acceptance, evidence-waiver, cross-arc, exhausted-iteration or substantive
re-slicing decisions through preserved crc-escalationNN.md; CDC returns a
preserved cdc-directiveNN.md via the Operator before affected work resumes.
An unavailable CRC does not transfer its acceptance role silently.

New slice reviews use crc-verification.md. Historical cdc-verification.md
records retain their exact paths, authors and accepted states. Future arc and
project closure needs BOTH crc-verification.md (CRC's operational/composition
packet) and cdc-verification.md (independent design/composition verification)
for the same candidate, plus unchanged Operator gates. A reviewer implementing
a repair cannot independently accept it.

Expedited Mode remains enabled: scoped explicit-file commits, verified slice
closure and immediate next planned slice handoff within delegated authority.
It does not waive evidence, P-15, UAT, source fences or required escalation.
CRC returns arc readiness to CDC; CDC owns opening the next arc and first slice.

Historical workflow-transition state (current status is in the roadmap below):
source 020268248882358075b678bb855c0ac8d11b532a; planning
d6252b26878ead5045c843d1086b9194d516e2ee, both clean before these amendments.
Slice13 is closed at its recorded review; R1-R4 resolved. Live coverage remains
188 accepted / 367 remaining / 12 assigned / 355 outside. All six Slice14 rows,
all arc rows and all project rows remain open. No Slice14 implementation or
review packet is recorded at this transition; if concurrent work exists,
CRC must reconcile its assignment/state before proceeding.

At that transition the CC assignment became Slice14's cc-prompt-iteration01.md,
a routing
replacement of the preserved cc-prompt.md, not an executed repair pass.
CRC first reads/acknowledges the directive and checks the replacement before
the Operator relays it to fresh CC. The original prompt is not edited.
The recorded acknowledgement below completed that initial relay. Current
handoff: arc-level cdc-directive02.md answers CRC's post-Slice16 sizing request;
CRC has acknowledged it, independently closed exact Set A after Iteration01,
and opened exact Set B as Slice18 after fresh author readiness. Arc-level
exchange history lives in the arc plan.

### Design Handoff History

| Packet | Date | Predecessor / initiating decision | Scope / rows | Status | Next action |
| --- | --- | --- | --- | --- | --- |
| cdc-directive01.md | 2026-09-17 | No escalation/predecessor; Operator explicitly selects three contributors and Expedited Mode | Remaining Project08; Arc06 A6-1 through A6-10; Slice14 S14-1 through S14-6; P-1 through P-15 gates retained | Acknowledged by CRC context `01a0b07b-a4f0-7882-9881-b95ebb600779` on 2026-09-17 after reading the directive, plans, ledgers, current and frozen coverage, Slice13 review, and both Slice14 prompts; source `020268248882358075b678bb855c0ac8d11b532a`, planning `d2a6ddcaeaadd8251156422dcc8897ccad985ab4`, both clean | CRC releases `arc06-semantic-families-and-capability-requirements/slice14-provenance-context-and-reference-semantics/cc-prompt-iteration01.md` through the Operator to fresh CC; CC returns its packet to CRC for independent review |
| arc06/cdc-directive02.md | 2026-09-18 | Response to CRC escalation02 after independent Slice16 closure | Exact Slice17-21 Sets A-E; A6-1/A6-3/A6-6 and all P gates retained | Acknowledged by the same CRC context on 2026-09-18 against clean planning `c6d445b8` and source `ce3f7710`; Slice17 CRC-closed on 2026-09-19 after Iteration01; Slice18 exact-set, coverage, full native witnesses, guidance and prompt-author readiness checked | Operator relays `arc06-semantic-families-and-capability-requirements/slice18-run-scope-workers-and-outputs/cc-prompt.md` to fresh CC; Slice19-21 remain unopened |

Do not mark acknowledgement on CRC's behalf. CRC records its actual session
identity, read state, date and next action in this history before execution.
Any later assignment correction gets a new packet; issued packets stay intact.

## Continued Research Direction

Targeted primary-source research may now accompany family work before the
entire inventory closes. Compare alternatives against actual capability gaps;
do not adopt standards by name or design a final profile inside an inventory
packet. Final requirements/architecture still wait for complete, composed
inventory and research evidence. An early fixture is a diagnostic aid, not
proof of final-profile equivalence or real extraction quality.

Acceptance has three separate levels: evidence-backed inventory interpretation;
researched architecture with loss analysis and executable behavior checks; and
implemented skills demonstrated through repeated real extraction and operator
quality review. No earlier level substitutes for a later one.

## Arc Roadmap: Current Dependency Order

| Arc | Capability | Depends On | Current State |
| --- | --- | --- | --- |
| `arc01-metadata-research-and-requirements` | Historical inventory foundation and bounded contextual evidence; original broader scope preserved below | Baseline/operator brief | Closed-with-transfers, not fully delivered; 115 accepted pairs retained |
| `arc06-semantic-families-and-capability-requirements` | Complete family semantics, reusable evidence/replay, targeted standards research and no-loss capability/UAT requirements | Accepted Arc01 inputs and explicit transfer register | Active; Slice01/02/03/12-17 closed; 238 accepted and 317 remaining; Slice18 open with 22 assigned; Slice19-21 unopened |
| `arc02-metadata-architecture` | Usable profile, field authorities, compatibility/migration, specification and schema design as agreed with the operator | Independently composed Arc06, including transferred Arc01 requirements; P-15 discussion gate | Hypothesis; discuss before finalizing the contract |
| `arc03-skill-and-template-updates` | Implemented profile and extraction handoffs with representative examples and focused checks | Arc02 | Hypothesis; detailed plan when near |
| `arc04-real-extraction-and-refinement` | Repeated real-source extraction, body/metadata refinements, cross-source trials and conditional full-book delivery | Initial Arc03 profile; feeds back into design and implementation | Intentionally expandable; no fixed slice count |
| `arc05-package-gates-and-closure` | Fresh packaging/install evidence, migration and UAT reconciliation, independent project acceptance | Arc04 quality and coverage evidence | Closure cannot outrun UAT |

Arc06 is the next arc in dependency order, not a post-closure addendum.
Slice02 and Slice03 remain independently closed in their recorded history.
Slice13 repair d94ab1c6 now closes all six rows after independent CDC review
of R1-R4. Its 51 hashes, 37-record census, 2,054-record legacy comparison,
native diagnostics and exact contribution boundaries reproduce. The source
checkout advanced outside the relevant skills; the CDC report records the
failed literal HEAD guard and the equivalent pinned-input replay explicitly.
No CC supporting artifact was repaired by the reviewer.

Current accounting: 238 accepted / 317 remaining / 22 assigned / 295 outside
after independent Slice17 closure and fresh Slice18 opening. Slice14 accepted actor/actor.id in memory-admission,
preservation-decision, relationship-edge, source-locator, source-support and
validation-result. CDC's response to Arc06 escalation01 approves a kind-aligned
mode/role split: eight pairs in Slice15 and twelve in Slice16, now accepted.
Arc directive02 divides the retained provenance work into Slice17 operation/
inputs/method/time (18 pairs), Slice18 scope/workers/outputs (22), Slice19
cross-record run references (19), Slice20 creation time (11) and Slice21
preparation/method references (17). Each opens only after predecessor acceptance
and fresh CRC readiness. Slice17 now satisfies that gate; Slice18 is the sole
open provenance unit.
See [the current arc directive](./arc06-semantic-families-and-capability-requirements/cdc-directive02.md).
It explicitly retains the other 248 pairs with later semantic owners, including
synthetic/surface markers and CQ retrieval/revision interfaces. Scope approval
does not accept meanings or assign pairs; P-15 remains open.
CRC acknowledged and completed pre-opening native recount/witness inspection
and prompt-author readiness before opening Slice15. The directive alone
assigned/accepted no pairs and did not reopen CRC-accepted Slice14; this
CRC-issued Slice15 open set assigned eight without accepting them; the later
independent Iteration01 review accepted exactly those eight. Was: all these
responsibilities in unsized Slice15; no project capability or gate is reduced.
Was: Slice13 Iteration 01 pending and an unsized Slice14 complement.
This is the authorized late sizing of retained work, not scope reduction.
P-15, all UAT requirements and later evidence/lifecycle owners are unchanged.
The [three-slice workload assessment](./artifacts/cc-workload-observations.md)
is complete; its observations support a bounded, better-integrated repair,
not an automatic model change or a reduction of evidence requirements.
Existing Arc02-05 IDs and Arc04's operating contract remain stable. Numeric
order is not dependency order. Further findings may split or add arcs/slices;
record the changed owners and re-entry conditions before issuing new work.

[The transition register](./artifacts/arc01-transition-obligations.md) retains
every original S1/S4/A1 row and never-opened Slice02/03/05 obligation. Arc01
administrative closure accepts the transfer, not the unperformed semantics,
research or composition. Arc06's final acceptance must reconcile those exact
criteria. All project ledger rows remain open.

The operator's request to implement this direction supersedes the prior pause.
Expedited Mode resumes for scoped commits, independent review and planning
advance; it does not authorize CC to execute unopened work or override operator
quality gates.

## Historical Roadmap And Pause (Superseded As Execution Instructions)

The following v1.13 roadmap and pause are retained verbatim as planning history.
Their research sequencing and active-arc routing are superseded by v1.14 above;
their required outcomes and Arc04/05 quality obligations are not reduced.

### Original Five-Arc Starting Hypothesis

| Arc | Capability | Depends On | Current State |
| --- | --- | --- | --- |
| `arc01-metadata-research-and-requirements` | Historical/current inventory, primary-source standards research, capability and no-loss requirements | Baseline and operator brief | Batch01 and Slice06 through Slice09 accepted; execution paused by operator for progress/process discussion; Slice04/01 still unclosed |
| `arc02-metadata-architecture` | Usable profile, field authorities, compatibility/migration and validation design | Arc01 | Hypothesis; detailed plan when near |
| `arc03-skill-and-template-updates` | Implemented profile and extraction handoffs with representative examples and focused checks | Arc02 | Hypothesis; detailed plan when near |
| `arc04-real-extraction-and-refinement` | Repeated real-source extraction, body/metadata refinements, cross-source trials and conditional full-book delivery | Initial Arc03 profile; feeds back into design and implementation | Intentionally expandable; no fixed slice count |
| `arc05-package-gates-and-closure` | Fresh packaging/install evidence, migration and UAT reconciliation, independent project acceptance | Arc04 quality and coverage evidence | Closure cannot outrun UAT |

These arcs can split, grow or be resequenced when findings justify it. Arc04 can
change skills and revisit Arc02 decisions through newly scoped slices; Arc03's
completion does not freeze implementation. Record additions and superseded
assumptions in plan histories and ledgers. A coherent new capability may warrant
an additional arc rather than overloading Arc04.

Operator pause after Slice09 review (2026-09-13): complete independent review
and report progress, then stop before opening further work. Slice09 is now
CDC-closed after 4ae905c2. No next slice or revised execution strategy is
authorized by this pause; all required outcomes remain. Discuss the balance
between substantive semantic work and repeated evidence-maintenance cycles
before resuming. Was: automatic next-slice opening in Expedited Mode.

## Arc04 Operating Contract

Plan each next slice using the findings from the previous run. A normal sequence
is protocol/baseline capture, CC extraction, independent comparison and operator
review, targeted source refinement, then extraction in a fresh CC session. Keep
execution units bounded while allowing arbitrarily many such slices.

Require at least three new, separately identified CC extraction runs during
Arc04, including at least two fresh sessions on the final candidate profile and
the same bounded CompCogNeuro input. This is a minimum for observing consistency,
not an automatic stop count. Historical workbench outputs are comparison inputs
and do not satisfy the new-run requirement. A material change after a successful
run requires fresh evidence against the changed profile.

Pin source snapshots, skill files and hashes, prompts, actual loaded routes,
model/settings where available, tools, task scope, and output locations. Keep
prior answers and review conclusions out of fresh extraction contexts; give
them to the comparison context afterward. Record unavoidable contamination or
configuration differences. Count all attempts, including failed runs, and retain
their raw outputs before any manual correction. Label edited outputs separately.

Before generation, define anchored qualitative criteria for definitions,
construction/recognition, concrete examples, common errors, relationship richness,
source fidelity, metadata completeness, graph use, and usability. Section counts,
YAML parsing, verbosity and package gates are supporting observations, not quality
verdicts. Match the original subset for controlled comparisons; use historical
music/Erlang cards as quality references with cross-domain limitations recorded.

Inspect metadata and prose together. Exercise prerequisite traversal, extension,
contrast and related-concept queries from structured fields with a disposable
local harness. Verify edge direction, missing endpoints, cycles and uncertain
relations against expected results; a production graph server is unnecessary
for this acceptance evidence. Include the operator's fugue prerequisite question
as a motivating query and source-grounded analogues for the trial corpus.

Use representative bounded samples spanning all five source types named above;
choose actual accessible/licensed sources and controls before their runs. Separate
type from format, and test locator/identity behavior for the preparation formats
the profile claims to support. Do not force every source to contain a chapter,
page number, procedure, or other inapplicable feature.

Once repeated subset runs satisfy the agreed criteria and the operator accepts
their body and metadata quality, open full-book slices. Account for every chapter,
appendix and dependency with explicit disposition, stable concept identities,
duplicate/boundary reconciliation, cross-chapter edges and review coverage.
Sampling cannot be relabeled full-book extraction. Full-book findings can reopen
refinement and require affected subset/full-book reruns. An unavailable input or
capacity limit is an unresolved condition with a re-entry plan, not proof of done.

## Complete Musician Same-Chapter Trial

Operator addition, 2026-09-13: this is a required Arc04 regression/UAT track,
not merely another cross-domain illustration. Arc06 Slice11 now carries its
protocol requirements into the architecture/UAT handoff (was: Arc01 Slice03).
Arc04 will open bounded
intake/protocol, fresh-extraction and comparison/refinement slices when near;
no chapter or execution slice is selected/opened by this amendment.

Inputs (preserve the actual source-directory spelling):

- Prepared source: `/Users/oubiwann/Dropbox/Apps/sources-md/music-theory/complete-muscician/*.md`.
- Historical cards: `/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/*.md`.

Both local roots were found during planning. Availability is not edition,
conversion-fidelity or baseline-lineage verification. Before generation:

1. Freeze eligibility and chapter-selection rules without seeing new outputs.
   Require a complete readable chapter, accessible relevant notation/images,
   and traceable older-card coverage. Prefer a recorded seeded selection among
   eligible chapters; retain exclusions and reasons. Record prior familiarity
   with chapters/cards rather than claiming a pristine holdout. Freeze the
   selected chapter before tuning on its outputs.
2. Pin chapter bytes, source edition/representation, media/dependencies, legacy
   card files/hashes and any recoverable old prompt/run/edit history. Resolve
   chapter attribution against content, not filename or chapter_number alone.
   Explicitly map partial/cross-chapter cards and external prerequisite targets.
   Do not copy the textbook or images into this public repository; keep source
   material read-only and retain manifests/review evidence in approved homes.
3. Pre-register a source-grounded coverage checklist, task boundaries, measures,
   ordinal score anchors, unacceptable regressions, acceptance rules, run count
   and stopping conditions. Do this before new generation or scoring. Include
   definitions, source fidelity, construction/recognition, concrete examples,
   common errors/confusions, relationships, useful classification, source
   locators, machine-query capability and body readability. Measure shared
   capabilities separately from new lifecycle/provenance capabilities; neither
   old field names nor the new template shape define quality by themselves.
4. Generate from the chapter afresh, not by re-extracting the legacy cards.
   Keep legacy outputs, comparison conclusions and this conversation out of the
   execution context. Use at least two independently identified fresh new-skill
   runs on the pinned chapter/profile, recording loaded instructions, model/
   settings, tools, resource access, budgets and interventions. Preserve every
   raw attempt; manual fixes and revised-profile attempts are separate records.
   Record any unavoidable installed-skill or memory contamination.
5. Use source-grounded independent reviewers and randomized anonymous labels
   with counterbalanced order where feasible. Keep the identity key outside
   their context until judgments are frozen. For the shared-body comparison,
   use reversible presentation-only views that hide run labels but preserve
   substantive text; inspect native metadata separately for actual usability.
   Do not conceal missing fields, remove awkward material or rewrite either
   output to improve its score. Record residual style/schema recognizability
   and reviewer familiarity; blinding reduces bias but cannot guarantee none.
6. Compare both matched concepts and the entire chapter's coverage. Account for
   omissions, unsupported additions, duplicates and one-to-many splits/merges;
   do not cherry-pick matching cards or equate card count with recall. Treat the
   source as evidence, not the older cards as an infallible answer key. Exercise
   the same discovery/prerequisite/relationship questions over both native
   representations, recording mappings and unavailable external dependencies.
   Any test adapter must not invent relationships from narrative prose.
7. Report paired findings, disagreements, per-run variability and uncertainty,
   not just an aggregate winner. Do not treat many cards from one chapter as
   independent experimental replications or infer full-book/domain superiority.
   Historical models, inputs, revisions and interventions may be unknown:
   label this primarily a historical-output regression comparison, not proof
   that the skill alone caused a difference. If causal attribution is needed,
   plan a separate matched old-prompt/new-skill rerun on identical inputs and
   comparable settings, retaining the actual historical cards as a third,
   distinct baseline rather than replacing them.
8. Trace material regressions into skill/body/metadata refinement and fresh
   reruns; do not edit the baseline or move thresholds after seeing results.
   Record repeated-chapter tuning as contamination and use a separately
   preselected held-out check before generalizing an improvement. Require
   independent review plus operator quality acceptance for this track; a
   mixed/inconclusive result remains explicit, not an automatic success.

This track supplements the existing CompCogNeuro same-subset repetitions,
five-source-type trials and conditional full-book goal. It replaces none of
them. Package success, baseline age or a successful single music run cannot
discharge the new project ledger row P-14. Full-book Complete Musician
extraction is not added by this bounded chapter requirement.

## Scope And Version Boundaries

The expected concept-cards delivery range is 4.9.x, continuing the released 4.x
line from 4.8.1. Recheck the live authority on each implementation slice. Design
compatibility and explicit migration within that intent; do not conceal a breaking
change to fit a version number. Escalate a genuine conflict with the version
intent as a recorded design decision. Other skills own their own versions.

Focused parsers, validation fixtures, migration demonstrations and local graph
query checks are in scope when required to prove the profile. Decide the form
of any shipped schema/validator in Arc02; do not inherit Project05's exclusion
as an obstacle to this project's requirements. A general ontology-engineering
skill remains a future possibility, not a prerequisite to completing this work.

Production graph DB, MCP/RAG service deployment and automatic memory admission
remain downstream. Preserve the data and query capability needed for them.
Publishing releases, installing into managed user directories and changing
unrelated skills require their own applicable scope. Install smoke uses an
explicit temporary `INSTALL_DIR`.

## Closure And Plan Changes

The sibling [ledger](./ledger.md) governs acceptance. Formal closure requires
independent composition evidence and the operator's explicit quality decision.
Do not discharge a substantive gap as a no-op merely because current guidance
mentions the topic: compare generated behavior and explain the observed result.
Record each finding, affected requirements, source fix or justified disposition,
and rerun evidence. Add slices before advancing past unresolved failures.

No fixed timeline, slice count or green package report overrides these outcomes.
Reducing a required capability or moving unfinished quality work to a future
project requires an explicit operator decision recorded in the plan.

## Version History

- 1.37 (2026-09-19): CRC independently closes Slice17 after reproducing its
  Iteration01 controls and committed wrapper, accepting exactly eighteen Set A
  pairs. Opens directive02 Set B as Slice18 after fresh native/guidance and
  prompt-author readiness. Coverage is 238/317/22/295; no schema, source, UAT
  or project-criterion change occurs.
- 1.36 (2026-09-18): CRC acknowledges arc directive02 and opens only its
  approved eighteen-pair Slice17 after exact-set, native-witness and prompt-
  author readiness checks. Live coverage becomes 220/335/18/317 with no new
  acceptance; Slice18-21, the 248 later-family pairs, P-15 and UAT remain open.
- 1.35 (2026-09-18): CDC answers arc escalation02 with five exact provenance
  units (18/22/19/11/17) and explicit remainder ownership. CRC may open them
  sequentially after acknowledgement, predecessor acceptance and fresh author
  readiness. Reconciles stale live status to 220/335/0/335; no acceptance,
  source, schema, UAT or project-criterion changes.
- 1.34 (2026-09-18): CRC independently closes Slice16 after its focused
  replay repair. Twelve bounded supporting-kind mode/role pairs enter accepted
  coverage once, reaching 220/335/0/335. Slice17 remains held for CDC sizing;
  P-15, source, schema, runtime, UAT and operator gates remain open.
- 1.33 (2026-09-17): CRC opens CDC-approved twelve-pair Slice16 after native
  recount and prompt-author readiness. Coverage is 208/347/12/335 with no
  new acceptance; Slice17, P-15 and UAT gates remain unchanged.
- 1.32 (2026-09-17): CRC independently accepts Slice15's eight bounded
  mode/role pairs after Iteration01, reaching 208/347/0/347. Slice16 awaits
  its own readiness; Slice17, P-15 and all real-use gates remain intact.
- 1.31 (2026-09-17): CRC acknowledges Arc06 directive01 and opens its
  approved eight-pair Slice15 after pre-opening native recount and prompt
  authoring. Live coverage becomes 200/355/8/347; no new acceptance.
  Slice16/17, P-15 and real-use gates remain intact. Was: 200/355/0/355
  while Slice15 issuance awaited readiness.

- 1.30 (2026-09-17): Arc06 CRC escalation01 answered with an eight/twelve
  mode-role boundary and explicit Slice17 provenance ownership. CRC prepares
  subsequent open sets after acknowledgement/readiness. Was: unsized Slice15;
  no acceptance, source, UAT or P-15 scope changes.

- 1.29 (2026-09-17): Independent CRC review closes Slice14's six rows and
  accepts twelve bounded actor-identity pairs, bringing live coverage to
  200/355/0/355. Slice15 remains unsized under CDC design authority; all
  Arc06 and project rows, P-15 and the UAT obligations remain open. Was:
  Slice14 assigned at 188/367/12/355.

- 1.28 (2026-09-17): Operator selects CDC/CRC/CC plus Expedited Mode for
  remaining Project08 from Slice14. Records seats, authority, initial directive,
  transition state and per-scale verification. Preserves the issued initial
  prompt and replaces its routing with iteration01; no semantic scope or
  acceptance changes. Was: two contributors after Slice13 closure.

- 1.27 (2026-09-17): Arc06 Slice13 repair independently closes, adding eight
  accepted pairs. Opens bounded 12-pair Slice14; Slice15 retains the broader
  provenance remainder for sizing. Records current two-contributor authority
  and no self-acceptance of reviewer repairs. Was: Slice13 Iteration 01 open;
  no scope or schema/UAT gate is reduced.

- 1.26 (2026-09-15): Arc06 Slice13 review reproduces the submitted replay
  but exposes false-success controls and incomplete evidence checks.
  Opens bounded Iteration 01, retaining scope/handoff and all prior acceptance;
  was: initial execution. No model change, schema adoption or scope reduction.

- 1.25 (2026-09-15): Arc06 Slice03 CDC closure verifies reusable replay with
  attributed control/snapshot corrections. Opens eight-pair Slice13 and
  preserves remaining provenance responsibilities under planned Slice14;
  was: unsized Slice13. No new semantic acceptance or schema adoption.

- 1.24 (2026-09-15): Arc06 Slice02 independently closes after ca1df926 and
  attributed replay completion; 180 accepted, 375 remaining. Splits the
  combined Slice03 hypothesis into bounded replay work now and preserved
  provenance semantics in Slice13. Was: CQ repair pending.

- 1.23 (2026-09-15): Arc06 Slice02 CDC review opens bounded Iteration 01;
  was: first CQ submission. Preserves two verified rows, 150 accepted pairs,
  all remaining work and P-15. Records completion of the three-slice workload
  observation window without claiming causal model comparison.

- 1.22 (2026-09-15): Arc06 Slice12 R5/R6 independently reproduce; original
  Slice01 recomposes with all seven rows done. Records attributed restoration
  of prior handoff text, 150 accepted/405 remaining in a new current register,
  and a bounded 30-pair Slice02. Was: Slice12 repair open. Frozen transition,
  P-15 schema/spec discussion and all real-use quality gates remain unchanged.

- 1.21 (2026-09-14): Operator approves a small Arc06 Slice12 for the two
  residual Slice01 findings; was: sizing decision pending. Adds an explicit
  schema/specification discussion gate and P-15 before design formalization,
  carrying it through Arc06 Slice11 into Arc02. No schema form is selected,
  Slice01 is not closed, and existing quality/version/UAT obligations remain.

- 1.20 (2026-09-14): Arc06 Slice01 Luna/xhigh repair closes S1-2/S1-5,
  retaining S1-1/S1-4/S1-6. Historical requiredness and search-error handling
  still block S1-3/S1-7. Records a bounded remediation proposal after the fifth
  iteration; was: Iteration 05 execution. No automatic Iteration 06, new slice,
  scope transfer or acceptance of the 35 pairs. Operator sizing decision remains
  pending; all source/UAT/architecture obligations are unchanged.

- 1.19 (2026-09-14): Arc06 Slice01 Terra/high repair reproduces native
  symmetry/endpoint controls and closes S1-4 alongside S1-1/S1-6. Opens bounded
  Iteration 05 for missing teaching context, observed-versus-required meaning,
  and complete current replay; was: Iteration 04. Records the operator's
  possible Luna/xhigh trial without changing settings or acceptance criteria.
  The five-iteration sizing safeguard, 115 accepted pairs and all UAT gates
  remain; no next slice or new semantic coverage is accepted.

- 1.18 (2026-09-14): Fresh-session Slice01 repair improves native checks and
  semantic integration; CDC closes handoff row S1-6, not the slice. Iteration
  04 targets remaining census/context and result-comparison work; was:
  Iteration 03. Reuses accepted readings, recommends an operator-selected
  higher-effort trial, and preserves scope, 115 accepted pairs and all UAT gates.

- 1.17 (2026-09-14): Arc06 Slice01 Iteration 02 structural checks pass,
  but native replay, actual reading and semantic integration remain open.
  Requires a new execution session for Iteration 03; was: Iteration 02.
  Preserves verified witnesses, every original criterion and 115 accepted pairs.

- 1.16 (2026-09-14): Arc06 Slice01 repair review retains verified gains but
  finds incomplete contextual evidence, native-query replay and registry
  alignment. Opens Iteration 02 in a new CC session; was: Iteration 01.
  Records unchanged settings and same-task reuse without a causal load claim.
  No scope, accepted coverage, architecture or UAT gate changes.

- 1.15 (2026-09-14): Arc06 Slice01 review preserves structural successes
  and requires contextual evidence, executed queries and legacy assertion
  semantics repair. Records workload observations without changing model/effort,
  scope, accepted coverage or any UAT gate; Slice02 remains unopened.

- 1.14 (2026-09-14): Operator accepts the semantic-family/capability pivot
  after Arc01 Slice09 and requests the next arc. Preserves the assessment,
  accepted 115 pairs and all prior planning; transfers 440 pairs and original
  integration/research/UAT-design obligations into new Arc06. Allows targeted
  research before full inventory closure; retains Arc02-05 identifiers, all
  quality/version gates and the bounded iterative method where appropriate.
  Arc01 closes administratively with explicit deferrals, not a success claim.

- 1.13 (2026-09-13): Arc01 closes Slice09 after 4ae905c2; operator requests
  a pause for progress/process assessment before further work. Records 115
  accepted contextual pairs without implying project completion or changing
  scope, research dependencies or UAT gates.

- 1.12 (2026-09-13): Arc01 closes Slice08 after independent review of
  3436020a, retaining unresolved reference components as bounded findings.
  Opens 21-pair Slice09 for claim/card assertion and source/support linkage.
  All original composition, repeated-run and P-14 quality gates remain.

- 1.11 (2026-09-13): Arc01 closes Slice07 after independent review of
  f82d0524 and opens the 27-pair Slice08 source-support comparison. Updates
  status only; all no-loss, composition, repeated-run and P-14 gates remain.

- 1.10 (2026-09-13): Operator adds a required Complete Musician same-chapter
  historical-output regression/UAT track. Records source/card roots, pre-run
  selection and scoring, fresh repetitions, bias controls and causal limits.
  Adds P-14; Arc01 Slice03 plans the protocol, Arc04 executes/refines it.
  Existing trials and active Slice07 scope are unchanged.

- 1.9 (2026-09-13): Arc01 Slice06 closes after independent review and an
  explicitly attributed CDC replay-documentation completion. Opens Slice07
  for twenty source/locator pairs; was: Slice06 remediation. All original
  composition and quality gates remain, with no project scope reduction.

- 1.8 (2026-09-12): Arc01 Slice04 Batch01 delivers accepted ten-pair semantic
  evidence after an explicitly CDC-authored replay-documentation correction.
  Opens bounded sibling Slice06 for 37 record-identity/type/classification
  pairs. Was: first checkpoint pending. All other work and composition gates
  remain owned; no full-slice closure or project requirement reduction.

- 1.7 (2026-09-12): Arc01 Slice04 follow-up reports diagnosis without new
  semantic artifacts. Authorizes one bounded identity-evidence checkpoint
  within the existing corrective iteration before sizing further execution.
  Was: whole-packet repair as the next delivery. All outcomes and gates remain.

- 1.6 (2026-09-12): Arc01 Slice04 review reproduces exact 555-pair coverage
  but finds incorrect semantic assignments and missing evidence/closeout.
  Opens a corrective iteration without changing project requirements. Was:
  Slice04 initial execution; Slice05 still awaits independently verified inputs.

- 1.5 (2026-09-12): Arc01 Slice01 sizing in `2b26282e` justifies two
  additional remediation slices. Slice04 opens for identity/source/graph
  semantics; Slice05 will finish lifecycle semantics and replay. Was: one
  Iteration 04 assignment. Slice01's original requirements stay open for
  recomposition before Slice02 research; no quality objective is deferred.

- 1.4 (2026-09-12): CDC reproduced Iteration 03's focused control-character
  and document-classification repairs. CC explicitly leaves R2/R4 open.
  Iteration 04 prioritizes the authored semantic-family map and literal
  reproduction route; outstanding implementation instructions remain visible.
  Was: Iteration 03 required. Project acceptance scope is unchanged.

- 1.3 (2026-09-12): CDC reproduced Iteration 02's boolean/shape and 308-path
  corrections. Iteration 03 addresses remaining JSON/framing edge cases,
  incomplete semantic analysis and a failing verification recipe. Was:
  Iteration 02 required. No advancement or scope reduction.

- 1.2 (2026-09-12): Slice01 Iteration 01 committed with operator approval.
  CDC reproduced deterministic parsing but found boolean/type loss, omitted
  null/empty field paths and unresolved semantic crosswalk work. Iteration 02
  continues the same scope; was: Iteration 01 required.

- 1.1 (2026-09-12): Slice01 CDC review requires a Fennel helper replacement,
  complete field dispositions, corrected counts, reproducible commands and
  refreshed source availability. Operator language preference and commit hold
  are recorded in AGENTS.md. Was: Slice01 ready for its initial CC run.

- 1.0 (2026-09-12): Operator-authorized Project08 opening. Adopts five provisional
  arcs, the 4.8.1 baseline and 4.9.x intent, broad metadata preservation, body
  refinement, uncapped Arc04 slices, separate CC runs and conditional full-book
  extraction. Addresses quality gaps surfaced after Project05 closure.
