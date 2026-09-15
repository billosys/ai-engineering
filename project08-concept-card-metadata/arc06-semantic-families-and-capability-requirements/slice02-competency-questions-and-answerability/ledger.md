# Arc06 Slice02 Ledger

CDC review of 753bacb0 on 2026-09-15: changes required. Iteration 01 repairs
the four open rows as CC-attested/proposed-done; S2-1 and S2-5 remain
independently done at their recorded scope. The initial CC attestation and CDC
finding history remain in closing-report.md and cdc-verification.md. All six
original criteria remain; no new memberships are accepted and CDC must rerun
the repair before closure.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S2-1 | Exactly 30 assigned pairs retain complete ownership boundaries | Compare plan/current register/frozen sets and 150/30/375 accounting | serious | A6-1/P-1 | done | cdc-verification.md: Independent Checks and Row Walk; artifacts/semantic-membership.json | CDC reproduced 30 unique pairs, inclusion/disjointness and explicit owners; no lifecycle absorption or semantic acceptance |
| S2-2 | Rules and actual contexts support selected-field meanings | Inspect named records, both evidence layers, family census and all input hashes | correctness-grade | A6-2/A6-6 | done (CC-attested) | artifacts/semantic-evidence.md; artifacts/semantic-membership.json; artifacts/validation-evidence.md | Repair corrects 8/5/18 census, exact malformed exclusions and two original/copy manifest mappings; CDC must reproduce |
| S2-3 | Question, component, coverage and answerability semantics are field-specific | Review all 30 dispositions and concrete reader/query/migration consequences | serious | A6-2/P-3/P-4 | done (CC-attested) | artifacts/semantic-membership.json; artifacts/semantic-evidence.md | Repair separates required answer component, mapped constructs, assertion identity and rationale; null encoding remains uncertain; CDC must reproduce |
| S2-4 | Four native comparisons and controls reproduce bounded behavior | Execute native-derived objects versus independent expectations; reject wrong targets and lookup errors | serious | P-3, Slice01/Slice12 lessons | done (CC-attested) | artifacts/query-cases.json; artifacts/validation-evidence.md | Repair derives native observations, records stdout/status, preserves exit-2 errors and rejects altered identity/revision; CDC must reproduce |
| S2-5 | Handoff preserves concrete questions and adjacent owners | Trace findings to research/shared-reference/lifecycle decisions and P-15 | correctness-grade | A6-8/A6-9 | done | cdc-verification.md: Row Walk; artifacts/handoff.md | CDC verified concrete questions/owners/P-15; R2 still corrects local path/tool claim, not endorsed by this row |
| S2-6 | Complete replay and scoped closeout are independently reproducible | Run literal route, JSON, hashes, census, preservation, whitespace and seven-file scope | correctness-grade | Work verification | done (CC-attested) | artifacts/validation-evidence.md; closing-report.md | Repair pins planning authority commits, preserves accepted packets and supports pre/post-commit endpoints; CDC must reproduce and decide closure |
