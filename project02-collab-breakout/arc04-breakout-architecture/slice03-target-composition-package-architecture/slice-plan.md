# Slice 03: Target Composition And Package Architecture

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice03-target-composition-package-architecture
status: open
opened-on: 2026-08-31
artifact-home: artifacts/
depends-on:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-architecture-decision-instrument:verified-closed
  - ../slice02-component-contract-evaluation:verified-closed
blocks:
  - slice04-operator-acceptance-architecture-synthesis
related:
  - ../../project-plan.md
  - ../../ledger.md
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-architecture-decision-instrument/cdc-verification.md
  - ../slice01-architecture-decision-instrument/artifacts/architecture-decision-method.md
  - ../slice01-architecture-decision-instrument/artifacts/component-contract-schema.md
  - ../slice01-architecture-decision-instrument/artifacts/operator-decision-and-risk-register.md
  - ../slice02-component-contract-evaluation/cdc-verification.md
  - ../slice02-component-contract-evaluation/artifacts/component-contract-evaluation-matrix.md
  - ../slice02-component-contract-evaluation/artifacts/candidate-component-contracts.md
  - ../slice02-component-contract-evaluation/artifacts/support-adapter-constraint-dispositions.md
  - ../slice02-component-contract-evaluation/artifacts/package-release-gate-dispositions.md
  - ../slice02-component-contract-evaluation/artifacts/slice03-composition-inputs.md
```

## Goal

Compose the verified Slice02 component-contract evaluation outputs into a
proposed target architecture for the collaboration-framework breakout:
component graph, dependency order, top-level composer contract,
project-management family package strategy, support-asset travel, adapter
placement, source/package path assumptions, README/SKILL wayfinding
implications, and release-gate strategy.

This slice should produce a coherent architecture proposal for Slice04
operator acceptance. It should not treat the proposal as accepted
architecture, approve final package paths, plan Arc05 implementation slices,
or edit source files.

## Scope

In scope:

- Consume the verified Slice01 decision instrument and verified Slice02
  component-contract evaluation outputs.
- Compose `CAW-01` through `CAW-26` into a proposed target component graph,
  preserving go / adjust / defer posture and source IDs.
- Decide proposed dependency direction and load order among posture,
  methodology, ledger, project management, audit, coverage, delegation,
  contribution, composer, adapters, support assets, constraints, and
  package/release gates.
- Define a proposed package architecture, including which components are
  standalone packages, which are a component family, which support assets
  travel with owners, and which rows remain adapters, constraints, gates,
  dependency edges, non-components, or deferred questions.
- Preserve Project01 source/package, package-local link, zip root, README,
  `SKILL.md`, Makefile, CCDP separation, release surface, and
  `make check-package-paths` gates before assigning package paths.
- Define the proposed top-level `collaboration-framework` composer behavior:
  thin but not link-only, with a compact safety floor and route table.
- Define agent-adapter and repository-orientation placement, including local
  notes required for standalone component readability.
- Produce Slice04-ready operator acceptance inputs, including proposed
  decisions, risks, rejected alternatives, deferred questions, and Arc05
  implementation-plan implications.

Out of scope:

- Obtaining operator acceptance.
- Marking component names, package paths, source moves, or package graph as
  final.
- Creating the Arc05 implementation plan.
- Editing source `SKILL.md`, README, Makefile, framework docs, templates,
  package files, generated zip artifacts, or any source file.
- Editing planning artifacts outside Project02.
- Reopening Arc02 conceptual analysis or Arc03 functional analysis unless a
  concrete input gap is discovered; record any such gap as an Arc04 risk.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `target-component-architecture.md` - proposed component graph, component
  family shape, dependency edges, and CAW row placement for `CAW-01` through
  `CAW-26`.
- `dependency-and-composition-order.md` - proposed load order and composition
  paths for standalone use, composed framework use, PM lifecycle use,
  ledgered verification, audit, coverage, delegation, contribution, and
  source/package reader modes.
- `package-and-release-architecture.md` - proposed package roots, source path
  assumptions, package-local link behavior, README/`SKILL.md`/Makefile
  surface changes, CCDP separation, validation commands, and release gates.
- `wayfinding-adapter-and-support-plan.md` - top-level composer contract,
  PM wayfinder treatment, agent-adapter placement, repository-orientation
  adapter, support-asset travel, and non-component/deferred row placement.
- `slice04-operator-acceptance-inputs.md` - acceptance packet inputs for
  Slice04, including proposed operator decisions, open risks, rejected
  alternatives, deferred/re-entry conditions, and Arc05 implementation-plan
  fields.

## Verification Approach

The slice verifies by checking that required artifacts exist under
`artifacts/`, consume the verified Slice01 and Slice02 inputs, account for all
`CAW-01` through `CAW-26` rows, preserve D/OQ/ARG decision and risk IDs,
compose gates before package paths, define proposed component/package/
wayfinding architecture without claiming operator acceptance, produce Arc05
implementation-plan inputs for later use, and leave the implementation source
checkout untouched.

## Exit Criteria

- Verified Slice01 and Slice02 inputs are consumed and cited.
- Every `CAW-01` through `CAW-26` row is placed in the proposed architecture
  as component, component family, support asset, adapter, constraint,
  package/release gate, dependency edge, non-component, or deferred question.
- The proposed target graph and load order distinguish standalone direct-load
  use from composed `collaboration-framework` use.
- Project01 source/package gates are composed before package paths and bind
  every proposed standalone component, family, support asset, and composer
  path.
- The top-level composer is specified as thin but not link-only, and adapter
  placement covers agent role language plus source/package reader modes.
- Support assets, non-components, and deferred concepts have explicit owners,
  citation edges, or re-entry conditions.
- D-01 through D-12, OQ-01 through OQ-09, and ARG-01 through ARG-12 are
  preserved or explicitly merged with source IDs for Slice04 acceptance.
- Slice04 receives a concrete acceptance packet input, including proposed
  decisions, risks, rejected alternatives, deferred questions, and Arc05
  implementation-plan fields.
- Outputs remain proposed architecture inputs, not operator-accepted final
  architecture.
- No source files are edited.
