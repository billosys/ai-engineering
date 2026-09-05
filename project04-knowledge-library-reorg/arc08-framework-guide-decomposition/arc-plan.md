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
files for collaboration posture, engineering methodology, and the remaining
framework components become focused guide files with stable numbered routes,
framework component version history moves to sibling `version-history.md` files
beside each component `SKILL.md`, and project-management layout is reconciled
against the accepted architecture.

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

The operator also re-confirmed on 2026-09-04 that the remaining accepted
component guide decomposition belongs in Arc08, not a later arc. The remaining
target layout is:

```text
project-management/
  SKILL.md
  version-history.md
  guides/
    01-scales-of-work.md
    02-canonical-planning-worktree.md
    03-planning-top-down.md
    04-closing-slices.md
    05-closing-arcs.md
    06-confirmation-protocol.md
    07-anti-patterns.md
    08-maintenance.md
  examples/
    01-worked-example-odm.md

work-verification/
  SKILL.md
  version-history.md
  guides/
    01-ledger-discipline.md
    02-evidence-strength.md
    03-row-closure.md
    04-silent-drop-checks.md
    05-independent-verification.md
  templates/
    LEDGER-DISCIPLINE.md

testing/
  SKILL.md
  version-history.md
  guides/
    01-testing-discipline.md
    02-coverage-hardening.md
    03-validation-gates.md

code-auditing/
  SKILL.md
  version-history.md
  guides/
    01-audit-scope-and-map.md
    02-findings-and-severity.md
    03-scale-aware-auditing.md
    04-modernization-synthesis.md
    05-audit-to-hardening-handoff.md

agent-coordination/
  SKILL.md
  version-history.md
  guides/
    01-when-to-delegate.md
    02-context-packets.md
    03-result-integration.md
    04-anti-patterns.md

contribution-style/
  SKILL.md
  version-history.md
  guides/
    01-contribution-style.md
    02-upstream-ticket-workflow.md
  templates/
    CONTRIBUTION-TICKET.md
```

Slice01 confirmed the first two source-decomposition maps. The remaining map
above is now accepted as downstream Arc08 scope by operator direction; each
source-edit slice should still inspect current source, preserve semantics, and
record any implementation-specific conflicts before editing.

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
- It does not authorize inferred source scope, any reduction or other change in
  scope, or additional process changes.
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

The operator confirmed on 2026-09-04 that the version-history management
practice also needs durable documentation for future sessions. Slice02 should
use top-level `AGENTS.md` as the expected home unless source evidence shows a
better location and records the rationale.

## Boundaries

In scope:

- Source edits to framework component `SKILL.md`, `guides/`, `templates/`,
  `version-history.md`, Makefile package lists, package-path exceptions,
  README/docs/AGENTS references, release notes, and project-management
  Expedited Mode wording when authorized by a slice.
- Semantic splitting of the two monolith guides into focused files, including
  route text, headings, introductions, and local link repairs needed to keep
  the framework just as usable and more selectively loadable.
- Semantic splitting of the remaining accepted framework component guide
  families into the operator-confirmed target files.
- Reconciliation of project-management's current `guides/09-worked-example-odm.md`
  against the accepted `examples/01-worked-example-odm.md` target.
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

Status: verified-closed.

Scope: update Expedited Mode wording in project-management source instructions,
update collaboration-framework `SKILL.md` routing text that mentions Expedited
Mode, move project-management `version-history.md` beside `SKILL.md`, repair
routes, document the framework component version-history management practice
for future sessions, and establish the version-history normalization pattern
for later slices.

### Slice 03: Collaboration-Framework Posture Guide Split

Status: verified-closed.

Scope: split `AI-CONSTITUTION-SUPPLEMENT.md` into the four approved numbered
collaboration-framework guides, update the collaboration-framework `SKILL.md`
route table and package list, and reconcile collaboration-framework version
history into `knowledge/collaboration-framework/version-history.md`.

### Slice 04: Engineering-Methods Guide Split

Status: verified-closed.

Scope: split `AI-ENGINEERING-METHODOLOGY.md` into the six accepted numbered
engineering-methods guides, update engineering-methods and framework routes,
and reconcile engineering-methods version history into
`knowledge/engineering-methods/version-history.md`.

### Slice 05: Remaining Framework Component Version-History Normalization

Status: verified-closed.

Scope: normalize sibling `version-history.md` files and embedded history
sections for `work-verification`, `testing`, `code-auditing`,
`agent-coordination`, and `contribution-style`, with route/link/package repairs.
This slice should feed the downstream guide-decomposition slices; it should not
perform those guide splits itself.

### Slice 06: Project-Management Example Layout Reconciliation

Status: verified-closed.

Scope: compare the current project-management guides against the accepted
architecture, especially the current `guides/09-worked-example-odm.md` route
versus the accepted `examples/01-worked-example-odm.md` target. Repair
`SKILL.md`, Makefile/package routes, public docs, local links, and release
notes as needed while preserving the eight numbered project-management guide
routes.

### Slice 07: Work-Verification Guide Split

Status: verified-closed.

Scope: split the ledger-discipline source into the accepted work-verification
guide set: `01-ledger-discipline.md`, `02-evidence-strength.md`,
`03-row-closure.md`, `04-silent-drop-checks.md`, and
`05-independent-verification.md`, while preserving
`templates/LEDGER-DISCIPLINE.md` as a package-local support asset if still
needed.

### Slice 08: Testing Guide Split

Status: verified-closed.

Scope: split testing guidance into `01-testing-discipline.md`,
`02-coverage-hardening.md`, and `03-validation-gates.md`, broadening the old
coverage prompt into testing-discipline routing without overclaiming future
TDD material.

### Slice 09: Code-Auditing Guide Split

Status: verified-closed.

Scope: split code-auditing guidance into `01-audit-scope-and-map.md`,
`02-findings-and-severity.md`, `03-scale-aware-auditing.md`,
`04-modernization-synthesis.md`, and `05-audit-to-hardening-handoff.md`,
preserving the diagnosis-only audit contract and severity/file-line output
discipline.

### Slice 10: Agent-Coordination Guide Split

Status: open.

Scope: split the old subagent delegation policy into
`01-when-to-delegate.md`, `02-context-packets.md`,
`03-result-integration.md`, and `04-anti-patterns.md`, with
`agent-coordination/SKILL.md` carrying the CC/CDC/operator terminology and
route-level coordination contract.

### Slice 11: Contribution-Style Guide Split

Status: planned after Slice10.

Scope: split contribution guidance into `01-contribution-style.md` and
`02-upstream-ticket-workflow.md`, while preserving
`templates/CONTRIBUTION-TICKET.md` as the package-local authoring template.

### Slice 12: Final Package, Install, Link, and Release Reconciliation

Status: planned after Slice11.

Scope: run final README/docs/AGENTS/SKILL/component link validation, package
validation, generated package inspection, isolated install smoke, CCDP package
disposition, and release-note reconciliation. Confirm the old monolith and
pre-split guide filenames are no longer the live load targets unless explicitly
retained as compatibility/provenance stubs or package-local templates.

## Dependencies

- Slice01 requires operator confirmation before Slice02 opens.
- Slice02 must land before decomposition source slices so Expedited Mode no
  longer reinforces shortcut or timeline interpretations.
- Slice03 and Slice04 must preserve source meaning while improving selective
  loadability.
- Slice05 depends on the version-history pattern established in Slice02 and
  the component-specific histories created in Slices03-04.
- Slice06 depends on Slice05 and the accepted Project02 project-management
  layout.
- Slices07-11 depend on Slice05's sibling version-history normalization and the
  operator-confirmed remaining component guide map.
- Slice12 depends on all source splits and version-history normalization.

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

### v1.2 - 2026-09-04

Recorded operator approval of the Slice01 confirmation packet with two
clarifications: the framework component version-history management practice
needs durable documentation for future sessions, expected in top-level
`AGENTS.md`, and Expedited Mode should explicitly mean no inferred source scope
and no reduction or other change in scope. Opened Slice02 against those
clarifications.

### v1.3 - 2026-09-04

Closed Slice02 after CDC verification. Slice02 delivered the process/history
baseline: corrected Expedited Mode wording, moved project-management
version-history to the sibling component path, repaired package routes, and
documented framework component version-history management in top-level
`AGENTS.md`. Opened Slice03 for the collaboration-framework posture guide
split.

### v1.4 - 2026-09-04

Closed Slice03 after CDC verification. Slice03 split the collaboration-framework
posture monolith into the four approved numbered guides, normalized
collaboration-framework history into sibling `version-history.md`, repaired
live routes, and confirmed the generated collaboration-framework package no
longer contains the old supplement path. Opened Slice04 for the
engineering-methods guide split.

### v1.5 - 2026-09-04

Closed Slice04 after CDC verification. Slice04 split the engineering-methods
monolith into six accepted numbered guides, normalized engineering-methods
history into sibling `version-history.md`, repaired live routes, and confirmed
the generated collaboration-framework package no longer contains the old
methodology path.

Opened Slice05 for the already-approved remaining framework component
version-history normalization. Operator review also surfaced broader
component-guide decomposition proposals from the project-level component layout
plan, including an agent-coordination delegation-policy split; those are
recorded as a deferred re-entry surface, not inferred Slice05 source scope.

### v1.6 - 2026-09-04

Integrated the operator's remaining accepted component guide layout into
Arc08 rather than opening a new arc. Added downstream slices for
project-management example layout reconciliation, work-verification guide
split, testing guide split, code-auditing guide split, agent-coordination guide
split, contribution-style guide split, and final package/install/release
reconciliation. Slice05 remains scoped to version-history normalization and
feeds the later guide-decomposition slices instead of performing them.

### v1.7 - 2026-09-04

Closed Slice05 after CDC verification. Slice05 normalized the five remaining
framework component histories into sibling `version-history.md` files, moved
or reconciled embedded histories from work-verification and code-auditing,
updated component entrypoints and the collaboration-framework package list,
and confirmed the generated collaboration-framework package contains 61
entries with no guide/template-local component history files.

Opened Slice06 for project-management guide/example layout reconciliation.
This supersedes the original Slice05 close-report bubble-up that named final
package reconciliation as Slice06; final reconciliation is now Slice12 after
the operator-expanded Arc08 guide split sequence.

### v1.8 - 2026-09-04

Closed Slice06 after CDC verification. Slice06 moved the project-management
worked example from the numbered guide surface to the accepted
`examples/01-worked-example-odm.md` path, preserved the eight numbered
project-management guides and wayfinder, repaired package routes, and
confirmed the generated collaboration-framework package contains 62 entries
with the accepted example path.

Opened Slice07 for the work-verification guide split.

### v1.9 - 2026-09-04

Closed Slice07 after CDC verification. Slice07 split the work-verification
component into five selective-load guides, preserved
`templates/LEDGER-DISCIPLINE.md` as the retained full protocol and copyable
ledger-table support asset, repaired framework/project-management/
engineering-methods routes, and confirmed the generated collaboration-framework
package contains 68 entries with the five work-verification guides and retained
template.

Opened Slice08 for the testing guide split.

### v1.10 - 2026-09-04

Closed Slice08 after CDC verification. Slice08 split the testing component into
three selective-load guides, preserved the old `CODE-COVERAGE.md` file history
by renaming it to `02-coverage-hardening.md`, repaired framework and
engineering-methods routes, and confirmed the generated collaboration-framework
package contains 70 entries with the three testing guides and no old
`CODE-COVERAGE.md` package path.

Opened Slice09 for the code-auditing guide split.

### v1.11 - 2026-09-05

Closed Slice09 after CDC verification. Slice09 split code-auditing into five
accepted numbered guides, removed `CODE-AUDIT.md` as a live route, repaired
framework/component/docs/package/release references, and confirmed the
generated collaboration-framework package contains 74 entries with all five
code-auditing guides and no old `CODE-AUDIT.md` package path.

Opened Slice10 for the agent-coordination guide split.
