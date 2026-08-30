# Slice 02: Candidate Boundary Evaluation

```yaml
project: project02-collab-breakout
arc: arc02-conceptual-analysis
slice: slice02-candidate-boundary-evaluation
status: proposed-done
opened-on: 2026-08-30
proposed-done-on: 2026-08-30
artifact-home: artifacts/
depends-on:
  - slice01-boundary-analysis-instrument:verified-closed
blocks:
  - slice03-ontology-decision-synthesis
related:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-boundary-analysis-instrument/cdc-verification.md
  - ../slice01-boundary-analysis-instrument/artifacts/conceptual-analysis-method.md
  - ../slice01-boundary-analysis-instrument/artifacts/component-boundary-ledger.md
  - ../slice01-boundary-analysis-instrument/artifacts/arc02-input-evidence-register.md
  - ../../arc01-framework-inventory/closing-report.md
  - ../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc01-synthesis.md
  - ../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md
  - ../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc02-question-register.md
  - operator-provided soft layout hypothesis, 2026-08-30 conversation attachment
```

## Goal

Evaluate every seeded Arc01 candidate label using the Slice01
conceptual-analysis method, producing a non-final candidate-boundary evaluation
that Slice03 can synthesize into an ontology, naming critique, and operator
decision register.

This slice converts the seeded ledger from setup state into evaluated evidence.
It should classify each label, explain its reason to load, state its problem
ownership, write competency questions, record typed relationships, apply
path/package gates, identify conceptual risks, and assign a provisional
disposition.

## Scope

In scope:

- Consume the Slice01 conceptual-analysis method, seeded component-boundary
  ledger, input evidence register, and CDC verification.
- Evaluate all 26 seeded candidate labels without leaving any row in
  `seeded-for-Slice02` status.
- Classify each label using the Slice01 vocabulary: concept, candidate
  component, component family member, support asset, adapter, dependency edge,
  constraint, template, package/release gate, or non-component concept.
- Record reason to load, problem ownership, competency questions,
  relationship edges, evidence grade, memory admission, Project01
  path/package gates, conceptual risks, source evidence, and provisional
  disposition for each label.
- Produce a typed relationship map that makes dependency, support, constraint,
  contrast, composition, extension, and routing relations explicit.
- Produce a conceptual risk register covering mislabels, improper merges,
  improper splits, missing concepts, overclaimed mechanisms, underfit, overfit,
  overlap, and duplication.
- Treat the operator-provided layout sketch as a low-weight hypothesis to test
  against evidence, not as a recommendation to adopt.
- Preserve source/package path constraints as cross-cutting gates for every
  evaluation.
- Keep every classification analytical and non-final.

Out of scope:

- Selecting final collaboration-framework component boundaries.
- Creating the Arc02 synthesis or operator decision register reserved for
  Slice03.
- Treating the operator-provided layout sketch as accepted architecture or as a
  substitute for candidate-by-candidate evidence.
- Performing Arc03 functional usage analysis.
- Editing source `SKILL.md`, `README.md`, framework docs, templates,
  Makefiles, package scripts, generated zips, or package exceptions.
- Editing planning artifacts outside Project02.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `candidate-boundary-evaluation.md` - one completed evaluation row per seeded
  candidate label.
- `component-relationship-map.md` - typed relationship edges, likely component
  families, support assets, adapters, constraints, and unresolved relationship
  questions.
- `conceptual-risk-register.md` - conceptual risks found during evaluation,
  including mislabels, improper merges/splits, missing concepts, overclaimed
  mechanisms, underfit/overfit, overlap, duplication, and required follow-up.

## Soft Layout Hypothesis

The operator supplied a 2026-08-30 screenshot as a soft layout hypothesis. It
is explicitly a guess and should not outrank Project02 evidence. Preserve it
only as a hypothesis to test.

The sketch suggests a possible future source/package shape:

- `knowledge/collaboration-framework/` as the top-level composer, with
  `SKILL.md` and guides for posture and ethics, engineering methodology,
  verification methodology, and maintenance.
- `knowledge/project-management/` as a project-management wayfinder, with
  guides for scales of work, planning worktree, planning top-down, closing
  slices, closing arcs, confirmation protocol, and anti-patterns.
- `knowledge/ledger-discipline/` as a standalone component, with guides for
  evidence ladder, row closure, verification, and templates.
- Additional component candidates for code audit, coverage hardening,
  delegation policy, and contribution guidance.

Slice02 should compare this hypothesis against the evaluated component
boundaries. Where evidence supports it, say so with evidence grade. Where it
over-splits, under-splits, mislabels, or prematurely chooses architecture,
record that as a finding for Slice03.

## Verification Approach

The slice verifies by checking that the required artifacts exist under
`artifacts/`, that all 26 seeded labels are evaluated, that no row remains
`seeded-for-Slice02`, that each artifact uses the Slice01 method vocabulary,
that relationship and risk outputs use the required typed categories, that
Project01 path/package gates are carried through, that the outputs remain
analytical and non-final, and that the implementation source checkout remains
unchanged.

## Exit Criteria

- Slice01's method, seeded ledger, input register, and CDC verification are
  consumed as the local input contract.
- `artifacts/candidate-boundary-evaluation.md` contains exactly 26 completed
  candidate rows and no `seeded-for-Slice02` rows.
- Candidate rows include final classification, reason to load, problem
  ownership, competency questions, relationship edges, evidence grade, memory
  admission, source evidence, conceptual risks, path/package gates, and
  provisional disposition.
- `artifacts/component-relationship-map.md` records typed relationships using
  the Slice01 relationship vocabulary.
- `artifacts/conceptual-risk-register.md` covers mislabels, improper merges,
  improper splits, missing concepts, overclaimed mechanisms, underfit, overfit,
  overlap, and duplication, even when a category has no confirmed instance.
- The operator-provided soft layout hypothesis is tested against evidence and
  clearly marked as a low-weight hypothesis, not accepted architecture.
- Project01 path/package constraints are applied as cross-cutting gates and
  package/release gates rather than promoted into final architecture.
- The outputs remain analytical and non-final; final architecture remains
  deferred to Arc04 after Arc03 functional analysis and operator acceptance.
- No source files are edited.
