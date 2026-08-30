# Project 03: Concept Card Method

```yaml
project: project03-concept-card-method
status: active
depends-on:
  - project02-collab-breakout:arc01-synthesis
blocks:
  - project02-collab-breakout:arc02-conceptual-analysis
  - future concept-card-method v4.0 knowledge skill
  - provenance-bearing memory-consolidation workflow
related:
  - /Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md
  - /Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md
  - /Users/oubiwann/lab/billosys/ai-engineering/docs/AI-ENGINEERING-METHODOLOGY.md
  - /Users/oubiwann/lab/billosys/ai-engineering/protocols/ccdp
  - project02-collab-breakout
```

## Planning Substrate

Planning artifacts live on orphan branch `planning`, worktree
`.worktrees/planning`, under `project03-concept-card-method/`, per
`docs/PROJECT-MANAGEMENT.md`.

The implementation checkout is the source repository's `main` worktree at
`/Users/oubiwann/lab/billosys/ai-engineering`. This project is planning-only
until an implementation arc explicitly authorizes source edits.

Slice-generated durable artifacts live under the owning slice's `artifacts/`
directory unless the operator records an override.

## Definition of Done

The project is done when the v3.2 concept-card extraction methodology has been
assessed as the source baseline and a v4.0 concept-card method has been
planned as a repo knowledge skill that supports concept extraction, ontology
critique, provenance-bearing memory consolidation, and CCDP-compatible
evidence grading.

Specifically:

- The current v3.2 concept-card docs are inventoried from the workbench copies
  as the baseline, with source purpose, schema, workflow phases, validation
  checks, and known limitations mapped to source locations.
- The method's conceptual model is defined: concept card, source span, claim,
  evidence grade, relationship, competency question, extraction run, verifier,
  and memory-admission status.
- The skill architecture is planned using Project02-style component-selection
  criteria: reason to load, problem ownership, dependency direction, package
  behavior, and maintenance ownership.
- The proposed skill layout defines `SKILL.md`, `guides/`, templates, any
  deterministic validation scripts, examples, package behavior, and README
  integration.
- The Project02 Arc02 conceptual-analysis work receives a compact boundary aid
  before it selects collaboration-framework component boundaries.
- The implementation plan is detailed enough to begin source edits only after
  the architecture is accepted, including Makefile/package updates,
  package-path validation, and verification gates.

## Boundaries

In scope:

- The two v3.2 concept-card methodology docs currently copied to `workbench/`.
- The relationship between concept-card extraction, knowledge skills,
  ontology critique, competency questions, provenance, CCDP, and memory
  augmentation.
- A Project02 support artifact that sharpens Arc02 component-boundary analysis.
- Planning a future v4.0 repo knowledge skill with a thin `SKILL.md` wayfinder,
  focused guides, templates, and optional validation scripts.
- Package and README planning for the eventual skill.

Out of scope until an accepted implementation plan:

- Editing source `SKILL.md`, `README.md`, `Makefile`, packaged skill lists,
  concept-card docs, framework docs, or generated zips.
- Treating the v3.2 workbench docs as already accepted source docs.
- Reorganizing Project02's collaboration-framework components directly.
- Building a full GraphRAG, memory runtime, CCDP service, or ontology database.

## Arc Roadmap

### Arc 01: Method Positioning and Project02 Aid

Status: active.

Capability: establish the minimum concept-card method context needed before
Project02 Arc02 selects collaboration-framework component boundaries, while
opening Project03 with a clear roadmap and evidence contract.

Slices:

- `slice01-project02-boundary-aid`: create the Project03 planning scaffold and
  produce a compact conceptual-boundary aid for Project02 Arc02.
- `slice02-project02-acceptance-handoff`: produce the handoff/readiness packet
  that lets the operator decide whether Project02 Arc02 can consume the aid,
  and lets Arc01 close with a clear composition record.

### Arc 02: Method Inventory and Gap Analysis

Status: placeholder.

Expected capability: inventory the v3.2 concept-card baseline docs from actual
files, map their schema, workflow, validation, and re-extraction mechanics,
and identify the gaps that make the next method revision a v4.0 change rather
than a v3.3 cleanup.

Detailed arc planning is deferred until Arc 01 closes.

### Arc 03: Conceptual Model

Status: placeholder.

Expected capability: define the ontology of the method: concept cards, claims,
source spans, evidence grades, relationships, competency questions, extraction
runs, verifier roles, reconciliation, and memory admission for the v4.0 method.

Detailed arc planning is deferred until Arc 02 closes.

### Arc 04: Skill Architecture

Status: placeholder.

Expected capability: propose the v4.0 skill's target layout, including entrypoint
contract, guide set, templates, optional scripts, examples, package behavior,
README integration, and relationship to Project02 framework components.

Detailed arc planning is deferred until Arc 03 closes.

### Arc 05: Implementation Plan

Status: placeholder.

Expected capability: convert the accepted architecture into sliceable source
edits and verification gates for creating the concept-card method skill.

Detailed arc planning is deferred until Arc 04 closes.

## Current Status

Project03 is open for planning. Arc 01 is active and ready for formal arc
close: Slice01 and Slice02 are both verified-closed, and the Project02 Arc02
acceptance handoff is ready for operator decision. Project02 Arc02 does not
wait for the full Project03 v4.0 skill.

## Version History

### v1.0 - 2026-08-30

Initial roadmap opened from operator acceptance of a soft Project03 dependency
before Project02 Arc02. The project treats Project02's emerging component
architecture as design precedent while keeping concept-card methodology work
in its own project.

### v1.1 - 2026-08-30

Arc01 Slice01 marked verified-closed with a same-context CDC-style verification
pass. The Project02 conceptual-boundary aid is now available as a non-final
input for Project02 Arc02 operator acceptance.

### v1.2 - 2026-08-30

Recorded operator direction that the method revision is a major-version move:
Project03 targets v4.0, with v3.2 preserved as the source baseline rather than
treated as a minor v3.3 continuation.

### v1.3 - 2026-08-30

Opened Arc01 Slice02, `slice02-project02-acceptance-handoff`, to turn the
Slice01 boundary aid into an operator-facing readiness packet before Arc01
formal close and Project02 Arc02 detailed planning.

### v1.4 - 2026-08-30

Arc01 Slice02 marked verified-closed by CDC. Arc01 is now ready for formal arc
close, while Project02 Arc02 still waits for operator acceptance of the
handoff rather than the full Project03 v4.0 skill.
