# Arc06 Slice01 Ledger

CDC review of a24758b4 (2026-09-14): changes required. S1-1 and S1-6 are
reproduced; five criteria remain open. Iteration 04 targets complete context
census and native-result comparisons. The CC closing report is retained as
attestation. Criteria and scope unchanged; no new memberships accepted.
See cdc-verification.md; 35 assigned pairs are not accepted semantic coverage.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1-1 | All 35 pairs are uniquely covered without absorbing other fields | Compare plan/frozen/registry sets and 115/35/405 accounting | serious | A6-1 | done | cdc-verification.md: exact-set replay, reproduced | Finer contexts do not silently change scope |
| S1-2 | Rules and populated/template/anomalous contexts are registered and inspected | Check hashes/references/census and both full v3.2 prompts and named records | correctness-grade | A6-2/A6-6, transferred S4-1 | open | cdc-verification.md: Iteration 03 R1 | Nineteen hashes/read gains retained; full census, distinct witnesses and provenance correction remain |
| S1-3 | Every component has a supported meaning and specific consequence | Review orientation, predicates/roles, inverse/symmetry and naming differences | serious | A6-2/A6-6 | open | cdc-verification.md: Iteration 03 row walk | Contrast repair retained; remaining context/state exceptions need census-backed interpretation |
| S1-4 | Endpoint/card-edge/support linkage and closure limits are explicit | Follow bounded targets; compare requested and declared components | serious | A6-2, Arc01 interfaces | open | cdc-verification.md: Iteration 03 R2 | Native matches retained; target revisions and complete result comparison not wired |
| S1-5 | Diagnostic cases and body comparisons show actual behavior and limits | Reproduce at least four cases and inspect structured versus prose capability | serious | P-3, S4-5 | open | cdc-verification.md: Iteration 03 R1/R2 | First two comparisons improve; symmetry/endpoint counterexamples and body distinctions remain |
| S1-6 | Handoff preserves ownership and concrete CQ/research questions | Trace findings to decisions/interfaces and all 405 other pairs | correctness-grade | A6-1/A6-8/A6-9 | done | cdc-verification.md: Iteration 03; handoff.md, reproduced | 405 ownership, explicit Slice02 boundary and concrete questions; not acceptance of case results or 35 pairs |
| S1-7 | Evidence/closeout are reproducible, planning-only and scoped | Run literal checks; inspect JSON, preservation/diff and seven-row report | correctness-grade | Work verification | open | cdc-verification.md: Iteration 03 replay/preservation | Three blocks pass; pre-commit check adapted by fixed commit inspection; full census/case replay remains |
