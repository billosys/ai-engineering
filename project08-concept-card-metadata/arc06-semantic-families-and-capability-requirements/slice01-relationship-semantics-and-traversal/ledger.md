# Arc06 Slice01 Ledger

CDC review of 30d9815c (2026-09-14) independently reproduces S1-2/S1-5,
retaining S1-1/S1-4/S1-6. S1-3 and S1-7 remain open for documented-rule
reconciliation and fail-closed search errors. See cdc-verification.md and the
post-Iteration 05 sizing proposal. No sixth iteration, scope transfer or new
semantic memberships are accepted; the exact 35-pair assignment remains.

Operator decision 2026-09-14: Slice12 executes the two remaining repairs.
This ledger retains all seven original criteria and current statuses until
CDC recomposes Slice01. Slice12 CC attestation belongs in its own close packet.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1-1 | All 35 pairs are uniquely covered without absorbing other fields | Compare plan/frozen/registry sets and 115/35/405 accounting | serious | A6-1 | done | cdc-verification.md: exact-set replay, reproduced | Finer contexts do not silently change scope |
| S1-2 | Rules and populated/template/anomalous contexts are registered and inspected | Check hashes/references/census and both full v3.2 prompts and named records | correctness-grade | A6-2/A6-6, transferred S4-1 | done | cdc-verification.md: Iteration 05, reproduced | 27 hashes, original/copy mapping, six card families, legacy/edge census and teaching/null-field evidence reproduced; meaning contradiction is S1-3 |
| S1-3 | Every component has a supported meaning and specific consequence | Review orientation, predicates/roles, inverse/symmetry and naming differences | serious | A6-2/A6-6 | open | cdc-verification.md: Iteration 05 finding R5, reproduced counterexample | v3.2 explicitly requires prerequisites and general template conformance; observed omissions/nulls cannot erase the documented policy |
| S1-4 | Endpoint/card-edge/support linkage and closure limits are explicit | Follow bounded targets; compare requested and declared components | serious | A6-2, Arc01 interfaces | done | cdc-verification.md: Iteration 04, reproduced | Native requested/declared identities and revisions, bounded missing targets/support, and negative controls pass |
| S1-5 | Diagnostic cases and body comparisons show actual behavior and limits | Reproduce at least four cases and inspect structured versus prose capability | serious | P-3, S4-5 | done | cdc-verification.md: Iteration 05, reproduced | Four current native comparisons and controls pass; teaching and null-field prose are inspected without invented stored edges |
| S1-6 | Handoff preserves ownership and concrete CQ/research questions | Trace findings to decisions/interfaces and all 405 other pairs | correctness-grade | A6-1/A6-8/A6-9 | done | cdc-verification.md: Iteration 03; handoff.md, reproduced | 405 ownership, explicit Slice02 boundary and concrete questions; not acceptance of case results or 35 pairs |
| S1-7 | Evidence/closeout are reproducible, planning-only and scoped | Run literal checks; inspect JSON, preservation/diff and seven-row report | correctness-grade | Work verification | open | cdc-verification.md: Iteration 05 finding R6, reproduced counterexample | Normal-input replay and CDC supplemental projections pass; injected search error still returns success as no match |
