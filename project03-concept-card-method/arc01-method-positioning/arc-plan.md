# Arc 01: Method Positioning and Project02 Aid

```yaml
project: project03-concept-card-method
arc: arc01-method-positioning
status: active
depends-on:
  - project02-collab-breakout:arc01-synthesis
blocks:
  - project02-collab-breakout:arc02-conceptual-analysis
  - project03-concept-card-method:arc02-method-inventory
related:
  - ../../project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc01-synthesis.md
  - ../../project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md
  - ../../project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc02-question-register.md
```

## Capability

Arc 01 creates the minimum Project03 planning substrate and produces a compact
conceptual-boundary aid for Project02 Arc02. It does not build the final v4.0
concept-card skill, and it does not decide Project02 component boundaries.

The arc's purpose is to make Project02's conceptual analysis sharper by giving
it a reusable lens for distinguishing components, support assets, adapters,
constraints, templates, evidence semantics, and memory-bearing substrate.

## Slice Breakdown

### Slice 01: Project02 Boundary Aid

Directory: `slice01-project02-boundary-aid`

Status: verified/closed in same-context CDC-style pass on 2026-08-30.

Scope: create the Project03 project/arc/slice planning set, produce the
Project02 conceptual-boundary aid under `artifacts/`, and mark Project02 Arc02
as softly paused until this aid is available.

Blocks: no longer blocking Project02 Arc02 aid consumption; Project03 Arc02 may
be planned after Arc01 close.

### Slice 02: Project02 Acceptance Handoff

Directory: `slice02-project02-acceptance-handoff`

Status: open.

Scope: produce a compact handoff/readiness packet that lets the operator decide
whether Project02 Arc02 can consume the Slice01 boundary aid as sufficient input
for detailed conceptual-analysis planning. The packet should also make Arc01's
composition evidence easier to close.

Blocks: Project02 Arc02 detailed planning and Project03 Arc01 formal close.

## Dependencies

Consumes:

- Project02 Arc01 Slice03 synthesis artifacts.
- The v3.2 concept-card workbench docs as baseline planning inputs.
- Current Project02 candidate-component criteria.

Leaves for later arcs:

- A Project02 aid artifact that can be cited in Arc02 conceptual analysis.
- A Project03 roadmap and ledger for full method inventory, conceptual model,
  v4.0 skill architecture, and implementation planning.

## Version History

### v1.0 - 2026-08-30

Initial Arc01 plan opened with one small slice to produce a Project02
conceptual-boundary aid before Project02 Arc02 proceeds.

### v1.1 - 2026-08-30

Slice01 marked verified-closed with same-context CDC-style verification. The
boundary aid is available for Project02 Arc02 operator acceptance; Arc01 still
needs its own formal arc close before Project03 Arc02 detailed planning.

### v1.2 - 2026-08-30

Recorded operator direction that Project03 targets a v4.0 method/skill rather
than a v3.3 continuation; Arc01 continues to use the v3.2 workbench docs only
as baseline evidence.

### v1.3 - 2026-08-30

Opened Slice02 for the Project02 acceptance handoff. This expands Arc01 from
one slice to two: Slice01 produced the boundary aid, and Slice02 prepares the
operator-facing handoff needed before Arc01 formal close and Project02 Arc02
detailed planning.
