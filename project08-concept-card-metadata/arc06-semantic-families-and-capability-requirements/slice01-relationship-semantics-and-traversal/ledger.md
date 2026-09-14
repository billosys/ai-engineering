# Arc06 Slice01 Ledger

CDC review of repair 7de68374 (2026-09-14): changes required. S1-1 is reproduced;
the other six criteria remain open. Iteration 03 requires a new CC session.
CC attestations in closing-report.md are retained, not independent closure.
Criteria and scope unchanged.
See cdc-verification.md; 35 assigned pairs are not accepted semantic coverage.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1-1 | All 35 pairs are uniquely covered without absorbing other fields | Compare plan/frozen/registry sets and 115/35/405 accounting | serious | A6-1 | done | cdc-verification.md: exact-set replay, reproduced | Finer contexts do not silently change scope |
| S1-2 | Rules and populated/template/anomalous contexts are registered and inspected | Check hashes/references/census and both full v3.2 prompts and named records | correctness-grade | A6-2/A6-6, transferred S4-1 | open | cdc-verification.md: Iteration 02 R1 | Seventeen hashes pass; discarded read output and missing comparisons remain |
| S1-3 | Every component has a supported meaning and specific consequence | Review orientation, predicates/roles, inverse/symmetry and naming differences | serious | A6-2/A6-6 | open | cdc-verification.md: Iteration 02 R3 | Registry interpretations unchanged; handoff gains retained |
| S1-4 | Endpoint/card-edge/support linkage and closure limits are explicit | Follow bounded targets; compare requested and declared components | serious | A6-2, Arc01 interfaces | open | cdc-verification.md: Iteration 02 R1/R3 | Endpoint matches reproduced; contradictory live support/path claims remain |
| S1-5 | Diagnostic cases and body comparisons show actual behavior and limits | Reproduce at least four cases and inspect structured versus prose capability | serious | P-3, S4-5 | open | cdc-verification.md: Iteration 02 R2 | Genuine witnesses; no native-input replay, incomplete body comparison |
| S1-6 | Handoff preserves ownership and concrete CQ/research questions | Trace findings to decisions/interfaces and all 405 other pairs | correctness-grade | A6-1/A6-8/A6-9 | open | cdc-verification.md: Iteration 02 row walk | Ownership and contrast improvement retained; evidence dependencies incomplete |
| S1-7 | Evidence/closeout are reproducible, planning-only and scoped | Run literal checks; inspect JSON, preservation/diff and seven-row report | correctness-grade | Work verification | open | cdc-verification.md: Iteration 02 replay | All three structural blocks pass; native replay and attestation reconciliation remain |
