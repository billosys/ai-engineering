---
project: project08-concept-card-metadata
arc: arc06-semantic-families-and-capability-requirements
slice: slice02-competency-questions-and-answerability
status: active
depends-on: [slice01-relationship-semantics-and-traversal, slice12-relationship-policy-and-replay-remediation]
version: "1.1"
---

# Competency Questions And Answerability

Compare the useful legacy question index with current CQ records, coverage
assertions, answerability and card references. Explain what is directly
queryable and what remains a documented or unresolved claim. This is bounded
semantic inventory, not schema adoption, new extraction or an answering service.

## Current Review

CDC review of 753bacb0 on 2026-09-15 requires changes. S2-1 and S2-5 are
independently done at their recorded scope; S2-2/S2-3/S2-4/S2-6 remain open.
Execute [Iteration 01](./artifacts/iteration-01-cc-prompt.md) in a new CC
session; was: initial submission awaiting CDC. Repair the census/exclusion
and witness mapping, answer-component distinction, native diagnostics and
snapshot-aware replay. Retain verified work and the exact original scope.
See [CDC findings R1-R4](./cdc-verification.md). Slice03 stays unopened.

## Exact Scope

Thirty frozen path/kind pairs: two legacy, six card-link and 22 CQ pairs.
Original Slice01/Slice12 are independently closed. Starting accounting is
150 accepted / 405 remaining; this assignment leaves 375 outside.
Use the project current-coverage register, not the immutable transition's
historical next-slice field. Reading adjacent fields does not absorb them.

| Field path | Record kind |
| --- | --- |
| `answer_criteria` | `competency-question` |
| `answerability_state` | `competency-question` |
| `answers_questions` | `untyped` |
| `answers_questions[]` | `untyped` |
| `competency_question_refs` | `concept-card` |
| `component_refs` | `competency-question` |
| `component_refs[]` | `competency-question` |
| `component_refs[].id` | `competency-question` |
| `component_refs[].revision` | `competency-question` |
| `component_refs[].role` | `competency-question` |
| `coverage_assertions` | `competency-question` |
| `coverage_assertions[]` | `competency-question` |
| `coverage_assertions[].assertion` | `competency-question` |
| `coverage_assertions[].component` | `competency-question` |
| `coverage_assertions[].coverage_state` | `competency-question` |
| `coverage_assertions[].covered_refs` | `competency-question` |
| `coverage_assertions[].id` | `competency-question` |
| `coverage_assertions[].revision` | `competency-question` |
| `coverage_assertions[].source_support_refs` | `competency-question` |
| `coverage_state` | `competency-question` |
| `cq_refs` | `concept-card` |
| `cq_refs[]` | `concept-card` |
| `cq_refs[].id` | `concept-card` |
| `cq_refs[].path` | `concept-card` |
| `cq_refs[].revision` | `concept-card` |
| `cq_status` | `competency-question` |
| `intended_use` | `competency-question` |
| `question` | `competency-question` |
| `requirement_source_ref` | `competency-question` |
| `roles` | `competency-question` |

The following nearby fields remain outside this slice with explicit owners:
- CQ actor/created_at/run/requirement provenance mechanics beyond the selected
  requirement_source_ref role: Slice03 shared-reference/provenance work.
- CQ evidence_grade/extraction_confidence: Slice04.
- CQ validation/verification/result-reference fields and retrieval observation/
  result fields (retrieval_probe_use, retrieval_result_refs, retrieval_state):
  Slice05, with Slice03 for shared reference mechanics.
- CQ reconciliation/prior_cq_refs/replacement_cq_ref/reentry_condition:
  Slice06; preservation fields: Slice07; admission fields: Slice08.
- CQ surface_class/synthetic discovery markers: Slice09 integration must assign
  their contextual semantics before closure; no generic catch-all acceptance.
- Root record id/revision/type: accepted identity inputs, not newly assigned.
  The selected embedded coverage assertion id/revision remain in scope because
  they identify the coverage assertion, not the parent CQ.

cq_status is included only for the question's draft/active status versus
coverage and answerability. It does not absorb the other lifecycle fields.

## Working Context And Sizing

Prefer a fresh CC context. Read current project/arc plans and ledgers, project
AGENTS, this open set, and the latest Slice01/Slice12 CDC closure sections plus
the restored Slice01 handoff. Reuse accepted historical reading; do not reload
every prior correction packet.

Read source concept-cards SKILL, guide 06-graph-cq, the CQ/card templates,
cq-coverage/minimal/rich examples and relevant field-group/reference sections.
Use the two registered v3.2 historical prompts' CQ, quality and template
sections directly for new claims. Both have explicit historical CQ
requirements; contrast rules with outputs instead of assuming either is absent.

Use the frozen Arc01 inventory for structured values and original/copy
manifests for generated baselines. Keep the six current card families distinct.
The standalone CQ population is two records: a null/template and a populated
synthetic example. Embedded body CQs may have different declaration evidence;
do not infer standalone record identity or revision from a heading alone.

## Work

1. Derive a complete selected-field census for the 2,054 legacy mappings,
   31 parsed cards by six families and two CQ records. Include presence, null,
   empty/populated, scalar/container/item types and relevant value differences.
   Exclude malformed rich inputs explicitly. Census is not membership count.
2. Inspect named legacy music/Erlang cards with actual questions, the current
   template/minimal/rich examples, and representative pilot, rich-rerun and
   teaching-rerun cards. Account for every family in the census; direct reads
   can be representative, not all cards. Add a state outlier only when it
   materially changes interpretation. Pin paths/hashes and original/copy roles.
3. Explain question text versus reference identity; requirement/intended-use/
   role versus answer criterion; component reference versus coverage assertion;
   coverage versus answerability versus question status. Compare the template's
   coverage_assertions with the example's component_refs without equating them
   by shape or inferring unsupported conformance. Register both shared meanings
   and component-specific consequences.
4. Run four small native diagnostic comparisons described below. Preserve
   unknown target/fragment/revision outcomes. Existing graph cases can inform
   questions but are not reimplemented here.
5. Write a concrete handoff for shared references, lifecycle owners, research
   and the P-15 schema/spec discussion. Explain lost/preserved query and teaching
   capability, not generic "retain for Arc02" dispositions.

## Native Diagnostics

- Legacy question-to-card reverse lookup: select one exact observed question
  from Music and one from Erlang, return matching source card paths using
  native stored strings, then inspect those bodies. Question presence is a
  discoverability assertion, not proof the answer is adequate.
- Current rich-profile card-to-CQ lookup: compare the actual requested tuple
  with the bounded declared path and available target outcome. Keep path
  availability separate from identity/revision and question answerability.
- Embedded generated CQ lookup: inspect one usable rich-rerun and one teaching
  card (cc-model-data-constraints is available in both). Compare requested
  fragment/ID/revision to literal heading or declaration evidence and actual
  text. Heading lookup is not automatically a rendered anchor or inherited
  embedded revision. Reuse original/copy mapping; disclose unresolved parts.
- CQ component/coverage/answerability contrast: derive the synthetic example's
  native component refs and states, inspect its named targets and compare the
  template's assertion slots. Distinguish stored partial claims, target
  availability and actual evidence; do not manufacture a completed answer or
  require a source-support record that is not available.

Record registered inputs, exact operation, independently authored expected
results, native-derived observed results and limitations. Include a deliberate
wrong-target/value control and a tool-error control where lookup occurs.
A command error must never pass as no-match. Use existing jq/Bash tools and the
frozen parsed inventory, not a custom YAML parser. Synthetic controls are not
additional corpus witnesses. No graph/RAG/MCP runtime is authorized.

## Outputs And Acceptance

Durable artifacts under this slice's artifacts/:
- semantic-membership.json: registered evidence, meanings and exact 30
  memberships; reuse the accepted field_path/record_kind/meaning_id/
  effective_meaning/evidence_ids/disposition contract.
- semantic-evidence.md: contextual census, selected readings, concrete
  semantic/value differences and operator-facing consequences.
- query-cases.json: native diagnostic operations/results/controls and limits.
- validation-evidence.md: one designated literal current replay with cwd,
  dependencies, all registered hashes, exact accounting, full advertised census,
  references, native cases/controls, preservation and actual outcomes.
- handoff.md: retained capabilities, loss risks, bounded unknowns, outside
  owners and specific architecture/research questions.

Keep the packet compact with tables/shared rules and explicit member
exceptions; avoid repeated boilerplate. Use prior evidence by reference with
hash/role checks. Stop to size/split work before expanding into a new family.
No new helper, Ruby/Python, schema/validator implementation or source edit.

Validate exact equality to this plan's 30 pairs, current remaining inclusion,
accepted-150 disjointness and 375 outside. Validate both evidence layers,
all registered hashes, full tables, native comparisons and error controls.
Pin opening planning HEAD and committed endpoint; preserve Arc01, project
coverage snapshots and accepted Slice01/Slice12 packets. Never rewrite frozen
data or expected outputs merely to satisfy a check.

CC walks the six local ledger rows, commits only seven named outputs and
reports proposed-done. CDC independently reviews before acceptance or next
opening. P-15 schema/spec discussion and all real-extraction/UAT goals remain
open. Package/install gates are not applicable to this planning-only slice.

## Version History

- 1.1 (2026-09-15): CDC review retains two verified rows and opens bounded
  Iteration 01 for R1-R4; was: initial run. No pair acceptance, scope reduction,
  source change or schema decision. Requires native observed values and
  committed authority inputs distinct from mutable review status.

- 1.0 (2026-09-15): Opens 30-pair CQ/answerability comparison after independent
  relationship closure. Preserves 150 accepted, explicit ownership of the
  other 375, bounded native diagnostics and the operator schema/spec gate.
