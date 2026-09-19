# Slice18 semantic evidence: run scope, workers and outputs

Status: CC proposed-done. This is planning-only semantic inventory evidence
for CRC review; it is not a schema, source repair, extraction trace,
verification result, memory admission, coverage acceptance or Operator
acceptance.

## Intake and contract readback

The source checkout is
`/Users/oubiwann/lab/billosys/ai-engineering`, clean at
`ce3f77103eff5e07b3533a03c65f158684fc1039`. The canonical planning checkout is
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`, clean at
issued planning HEAD `961c748f7915c71ba59ef37a2dd65253800be268`. The preserved
pre-opening Slice17 baseline is `eb7b606baac634f0a3beb3db5d7dcfea26c986e3`;
Set B authority is escalation commit
`dee3052c88e0fd9361e74200fd1eea26ade76435`. The frozen inventory SHA-256 is
`afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`.

The required-full packet was loaded before dependent drafting: the active
429-line prompt, 175-line slice plan, 15-line ledger, directive02 (220 lines),
Project08 AGENTS (90 lines), the three complete run witnesses (81/44/43
lines), the complete claim target (54), field/audit references (31/24),
concept-cards entrypoint (158), Slice03 replay contract/worked replay
(93/296), Slice17 handoff/CRC record (77/124), and historical v3.2 sections
311-342 and 512-624. Required sections were loaded completely from the
project/arc plans and source guides 01-04, 07-08 plus agent-coordination
guides 01-04. One combined source-guide read was truncated; its affected
guides were recovered with contiguous bounded reads before this record was
written. No required input was unavailable.

The contract readback is: inspect exactly the 22 Set B
`extraction-run` pairs, derive observations from the pinned inventory and
source witnesses, and keep assignment separate from the 238 accepted and 295
outside pairs. Root absence, parent absence, wrong-parent shape, child
absence, null, empty collections, populated mappings/sequences and
sequence-element children remain distinct. The template's `output_refs`
mapping and trace's typed sequence are incompatible observed shapes. The
template's `parallel_worker_count` means additional workers, while the
synthetic `worker_scope.worker_count` values are on a different surface.
`worker_scope` is not `agent_scope`, `actor.mode`, a contributor seat or
independent verification; `worker_outputs` is not `output_refs`. The
parallel example records two workers while omitting `worker_outputs`, so the
guidance/example conflict is preserved for a named policy owner. Exact target
lookup requires id, record type and revision; match, successful no-match,
comparison failure and tool/input error remain separate. The six-file fence,
CRC independent review, CDC composition and P-15/operator gates remain
binding.

The complete required-data queries and their retained outputs are in
`validation-evidence.md`; the registry in `semantic-membership.json` records
each authoritative input, hash, range, role, interpretation and limit.

## Exact population, exclusion and coverage census

The preserved escalation Set B and live current register were compared with
`jq -n -e`; exit status was 0. Results:

- 22 unique assigned pairs, exactly the Set B path;
- 22 pairs in current remaining, 0 in accepted;
- full 555, accepted 238, remaining 317, assigned 22, outside 295;
- current `next_slice` is exactly
  `arc06-semantic-families-and-capability-requirements/slice18-run-scope-workers-and-outputs`;
- the frozen 555-pair union remains intact and the 248-pair later-family
  complement remains outside this slice.

The complete frozen inventory contains 2,124 rows: 2,106 parsed/frontmatter
records, 3 YAML parse errors and 15 `no-opening-frontmatter` rows. Exactly
three parsed records have `record_kind == "extraction-run"`:

1. `knowledge/concept-cards/templates/extraction-run.md`: all selected roots
   are present in the template shape. The four scope/intent roots and
   `parallel_worker_count` are null; `worker_outputs` is `[]`;
   `output_refs` is a mapping with six empty-list children; `worker_scope`
   is absent.
2. `knowledge/concept-cards/examples/extraction-run-trace.md`: the four
   scope/intent roots, `parallel_worker_count` and `worker_outputs` are
   absent; `output_refs` is a two-element typed sequence; `worker_scope` is
   `{mode: agent-direct, worker_count: 1, roles: [extractor]}`.
3. `knowledge/concept-cards/examples/parallel-worker-default-recipe.md`:
   the four scope/intent roots, `parallel_worker_count`,
   `worker_outputs` and `output_refs` are absent; `worker_scope` is
   `{mode: agent-direct, worker_count: 2, roles: [source-scope, claim-support]}`.

The three YAML parse-error paths are:

- `workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-memory-forms.md`
- `workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-priming-forms.md`
- `workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-recognition-dual-process.md`

The fifteen `no-opening-frontmatter` paths are:

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

Neither exclusion group is an absent Set B field.

## Complete native state/value matrix

The following is a lossless projection of all 3 records across all 22 assigned
paths. `parent-unexpected-*` retains the complete incompatible parent value;
`sequence-element-children` retains every element index and child value.

~~~json
{
  "template": {
    "actual_coverage": {"state": "null", "value": null},
    "agent_scope": {"state": "null", "value": null},
    "intended_outputs": {"state": "null", "value": null},
    "intended_scope": {"state": "null", "value": null},
    "output_refs": {"state": "populated-mapping", "value": {"cards": [], "claims": [], "cqs": [], "edges": [], "locators": [], "source_support": []}},
    "output_refs.cards": {"state": "empty-list", "value": []},
    "output_refs.claims": {"state": "empty-list", "value": []},
    "output_refs.cqs": {"state": "empty-list", "value": []},
    "output_refs.edges": {"state": "empty-list", "value": []},
    "output_refs.locators": {"state": "empty-list", "value": []},
    "output_refs.source_support": {"state": "empty-list", "value": []},
    "output_refs[]": {"state": "parent-unexpected-mapping", "value": {"cards": [], "claims": [], "cqs": [], "edges": [], "locators": [], "source_support": []}},
    "output_refs[].id": {"state": "parent-unexpected-mapping", "value": {"cards": [], "claims": [], "cqs": [], "edges": [], "locators": [], "source_support": []}},
    "output_refs[].record_type": {"state": "parent-unexpected-mapping", "value": {"cards": [], "claims": [], "cqs": [], "edges": [], "locators": [], "source_support": []}},
    "output_refs[].revision": {"state": "parent-unexpected-mapping", "value": {"cards": [], "claims": [], "cqs": [], "edges": [], "locators": [], "source_support": []}},
    "parallel_worker_count": {"state": "null", "value": null},
    "worker_outputs": {"state": "empty-list", "value": []},
    "worker_scope": {"state": "absent", "value": null},
    "worker_scope.mode": {"state": "parent-absent", "value": null},
    "worker_scope.roles": {"state": "parent-absent", "value": null},
    "worker_scope.roles[]": {"state": "parent-absent", "value": null},
    "worker_scope.worker_count": {"state": "parent-absent", "value": null}
  },
  "trace": {
    "actual_coverage": {"state": "absent", "value": null},
    "agent_scope": {"state": "absent", "value": null},
    "intended_outputs": {"state": "absent", "value": null},
    "intended_scope": {"state": "absent", "value": null},
    "output_refs": {"state": "populated-sequence", "value": [{"id": "cc-claim-support-is-assertion-specific", "revision": 1, "record_type": "concept-card"}, {"id": "claim-support-is-assertion-specific", "revision": 1, "record_type": "claim"}]},
    "output_refs.cards": {"state": "parent-unexpected-sequence", "value": [{"id": "cc-claim-support-is-assertion-specific", "revision": 1, "record_type": "concept-card"}, {"id": "claim-support-is-assertion-specific", "revision": 1, "record_type": "claim"}]},
    "output_refs.claims": {"state": "parent-unexpected-sequence", "value": [{"id": "cc-claim-support-is-assertion-specific", "revision": 1, "record_type": "concept-card"}, {"id": "claim-support-is-assertion-specific", "revision": 1, "record_type": "claim"}]},
    "output_refs.cqs": {"state": "parent-unexpected-sequence", "value": [{"id": "cc-claim-support-is-assertion-specific", "revision": 1, "record_type": "concept-card"}, {"id": "claim-support-is-assertion-specific", "revision": 1, "record_type": "claim"}]},
    "output_refs.edges": {"state": "parent-unexpected-sequence", "value": [{"id": "cc-claim-support-is-assertion-specific", "revision": 1, "record_type": "concept-card"}, {"id": "claim-support-is-assertion-specific", "revision": 1, "record_type": "claim"}]},
    "output_refs.locators": {"state": "parent-unexpected-sequence", "value": [{"id": "cc-claim-support-is-assertion-specific", "revision": 1, "record_type": "concept-card"}, {"id": "claim-support-is-assertion-specific", "revision": 1, "record_type": "claim"}]},
    "output_refs.source_support": {"state": "parent-unexpected-sequence", "value": [{"id": "cc-claim-support-is-assertion-specific", "revision": 1, "record_type": "concept-card"}, {"id": "claim-support-is-assertion-specific", "revision": 1, "record_type": "claim"}]},
    "output_refs[]": {"state": "populated-sequence", "value": [{"id": "cc-claim-support-is-assertion-specific", "revision": 1, "record_type": "concept-card"}, {"id": "claim-support-is-assertion-specific", "revision": 1, "record_type": "claim"}]},
    "output_refs[].id": {"state": "sequence-element-children", "value": [{"index": 0, "state": "populated-string", "value": "cc-claim-support-is-assertion-specific"}, {"index": 1, "state": "populated-string", "value": "claim-support-is-assertion-specific"}]},
    "output_refs[].record_type": {"state": "sequence-element-children", "value": [{"index": 0, "state": "populated-string", "value": "concept-card"}, {"index": 1, "state": "populated-string", "value": "claim"}]},
    "output_refs[].revision": {"state": "sequence-element-children", "value": [{"index": 0, "state": "populated-number", "value": 1}, {"index": 1, "state": "populated-number", "value": 1}]},
    "parallel_worker_count": {"state": "absent", "value": null},
    "worker_outputs": {"state": "absent", "value": null},
    "worker_scope": {"state": "populated-mapping", "value": {"mode": "agent-direct", "roles": ["extractor"], "worker_count": 1}},
    "worker_scope.mode": {"state": "populated-string", "value": "agent-direct"},
    "worker_scope.roles": {"state": "populated-sequence", "value": ["extractor"]},
    "worker_scope.roles[]": {"state": "sequence-elements", "value": [{"index": 0, "state": "populated-string", "value": "extractor"}]},
    "worker_scope.worker_count": {"state": "populated-number", "value": 1}
  },
  "parallel": {
    "actual_coverage": {"state": "absent", "value": null},
    "agent_scope": {"state": "absent", "value": null},
    "intended_outputs": {"state": "absent", "value": null},
    "intended_scope": {"state": "absent", "value": null},
    "output_refs": {"state": "absent", "value": null},
    "output_refs.cards": {"state": "parent-absent", "value": null},
    "output_refs.claims": {"state": "parent-absent", "value": null},
    "output_refs.cqs": {"state": "parent-absent", "value": null},
    "output_refs.edges": {"state": "parent-absent", "value": null},
    "output_refs.locators": {"state": "parent-absent", "value": null},
    "output_refs.source_support": {"state": "parent-absent", "value": null},
    "output_refs[]": {"state": "parent-absent", "value": null},
    "output_refs[].id": {"state": "parent-absent", "value": null},
    "output_refs[].record_type": {"state": "parent-absent", "value": null},
    "output_refs[].revision": {"state": "parent-absent", "value": null},
    "parallel_worker_count": {"state": "absent", "value": null},
    "worker_outputs": {"state": "absent", "value": null},
    "worker_scope": {"state": "populated-mapping", "value": {"mode": "agent-direct", "roles": ["source-scope", "claim-support"], "worker_count": 2}},
    "worker_scope.mode": {"state": "populated-string", "value": "agent-direct"},
    "worker_scope.roles": {"state": "populated-sequence", "value": ["source-scope", "claim-support"]},
    "worker_scope.roles[]": {"state": "sequence-elements", "value": [{"index": 0, "state": "populated-string", "value": "source-scope"}, {"index": 1, "state": "populated-string", "value": "claim-support"}]},
    "worker_scope.worker_count": {"state": "populated-number", "value": 2}
  }
}
~~~

## Evidence classes and separate analyses

### Documented rules and observed values

Documented current guidance requires run-local intended scope and outputs to be
distinguished from actual coverage, and requires worker identity, inputs,
coverage, returned outputs, conflicts and integration decisions when parallel
work actually occurs. It says worker agreement is not independent
verification. The concept-card entrypoint keeps extraction confidence,
validation, verification, reconciliation, preservation and admission separate.

The template is a supported surface with null scalar placeholders, an empty
worker-output list and a categorized output mapping. It is not a completed
run. The trace is a synthetic single-worker example with a typed output
sequence and no scope/output roots. The parallel example is a synthetic
two-worker recipe with worker scope but no `worker_outputs` or `output_refs`.
The historical v3.2 process requires exactly five balanced agents and a
source-first prompt, but current guidance does not require five extraction
workers. These are distinct evidence classes.

### Intent and actual scope

`intended_scope`, `intended_outputs`, `actual_coverage` and `agent_scope` have
no populated native witness. Their null/absent states establish availability
boundaries only. Current guidance supports the distinction between what was
planned, what was actually covered and what outputs were returned; it does not
settle an exact future shape or requiredness policy. `agent_scope` remains
distinct from `worker_scope` and from the CC/CRC/CDC contributor seats.

### Output references and exact targets

The template's `output_refs` is a mapping with six empty child lists. The trace
uses a two-entry sequence with:

1. `{id: cc-claim-support-is-assertion-specific, record_type: concept-card, revision: 1}`,
   which matches exactly one inventory record at
   `knowledge/concept-cards/examples/claim-backed-card.md`;
2. `{id: claim-support-is-assertion-specific, record_type: claim, revision: 1}`,
   which has no standalone inventory target. Embedded or nested mentions are
   not matches.

The parallel example has no `output_refs` root. Exact lookup is structural
identity evidence only: it does not prove that a run produced the target,
that the target is source-supported, or that it passed any lifecycle review.

### Worker counts, modes and roles

The template body documents `parallel_worker_count` as the number of additional
workers, but the root is null. The trace and parallel examples omit that root
and instead populate `worker_scope.worker_count` with 1 and 2. The prompt and
examples do not say whether a coordinating context is included in the latter
count. Both synthetic worker scopes use `mode: agent-direct`, but repeated
spelling does not create a vocabulary or inheritance rule. Their role lists
are contextual observations, not a closed role taxonomy.

### Worker output provenance

The template's empty `worker_outputs` is distinct from the parallel example's
absence. Current extraction and re-extraction guidance asks for per-worker
inputs, scope, outputs, overlaps, disagreements and integration decisions when
parallel work occurs, but the synthetic record omits the field. No backfill or
normalization is authorized. A worker output, an output reference, a
verification result and a contributor handoff are separate constructs.

### Historical comparison

All 2,054 parsed records under the Complete Musician and Erlang roots were
queried. Zero records have any of the eight Set B root fields:
`actual_coverage`, `agent_scope`, `intended_outputs`, `intended_scope`,
`output_refs`, `parallel_worker_count`, `worker_outputs` or `worker_scope`.
This is bounded absence in those card inputs, not proof that the historical
extraction processes had no scope, workers or outputs.

## Author inference, consequences and unresolved owners

The member-specific reader, extractor, query and migration consequences are
recorded in all 22 registry members. The shared rule is conservative: preserve
the literal subject, path, shape, identity and state first; derive no global
requiredness, worker-count convention, role vocabulary, output migration,
delegation policy or source-support warrant from these witnesses.

Unresolved owners are explicit: Arc02/P-15 for future run shapes, requiredness,
target identity and count policy; source-guidance/document-extraction owners
for worker-output and prepared/input provenance details; Slice19 for cross-run
references; later CQ/relationship owners for their output semantics; and
repeated real-run work for actual scope/worker/output behavior. P-15 remains
open.

## Limits

The inventory is a metadata/frontmatter projection. The three run witnesses
are one template and two synthetic examples, not real extraction executions.
The historical comparison is limited to the two named roots. Hashes, ranges,
target matches and replay statuses establish structural identity and checked
operation outcomes only. CRC independent verification, CDC arc composition,
repeated real extractions, Complete Musician trial, conditional full-book
work, runtime/graph/memory behavior, package/UAT checks and Operator quality
acceptance remain unperformed or open.
