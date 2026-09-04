# Arc 07 Closing Report: Knowledge Component Entrypoints and Guide Layout

Status: closed.

## Capability

Arc07 resolved the post-move cleanup surfaced by operator review after Arc06:
framework component material no longer keeps stale `docs/` holdovers after
moving into `knowledge/`, component roots have concise `SKILL.md` wayfinders,
and package/install behavior remains valid.

Composition verdict: delivered.

## Slice Walk

| Slice | Outcome | Evidence |
| --- | --- | --- |
| Slice01: Component Entrypoint Contract and Migration Map | Delivered | `slice01-component-entrypoint-contract/cdc-verification.md` verified the component layout inventory, entrypoint/guide/template decisions, migration impact map, validation command inventory, and implementation roadmap. |
| Slice02: Collaboration Framework Entrypoint Relocation | Delivered | `slice02-collaboration-framework-entrypoint-relocation/cdc-verification.md` verified the move of the collaboration-framework source entrypoint to `knowledge/collaboration-framework/SKILL.md` while preserving the package-root `collaboration-framework/SKILL.md` entrypoint. |
| Slice03: Component Guide Layout and Standalone Entrypoints | Delivered | `slice03-component-guide-layout/cdc-verification.md` verified component `SKILL.md` wayfinders, guide layout, removal of stale component `docs/` holdovers, project-management guide migration, package/list repairs, and package inspection. |
| Slice04: Reconciliation, Package Validation, and Release Notes | Delivered | `slice04-reconciliation-package-validation/cdc-verification.md` verified README/docs links, skill/package/install validation, package-path checks, release-note reconciliation, and CCDP package validation after CDC's date-only assembled-protocol refresh. |

## Composition Check

Arc07's slices compose into the promised capability:

- `knowledge/collaboration-framework/SKILL.md` is the source entrypoint for the
  collaboration-framework composer.
- Framework component roots have concise `SKILL.md` wayfinders.
- Long component material lives under `guides/` or `templates/` as appropriate.
- Legacy tracked component `docs/` holdovers and `docs/pm` paths were removed
  or migrated.
- `collaboration-framework.zip` still exposes `collaboration-framework/SKILL.md`
  as its root entrypoint and includes the accepted component wayfinders, guides,
  and templates.
- Package and install validation remain green, with CCDP preserved as a
  separate protocol package rather than an installable skill.
- Release notes were reconciled under
  `workbench/release-notes/RELEASE-0.5.0.md`.

No Arc07 scope item is known to have been silently dropped.

## Accumulated Arc-Plan Change Log

Arc07 received four tracked arc-plan updates:

- v1.1 closed Slice01 and accepted the component entrypoint contract.
- v1.2 closed Slice02 and surfaced the Slice03 source-reference repairs.
- v1.3 closed Slice03 and opened final reconciliation/release-note validation.
- v1.4 closed Slice04 after CDC verification and recorded the CDC CCDP
  date-only freshness repair.

## Bubble-Up to Project04

Arc07 delivered project ledger row P-8: accepted knowledge component
entrypoints, removal/disposition of stale component `docs/` holdovers,
project-management guide migration, and package/install reconciliation.

Operator review after Arc07 surfaced one remaining project-level gap: the
accepted framework guide split and sibling component `version-history.md`
contract were recorded in project-level support artifacts but not yet
implemented. Project04 therefore needs a follow-on arc that:

- tightens Expedited Mode wording so it only means the explicit process changes
  listed, not shortcuts, weaker evidence, inferred scope changes, or timeline
  compression;
- directly uses `artifacts/operator-accepted-architecture.md` and
  `artifacts/component-file-layout-plan.md` as support for the split;
- splits the collaboration-framework and engineering-methods monolith guides
  into the approved focused guide files;
- normalizes framework component version history into sibling
  `version-history.md` files beside each component `SKILL.md`; and
- verifies at arc close that selective loading/access is improved without
  losing framework usability, meaning, or package integrity.

Project04 should open Arc08 for this work before project-level acceptance.
