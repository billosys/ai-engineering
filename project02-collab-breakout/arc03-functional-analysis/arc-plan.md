# Arc 03: Functional Analysis

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
status: closed
opened-on: 2026-08-30
depends-on:
  - arc02-conceptual-analysis
blocks:
  - arc04-breakout-architecture
related:
  - ../project-plan.md
  - ../ledger.md
  - ../arc01-framework-inventory/closing-report.md
  - ../arc02-conceptual-analysis/closing-report.md
  - ../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md
  - ../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md
  - ../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md
  - ../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-close-readiness.md
```

## Capability

Arc 03 performs the functional analysis of the current collaboration framework
as a working system. It examines how humans and LLMs use the framework across
direct source-clone reading, packaged skill reading, session start, planning,
execution, slice and arc close, audit, coverage, delegation, contribution, and
mixed-component workflows.

The central question is not "which concepts are distinct?" Arc02 answered that
at conceptual-analysis scale. Arc03 asks "how does this system actually work
for expected users, and where does it fail or cost too much?"

Arc03 does not select the final breakout architecture. Its job is to produce a
functional model, usage-scenario evidence, load-path findings, friction and
deficiency registers, and Arc04-ready architecture inputs.

## Slice Breakdown

### Slice 01: Usage Surface Instrument

Directory: `slice01-usage-surface-instrument`

Status: verified/closed on 2026-08-30.

Scope: define the Arc03 functional-analysis method, inventory the usage
surfaces and load paths that the current framework must support, and build the
scenario matrix that later slices apply. The slice should consume Arc02 close
outputs and turn them into functional questions without evaluating every
scenario yet.

Delivered: Slice 01 produced Arc03's functional-analysis method,
usage-surface inventory, scenario matrix, and input register. CDC verified the
close in `slice01-usage-surface-instrument/cdc-verification.md`.

Durable analysis outputs live under the slice-local `artifacts/` directory.

### Slice 02: Current Workflow Evaluation

Directory: `slice02-current-workflow-evaluation`

Status: verified/closed on 2026-08-30.

Scope: apply the Slice01 scenario matrix to the current monolithic framework
and record how the existing files behave for humans and LLMs. Evaluate source
clone reading, packaged skill reading, session start, PM execution, close
flows, audit, coverage, delegation, contribution, role-language routing, and
source/package path behavior. Produce functional friction, inefficiency, and
deficiency findings without proposing architecture.

Delivered: Slice 02 produced the current-workflow evaluation, load-path
friction register, functional-deficiency register, and source/package
role-language notes. CDC verified the close in
`slice02-current-workflow-evaluation/cdc-verification.md`.

Durable analysis outputs live under the slice-local `artifacts/` directory.

### Slice 03: Standalone And Composition Scenario Evaluation

Directory: `slice03-standalone-composition-evaluation`

Status: verified/closed on 2026-08-30.

Scope: use the Arc02 conceptual model plus Slice02 current-workflow findings
to test candidate standalone and composed component usage scenarios. Evaluate
likely direct load moments, minimum useful load sets, dependency ordering,
component-family behavior, support-asset travel, adapter needs, and whether
any concept lacks a real functional load path.

Delivered: Slice 03 produced standalone and composition scenario evaluations,
the minimum-load and dependency matrix, component dependency/adapter findings,
and Arc03 functional decision inputs. CDC verified the close in
`slice03-standalone-composition-evaluation/cdc-verification.md`.

Durable analysis outputs live under the slice-local `artifacts/` directory.

### Slice 04: Arc03 Functional Synthesis

Directory: `slice04-functional-synthesis`

Status: verified/closed on 2026-08-30.

Scope: synthesize Arc03 into a functional model and Arc04 architecture input
set: scenario coverage, load-cost findings, standalone/composition fit,
functional risks, unresolved operator questions, and close-readiness for the
functional-analysis arc.

Blocks: Arc03 close.

Delivered: Slice 04 produced the Arc03 functional model, scenario coverage
synthesis, functional fit and risk synthesis, Arc04 architecture inputs, and
Arc03 close-readiness assessment. CDC verified the close in
`slice04-functional-synthesis/cdc-verification.md`.

Durable analysis outputs live under the slice-local `artifacts/` directory.

## Dependencies

Consumes:

- Closed Project02 Arc01 evidence for current source locations, problem
  classes, and candidate labels.
- Closed Project02 Arc02 evidence, especially the conceptual model, boundary
  and naming findings, operator decision register, and close-readiness
  assessment.
- Project01 path/package constraints carried forward through Arc01 and Arc02.
- Current source checkout only as read-only grounding; no source edits belong
  to this arc.

Leaves for later arcs:

- A functional model of how the current framework is actually used.
- A scenario matrix and usage-surface inventory suitable for architecture
  decisions.
- Evidence about standalone versus composed component usability.
- A functional friction and deficiency register for Arc04 architecture.
- Load-path, context-cost, source/package, and role-language findings that
  Arc04 must resolve before accepting component boundaries.


## Version History

### v1.0 - 2026-08-29

Placeholder opened with dependency on Arc 02.

### v1.1 - 2026-08-30

Opened Arc03 as active after Arc02 closed/composed. Planned four slices:
usage-surface instrument, current workflow evaluation, standalone/composition
scenario evaluation, and functional synthesis.

### v1.2 - 2026-08-30

Recorded Slice 01 as verified/closed. Slice 02 can now open against the
scenario matrix to evaluate current monolith workflows, with no Arc03 plan
change required before opening it.

### v1.3 - 2026-08-30

Opened Slice 02 for current workflow evaluation against the Slice01
functional-analysis method, usage-surface inventory, scenario matrix, and input
register.

### v1.4 - 2026-08-30

Recorded Slice 02 as verified/closed. Slice 03 can now open against the
current-monolith findings to evaluate candidate standalone and composed
component scenarios.

### v1.5 - 2026-08-30

Opened Slice 03 for standalone and composition scenario evaluation against the
Slice01 scenario matrix, Slice02 current-workflow findings, and Arc02
conceptual model.

### v1.6 - 2026-08-30

Recorded Slice 03 as verified/closed. Slice 04 can now open against the
current-monolith baseline and standalone/composed comparison findings to
synthesize Arc03.

### v1.7 - 2026-08-30

Opened Slice 04 for Arc03 functional synthesis and close-readiness analysis
against the verified Slice01, Slice02, and Slice03 evidence.

### v1.8 - 2026-08-30

Recorded Slice 04 as verified/closed. Arc03 now has all planned slices
verified/closed and is ready for formal arc close; Arc04 detailed planning
remains deferred until that arc-level composition check is complete.

### v1.9 - 2026-08-30

Recorded formal Arc03 close. The four verified slices compose into the
functional-analysis capability, with final breakout architecture and operator
acceptance still deferred to Arc04.
