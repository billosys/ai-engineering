# Arc06 Slice01 Ledger

CDC review of repair 904a5a0d (2026-09-14): changes required. S1-1 is reproduced;
Iteration 02 supplies CC attestation for the other six rows, all CDC-pending.
CC attestations in closing-report.md are retained, not independent closure.
Criteria and scope unchanged.
See cdc-verification.md; 35 assigned pairs are not accepted semantic coverage.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1-1 | All 35 pairs are uniquely covered without absorbing other fields | Compare plan/frozen/registry sets and 115/35/405 accounting | serious | A6-1 | done | cdc-verification.md: exact-set replay, reproduced | Finer contexts do not silently change scope |
| S1-2 | Rules and populated/template/anomalous contexts are registered and inspected | Check hashes/references/census and both full v3.2 prompts and named records | correctness-grade | A6-2/A6-6, transferred S4-1 | done (CC; CDC pending) | semantic-evidence.md | Census/witnesses/prompt read repaired |
| S1-3 | Every component has a supported meaning and specific consequence | Review orientation, predicates/roles, inverse/symmetry and naming differences | serious | A6-2/A6-6 | open | cdc-verification.md: R1/R3 residuals | Shared assertion repair retained; member/context alignment incomplete |
| S1-4 | Endpoint/card-edge/support linkage and closure limits are explicit | Follow bounded targets; compare requested and declared components | serious | A6-2, Arc01 interfaces | open | cdc-verification.md: R1 residuals | Available endpoints untraced; support owner/path conflated |
| S1-5 | Diagnostic cases and body comparisons show actual behavior and limits | Reproduce at least four cases and inspect structured versus prose capability | serious | P-3, S4-5 | done (CC; CDC pending) | query-cases.json; validation-evidence.md | Computed native cases replayed |
| S1-6 | Handoff preserves ownership and concrete CQ/research questions | Trace findings to decisions/interfaces and all 405 other pairs | correctness-grade | A6-1/A6-8/A6-9 | open | cdc-verification.md: seven-row review | Ownership retained; handoff still relies on incomplete cases |
| S1-7 | Evidence/closeout are reproducible, planning-only and scoped | Run literal checks; inspect JSON, preservation/diff and seven-row report | correctness-grade | Work verification | open | cdc-verification.md: independent replay | Block 2 fails; structural successes do not establish semantic replay |
