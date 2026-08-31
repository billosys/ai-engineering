# Arc 04: Breakout Architecture

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
status: active
opened-on: 2026-08-30
depends-on:
  - arc02-conceptual-analysis
  - arc03-functional-analysis
blocks:
  - arc05-implementation-plan
related:
  - ../project-plan.md
  - ../ledger.md
  - ../arc02-conceptual-analysis/closing-report.md
  - ../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md
  - ../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md
  - ../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md
  - ../arc03-functional-analysis/closing-report.md
  - ../arc03-functional-analysis/slice04-functional-synthesis/artifacts/arc03-functional-model.md
  - ../arc03-functional-analysis/slice04-functional-synthesis/artifacts/scenario-coverage-synthesis.md
  - ../arc03-functional-analysis/slice04-functional-synthesis/artifacts/functional-fit-and-risk-synthesis.md
  - ../arc03-functional-analysis/slice04-functional-synthesis/artifacts/arc04-architecture-inputs.md
```

## Capability

Arc04 proposes and secures operator acceptance for the target functional
division of the current collaboration framework into standalone, reusable, and
composable components. It defines each accepted component's name, purpose,
contract, boundaries, dependencies, wayfinding behavior, package shape,
support assets, adapter needs, source/package constraints, release gates, and
relationship to the top-level `collaboration-framework` composition.

Arc04 consumes Arc02 conceptual evidence and Arc03 functional evidence, but it
does not edit source files. It turns the evidence into an accepted architecture
that Arc05 can later translate into an implementation plan.

The arc ends only after the proposed breakdown has been discussed and accepted
by the operator.

## Slice Breakdown

### Slice 01: Architecture Decision Instrument

Directory: `slice01-architecture-decision-instrument`

Status: verified/closed on 2026-08-31.

Scope: consolidate closed Arc02 and Arc03 evidence into an Arc04 decision
instrument. Define the architecture decision method, component-contract schema,
candidate worklist, operator-decision worklist, and risk/gate register that
later Arc04 slices must use. This slice should not accept final component
boundaries or package paths.

Blocks: Slice 02 component contract evaluation.

Delivered: Slice 01 produced the architecture input register, architecture
decision method, component contract schema, candidate architecture worklist,
and operator decision/risk register. CDC verified the close in
`slice01-architecture-decision-instrument/cdc-verification.md`.

Durable analysis outputs live under the slice-local `artifacts/` directory.

### Slice 02: Candidate Component Contract Evaluation

Directory: `slice02-component-contract-evaluation`

Status: verified/closed on 2026-08-31.

Scope: apply the Slice01 decision instrument to every candidate component,
component family, support asset, adapter, constraint, and package/release gate
carried from Arc02 and Arc03. Produce evaluated component-contract candidates
and go / adjust / defer dispositions, without yet finalizing the full package
graph.

Blocks: Slice 03 target composition and package architecture.

Delivered: Slice 02 produced the component contract evaluation matrix,
candidate component contracts, support/adapter/constraint dispositions,
package/release gate dispositions, and Slice03 composition inputs. CDC
verified the close in
`slice02-component-contract-evaluation/cdc-verification.md`.

Durable analysis outputs live under the slice-local `artifacts/` directory.

### Slice 03: Target Composition And Package Architecture

Directory: `slice03-target-composition-package-architecture`

Status: verified/closed on 2026-08-31.

Scope: compose the accepted and adjusted candidate contracts into a target
architecture: component graph, dependency order, top-level composer contract,
PM-family package strategy, support-asset travel, adapter placement,
source/package path assumptions, README/SKILL wayfinding implications, and
release-gate strategy.

Blocks: Slice 04 operator acceptance and architecture synthesis.

Delivered: Slice 03 produced the target component architecture, dependency
and composition order, package and release architecture, wayfinding/adapter/
support plan, and Slice04 operator acceptance inputs. CDC verified the close
in `slice03-target-composition-package-architecture/cdc-verification.md`.

Durable analysis outputs live under the slice-local `artifacts/` directory.

### Slice 04: Operator Acceptance And Architecture Synthesis

Directory: `slice04-operator-acceptance-architecture-synthesis`

Status: placeholder.

Scope: synthesize the target architecture into an acceptance packet for
operator review. Record accepted component names, contracts, dependencies,
package/source assumptions, deferred decisions, and Arc05 implementation-plan
inputs. This slice owns the operator acceptance checkpoint required before
Arc04 can close.

Blocks: Arc04 close and Arc05 implementation planning.

## Dependencies

Consumes:

- Closed Project02 Arc02 evidence: conceptual model, boundary and naming
  findings, operator decision register, and conceptual close report.
- Closed Project02 Arc03 evidence: functional model, scenario coverage,
  functional fit/risk synthesis, architecture inputs, and functional close
  report.
- Project01 path/package constraints carried through Arc01, Arc02, and Arc03.
- The operator-provided soft layout sketch as low-weight hypothesis evidence,
  not accepted architecture.

Leaves for later arcs:

- An operator-accepted target component map.
- Component contracts with names, purposes, boundaries, dependency edges,
  support assets, adapters, source/package behavior, package paths, and
  release gates.
- A top-level `collaboration-framework` composition contract.
- Arc05-ready implementation inputs covering source edits, README/SKILL
  updates, packaging lists, path validation, and verification gates.

## Version History

### v1.0 - 2026-08-29

Placeholder opened with dependency on Arc 03.

### v1.1 - 2026-08-30

Opened Arc04 as active after Arc03 closed/composed. Planned four slices:
architecture decision instrument, candidate component contract evaluation,
target composition and package architecture, and operator acceptance plus
architecture synthesis.

### v1.2 - 2026-08-31

Recorded Slice 01 as verified/closed. Slice 02 can open against the
architecture decision method, component contract schema, candidate worklist,
and operator decision/risk register, with no Arc04 plan change required first.

### v1.3 - 2026-08-31

Opened Slice 02 for component contract evaluation against the verified
Slice01 architecture decision instrument. Slice 02 owns evaluated candidate
contracts and dispositions, while final target composition remains deferred to
Slice 03.

### v1.4 - 2026-08-31

Recorded Slice 02 as verified/closed. Slice 03 can open against the evaluated
component contracts, support/adapter/constraint dispositions, package/release
gate dispositions, and Slice03 composition inputs, with no Arc04 plan change
required first.

### v1.5 - 2026-08-31

Opened Slice 03 for target composition and package architecture against the
verified Slice01 decision instrument and verified Slice02 component-contract
evaluation outputs. Slice 03 owns the proposed architecture inputs for
Slice04 operator acceptance, without accepting final architecture itself.

### v1.6 - 2026-08-31

Recorded Slice 03 as verified/closed. Slice 04 can open against the proposed
target component architecture, dependency/composition order, package/release
architecture, wayfinding/adapter/support plan, and operator acceptance inputs,
with no Arc04 plan change required first.
