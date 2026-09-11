# Slice01 acceptance ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S-01 | Contract names fields, types, optionality, identities and reference ownership at each scale | Review status-contract field tables and example records | correctness-grade | User schema request | open | attested: [field contract](artifacts/status-contract.md#2-documents-identity-and-ownership); [C-01](artifacts/contract-cases.md#c-01-complete-mixed-hierarchy-sparse-page-adoption) | Generic top-level status naming |
| S-02 | Progress, lifecycle, evidence strength and acceptance cannot silently substitute for one another | Positive/negative cases for pending verification, deferred closure and unknown counts | serious | Framework; trial | open | attested: [state and evidence](artifacts/status-contract.md#3-state-closure-and-acceptance); [worked cases](artifacts/contract-cases.md) | Named evidence with pointers |
| S-03 | Child summaries and computed totals have explicit ownership and consistency rules | Cases for mismatched totals, absent detail, zero/unknown denominator and duplicate child IDs | serious | Rootstock mismatch | open | attested: [count rules](artifacts/status-contract.md#5-counts-coverage-and-dependencies); [count cases](artifacts/contract-cases.md#positive-and-negative-fixture-matrix) | Optional detail is not missing required detail |
| S-04 | Contract represents each observed Lykn case without inventing hierarchy or evidence | Case matrix covers all six project shapes and decimal/direct-slice examples | serious | First consumer | open | attested: [six-project matrix](artifacts/contract-cases.md#observed-lykn-shapes-and-proposed-representation); [live read record](artifacts/verification-record.md#source-inspection-evidence) | Current statuses are inputs, not reverified claims |
| S-05 | Rootstock extraction decisions include views, gate semantics, findings, port lane and lessons | Source-to-contract disposition table and render-field mapping | correctness-grade | Trial extraction | open | attested: [extraction map](artifacts/status-contract.md#8-rootstock-extraction-map); [view mapping](artifacts/status-contract.md#9-view-to-field-contract) | No private example payload |
| S-06 | Schema evolution is compatible with repository-owned snapshots and explicit upgrades | Design separates schema compatibility from skill metadata and identifies migration responsibilities | serious | Operator correction | open | attested: [evolution and ownership](artifacts/status-contract.md#10-evolution-snapshots-and-adjacent-capabilities); [C-32–34](artifacts/contract-cases.md#positive-and-negative-fixture-matrix) | Exact runtime choice belongs to Slice02 |
| S-07 | Contract and cases are coherent, linked and ready for independent design review | Local link checks, diff check, decision review and no-silent-drop comparison | correctness-grade | Framework | open | attested: [author checks](artifacts/verification-record.md); [review decisions](artifacts/status-contract.md#11-review-decisions-and-slice02-handoff); [row walk](closing-report.md) | Initial notes alone do not close this row |

## Author evidence amendment — 2026-09-06

Added evidence pointers for all seven original rows after producing the draft
contract and worked cases. Criteria, scope and verification requirements are
unchanged; no rows added or removed. All rows remain `open` for independent
review, with CC-proposed dispositions in [closing-report.md](closing-report.md).
Q-01 through Q-06 remain proposed semantics; coordinating contributor/operator
acceptance precedes implementation. No independent closure is claimed by the
author's document checks.

## CDC review — 2026-09-06

[Draft-1 CDC review](cdc-verification.md) independently reproduces the document
and C-01 example checks. R-01 requires a structured child-exclusion association
or an explicit human-only boundary for the promised parent/child consistency
check. Q-01–06 remain design decisions for operator review. All seven rows stay
open; the presence of a CDC review does not mean this slice is closed.

## Operator correction and revision scope — 2026-09-10

The [progress decision](artifacts/progress-decision.md) supersedes draft-1
flattened project progress. S-03 verification must now include equal arc
weights, four-arc 25%/12.5% examples, differing slice counts, stable weights
through later decomposition, explicit unknowns and calculation/display precision.
S-01/S-04/S-07 must account for the resulting schema, mixed-hierarchy and case
changes. Required coverage-guide content is captured in project P-12. All seven
rows remain open until the revised contract and R-01 correction are reviewed.

## ODM input expansion — 2026-09-11

The handoff is held for operator discussion and the planned Slice03 metadata
contract. S-01/S-05/S-06/S-07 now also require a mapping from accepted planning
metadata and ODM research dispositions to status records. All original rows remain
open; their draft-1 author evidence is historical, not evidence for this expansion.
Q-03's hierarchical progress and R-01's child-exclusion correction remain required.
