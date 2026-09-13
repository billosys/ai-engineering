# Arc01 Slice07 Ledger

Initial CC attestation: d8a3a6c0. CDC review accepts S7-2/S7-7 and leaves
five rows open for Iteration 01. Criteria are unchanged; the slice remains open.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S7-1 | Exact inspected definitions and data have registered identities and roles | Resolve sections, hashes and historical/current context | correctness-grade | S4-1 | open (CDC changes required) | cdc-verification.md; artifacts/semantic-membership.json; artifacts/semantic-evidence.md | S7-R2: five hashes resolve; required historical/corpus/locator contexts missing |
| S7-2 | Registry covers the exact twenty pairs with no accepted-pair overlap | Independent expected set, uniqueness, inventory inclusion, Batch01/Slice06 disjointness | serious | S4-2 | done (CDC reproduced) | cdc-verification.md; artifacts/semantic-membership.json | Exact twenty unique pairs, inventory inclusion and accepted-47 disjointness pass |
| S7-3 | Legacy attribution and location meanings retain source-specific values, shapes and limitations | Replay scoped census; inspect named bodies and source-family differences | serious | S4-3/S4-5 | open (CDC changes required) | cdc-verification.md; artifacts/semantic-evidence.md | S7-R2: frozen census and source-family/body comparisons missing |
| S7-4 | Current locator meanings preserve identity, basis and mapping boundaries | Review thirteen fields against guidance, examples and available actual locators | serious | S4-3 | open (CDC changes required) | cdc-verification.md; artifacts/semantic-evidence.md | S7-R1/R2: generic definitions and missing concrete locator comparisons |
| S7-5 | Every membership has supported dispositions and useful old/current consequences | Resolve both evidence layers; inspect query/body/preservation differences | serious | S4-3/S4-5 | open (CDC changes required) | cdc-verification.md; artifacts/semantic-membership.json | S7-R1/R2: repeated dispositions lack field-specific consequences |
| S7-6 | Complete literal replay and handoff preserve all remaining obligations | Run recorded commands and seven-row walk; check 47/20/488 accounting | correctness-grade | S4-6/S4-7 | open (CDC changes required) | cdc-verification.md; artifacts/validation-evidence.md; artifacts/handoff.md | S7-R3: complete literal replay, seven-row report and concrete handoff missing |
| S7-7 | Work is scoped, input-preserving and uses approved tooling | Inspect explicit commit files, preserved prior packets/source and whitespace | serious | S4-8 | done (CDC reproduced) | cdc-verification.md; artifacts/validation-evidence.md | Six authorized files only; source/prior packets unchanged; whitespace clean |
