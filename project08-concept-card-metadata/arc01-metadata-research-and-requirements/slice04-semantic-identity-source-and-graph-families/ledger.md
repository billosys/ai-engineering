# Arc01 Slice04 Ledger

CDC review of 76d284f4 requires Iteration 01. Exact pair coverage is reproduced,
but contextual semantics remain incomplete. S4-8 passes within the inspected
commit/source scope; other rows remain open. See cdc-verification.md for
findings, reproduced checks and limitations. This ledger does not replace
or close Slice01's eight rows.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S4-1 | Actual inspected definitions and data are registered with exact identities | Resolve paths/sections and hashes; inspect full v3.2 prompt observations and predecessor comparison | correctness-grade | S1-1/S1-3, R4 | open | cdc-verification.md, S4-R3 | Abbreviations replace exact paths; no file hashes or named real samples |
| S4-2 | Assigned/remainder membership union covers all observed path-kind pairs without unexplained gaps or overlaps | Independently derive mechanical pairs and compare explicit memberships; review finer context distinctions | serious | S1-4, R2 | open | cdc-verification.md, structural reproduction and S4-R1/R2 | 555 exact pairs pass; finer contexts and correct semantic ownership do not |
| S4-3 | Every assigned identity, classification and source/locator membership has an authored meaning and supported disposition | Trace memberships to definitions, representative values and actual old/current differences | serious | S1-4, R2 | open | Batch01 attested: artifacts/batch01-identity-{evidence,membership} | Ten identity pairs covered; all remaining memberships open. |
| S4-4 | Every assigned claim/support, relationship and CQ membership preserves its contextual meaning in the comparison | Check subject, endpoint, direction, scope, support linkage and lookup consequences against actual records | serious | S1-4, R2 | open | cdc-verification.md, S4-R1/R2 | CQ group includes unrelated lifecycle, graph and support subjects |
| S4-5 | Concrete body/metadata and query/migration comparisons address operator concerns for all assigned families | Inspect source-connected examples and body sections; distinguish prose from structured lookup | serious | S1-5, R2 | open | cdc-verification.md, S4-R2 | No named real-body comparisons or per-context consequences |
| S4-6 | Slice05 receives a bounded, explicit remainder and research/integration handoff | Walk remaining memberships, family interfaces and questions; verify no original requirement lost | correctness-grade | S1-6, R2/R4 | open | cdc-verification.md, S4-R1/R3 | Correct ownership; give remainder families/reasons and residual instruction handoff |
| S4-7 | Evidence checks are reproducible and cover structural and semantic assertions separately | Run recorded checks, inspect cited evidence and review limitations | correctness-grade | S1-7, R4 | open | cdc-verification.md, S4-R3/R4 | Submitted commands count union without comparing expected pairs; close row walk absent |
| S4-8 | Changes remain planning-only, preserve inputs and use approved tooling with scoped commits | Inspect diff, source status, unchanged baseline/census and explicit commit file list | serious | S1-2/S1-8, operator tooling preference | done | cdc-verification.md, inspected commit and source status, reproduced | Seven scoped Markdown/JSON files; no helper/source edit; Slice01 unchanged in Git |
