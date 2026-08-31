# Slice 02: Component Contract Evaluation

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice02-component-contract-evaluation
status: proposed-done
opened-on: 2026-08-31
proposed-done-on: 2026-08-31
artifact-home: artifacts/
depends-on:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-architecture-decision-instrument:verified-closed
blocks:
  - slice03-target-composition-package-architecture
related:
  - ../../project-plan.md
  - ../../ledger.md
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-architecture-decision-instrument/cdc-verification.md
  - ../slice01-architecture-decision-instrument/artifacts/architecture-input-register.md
  - ../slice01-architecture-decision-instrument/artifacts/architecture-decision-method.md
  - ../slice01-architecture-decision-instrument/artifacts/component-contract-schema.md
  - ../slice01-architecture-decision-instrument/artifacts/candidate-architecture-worklist.md
  - ../slice01-architecture-decision-instrument/artifacts/operator-decision-and-risk-register.md
```

## Goal

Evaluate every seeded Arc04 candidate from the Slice01 architecture decision
instrument against the component-contract schema, producing evidence-backed
go / adjust / defer dispositions for candidate components, component families,
support assets, adapters, constraints, package/release gates, and
non-component or deferred concepts.

This slice should produce evaluated contracts and dispositions that Slice03
can compose into a target architecture. It should not finalize the full
component graph, accepted package paths, source moves, or operator acceptance.

## Scope

In scope:

- Consume the verified Slice01 architecture decision instrument.
- Evaluate all `CAW-01` through `CAW-26` rows from
  `artifacts/candidate-architecture-worklist.md`.
- Fill the component-contract schema for candidate components and component
  families strongly enough for Slice03 composition.
- Disposition support assets, adapters, constraints, package/release gates,
  dependency edges, non-components, and deferred questions.
- Preserve D/OQ/ARG decision and risk references where they affect candidate
  contract evaluation.
- Carry Project01 source/package, package-local, zip root, release surface,
  component contract, CCDP separation, and `make check-package-paths`
  constraints into every relevant evaluated row.
- Produce Slice03-ready composition inputs, including which rows are go,
  adjust, defer, gate, support asset, adapter, or non-component.

Out of scope:

- Selecting the final target component graph.
- Producing the accepted architecture packet.
- Obtaining operator acceptance for the final architecture.
- Creating the Arc05 implementation plan.
- Editing source `SKILL.md`, README, Makefile, framework docs, templates,
  package files, generated zip artifacts, or any source file.
- Editing planning artifacts outside Project02.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `component-contract-evaluation-matrix.md` - one row for each `CAW-01`
  through `CAW-26`, with classification, evidence, required contract status,
  risk disposition, and go / adjust / defer posture.
- `candidate-component-contracts.md` - evaluated contracts for candidate
  components and component families, using the Slice01 component-contract
  schema fields.
- `support-adapter-constraint-dispositions.md` - dispositions for support
  assets, adapters, constraints, dependency edges, non-components, and
  deferred concepts.
- `package-release-gate-dispositions.md` - source/package, package-local,
  zip root, release surface, README, `SKILL.md`, Makefile,
  `make check-package-paths`, CCDP separation, and package/release gate
  dispositions.
- `slice03-composition-inputs.md` - the evaluated row set that Slice03 should
  compose into the target architecture, including unresolved questions and
  required operator follow-up.

## Delivered

Slice02 produced the five required durable artifacts under `artifacts/`:

- `component-contract-evaluation-matrix.md`
- `candidate-component-contracts.md`
- `support-adapter-constraint-dispositions.md`
- `package-release-gate-dispositions.md`
- `slice03-composition-inputs.md`

The outputs evaluate contract candidates and dispositions only. They do not
accept final component architecture, package paths, source moves, or operator
acceptance.

## Verification Approach

The slice verifies by checking that required artifacts exist under
`artifacts/`, cite the verified Slice01 decision instrument, evaluate all 26
candidate worklist rows, fill the component-contract schema for candidate
components and families, disposition non-component/support/adapter/gate rows,
preserve operator decisions and risks, carry Project01 path/package gates
forward, remain non-final, and leave the implementation source checkout
untouched.

## Exit Criteria

- Verified Slice01 inputs are consumed and cited.
- `artifacts/component-contract-evaluation-matrix.md` accounts for every
  `CAW-01` through `CAW-26` row.
- `artifacts/candidate-component-contracts.md` evaluates candidate components
  and component families against the Slice01 component-contract schema.
- `artifacts/support-adapter-constraint-dispositions.md` dispositions support
  assets, adapters, constraints, dependency edges, non-components, and
  deferred concepts without silently promoting them to components.
- `artifacts/package-release-gate-dispositions.md` carries Project01
  source/package and package/release gate constraints into the candidate
  contract layer.
- Operator decisions, operator questions, ARG risks, and go / adjust / defer
  posture are preserved or explicitly merged with source IDs.
- `artifacts/slice03-composition-inputs.md` states which evaluated rows are
  ready for Slice03 composition, which require adjustment, and which remain
  deferred.
- Outputs remain evaluated contract candidates and dispositions, not accepted
  final architecture.
- No source files are edited.
