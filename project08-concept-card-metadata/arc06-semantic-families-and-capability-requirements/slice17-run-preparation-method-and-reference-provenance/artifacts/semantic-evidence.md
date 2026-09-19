# Slice17 semantic evidence: run preparation, method and reference provenance

Status: CC proposed-done; CRC independent verification and CDC composition are
still required. This packet is planning-only semantic inventory. It does not
adopt a schema, requiredness rule, timestamp policy, vocabulary, migration,
runtime, memory or UAT result.

## Intake and contract readback

The canonical planning checkout is
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`; the source
checkout is `/Users/oubiwann/lab/billosys/ai-engineering`. Intake was clean at
planning `c40e52fc1318e6213c60d5e0371fd01aa3208f1d` and source
`ce3f77103eff5e07b3533a03c65f158684fc1039`. The preserved pre-opening planning
baseline is `c6d445b8cf693e0c03a70a79d5b45c07e3337dcb`; Set A authority is
`dee3052c88e0fd9361e74200fd1eea26ade76435`. The frozen inventory SHA-256 is
`afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`.

The complete required-reading packet was loaded from the declared authorities:
the active prompt (400 lines), slice plan (141), ledger (15), CDC directive02
(220), Project08 AGENTS (90), the three current extraction-run witnesses
(81/44/43), field-group and audit references (31/24), concept-cards entrypoint
(158), the named bounded sections of guides 01-04, document-extraction output
contract (108), historical v3.2 sections, Slice03 replay contract/worked
replay, and the complete Slice16 handoff/CRC record (49/119). The project and
arc sections were read at their current issued HEAD. The first combined
terminal read truncated output; all affected content was recovered with
contiguous ranges before authoring. No required binding input was unavailable;
no semantic gap is silently filled. The evidence registry in
`semantic-membership.json` records the loaded extents, byte identities and
limits under IDs `set-a` through `target-trace-paths`.

The binding contract is: interpret exactly Set A's eighteen
`extraction-run` pairs, keep assignment separate from the 220 accepted pairs,
and preserve the 317 outside pairs plus unopened Slice18-21 ownership. Current
guidance treats an extraction run as a trace of source/prepared identity,
method/prompt, actor/scope, outputs and result references. It keeps source
support, extraction confidence, validation, verification, reconciliation,
preservation and memory admission separate. Prepared-source records are
upstream provenance and caveats, not assertion-level support. Historical v3.2
workflows provide comparison evidence only.

The easily missed shape boundary is preserved: the template's plural
`prepared_source_refs: []` and the synthetic examples' singular
`prepared_source_ref` mappings are different observed surfaces. This packet
does not declare them equivalent, choose one as required, or infer migration.
It likewise keeps absent, parent-absent, child-absent, null, empty collection,
empty mapping and populated values distinct. A successful no-match lookup is
not a missing input or a resolved target.

## Exact set and opening coverage

The eighteen pairs were read from `crc-escalation02.md` at the preserved Set A
authority and compared with the live issued register, frozen 555-pair union,
accepted set and remaining set. The exact command was the prompt's Set A
extraction followed by `jq -n -e`; exit status was 0. Results:

- 18 unique assigned pairs, all in current remaining;
- 0 assigned pairs in current accepted;
- 555 full, 220 accepted, 335 remaining, 18 assigned and 317 outside;
- current `next_slice` exactly names this Slice17 path;
- the two coverage sets are disjoint and the assigned set leaves 317 outside.

The exact pair list is the `scope.assignment` array in
`semantic-membership.json`; it is unchanged from the active slice plan. The
current coverage digest is
`a3db724d4864b84b04fe1ec7c6781e0bae2a27f7fa7dc07491bc6c50ad59842e` and the
frozen transition digest is
`3f1bf740a1c74f0e6c668b57d5c3eef5ba9ce936e56746817c2171a19daf17bd`.

## Complete native population and availability exclusions

The frozen inventory contains 2,124 records. Exactly three parsed records have
`record_kind == "extraction-run"`; all have `frontmatter: true` and
`error: null`.

| Record | Keys outside/within the selected surface | Complete parsed values |
| --- | --- | --- |
| `knowledge/concept-cards/examples/extraction-run-trace.md` | `extraction_confidence`, `id`, `input_source_ref`, `memory_admission_refs`, `output_refs`, `prepared_source_ref`, `preservation_decision_refs`, `reconciliation_result_refs`, `record_type`, `revision`, `surface_class`, `synthetic`, `validation_result_refs`, `verification_result_refs`, `worker_scope` | `extraction_confidence: "direct"`; `id: "extraction-synthetic-method-note-002"`; `input_source_ref: {id: "de-synthetic-method-note-002", path: "document-extraction/raw/synthetic-method-note-002.txt", revision: 1}`; `memory_admission_refs: []`; `output_refs: [{id: "cc-claim-support-is-assertion-specific", record_type: "concept-card", revision: 1}, {id: "claim-support-is-assertion-specific", record_type: "claim", revision: 1}]`; `prepared_source_ref: {id: "de-prepared-synthetic-method-note-002", path: "document-extraction/prepared/synthetic-method-note-002.md", revision: 1}`; `preservation_decision_refs: []`; `reconciliation_result_refs: []`; `record_type: "extraction-run"`; `revision: 1`; `surface_class: "trace-record"`; `synthetic: true`; `validation_result_refs: []`; `verification_result_refs: []`; `worker_scope: {mode: "agent-direct", roles: ["extractor"], worker_count: 1}`. |
| `knowledge/concept-cards/examples/parallel-worker-default-recipe.md` | `extraction_confidence`, `id`, `input_source_ref`, `memory_admission_refs`, `prepared_source_ref`, `preservation_decision_refs`, `reconciliation_result_refs`, `record_type`, `revision`, `surface_class`, `synthetic`, `validation_result_refs`, `verification_result_refs`, `worker_scope` | `extraction_confidence: "mixed"`; `id: "extraction-synthetic-parallel-recipe-001"`; `input_source_ref: {id: "de-synthetic-method-note-003", revision: 1}`; `memory_admission_refs: []`; `prepared_source_ref: {id: "de-prepared-synthetic-method-note-003", revision: 1}`; `preservation_decision_refs: []`; `reconciliation_result_refs: []`; `record_type: "extraction-run"`; `revision: 1`; `surface_class: "trace-record"`; `synthetic: true`; `validation_result_refs: []`; `verification_result_refs: []`; `worker_scope: {mode: "agent-direct", roles: ["source-scope", "claim-support"], worker_count: 2}`. |
| `knowledge/concept-cards/templates/extraction-run.md` | `actor`, `actual_coverage`, `agent_scope`, `extraction_confidence`, `finished_at`, `id`, `intended_outputs`, `intended_scope`, `memory_admission_refs`, `method_ref`, `old_card_inputs`, `operation`, `output_refs`, `parallel_worker_count`, `prepared_source_refs`, `preservation_refs`, `prior_run_refs`, `prompt_ref`, `reconciliation_refs`, `record_type`, `revision`, `settings`, `source_snapshot_refs`, `started_at`, `validation_refs`, `verification_refs`, `worker_outputs` | `actor: {id: null, mode: null, role: null}`; `actual_coverage: null`; `agent_scope: null`; `extraction_confidence: {assessment: "unassessed", rationale: null, scope: null}`; `finished_at: null`; `id: null`; `intended_outputs: null`; `intended_scope: null`; `memory_admission_refs: []`; `method_ref: null`; `old_card_inputs: []`; `operation: null`; `output_refs: {cards: [], claims: [], cqs: [], edges: [], locators: [], source_support: []}`; `parallel_worker_count: null`; `prepared_source_refs: []`; `preservation_refs: []`; `prior_run_refs: []`; `prompt_ref: null`; `reconciliation_refs: []`; `record_type: "extraction-run"`; `revision: null`; `settings: {}`; `source_snapshot_refs: []`; `started_at: null`; `validation_refs: []`; `verification_refs: []`; `worker_outputs: []`. |

Availability was measured across all 2,124 rows, not by treating failed
parsing as a field state. The three true YAML parse errors were:

1. `workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-memory-forms.md`
2. `workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-priming-forms.md`
3. `workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-recognition-dual-process.md`

The fifteen `no-opening-frontmatter` records were:

1. `.worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/README.md`
2. `.worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice04-expanded-corpus-card-generation/artifacts/candidate-cards/README.md`
3. `knowledge/concept-cards/references/README.md`
4. `knowledge/concept-cards/references/operator-review-gates.md`
5. `knowledge/concept-cards/references/record-field-groups.md`
6. `knowledge/concept-cards/references/semantic-audit-boundaries.md`
7. `knowledge/concept-cards/references/structural-validation-candidates.md`
8. `knowledge/concept-cards/references/vocabulary.md`
9. `workbench/compcogneuro-rich-rerun-2026-09-12/README.md`
10. `workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/INDEX.md`
11. `workbench/compcogneuro-rich-rerun-2026-09-12/comparison/evaluation-rubric.md`
12. `workbench/compcogneuro-rich-rerun-2026-09-12/comparison/subset-comparison.md`
13. `workbench/compcogneuro-teaching-rerun-2026-09-12/README.md`
14. `workbench/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/INDEX.md`
15. `workbench/compcogneuro-teaching-rerun-2026-09-12/comparison/teaching-profile-comparison.md`

Neither exclusion group is an absent extraction-run field.

## Complete 3 x 18 state/value matrix

The matrix was projected with the prompt's root/parent/child state distinction
and compared to an independently authored expected projection in the literal
replay. Values below are lossless for every assigned path; `parent-absent` and
`child-absent` are intentionally different.

| Field path | Template | Synthetic trace | Synthetic parallel recipe |
| --- | --- | --- | --- |
| `finished_at` | `null: null` | `absent` | `absent` |
| `input_source_ref` | `absent` | `populated-mapping: {id: de-synthetic-method-note-002, path: document-extraction/raw/synthetic-method-note-002.txt, revision: 1}` | `populated-mapping: {id: de-synthetic-method-note-003, revision: 1}` |
| `input_source_ref.id` | `parent-absent` | `populated-string: de-synthetic-method-note-002` | `populated-string: de-synthetic-method-note-003` |
| `input_source_ref.path` | `parent-absent` | `populated-string: document-extraction/raw/synthetic-method-note-002.txt` | `child-absent` |
| `input_source_ref.revision` | `parent-absent` | `populated-number: 1` | `populated-number: 1` |
| `method_ref` | `null: null` | `absent` | `absent` |
| `old_card_inputs` | `empty-list: []` | `absent` | `absent` |
| `operation` | `null: null` | `absent` | `absent` |
| `prepared_source_ref` | `absent` | `populated-mapping: {id: de-prepared-synthetic-method-note-002, path: document-extraction/prepared/synthetic-method-note-002.md, revision: 1}` | `populated-mapping: {id: de-prepared-synthetic-method-note-003, revision: 1}` |
| `prepared_source_ref.id` | `parent-absent` | `populated-string: de-prepared-synthetic-method-note-002` | `populated-string: de-prepared-synthetic-method-note-003` |
| `prepared_source_ref.path` | `parent-absent` | `populated-string: document-extraction/prepared/synthetic-method-note-002.md` | `child-absent` |
| `prepared_source_ref.revision` | `parent-absent` | `populated-number: 1` | `populated-number: 1` |
| `prepared_source_refs` | `empty-list: []` | `absent` | `absent` |
| `prior_run_refs` | `empty-list: []` | `absent` | `absent` |
| `prompt_ref` | `null: null` | `absent` | `absent` |
| `settings` | `empty-mapping: {}` | `absent` | `absent` |
| `source_snapshot_refs` | `empty-list: []` | `absent` | `absent` |
| `started_at` | `null: null` | `absent` | `absent` |

The historical comparison queried all 2,054 parsed records under the Complete
Musician and Erlang roots. Every Set A top-level root was present in zero
records: `finished_at`, `input_source_ref`, `method_ref`, `old_card_inputs`,
`operation`, `prepared_source_ref`, `prepared_source_refs`, `prior_run_refs`,
`prompt_ref`, `settings`, `source_snapshot_refs` and `started_at`. This is a
bounded absence in those inputs, not a claim that older extraction processes
lacked provenance.

## Evidence classes and contextual interpretation

| Evidence class | Findings | Limit |
| --- | --- | --- |
| Documented current rule | Current guides define source/prepared identity, run-local method/prompt/scope, source-primary re-extraction, prior-value preservation and separate lifecycle results. | Guidance documents intended boundaries; it does not prove that a native record populated a field. |
| Observed template | The template has null scalar placeholders, empty collections/mapping, and absent singular parents. | A placeholder is not global requiredness or a completed run. |
| Observed synthetic | The trace has populated singular source/prepared maps and paths; the parallel recipe has populated ids/revisions but absent paths; both omit the other Set A roots. | Examples are synthetic shapes, not resolved source targets or actual completed runs. |
| Historical comparison | v3.2 material describes source-first re-extraction, prior-card preservation and fixed five-agent planning. | It supplies process intent and omissions only; it does not override current guidance. |
| Author inference | The membership records describe bounded reader/extractor/query/migration consequences where current guidance and observed shape support them. | These are CC interpretations, not adopted schema or vocabulary. |
| Unresolved | Timestamp format/zone/precision, operation/method vocabulary, singular/plural policy, preparation identity and real prior-run linkage remain open with named owners. | Unknowns must return to Arc02/P-15, document-extraction or later exact units. |

### Operation, method, prompt and settings

The template's `operation`, `method_ref`, `prompt_ref` and time fields are null;
the synthetic examples omit them. The empty template `settings` mapping and
synthetic absence show availability of a surface without observed values. The
current extraction guide requires identifying source, method/prompt, material
settings, actor, scope and output set when a real run is established. Historical
v3.2 material likewise foregrounds provenance and fresh source derivation, but
does not establish a current operation vocabulary. No field is promoted to a
required method bundle.

### Source and prepared inputs

Both synthetic examples expose singular `input_source_ref` and
`prepared_source_ref` mappings. The trace records id/revision/path for both;
the parallel recipe records id/revision and omits both path children. The
template has neither singular parent, but has an empty plural
`prepared_source_refs` list. This is the central singular/plural finding:
shape, cardinality and availability remain separate. Current
document-extraction guidance requires prepared snapshot identity, manifests,
mappings, readiness and caveats when such records are used, but explicitly
keeps prepared provenance upstream of concept-card source support.

The two trace paths were looked up with `git ls-tree -r --name-only` against
source `ce3f77103eff5e07b3533a03c65f158684fc1039`:

| Declared path | stdout | status | stderr | classification |
| --- | --- | ---: | --- | --- |
| `document-extraction/raw/synthetic-method-note-002.txt` | empty | 0 | empty | successful no-match |
| `document-extraction/prepared/synthetic-method-note-002.md` | empty | 0 | empty | successful no-match |
| `document-extraction/no-such-input.md` (deliberately missing) | empty | 128 | nonempty | tool error |

The no-match results do not resolve either synthetic target and do not provide
claim support. The missing-input result is not a no-match.

### Old-card inputs and prior runs

The template exposes `old_card_inputs: []` and `prior_run_refs: []`; both
synthetic records omit both roots. Current re-extraction guidance requires
inventorying prior cards, claims, support, lifecycle records and prior runs
before rewriting, then deriving against the source first. It says to preserve
unique prior value without transferring old support or verification. The
historical v3.2 re-extraction workflow expresses the same source-primary and
unique-value intent but with an older template and fixed process. No prior-run
lineage or preservation outcome is observed in this population.

### Run times

`started_at` and `finished_at` are null in the template and absent in both
synthetic records. They are therefore run-local surfaces with no observed time
values. This packet does not infer format, timezone, precision, ordering,
duration, requiredness or relation to record-local `created_at`; Slice20 owns
the separate creation-time family.

## Field-specific consequences and unresolved owners

The complete member-specific consequences are in each membership object. In
summary: readers must display absence/null/empty/populated distinctions;
extractors must record actual input/preparation/method/time identity only when
observed; queries must resolve identity and paths against explicit revisions
and preserve no-match versus tool-error classes; migrations must not silently
normalize singular/plural, source/prepared, old-card/prior-run or null/absent
surfaces. The unresolved owners are:

| Question family | Owner | Current disposition |
| --- | --- | --- |
| Operation, method, prompt and settings vocabulary/requiredness | Arc02/P-15 and Slice21 | unresolved; no global bundle inferred |
| Source/prepared identity, path roots, revision and one-versus-many policy | document-extraction, Slice18/Slice21 and Arc02 | unresolved; preserve both surfaces |
| Prior-run and old-card reference applicability | Slice19, Slice21 and Arc02 | unresolved; source-first re-extraction remains current rule |
| Run-local timestamp policy versus created_at | Slice20 and Arc02/P-15 | unresolved; no format/zone/precision inferred |
| Synthetic target availability | document-extraction / future real-run work | unresolved; both declared paths are successful no-matches |

## Workload and execution notes

The prompt's bounded reading packet was completed with contiguous recovery after
one combined-output truncation. No context compaction was observed in this
execution. Model identity and measured effort are not available in the planning
records, so they are not invented. Correction categories were limited to
recovering the truncated read and correcting an exploratory jq parenthesis
error in the historical-root query; the corrected query returned 2,054 and all
zero-presence counts. No semantic scope correction was needed.

No source, schema, helper/parser, package/install, runtime, graph, memory,
extraction/UAT or current-coverage edit was performed. CRC independent review,
CDC composition and Operator quality acceptance remain separate gates.
