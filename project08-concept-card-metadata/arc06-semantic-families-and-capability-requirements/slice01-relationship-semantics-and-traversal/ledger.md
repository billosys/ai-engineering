# Arc06 Slice01 Ledger

CDC review of a24758b4 (2026-09-14) reproduced S1-1 and S1-6; the five other
criteria remained open. Iteration 04 now supplies CC attestation for the
complete context census and native-result comparisons, awaiting a fresh CDC
review. Criteria and scope are unchanged; no new memberships are accepted.
See cdc-verification.md; 35 assigned pairs are not accepted semantic coverage.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1-1 | All 35 pairs are uniquely covered without absorbing other fields | Compare plan/frozen/registry sets and 115/35/405 accounting | serious | A6-1 | done | cdc-verification.md: exact-set replay, reproduced | Finer contexts do not silently change scope |
| S1-2 | Rules and populated/template/anomalous contexts are registered and inspected | Check hashes/references/census and both full v3.2 prompts and named records | correctness-grade | A6-2/A6-6, transferred S4-1 | open | closing-report.md; semantic-evidence.md; validation-evidence.md (attested) | Literal census, four Erlang absent/null witnesses, direct originals/copy mapping, and corrected real-extraction candidate provenance await CDC reproduction |
| S1-3 | Every component has a supported meaning and specific consequence | Review orientation, predicates/roles, inverse/symmetry and naming differences | serious | A6-2/A6-6 | open | closing-report.md; semantic-membership.json; semantic-evidence.md (attested) | Contrast repair retained; census-backed state consequences and candidate distinctions await independent review |
| S1-4 | Endpoint/card-edge/support linkage and closure limits are explicit | Follow bounded targets; compare requested and declared components | serious | A6-2, Arc01 interfaces | open | query-cases.json; validation-evidence.md (attested) | Native comparator now derives requested/declaration identity and revision separately for both endpoints; CDC must reproduce |
| S1-5 | Diagnostic cases and body comparisons show actual behavior and limits | Reproduce at least four cases and inspect structured versus prose capability | serious | P-3, S4-5 | open | query-cases.json; semantic-evidence.md; validation-evidence.md (attested) | Four cases include native-derived symmetry/endpoint structures and wrong-expectation controls; body/metadata distinction awaits CDC review |
| S1-6 | Handoff preserves ownership and concrete CQ/research questions | Trace findings to decisions/interfaces and all 405 other pairs | correctness-grade | A6-1/A6-8/A6-9 | done | cdc-verification.md: Iteration 03; handoff.md, reproduced | 405 ownership, explicit Slice02 boundary and concrete questions; not acceptance of case results or 35 pairs |
| S1-7 | Evidence/closeout are reproducible, planning-only and scoped | Run literal checks; inspect JSON, preservation/diff and seven-row report | correctness-grade | Work verification | open | validation-evidence.md; closing-report.md (attested) | Current literal replay adds census and native controls, labels pre-commit state, and records fixed prior/repair committed-review routes; CDC must reproduce |
