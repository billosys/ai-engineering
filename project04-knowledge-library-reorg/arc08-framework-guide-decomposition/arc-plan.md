# Arc 08: Framework Guide Decomposition and Version History Normalization

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
status: active
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: per-slice-after-operator-confirmation
operating-mode: expedited-with-explicit-operator-gate
```

## Capability

Arc08 finishes the framework component decomposition that Project02 accepted
and Project04 repeatedly preserved as future work: the current monolith guide
files for collaboration posture and engineering methodology become focused
guide files with stable numbered routes, and framework component version
history moves to sibling `version-history.md` files beside each component
`SKILL.md`.

The arc also tightens Expedited Mode wording so it means only the explicit
process changes the operator named. Expedited Mode must not be interpreted as
permission to skip checks, weaken review, infer extra source scope, compress
semantic work into mechanical moves, or optimize for apparent speed over
fidelity.

## Support Artifacts

Arc08 directly depends on these Project04 project-level inputs:

- `artifacts/operator-accepted-architecture.md`: accepted component map and
  layout sketch, including component root names, sibling `version-history.md`,
  numbered engineering-methods guides, and collaboration-framework posture
  guide names.
- `artifacts/component-file-layout-plan.md`: component layout notes, current
  source basis, versioning plan, and accepted guide split families.

These support artifacts are binding planning evidence for this arc. They are
not optional background, and implementation slices must cite them when
confirming the split map and source edits.

## Approved Split Map

The operator approved the following collaboration-framework guide order on
2026-09-04:

1. `knowledge/collaboration-framework/guides/01-posture-and-ethics.md`
2. `knowledge/collaboration-framework/guides/02-structural-pulls.md`
3. `knowledge/collaboration-framework/guides/03-collaborative-rights.md`
4. `knowledge/collaboration-framework/guides/04-component-route-table.md`

The engineering-methods guide sequence remains the accepted Project02/Project04
layout:

1. `knowledge/engineering-methods/guides/01-engineering-methodology.md`
2. `knowledge/engineering-methods/guides/02-knowledge-substrate.md`
3. `knowledge/engineering-methods/guides/03-process-rigour.md`
4. `knowledge/engineering-methods/guides/04-operational-routing.md`
5. `knowledge/engineering-methods/guides/05-component-boundary-analysis.md`
6. `knowledge/engineering-methods/guides/06-source-package-release-gates.md`

Slice01 must confirm this exact map with the operator before any source
decomposition slice starts. If the operator changes the map, update this
arc-plan and ledger before opening the first source-edit slice.

## Version History Contract

Arc08 accepts the component-level version-history rule:

- Each framework component root has one component version in its `SKILL.md`.
- Each framework component root has one sibling `version-history.md` file.
- Changes to a component `SKILL.md`, its `guides/`, its `templates/`, or its
  `examples/` are recorded in that sibling component history.
- Version history should not live under `guides/` merely because a guide was
  edited.
- Embedded `## Version History` sections in component `SKILL.md`, guides, or
  templates should be moved or reconciled into the sibling history file unless
  a slice records an explicit exception.

Framework component roots in scope for normalization:

- `knowledge/collaboration-framework/`
- `knowledge/engineering-methods/`
- `knowledge/project-management/`
- `knowledge/work-verification/`
- `knowledge/testing/`
- `knowledge/code-auditing/`
- `knowledge/agent-coordination/`
- `knowledge/contribution-style/`

Known current correction: move
`knowledge/project-management/guides/version-history.md` to
`knowledge/project-management/version-history.md` and repair local links.

## Expedited Mode Correction

Arc08 must update the source project-management instructions for Expedited Mode
so the mode is narrowly defined:

- Expedited Mode only changes the explicit commit, close, and advance behaviors
  listed in the written instructions.
- It does not authorize shortcuts.
- It does not authorize skipped validation, reduced evidence, or weaker CDC
  review.
- It does not authorize inferred source scope or additional process changes.
- It does not mean "finish faster" as an independent goal.
- It does not replace explicit operator approval gates recorded in a plan.

This correction is a project-management behavior fix and a guardrail against
the repeated failure to implement accepted semantic splits.

Known current source surfaces that mention Expedited Mode and must be
inventoried in Slice01:

- `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/project-management/guides/version-history.md`, which should move
  to `knowledge/project-management/version-history.md` during normalization.

## Boundaries

In scope:

- Source edits to framework component `SKILL.md`, `guides/`, `templates/`,
  `version-history.md`, Makefile package lists, package-path exceptions,
  README/docs/AGENTS references, release notes, and project-management
  Expedited Mode wording when authorized by a slice.
- Semantic splitting of the two monolith guides into focused files, including
  route text, headings, introductions, and local link repairs needed to keep
  the framework just as usable and more selectively loadable.
- Version-history extraction, reconciliation, and sibling-file normalization
  for the eight framework component roots.
- Validation that source, package, install, and CCDP behavior remain coherent.

Out of scope:

- Domain/tooling skill version-history normalization outside the framework
  component roots.
- Reopening the accepted component names or public skill kind/topology
  vocabulary unless implementation exposes a concrete contradiction.
- Repackaging CCDP as an installable skill.
- Implementing `concept-card-method`.
- Committing generated zips, `build/`, or `target/skills`.

## Slice Breakdown

### Slice 01: Confirm Split Map, Version-History Contract, and Expedited Wording

Status: verified-closed.

Scope: read-only confirmation slice. Inventory current monolith guide headings,
embedded version-history sections, source/package routes, and Expedited Mode
wording. Produce an operator-confirmation packet that states the exact split
map, the version-history normalization set, and the exact Expedited Mode
wording target before any source decomposition starts.

Source edits are not authorized in Slice01.

### Slice 02: Project-Management Process Wording and Version-History Baseline

Status: planned after Slice01 operator confirmation.

Scope: update Expedited Mode wording in project-management source instructions,
update collaboration-framework `SKILL.md` routing text that mentions Expedited
Mode, move project-management `version-history.md` beside `SKILL.md`, repair
routes, and establish the version-history normalization pattern for later
slices.

### Slice 03: Collaboration-Framework Posture Guide Split

Status: planned after Slice02.

Scope: split `AI-CONSTITUTION-SUPPLEMENT.md` into the four approved numbered
collaboration-framework guides, update the collaboration-framework `SKILL.md`
route table and package list, and reconcile collaboration-framework version
history into `knowledge/collaboration-framework/version-history.md`.

### Slice 04: Engineering-Methods Guide Split

Status: planned after Slice03.

Scope: split `AI-ENGINEERING-METHODOLOGY.md` into the six accepted numbered
engineering-methods guides, update engineering-methods and framework routes,
and reconcile engineering-methods version history into
`knowledge/engineering-methods/version-history.md`.

### Slice 05: Remaining Framework Component Version-History Normalization

Status: planned after Slice04.

Scope: normalize sibling `version-history.md` files and embedded history
sections for `work-verification`, `testing`, `code-auditing`,
`agent-coordination`, and `contribution-style`, with route/link/package repairs.

### Slice 06: Final Package, Install, Link, and Release Reconciliation

Status: planned after Slice05.

Scope: run final README/docs/AGENTS/SKILL/component link validation, package
validation, generated package inspection, isolated install smoke, CCDP package
disposition, and release-note reconciliation. Confirm the old monolith guide
filenames are no longer the live load targets unless explicitly retained as
compatibility/provenance stubs.

## Dependencies

- Slice01 requires operator confirmation before Slice02 opens.
- Slice02 must land before decomposition source slices so Expedited Mode no
  longer reinforces shortcut or timeline interpretations.
- Slice03 and Slice04 must preserve source meaning while improving selective
  loadability.
- Slice05 depends on the version-history pattern established in Slice02 and
  the component-specific histories created in Slices03-04.
- Slice06 depends on all source splits and version-history normalization.

## Version History

### v1.0 - 2026-09-04

Opened Arc08 from operator review after Arc07 close. The operator approved the
numbered collaboration-framework guide order and explicitly broadened the arc
to include framework component version-history normalization and Expedited Mode
wording correction. Slice01 is opened as a read-only confirmation gate before
source decomposition starts.

### v1.1 - 2026-09-04

Closed Slice01 after CDC verification. Slice01 produced the operator
confirmation packet, source-impact plan, monolith/history inventory, and
approval-gate artifact without source edits. The A-1 arc ledger row was
corrected from `operator-confirmed split map` to `operator-confirmation packet`
because operator approval is the gate after Slice01, not evidence created
inside Slice01. Slice02 remains blocked until operator approval is recorded.
