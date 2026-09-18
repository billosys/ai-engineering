# Slice16 handoff

Status: CC proposed-done; CRC and CDC gates remain open. This handoff records
the bounded actor-mode/actor-role evidence only. It does not authorize schema,
vocabulary, implementation, migration, runtime, package, memory, UAT or
coverage changes.

## Completed boundary

The exact assignment is the twelve pairs `actor.mode` and `actor.role` across
`memory-admission`, `preservation-decision`, `relationship-edge`,
`source-locator`, `source-support` and `validation-result`. The opening
coverage was 555 full, 208 accepted, 347 remaining, 12 assigned and 335
outside. Slice15's eight accepted pairs are compared but not reaccepted or
reassigned here.

The frozen parsed inventory yields 12 assigned records: two parent-absent
synthetic records, six template records with null actor children and four
populated pilot source-support records. The four populated witnesses preserve
the exact support-local actor `{id: codex-cc, mode: agent-direct, role:
extractor}`. Three YAML parse errors, fifteen no-frontmatter records and the
2,054-record legacy untyped absence census remain separate states.

## Boundary decisions for downstream work

- `actor.mode` and `actor.role` remain record-local supporting-record fields.
- Support-record actor values do not propagate through `subject_ref` to a
  claim, card or global run actor.
- `agent-direct` and `extractor` are observations, not an enum, vocabulary,
  authority registry, inheritance rule or acceptance role.
- Actor fields remain distinct from `worker_scope.mode`, CQ roles,
  `endpoint_roles`, `validator_identity`, source authorship,
  `decision_authority_ref`, disposition, review, and operator acceptance.
- The eight null/absent non-support records do not justify a population policy.

## Retained work and open gates

Slice17 retains run identity/scope/workers/outputs, preparation and method
provenance, shared references and remaining CQ provenance. Existing owners
retain evidence/confidence, validation/verification, reconciliation,
preservation and memory-admission meanings. P-15 and UAT remain open. The
CRC must independently reproduce the registry and route; CDC must compose the
result without silently promoting proposed-done evidence.

The durable packet is the six-file Slice16 contribution: semantic membership,
semantic evidence, validation evidence, this handoff, the ledger and the
closing report. The wrapper must load the registry from the CC commit and the
recipe from a separately named replay endpoint; missing or foreign endpoints
fail closed.
