# Arc 02: Method Inventory and Gap Analysis

```yaml
project: project03-concept-card-method
arc: arc02-method-inventory
status: active
depends-on:
  - arc01-method-positioning
blocks:
  - arc03-conceptual-model
related:
  - ../arc01-method-positioning/closing-report.md
  - /Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md
  - /Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md
```

## Capability

Arc02 inventories the v3.2 concept-card method from the actual workbench docs
and identifies the source-backed gaps that justify v4.0.

The arc does not design the final v4.0 ontology or skill architecture. It
produces the factual method inventory and gap register that Arc03 can turn into
an accepted conceptual model.

## Slice Breakdown

### Slice 01: v3.2 Source Inventory

Directory: `slice01-v32-source-inventory`

Status: open.

Scope: preserve the two v3.2 baseline workbench docs as slice artifacts,
preserve the pre-Project03 assessment memo, then inventory the baseline method
by mapping schema, workflow phases, validation checks, provenance model,
relationship model, competency-question treatment, confidence semantics,
re-extraction mechanics, and preservation checks into durable source-backed
artifacts.

Blocks: Slice02.

Durable synthesis outputs belong under the slice-local `artifacts/` directory.

### Slice 02: v4.0 Gap Analysis

Directory: `slice02-v40-gap-analysis`

Status: placeholder.

Expected scope: compare the Slice01 baseline inventory against Project03's
v4.0 target concerns: evidence/provenance grading, independent verification,
reconciliation, memory admission, graph-native relationships, CCDP-compatible
evidence semantics, and skill packaging.

Detailed planning is deferred until Slice01 closes.

### Slice 03: Inventory Synthesis

Directory: `slice03-inventory-synthesis`

Status: placeholder.

Expected scope: synthesize the baseline inventory and gap analysis into the
Arc02 close input for Arc03: what v3.2 keeps, what v4.0 must change, what
requires operator choice, and what remains out of scope.

Detailed planning is deferred until Slice02 closes.

## Dependencies

Consumes:

- Closed Arc01 planning substrate and close report.
- The two v3.2 concept-card workbench docs as read-only baseline sources.
- Project03's accepted v4.0 target framing.

Leaves for later arcs:

- A source-backed v3.2 method inventory.
- A gap register separating minor cleanups from v4.0 architectural changes.
- Explicit inputs for Arc03's conceptual model.

## Version History

### v1.0 - 2026-08-30

Arc02 opened after Arc01 formal close. The arc is scoped to inventory and gap
analysis only; v4.0 ontology design is deferred to Arc03.

### v1.1 - 2026-08-30

Slice01 scope expanded to preserve exact v3.2 source snapshots and the
pre-Project03 assessment memo before producing the source inventory.
