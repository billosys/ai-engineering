---
slice: slice01-schema-and-field-inventory
status: planned
depends-on: [arc01-portable-contract]
blocks: [slice02-book-card-metadata, slice03-web-card-metadata]
---

# Slice01 — Schema and Field Inventory

## Goal and exact scope

Establish the selected metadata contract, complete field-state inventory and
safe normalization/rendering procedure before editing any design card. Read-only
SOURCE; every one of the 233 baseline card headers is in scope. Existing body
content is used only for delimiter/location and preservation boundaries, not a
new semantic review. Starting evidence is in
[preparation notes](artifacts/preparation-notes.md); it is author preparation,
not an independently accepted Slice01 output.

## Authority and preservation

The [arc plan](../arc-plan.md), [arc ledger](../ledger.md),
[project plan](../../project-plan.md) and [project ledger](../../ledger.md) govern.
Operator addition 2026-10-10; Two-Contributor Workflow, Expedited Mode.
This is a planned slice, not a CC assignment. At activation CDC issues a complete
`cc-prompt.md` with exact pins/read manifest, paths and commit instructions.
There is no current prompt or implied permission to modify SOURCE.

All existing values/extensions and absent/null/empty states remain explicit.
No missing-field population or source/semantic acceptance. Preserve original
233-card lineage, all issued Arc01/02 records, source originals and unrelated
Project12/knowledge/lfe. Per-card metadata-only changes must leave body bytes
unchanged and record new whole-file hashes/line locators. No close/CDC record
is created before actual delivery and review.

## Inspection and design method

1. Read current Project10 authority and Arc01 manifest/index; freeze current
   source and schema input revisions with blobs, hashes, sizes and read ranges.
   Reconcile baseline/current path sets, including any earlier semantic edits.
2. Inspect Project08 plan/P-15/discussion record and exact accepted schema
   artifacts. Use the preserved 3.2 definitions now; only an explicit recorded
   accepted replacement permits another selection before this contract freezes.
   Separate schema identifier, skill release, template examples and design drafts.
3. Enumerate raw headers and parsed paths/values/types for all cards, including
   nested extension fields and absence/null/empty/populated states. Detect duplicate
   keys before a parser can overwrite them. Preserve parser failures/exclusions;
   do not turn them into a smaller denominator. Use an existing local parser,
   with actual version and typed edge fixtures, rather than installing a new tool
   or assuming a loader preserves all types. No maintained framework is required.
4. Build a field-by-field crosswalk to documented historical rules. Cite exact
   definition sections; distinguish rules from examples and unsupported requiredness.
   Map every extension, sentinel and ambiguity explicitly. Record missing fields
   and unresolved mappings without supplying defaults or inferring new values.
5. Specify one leading UTF-8 YAML mapping, delimiter/indentation/quoting/key-order
   rules and extension preservation. For documented string-list slots allow the
   recorded `[[]]` empty sentinel to become `[]`; do not flatten nonempty nested
   objects or turn a null into an empty list. Serialization must preserve decoded
   strings and list order. Do not repair body literal escapes in this assignment.
6. Diagnose the GitHub symptom on pinned rendered repository file views and a
   newer rendering reference. Record before/expected outcomes; do not claim the
   nested-list census establishes its cause. Define common automated checks and
   hosted-view expectations for every actual metadata shape and for the final
   233-card rendering matrix. Local Markdown output is a distinct check.
7. Produce an exact representative pilot and cohort/batch proposal, with every
   card assigned once, body-hash and metadata-equivalence oracles, idempotence and
   meaningful negative fixtures. Need no full-body readings or original-source
   acquisition to plan a representation correction. Unresolved semantic fields
   retain Arc02/P10-11 owners. Return all rows and limits to CDC.

## Outputs and sizing

Durable outputs under `artifacts/`: `schema-selection.md`,
`metadata-inventory.jsonl`, `field-crosswalk.md`, `metadata-gap-register.md`,
`normalization-and-rendering-contract.md`, `batch-allocation.jsonl`,
`execution-notes.md`. At issue, CDC specifies these exact files plus slice
ledger/closing report; no source outputs. The 233 headers are a bounded
structured-data census, not 233 teaching bodies or one giant migration.
Every raw key/value occurrence and nested path is queried; receipts distinguish
text reading from structured projection coverage. Record all attempts and errors.

CDC acceptance freezes the contract and pilot/mutation recipe for later source
slices. If the field/syntax investigation itself exceeds context headroom, split
it explicitly while keeping the complete population obligation here. No iteration
or subsequent source assignment is issued by this initial plan.

## Exit criteria and version history

All [six ledger rows](ledger.md) require reproduced evidence and CDC acceptance.
A missing field can remain a documented gap under the Operator's no-fill rule;
unresolved normalization meaning blocks that field's transformation. Schema
alignment is not full conformance or semantic verification.

- 1.0 (2026-10-10): Planned read-only contract/census and GitHub diagnosis from
  Operator addition; preliminary source counts do not close any row.
