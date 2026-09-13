# Arc01 Slice07 Ledger

Latest CC attestation: d077bbe8. CDC retains S7-2/S7-7 and leaves five rows
open for Iteration 02. Partial contextual improvements are retained; criteria
are unchanged and the slice remains open.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S7-1 | Exact inspected definitions and data have registered identities and roles | Resolve sections, hashes and historical/current context | correctness-grade | S4-1 | open (CDC changes required) | cdc-verification.md; artifacts/semantic-evidence.md | S7-R2: new hashes match; input registration and historical/sample evidence incomplete |
| S7-2 | Registry covers the exact twenty pairs with no accepted-pair overlap | Independent expected set, uniqueness, inventory inclusion, Batch01/Slice06 disjointness | serious | S4-2 | done (CDC reproduced) | cdc-verification.md; artifacts/semantic-membership.json | Exact twenty unique pairs, inventory inclusion and accepted-47 disjointness pass |
| S7-3 | Legacy attribution and location meanings retain source-specific values, shapes and limitations | Replay scoped census; inspect named bodies and source-family differences | serious | S4-3/S4-5 | open (CDC changes required) | cdc-verification.md; artifacts/semantic-evidence.md | S7-R2: three-field totals retained; full source-family/body comparison incomplete |
| S7-4 | Current locator meanings preserve identity, basis and mapping boundaries | Review thirteen fields against guidance, examples and available actual locators | serious | S4-3 | open (CDC changes required) | cdc-verification.md; artifacts/semantic-evidence.md | S7-R1/R2: concrete cases improved; field evidence/registry unresolved |
| S7-5 | Every membership has supported dispositions and useful old/current consequences | Resolve both evidence layers; inspect query/body/preservation differences | serious | S4-3/S4-5 | open (CDC changes required) | cdc-verification.md; artifacts/semantic-evidence.md; artifacts/semantic-membership.json | S7-R1: registry byte-identical; meanings/dispositions and new evidence links uncorrected |
| S7-6 | Complete literal replay and handoff preserve all remaining obligations | Run recorded commands and seven-row walk; check 47/20/488 accounting | correctness-grade | S4-6/S4-7 | open (CDC changes required) | cdc-verification.md; artifacts/validation-evidence.md; artifacts/handoff.md; closing-report.md | S7-R3: new replay descriptions are not commands; row-level closeout incomplete |
| S7-7 | Work is scoped, input-preserving and uses approved tooling | Inspect explicit commit files, preserved prior packets/source and whitespace | serious | S4-8 | done (CDC reproduced) | cdc-verification.md; artifacts/validation-evidence.md | Five authorized Iteration 01 files; source/prior packets unchanged; whitespace clean |
