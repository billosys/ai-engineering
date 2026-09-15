# Arc06 Slice01 Ledger

Current status (2026-09-15): independently closed. The table below carries
the final reproduced/reconciled evidence; preceding submission notes are
retained below as history, not active open conditions.

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
| S1-1 | All 35 pairs are uniquely covered without absorbing other fields | Compare plan/frozen/registry sets and 115/35/405 accounting | serious | A6-1 | done | cdc-verification.md: 2026-09-15, reproduced/reconciled | Original criteria recomposed after Slice12; bounded inventory acceptance only |
| S1-2 | Rules and populated/template/anomalous contexts are registered and inspected | Check hashes/references/census and both full v3.2 prompts and named records | correctness-grade | A6-2/A6-6, transferred S4-1 | done | cdc-verification.md: 2026-09-15, reproduced/reconciled | Original criteria recomposed after Slice12; bounded inventory acceptance only |
| S1-3 | Every component has a supported meaning and specific consequence | Review orientation, predicates/roles, inverse/symmetry and naming differences | serious | A6-2/A6-6 | done | cdc-verification.md: 2026-09-15, reproduced/reconciled | Original criteria recomposed after Slice12; bounded inventory acceptance only |
| S1-4 | Endpoint/card-edge/support linkage and closure limits are explicit | Follow bounded targets; compare requested and declared components | serious | A6-2, Arc01 interfaces | done | cdc-verification.md: 2026-09-15, reproduced/reconciled | Original criteria recomposed after Slice12; bounded inventory acceptance only |
| S1-5 | Diagnostic cases and body comparisons show actual behavior and limits | Reproduce at least four cases and inspect structured versus prose capability | serious | P-3, S4-5 | done | cdc-verification.md: 2026-09-15, reproduced/reconciled | Original criteria recomposed after Slice12; bounded inventory acceptance only |
| S1-6 | Handoff preserves ownership and concrete CQ/research questions | Trace findings to decisions/interfaces and all 405 other pairs | correctness-grade | A6-1/A6-8/A6-9 | done | cdc-verification.md: 2026-09-15, reproduced/reconciled | Original criteria recomposed after Slice12; bounded inventory acceptance only |
| S1-7 | Evidence/closeout are reproducible, planning-only and scoped | Run literal checks; inspect JSON, preservation/diff and seven-row report | correctness-grade | Work verification | done | cdc-verification.md: 2026-09-15, reproduced/reconciled | Original criteria recomposed after Slice12; bounded inventory acceptance only |
