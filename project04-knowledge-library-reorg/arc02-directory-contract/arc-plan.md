# Arc 02: Target Directory Contract and Migration Plan

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
status: active
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
operating-mode: expedited
```

## Capability

Arc02 defines the accepted target directory contract and migration plan for
Project04. It decides how `docs/`, `knowledge/`, `templates/`, `protocols/`,
`README.md`, `SKILL.md`, source roots, package roots, compatibility surfaces,
package-path exceptions, and validation gates should relate before any source
file moves begin.

The arc consumes Arc01's source-backed inventory, imported-architecture
integration, skill kind/topology classification, and Arc02 readiness synthesis.
It must preserve the distinction between accepted facts, working hypotheses,
operator decisions, source-edit risks, validation obligations, and re-entry
conditions.

## Inputs

- Project04 `project-plan.md` and project `ledger.md`.
- Arc01 close: `arc01-material-inventory/closing-report.md`.
- Arc01 Slice04 artifacts:
  - `arc01-material-inventory/slice04-arc01-synthesis/artifacts/arc02-readiness-packet.md`
  - `arc01-material-inventory/slice04-arc01-synthesis/artifacts/directory-contract-requirements.md`
  - `arc01-material-inventory/slice04-arc01-synthesis/artifacts/arc01-synthesis-decision-register.md`
- Arc01 Slice01-Slice03 artifacts when the Arc02 work needs source-backed
  detail beneath the synthesis.
- Source checkout at `/Users/oubiwann/lab/billosys/ai-engineering`, read-only
  unless a later implementation arc explicitly authorizes edits.

## Boundaries

In scope:

- A target directory contract for `docs/` as end-user explanation and
  `knowledge/` as raw and derived knowledge-library substrate, including
  explicit exceptions.
- A source-root and package-root contract for current domain/tooling skills,
  planned Project02 framework/operational components, planned Project03 method
  skill surfaces, Biome-style multi-entrypoint roots, templates, and CCDP.
- A compatibility strategy covering README routes, `SKILL.md`, `AGENTS.md`,
  `CLAUDE.md`, Makefile lists/targets, package-path exceptions, package-local
  links, old paths, wrapper docs, and migration notes.
- A migration sequence and validation matrix that later implementation slices
  can execute without mixing mechanical moves with public prose rewrites.
- Explicit operator-decision points where multiple viable contracts remain.

Out of scope:

- Moving, deleting, or renaming source files.
- Editing source `README.md`, source `SKILL.md`, `docs/`, `knowledge/`,
  `templates/`, `protocols/`, `Makefile`, package-path exceptions, generated
  zips, or package contents.
- Writing final end-user documentation.
- Treating Arc02 planning artifacts as public taxonomy or implementation
  authorization.
- Re-opening Project02, Project03, or CCDP policy unless an Arc02 re-entry row
  proves the accepted facts cannot be preserved.

## Expedited Mode

Project04 is operating in Expedited Mode as of 2026-09-02.

- CC prompts must instruct CC to commit after his changes, before CDC review,
  using explicit file lists for both `git add` and `git commit -- <paths>`.
- CDC commits after CDC review or planning changes and reports the result to
  the operator.
- When evidence is in place for a full slice close, close the slice rather than
  leaving it proposed-done.
- After a slice closes, open the next slice immediately and report the
  `cc-prompt.md` path relative to the project directory.
- After the last slice in an arc closes, continue to arc close, then open the
  next roadmap-provided arc and first slice.

## Slice Breakdown

### Slice 01: Decision Surface Inventory

Status: verified-closed on 2026-09-02.

Scope: convert Arc01 close evidence and Slice04 synthesis artifacts into the
Arc02 decision surface. Produce a target-contract decision surface, a
source-root option matrix, and a compatibility-obligation inventory. This
slice does not select the final contract.

Expected artifacts:

- `slice01-decision-surface-inventory/artifacts/target-contract-decision-surface.md`
- `slice01-decision-surface-inventory/artifacts/source-root-option-matrix.md`
- `slice01-decision-surface-inventory/artifacts/compatibility-obligation-inventory.md`

### Slice 02: Accepted Directory and Root Contract

Status: open.

Scope: turn Slice01's decision surface into an accepted directory contract and
source/package root contract. Decide what remains in `docs/`, what moves under
`knowledge/`, what remains under `protocols/`, how templates are owned, and
how source roots relate to package roots.

Expected artifacts:

- `slice02-accepted-directory-contract/artifacts/accepted-target-directory-contract.md`
- `slice02-accepted-directory-contract/artifacts/source-package-root-contract.md`
- `slice02-accepted-directory-contract/artifacts/operator-decision-register.md`

### Slice 03: Migration Sequence and Validation Plan

Status: not open.

Scope: define the implementation sequence, compatibility strategy, wrapper or
migration-note policy, package-path exception policy, and validation matrix
for the accepted contract.

Expected artifacts:

- `slice03-migration-validation-plan/artifacts/migration-sequence-plan.md`
- `slice03-migration-validation-plan/artifacts/validation-and-compatibility-matrix.md`
- `slice03-migration-validation-plan/artifacts/package-path-exception-policy.md`

### Slice 04: Arc02 Implementation Handoff

Status: not open.

Scope: synthesize the accepted contract and migration plan into an Arc03
implementation readiness packet with ordered source-edit slices, validation
gates, risks, and re-entry conditions.

Expected artifacts:

- `slice04-implementation-handoff/artifacts/arc03-readiness-packet.md`
- `slice04-implementation-handoff/artifacts/source-edit-slice-roadmap.md`
- `slice04-implementation-handoff/artifacts/arc02-decision-summary.md`

## Dependencies

- Slice01 must close before Slice02 because the accepted contract needs a full
  decision surface and compatibility inventory.
- Slice02 must close before Slice03 because migration sequencing depends on the
  accepted target contract.
- Slice03 must close before Slice04 because the Arc03 handoff must carry
  validation gates and implementation order.
- Arc03 must not open until Slice04 closes and Arc02 closes formally, unless
  the operator explicitly accepts a narrower implementation input set.

## Version History

### v1.0 - 2026-09-02

Opened Arc02 for the Project04 target directory contract and migration plan.
Recorded Expedited Mode, planned four slices, and opened Slice01,
`slice01-decision-surface-inventory`, to convert Arc01 close evidence into the
Arc02 decision surface.

### v1.1 - 2026-09-02

Recorded Slice01 as verified-closed. No Arc02 slice-breakdown change was
required; opened Slice02, `slice02-accepted-directory-contract`, to select the
accepted target directory contract and source/package root contract from the
verified decision surface.
