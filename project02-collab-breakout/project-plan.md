# Project 02: Collaboration Framework Breakout

```yaml
project: project02-collab-breakout
status: active
depends-on:
  - project01-harmonise-paths
blocks:
  - modular standalone use of collaboration-framework disciplines
  - updated collaboration-framework wayfinding after component breakout
  - README guidance for individual and composed framework components
related:
  - /Users/oubiwann/lab/billosys/ai-engineering
  - project01-harmonise-paths
  - project03-concept-card-method
  - SKILL.md
  - README.md
  - docs/AI-CONSTITUTION-SUPPLEMENT.md
  - docs/AI-ENGINEERING-METHODOLOGY.md
  - docs/PROJECT-MANAGEMENT.md
  - templates/LEDGER-DISCIPLINE.md
```

## Planning Substrate

Planning artifacts live on orphan branch `planning`, worktree
`.worktrees/planning`, under `project02-collab-breakout/`, per
`docs/PROJECT-MANAGEMENT.md`.

The implementation checkout is the source repository's `main` worktree at
`/Users/oubiwann/lab/billosys/ai-engineering`. This project is planning-only
until `project01-harmonise-paths` is closed and completely verified.

Slice-generated analysis artifacts that are part of planning or verification
live in the slice directory where they are generated.

## Definition of Done

The project is done when the current monolithic collaboration framework has
been analyzed, divided, and planned for implementation as a set of coherent,
standalone, composable components, with the top-level collaboration framework
remaining available as a composition of those components.

Specifically:

- The current framework is mapped from actual source artifacts, not memory or
  a summary, with each major concept, discipline, prompt, and template assigned
  to its current source location.
- Conceptual analysis identifies the framework's real ontology: which ideas
  are distinct, which are variants of the same discipline, which are mislabeled,
  and which current combinations or splits are suspect.
- Functional analysis identifies how humans and LLMs actually use the framework:
  load moments, context cost, dependency order, standalone use cases,
  composition paths, packaging constraints, and failure modes.
- The proposed breakout identifies each target component's contract, scope,
  dependencies, entry point, packaging behavior, and relationship to the
  top-level collaboration-framework skill.
- The implementation plan is detailed enough to begin source edits after
  `project01-harmonise-paths` closes, including README updates, SKILL.md
  updates or new SKILL.md files, packaging updates, and verification gates.

## Boundaries

In scope:

- The collaboration-framework entry point, framework docs, project-management
  docs, ledger discipline, audit prompt, coverage prompt, subagent policy,
  contribution style, and contribution ticket template.
- Critical analysis of naming, taxonomy, ontology, component boundaries,
  problem-solution fit, missed problems, and missed solutions.
- Functional analysis of expected human and LLM usage patterns, including
  source-clone and packaged-skill consumption.
- Planning the target component set and implementation slices.
- README planning for individual component usefulness, component use, and the
  composed collaboration-framework use case.

Out of scope until this project reaches implementation:

- Editing source `SKILL.md`, `README.md`, framework docs, templates, Makefiles,
  package staging scripts, or generated zip artifacts.
- Executing Slice 01 before `project01-harmonise-paths` has closed and been
  completely verified.
- Redesigning domain knowledge skills under `knowledge/`, except to describe
  how they compose with framework components.
- Treating current file boundaries as authoritative component boundaries.

## Arc Roadmap

### Arc 01: Framework Inventory and Problem Map

Status: closed/composed on 2026-08-30.

Capability: establish the evidence base for the breakout by inventorying the
current framework sources, mapping concepts and disciplines to source
locations, and connecting them to the historical and functional problems they
were meant to solve.

Slices:

- `slice01-source-inventory`: inventory the current framework entry points and
  source documents, record package/path dependencies from project01, and produce
  the first source-backed concept/problem map.
- `slice02-problem-solution-map`: refine the inventory into a historical
  problem-to-solution map with evidence for which current mechanisms address
  which failure modes.
- `slice03-arc01-synthesis`: synthesize the evidence base into explicit inputs
  for conceptual analysis: current components, candidate components, overlaps,
  suspected mislabels, and open questions.

### Arc 02: Conceptual Analysis

Status: closed/composed on 2026-08-30.

Expected capability: perform the taxonomy and ontology analysis of the current
framework, including critical checks for mislabeled concepts, improper merges,
  improper splits, missing concepts, overclaimed mechanisms, and gaps between
  stated aims and actual solution shape.

Detailed arc planning opened after Arc 01 closed and the operator accepted
using the Project03 Slice01 boundary aid plus
`slice02-project02-acceptance-handoff` as sufficient Project02 inputs.
Project02 consumes Project03 outputs only; Project03 control status does not
gate Project02 Arc02.

### Arc 03: Functional Analysis

Status: ready for detailed planning.

Expected capability: analyze how the framework works in expected usage
patterns: direct repo reading, packaged skill reading, LLM skill loading,
human orientation, session start, slice execution, audit, coverage, upstream
contribution, and combinations of these. Identify inefficiencies,
deficiencies, context-load problems, unclear handoffs, and missing functional
goals.

Detailed arc planning is deferred until Arc 02 closes.

### Arc 04: Breakout Architecture

Status: placeholder.

Expected capability: propose the target functional division into standalone
and composable components, including component names, contracts,
dependencies, wayfinders, package shape, migration risks, and how the
top-level collaboration-framework remains usable as a composition.

Detailed arc planning is deferred until Arc 03 closes.

### Arc 05: Implementation Plan

Status: placeholder.

Expected capability: turn the accepted breakout architecture into a sliceable
implementation plan covering source edits, README guidance, component SKILL.md
entry points, packaging behavior, path-contract validation, and verification.

Detailed arc planning is deferred until Arc 04 closes and
`project01-harmonise-paths` has closed.

## Current Status

Project 02 is opened for planning. Arc 01 and Arc 02 are closed/composed.
Arc 03 is ready for detailed functional-analysis planning.

Later arcs are intentionally placeholders so the roadmap is visible while
respecting the plan-late, plan-deep discipline.

## Version History

### v1.0 - 2026-08-29

Initial roadmap opened from the collaboration-framework breakout discussion.
The project depends on verified completion of `project01-harmonise-paths` so
the breakout consumes the accepted source/package path contract instead of
inventing parallel packaging semantics.

### v1.1 - 2026-08-29

Arc 01 Slice 01 marked verified/closed by CDC. The project is no longer blocked
by Project01 closure; Arc 01 can proceed to Slice 02 using the verified
inventory and Project01 path/package constraints.

### v1.2 - 2026-08-29

Arc 01 Slice 02 opened for problem-solution mapping. No source edits are in
scope; durable analysis outputs remain under the slice-local `artifacts/`
home.

### v1.3 - 2026-08-29

Arc 01 Slice 02 marked verified/closed by CDC. Slice 03 can now synthesize the
source inventory, problem-solution map, mechanism coverage matrix, critical
findings, and Project01 path/package constraints into Arc 02 inputs.

### v1.4 - 2026-08-30

Arc 01 Slice 03 opened for synthesis. The slice will prepare non-final
component-boundary inputs, constraint classifications, and operator questions
for Arc 02 conceptual analysis.

### v1.5 - 2026-08-30

Arc 01 Slice 03 marked verified/closed by CDC. Arc 01 now has all planned
slices verified/closed and is ready for formal arc close; Arc 02 remains
deferred until that close completes.

### v1.6 - 2026-08-30

Recorded the operator-accepted soft dependency on
`project03-concept-card-method` before Project02 Arc02 detailed planning.
Project02 does not wait for the full Project03 v4.0 skill; it waits only for
the Slice01 boundary aid that adapts the concept-card method into a focused
component-boundary analysis lens.

### v1.7 - 2026-08-30

Updated the Project03 soft dependency after opening Project03 Arc01 Slice02.
Project02 Arc02 now waits for the Slice01 boundary aid plus the Slice02
acceptance handoff, while still explicitly not waiting for the full Project03
v4.0 skill.

### v1.8 - 2026-08-30

Recorded CDC verification of Project03 Arc01 Slice02. Project02 Arc02 now waits
on operator acceptance of the boundary aid plus handoff packet and Project03
Arc01 formal close, not on production of the handoff or the full v4.0 skill.

### v1.9 - 2026-08-30

Opened Project02 Arc02 for detailed conceptual-analysis planning after Arc01
closed/composed and the operator accepted Project03's boundary aid and handoff
as useful inputs. Project02 consumes Project03 outputs only; Project03 control
status does not gate Project02 Arc02.

### v1.10 - 2026-08-30

Opened Arc02 Slice 02 after Slice 01 CDC verification. The project remains in
conceptual analysis; Slice 02 evaluates the seeded candidate labels but does
not select final breakout architecture.

### v1.11 - 2026-08-30

Opened Arc02 Slice 03 after Slice 02 CDC verification. Slice 03 owns Arc02
ontology and decision synthesis, including naming critique, merge/split
findings, missing/overclaimed concept findings, and operator decisions needed
before Arc04.

### v1.12 - 2026-08-30

Recorded Arc02 Slice 03 as verified/closed. Arc02 now has all planned slices
verified/closed and can proceed to formal arc close without a remediation
slice.

### v1.13 - 2026-08-30

Recorded formal Arc02 close. Arc02 delivered the conceptual-analysis capability
and bubbled up that Arc03 should test the conceptual model against actual usage
and load patterns before Arc04 accepts a breakout architecture.
