# Arc06 Slice13 Ledger

CDC review of 78be7fab verifies S13-1/S13-6 and retains four rows open for
Iteration 01 (R1-R4). The original CC report remains its attestation.
Exactly eight semantic pairs are assigned; none is accepted by this packet.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S13-1 | Exact eight-pair scope and outside ownership are preserved | Compare plan, registry, frozen/current sets and 180/8/367 accounting | serious | A6-1/A6-3/A6-6 | done | `artifacts/semantic-membership.json`; `artifacts/validation-evidence.md`; `cdc-verification.md` (reproduced/reconciled) | Exact assignment is present in the remaining set and disjoint from accepted; assignment is not acceptance |
| S13-2 | Actor/identity observations retain family, parent/child and parse distinctions | Reproduce complete selected-record census and inspect registered raw witnesses | correctness-grade | A6-3, no-loss requirement | open | `artifacts/semantic-evidence.md`; `artifacts/semantic-membership.json`; `cdc-verification.md` (changes required) | R1/R4: census completeness and native-to-authored checks; retain positive evidence |
| S13-3 | Each membership has contextual meanings, limits and operational consequences | Trace rules and observations through member/shared evidence; inspect counterexamples | serious | P-1/P-4/P-6 | open | `artifacts/semantic-membership.json`; `artifacts/semantic-evidence.md`; `cdc-verification.md` (changes required) | R4: evidence attribution and project-instruction registration; retain positive evidence |
| S13-4 | Native actor/state diagnostics and controls are genuine | Compare native outputs, wrong expected identity and actual missing-input error | correctness-grade | Slice03 replay contract | open | `artifacts/validation-evidence.md`; `cdc-verification.md` (changes required) | R3: raw-search error handling; retain positive evidence |
| S13-5 | Literal replay and preservation reproduce at claimed endpoint | Check hashes, references, original/copy mappings, both evidence layers, exact six-file scope and whitespace | correctness-grade | A6-7 | open | `artifacts/validation-evidence.md`; `cdc-verification.md` (changes required) | R1-R3: registry binding, snapshot separation and fail-closed checks; retain positive evidence |
| S13-6 | Handoff preserves unaccepted provenance scope and design gates | Trace complement to Slice14 and other family owners; inspect concrete next-work sizing | serious | A6-3/A6-6/P-15 | done | `artifacts/handoff.md`; `artifacts/semantic-evidence.md`; `cdc-verification.md` (reproduced/reconciled) | Slice14 complement, other owners and P-15 remain open; no schema adoption or silent transfer |
