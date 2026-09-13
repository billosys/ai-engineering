# Arc01 Slice04 Ledger

CDC review of 76d284f4 requires Iteration 01. Exact pair coverage is reproduced,
but contextual semantics remain incomplete. S4-8 passes within the inspected
commit/source scope; other rows remain open. See cdc-verification.md for
findings, reproduced checks and limitations. This ledger does not replace
or close Slice01's eight rows.

Batch01 revision 995c86d6 is independently accepted for its ten-pair/sample
scope, with CDC's explicit replay-documentation repair. No full-scope row is
closed by that checkpoint. Slice06's 37 pairs are now CDC-closed; Slice07
owns twenty further source/locator pairs. The remaining Slice04 work and
complete-artifact integration are still required. See Slice06's final CDC
review and this slice's updated plan; no full-scope row closes from that input.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S4-1 | Actual inspected definitions and data are registered with exact identities | Resolve paths/sections and hashes; inspect full v3.2 prompt observations and predecessor comparison | correctness-grade | S1-1/S1-3, R4 | open | cdc-verification.md, artifacts/batch01-identity-evidence.md | Batch01 registers prompts/template and five usable corpus records plus malformed-rich limitation; remaining contexts remain open |
| S4-2 | Assigned/remainder membership union covers all observed path-kind pairs without unexplained gaps or overlaps | Independently derive mechanical pairs and compare explicit memberships; review finer context distinctions | serious | S1-4, R2 | open | cdc-verification.md, structural reproduction and S4-R1/R2 | 555 exact pairs pass; finer contexts and correct semantic ownership do not |
| S4-3 | Every assigned identity, classification and source/locator membership has an authored meaning and supported disposition | Trace memberships to definitions, representative values and actual old/current differences | serious | S1-4, R2 | open | cdc-verification.md; Batch01 artifacts; ../slice06-record-identity-and-classification/cdc-verification.md | Ten plus 37 bounded pairs accepted; twenty more assigned to Slice07; full-scope criterion remains open |
| S4-4 | Every assigned claim/support, relationship and CQ membership preserves its contextual meaning in the comparison | Check subject, endpoint, direction, scope, support linkage and lookup consequences against actual records | serious | S1-4, R2 | open | cdc-verification.md, S4-R1/R2 | CQ group includes unrelated lifecycle, graph and support subjects |
| S4-5 | Concrete body/metadata and query/migration comparisons address operator concerns for all assigned families | Inspect source-connected examples and body sections; distinguish prose from structured lookup | serious | S1-5, R2 | open | cdc-verification.md, Batch01 acceptance and residual S4-R2 | Identity sample comparisons now accepted; remaining families still need evidence |
| S4-6 | Slice05 receives a bounded, explicit remainder and research/integration handoff | Walk remaining memberships, family interfaces and questions; verify no original requirement lost | correctness-grade | S1-6, R2/R4 | open | cdc-verification.md, S4-R1/R3 | Correct ownership; give remainder families/reasons and residual instruction handoff |
| S4-7 | Evidence checks are reproducible and cover structural and semantic assertions separately | Run recorded checks, inspect cited evidence and review limitations | correctness-grade | S1-7, R4 | open | cdc-verification.md, explicit CDC replay correction; artifacts/batch01-identity-evidence.md | Corrected Batch01 recipe independently executed; full-packet replay and close-row walk remain open |
| S4-8 | Changes remain planning-only, preserve inputs and use approved tooling with scoped commits | Inspect diff, source status, unchanged baseline/census and explicit commit file list | serious | S1-2/S1-8, operator tooling preference | done | cdc-verification.md, inspected commit and source status, reproduced | Seven scoped Markdown/JSON files; no helper/source edit; Slice01 unchanged in Git |
