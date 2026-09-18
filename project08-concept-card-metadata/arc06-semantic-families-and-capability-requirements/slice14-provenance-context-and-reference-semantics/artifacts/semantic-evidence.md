# Slice14 semantic evidence: actor context in supporting and result records

Status: CC proposed-done; independent CRC verification is required. This is a
bounded inventory interpretation, not a normative actor model, schema adoption,
source-truth acceptance, extraction-quality acceptance, operator acceptance,
memory admission or runtime work.

## Opening state and exact boundary

- Source checkout: /Users/oubiwann/lab/billosys/ai-engineering, opening
  020268248882358075b678bb855c0ac8d11b532a, clean and read-only.
- Planning checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning,
  opening 8c18f82a28b0d49d61ccc23e94939358a8777c01, clean.
- Current coverage is a live planning artifact at the opening state:
  188 accepted / 367 remaining / 12 assigned / 355 outside.
- The immutable transition remains 555 total, 115 accepted, 440 remaining,
  35 transition-assigned and 405 outside. It is not replaced by the current
  checkpoint.
- The executed assignment is cc-prompt-iteration03.md, the second corrective
  refinement after CRC review of cc-prompt-iteration02.md. The predecessor
  packet remains preserved; no pair is independently accepted.
- The packet covers exactly the following twelve field-path/record-kind pairs:

| Field path | Record kind |
| --- | --- |
| actor | memory-admission |
| actor | preservation-decision |
| actor | relationship-edge |
| actor | source-locator |
| actor | source-support |
| actor | validation-result |
| actor.id | memory-admission |
| actor.id | preservation-decision |
| actor.id | relationship-edge |
| actor.id | source-locator |
| actor.id | source-support |
| actor.id | validation-result |

Assignment is not acceptance. The exact scope, read set, source/planning
boundaries and six-file fence are registered in
artifacts/semantic-membership.json under the evidence IDs
assignmentPrompt, slicePlan, projectPlan, projectLedger, arcPlan and arcLedger.

### Iteration03 range correction

This iteration corrects only registered evidence locations and the literal
replay route. All 42 declared source_range values are resolved against the
file at each row's declared authority and read mode; valid multi-span and JSON
descriptors pass, while reversed and out-of-bounds controls fail. The native
census, meanings, exact twelve-pair scope and acceptance boundaries are
unchanged. This is structural evidence pending independent CRC verification.

### Iteration02 corrections

CRC's R1 correction is member-specific: source-support has five selected
records, four populated pilot records and one template/null record. The
actor.id-source-support meaning now states that denominator explicitly rather
than attributing the four template/null count to that member. R2-R4 are
addressed in the literal route: committed replay executes the validation code
from the explicit recipe revision, source comparison is path-scoped and
reports opening/current commits, and the authored YAML exclusions are checked
against the exact YAML-error paths derived from the pinned inventory. These
remain CC proposed-done repairs pending independent CRC reproduction.

## Native census

The frozen native inventory was read from its pinned planning snapshot and
filtered to parsed records whose record_kind is one of the six assigned kinds
and whose values is an object. The selected denominator is twelve:

| Record kind | Parsed records | Parent absent | Parent object / null id | Parent object / string id | Native witnesses |
| --- | ---: | ---: | ---: | ---: | --- |
| memory-admission | 2 | 1 | 1 | 0 | template; synthetic example |
| preservation-decision | 1 | 0 | 1 | 0 | template |
| relationship-edge | 2 | 1 | 1 | 0 | template; synthetic example |
| source-locator | 1 | 0 | 1 | 0 | template |
| source-support | 5 | 0 | 1 | 4 | template; four Arc07 pilot supports |
| validation-result | 1 | 0 | 1 | 0 | template |
| Total | 12 | 2 | 6 | 4 | six templates, two synthetic, four pilot |

No selected parent is null, an empty mapping or an unexpected type. At the
child level, the exact states are:

| actor.id state | Count | Meaning in this census |
| --- | ---: | --- |
| parent absent / child not inspectable | 2 | The synthetic memory-admission and relationship-edge examples omit actor; this is not a null child and not semantic inapplicability. |
| child null | 6 | Each selected template has actor: {id: null, mode: null, role: null}. |
| child missing in object | 0 | No selected object omits id. |
| empty string | 0 | No selected empty label. |
| non-empty string | 4 | The four Arc07 pilot source-support records use codex-cc. |
| unexpected type | 0 | No selected unexpected child type. |

The family breakdown is also part of the authored registry and is recomputed
by the literal validation route:

| Family | Records | Parent absent | Object/null id | Object/string id | Interpretation |
| --- | ---: | ---: | ---: | ---: | --- |
| templates | 6 | 0 | 6 | 0 | Reusable frontmatter/body contracts, not populated actor observations. |
| synthetic examples | 2 | 2 | 0 | 0 | Memory-admission and relationship-edge examples omit the actor parent. |
| Arc07 pilot supports | 4 | 0 | 0 | 4 | Candidate source-support records with populated record-local labels. |

All four populated support actors are exactly:

{id: codex-cc, mode: agent-direct, role: extractor}.

This is a repeated label/role/mode observation within the four pilot support
records. It does not establish that codex-cc names a human, model, tool,
process or composite, nor that it is globally comparable to any other label.
The four support records remain candidate support records with verification,
reconciliation, preservation and admission unassessed.

### Legacy comparison and exclusions

The same frozen inventory contains 2,054 parsed legacy mappings with
record_kind: untyped. The native query found:

- 2,054 actor parents absent;
- zero null, empty-object, populated-object or unexpected actor parents;
- 2,054 actor.id child states not applicable because the parent is absent;
- zero missing-in-object, null, empty-string or string child states; and
- zero literal dotted actor.id keys.

This is an exact result for the frozen parsed inventory, not a claim that
legacy provenance never existed outside that inventory. The three named rich
rerun files with YAML parse errors remain exclusions from the parsed
denominator:

1. workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-memory-forms.md
2. workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-priming-forms.md
3. workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-recognition-dual-process.md

Malformed input is not a negative actor observation. The inventory route does
not count it as a parsed mapping, and INDEX.md is not substituted for one.

## Contextual evidence and boundaries

### Field placement and method guidance

references/record-field-groups.md is a grouping convention, not a closed
schema. In its table, actor is explicitly named for the extraction-run and
preservation-decision rows; it does not itself establish actor placement for
memory-admission, relationship-edge, source-locator, source-support or
validation-result. The selected templates establish those other placements.

The six selected templates were read in full, including frontmatter and body:

- templates/memory-admission.md exposes an actor object with null children,
  and separately exposes decision_authority_ref and operator_acceptance.actor_ref.
  Its body says that a copied template grants no permission and that acceptance
  is not factual proof.
- templates/preservation-decision.md exposes an actor object with null
  children, while operator_review_required and operator_acceptance_ref remain
  separate. Its body distinguishes the decision actor from a disposition and
  from operator review.
- templates/relationship-edge.md exposes an actor object with null children,
  while endpoints, direction, symmetry and source support remain separate. Its
  body warns that valid endpoints do not warrant the relation.
- templates/source-locator.md exposes an actor object with null children.
  Its resolution section asks who inspected or reported a location but does
  not make that person or process the addressed resource.
- templates/source-support.md exposes an actor object with null children.
  Its subject, source spans, support comparison, evidence grade and lifecycle
  references have separate roles.
- templates/validation-result.md exposes an actor object with null children
  and a separate validator_identity. Its body explicitly treats a validation
  result as a record of checks, not a schema or semantic acceptance.

The relevant guidance reinforces the same separation. Operator workflow keeps
the reviewed record, source identity, actor, support and results distinct
(02-operator-workflow.md, especially the task/input, record-scope and
construct-boundary sections). Extraction guidance says an extraction run
records actual actor and scope but does not define an identity class.
Evidence-lifecycle guidance places actor and extraction confidence on the
actual record or support subject, not on every related construct.
Validation guidance keeps actor/reviewer provenance separate from structural
outcome and semantic verification. Memory-admission guidance distinguishes
the actor, decision authority and required acceptance. Preservation guidance
requires actor/run and decision implications but says preservation does not
establish support, reconciliation or admission. Graph guidance separates edge
actor from endpoints, direction and edge warrant.

The accepted Slice13 evidence is reused only for its bounded identity and
parent-state limits. Slice13's historical source-HEAD guard failure and its
equivalent replay against unchanged relevant source are preserved in slice13CDC;
this packet checks its own registered inputs and does not use a global HEAD
equality test as semantic evidence.

### Populated support witnesses and subject boundary

All four populated native records are the original Arc07 pilot support
records, not synthetic examples:

| Support record | Actor observation | Subject/source/run context | Body evidence and limit |
| --- | --- | --- | --- |
| support-emergent-explanation.md | codex-cc, agent-direct, extractor | Subject is claim claim-emergent-explanation; source is ccn-book; run is run-arc07-s02-pilot. | The body describes the reductionism/reconstructionism passage and gear figure. It does not make the actor the source author or semantic verifier. |
| support-memory-consolidation.md | codex-cc, agent-direct, extractor | Subject is claim claim-memory-consolidation; source is ccn-book; same pilot run. | The body preserves the source's qualified conclusion and says the cited primary work was not inspected. |
| support-model-data-constraints.md | codex-cc, agent-direct, extractor | Subject is claim claim-model-data-constraints; source is ccn-book; same pilot run. | The body supports a limited methodological statement and does not claim model truth. |
| support-pattern-separation.md | codex-cc, agent-direct, extractor | Subject is claim claim-pattern-separation; source is ccn-book; same pilot run. | The body keeps the cited Marr work and cross-reference caveated; the figure does not replace the text. |

The corresponding cc-emergent-explanation.md card was also read with its
body. It carries the same codex-cc card actor, a claim reference, source and
prepared-source references, and a support link. Its body explicitly says that
verification, reconciliation and memory admission remain unassessed. This
shows a card/support relationship and a repeated extraction label; it does not
make the card actor the source author, the claim actor, the support subject or
an independent reviewer.

The two synthetic examples establish different native states:

- examples/memory-admission.md has no actor parent, says the decision is
  deferred, records operator acceptance as not recorded and says no runtime
  write occurred.
- examples/relationship-edge.md has no actor parent but does have a
  directed precedes relation and endpoint references. Its body says the
  relation record does not mean that either endpoint proves the other.

Thus subject_ref, source identity, endpoint identity, decision outcome,
operator acceptance and actor are all distinct observed or documented surfaces.

## Per-kind semantic dispositions

The JSON registry contains one member-specific meaning and one shared-evidence
layer for each of the twelve pairs. The bounded readings are:

| Record kind | actor reading | actor.id reading | Concrete boundary |
| --- | --- | --- | --- |
| memory-admission | Record-local provenance for activity associated with creating or recording an admission assessment; the event and actor class are unknown. | Null in the template; not applicable when the synthetic parent is absent. | Do not infer decision authority, operator acceptance, target identity or runtime permission. |
| preservation-decision | Record-local provenance for activity associated with preparing or recording a preservation decision; decider versus recorder is unknown. | Template null. | Do not infer operator review/acceptance, source authorship or reconciliation authority. |
| relationship-edge | Record-local provenance for creating, revising or reviewing an edge; the actual event is unknown. | Null in the template; not applicable when the synthetic parent is absent. | Do not infer endpoint, relation direction, symmetry, support or warrant. |
| source-locator | Record-local provenance for recording or inspecting a location; the activity is unknown. | Template null. | Do not infer addressed-resource identity, source authorship or successful resolution. |
| source-support | Record-local provenance on a support record; four populated pilot records carry a bounded label and role/mode. | Four codex-cc labels and one template null. | Do not infer source author, supported-claim actor, semantic verifier or truth authority. |
| validation-result | Record-local provenance for a validation result; validator versus recorder is unknown. | Template null. | Do not equate actor with the distinct validator_identity field. |

For every row, a parent absence is retained as a structural lookup result, not
converted to child null and not interpreted as semantic inapplicability. A
template placeholder is retained as object/null, not converted to absent.

## Reader, extractor, query and migration consequences

| Kind | Reader | Extractor | Query | Migration |
| --- | --- | --- | --- | --- |
| memory-admission | Show absent or object/null actor as a provenance limit; do not label it decider/operator. | Keep actor separate from decision authority and acceptance actor. | Scope lookup to record kind and revision; absent is not null. | Preserve parent/child state; do not manufacture actor from target or acceptance fields. |
| preservation-decision | Show unresolved actor separately from disposition and review fields. | Record direct provenance only; do not fill it from prior/destination refs. | Do not treat operator-review or destination references as actor identity. | Carry object/null and future labels without assigning authority. |
| relationship-edge | Render actor separately from endpoints, direction and support. | Do not copy endpoint, support or run identity into actor. | An endpoint match is not an actor match; scope to edge revision. | Preserve absent/null and do not create reciprocal actor values. |
| source-locator | Display actor separately from resource and locator coordinates. | Record who inspected/reported only when directly evidenced. | Separate actor lookup from resource and resolution lookup. | Do not convert locator/source identity into actor identity. |
| source-support | Render exact label, role/mode and support-record revision without calling it authorship or verification. | Keep actor separate from subject, source, run, evidence grade and lifecycle state. | Equal labels are bounded observations, not a global principal join. | Preserve codex-cc, family and context; do not normalize or inherit into claims. |
| validation-result | Show actor and validator_identity as separate unassessed surfaces. | Do not fill actor from validator identity or target records. | Query both slots independently at result scope. | Preserve separate slots and do not infer precedence/equality. |

## Native diagnostics and limits

The validation artifact records two focused diagnostics using literal existing
tools:

1. It selects the populated support-emergent-explanation record, derives its
   native actor from the frozen inventory, and compares it with an independently
   authored codex-cc expectation. A deliberately wrong actor expectation is
   rejected. The same observation prints the support subject_ref and
   source-span source_ref as distinct objects, so the subject claim and
   addressed source cannot be mistaken for the actor.
2. It compares the memory-admission template's object/null actor with the
   synthetic memory-admission example's absent parent. A mutation that changes
   the absent state to null is rejected. The same parameterized lookup returns
   a successful empty result for a real no-match and a nonzero jq status with
   stderr for a missing inventory file.

The replay also rejects an invalid membership and dangling member/shared
evidence references, recomputes every registered hash, and derives the
selected and legacy census from native inventory values before comparing them
with authored expectations. Those checks establish evidence integrity and
bounded observations only; they do not establish actor authority, principal
equivalence, semantic verification, requiredness or admission.

## Outside work and next bounded unit

This slice does not accept any pair by assignment, and it does not update the
project coverage register. Slice15 retains the broader provenance owner. A
candidate next unit is the twenty remaining actor.mode and actor.role pairs
across the ten actor-bearing record kinds. That is a sizing recommendation
only: CRC/CDC must recount native contexts and split it before issue if review
headroom requires. Created-at, run/preparation/method, shared-reference and
remaining CQ-provenance work remain outside that candidate.

P-15 remains open. No schema language, specification format, requiredness,
identity authority, migration policy, source-truth rule, memory-admission rule,
package/runtime behavior or real-source quality decision is adopted here.
