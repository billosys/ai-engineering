# Slice 01: Decision Surface Inventory

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice01-decision-surface-inventory
status: open
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
artifact-home: artifacts/
operating-mode: expedited
```

## Goal

Produce the Arc02 decision surface from Arc01 close evidence. The slice should
make the decisions, options, compatibility obligations, authority levels, and
re-entry conditions explicit enough that Slice02 can select an accepted
directory/source/package contract without rediscovering Arc01.

## Inputs

- `../arc-plan.md` and `../ledger.md`.
- `../../arc01-material-inventory/closing-report.md`.
- `../../arc01-material-inventory/slice04-arc01-synthesis/artifacts/arc02-readiness-packet.md`.
- `../../arc01-material-inventory/slice04-arc01-synthesis/artifacts/directory-contract-requirements.md`.
- `../../arc01-material-inventory/slice04-arc01-synthesis/artifacts/arc01-synthesis-decision-register.md`.
- Earlier Arc01 artifacts as needed for source-backed detail beneath the
  synthesis.

## In Scope

- Create `artifacts/target-contract-decision-surface.md`, grouping the Arc01
  decision rows into Arc02 decision areas.
- Create `artifacts/source-root-option-matrix.md`, comparing viable source-root
  and package-root options for `docs/`, `knowledge/`, framework components,
  method skills, protocols, templates, Biome-style multi-entrypoint roots, and
  top-level compatibility surfaces.
- Create `artifacts/compatibility-obligation-inventory.md`, listing the
  validation commands, package/list surfaces, link responsibilities, wrapper or
  migration-note needs, and re-entry conditions for later slices.
- Preserve authority labels: accepted fact, working hypothesis, operator
  decision required, planned surface, not live source, source-edit risk, and
  re-entry condition.
- Keep skill kind and topology independent in all classification language.

## Out of Scope

- Selecting the final target directory contract.
- Moving, deleting, renaming, or editing source checkout files.
- Editing source `README.md`, source `SKILL.md`, `docs/`, `knowledge/`,
  `templates/`, `protocols/`, `Makefile`, package-path exceptions, generated
  zips, or package contents.
- Writing final public docs or Arc05 public vocabulary.
- Treating Project02 implementation hypotheses or Project03 planned surfaces
  as accepted Project04 source layout.

## Artifacts

Durable artifacts live under this slice's `artifacts/` directory:

- `artifacts/target-contract-decision-surface.md`
- `artifacts/source-root-option-matrix.md`
- `artifacts/compatibility-obligation-inventory.md`

## Verification Approach

The slice ledger uses grep-verifiable rows against the three artifacts, the
closing report, and source-checkout status. CC should run every Verify command
before reporting proposed-done. CDC will independently rerun them before
marking the slice verified-closed.

## Exit Criteria

- All three artifacts exist under `artifacts/`.
- The decision surface covers Arc01's decision rows and required surface
  families.
- The option matrix separates source roots from package roots and includes
  current edge cases.
- The compatibility inventory names validation commands, compatibility files,
  package lists, package-local links, exceptions, and re-entry conditions.
- Authority levels remain explicit and no source-edit authorization is implied.
- The source checkout remains untouched.

## Expedited Mode

CC must commit the proposed-done slice packet after his changes using explicit
file paths. CDC will then review, verify, update parent status, commit CDC
changes, and open the next slice immediately if this slice closes.
