# Slice 05: Component Version-History Normalization

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice05-component-version-history-normalization
status: verified-closed
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: authorized
operating-mode: expedited
artifact_home: artifacts/
depends-on: slice04-engineering-methods-guide-split/cdc-verification.md
```

## Goal

Normalize the remaining framework component version histories so each component
root carries one version in `SKILL.md` and one sibling `version-history.md`,
without silently expanding this slice into the broader component guide-splitting
work.

## Scope

In scope:

- Inventory version-history surfaces for:
  - `knowledge/work-verification/`
  - `knowledge/testing/`
  - `knowledge/code-auditing/`
  - `knowledge/agent-coordination/`
  - `knowledge/contribution-style/`
- Create or update sibling `version-history.md` files for those five component
  roots.
- Move, reconcile, or explicitly disposition embedded `## Version History`
  sections from component `SKILL.md`, guide files, templates, or examples.
- Update each affected component `SKILL.md` so its version/history route is
  coherent with the sibling-history rule.
- Repair source routes in collaboration-framework, public docs, AGENTS,
  release notes, Makefile package lists, package-path exceptions, or staging
  scripts when affected by the history normalization.
- Preserve the Slice02 Expedited Mode guardrails and the Slice03/Slice04 split
  guide routes.
- Record the broader component guide-decomposition proposals from
  `../../artifacts/component-file-layout-plan.md` as deferred re-entry items
  for operator review.
- Create Slice05 planning evidence artifacts under `artifacts/` and close the
  slice with explicit source and planning commits.

Out of scope:

- Splitting `knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md`
  into multiple focused guides.
- Splitting `knowledge/code-auditing/guides/CODE-AUDIT.md`,
  `knowledge/testing/guides/CODE-COVERAGE.md`,
  `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`, or
  `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md` into multiple
  guides.
- Renaming guide files except where a version-history file itself must move to
  the sibling component-root location.
- Changing the approved public skill kind/topology vocabulary.
- Committing generated zips, `build/`, or `target/skills`.

## Support Inputs

- `../slice01-split-map-version-history-confirmation/artifacts/operator-confirmation-packet.md`
- `../slice02-project-management-process-history/cdc-verification.md`
- `../slice03-collaboration-framework-posture-split/cdc-verification.md`
- `../slice04-engineering-methods-guide-split/cdc-verification.md`
- `../../artifacts/operator-accepted-architecture.md`
- `../../artifacts/component-file-layout-plan.md`
- Arc08 `arc-plan.md` and `ledger.md`

## Expected Artifacts

- `artifacts/current-remaining-history-surface-map.md`
- `artifacts/version-history-normalization-map.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/deferred-guide-decomposition-register.md`
- `artifacts/source-validation-results.md`

## Verification Approach

CC should inspect the five remaining component roots before editing. For each
component, distinguish between:

- an existing embedded history that must be moved or reconciled;
- no existing history, where the sibling file should be seeded from current
  component lineage and this slice's change;
- a guide/template history reference that should become a pointer to the
  sibling component history; and
- broader guide-splitting proposals that should be captured for later operator
  confirmation, not implemented here.

Validation must cover local links, package paths, generated
collaboration-framework package shape, and absence of newly created
guide-local component histories. Treat Expedited Mode as only the explicit
process behavior recorded in Arc08; do not infer source scope, reduce scope,
skip checks, weaken evidence, change review quality, or bypass approval gates.

## Exit Criteria

- The five remaining framework component roots have sibling
  `version-history.md` files or an explicitly recorded exception.
- Embedded component `## Version History` sections have been moved,
  reconciled, or explicitly dispositioned.
- No component version-history file remains under `guides/` merely because a
  guide was edited.
- Component `SKILL.md` files and route surfaces identify the sibling component
  history where appropriate.
- Makefile/package routes include any new sibling history files that belong in
  the collaboration-framework package.
- README/docs/AGENTS/SKILL/release-note references affected by the
  normalization are repaired or explicitly dispositioned.
- Broader component guide-decomposition proposals are captured in a deferred
  register for later operator confirmation.
- `make check-skills`, `make collab-framework`, and `make check-package-paths`
  pass with zero hard failures.
- Generated `collaboration-framework.zip` contains the expected sibling
  version-history files and no guide-local component history files created by
  this slice.
- Source and planning commits are created with explicit file lists and both
  required co-author trailers.

## CDC Closure

Slice05 was CDC-verified closed on 2026-09-04.

Verified source commit:

- `657f156c7ad8048e60727275c2eed0d910de7f45`

Verified planning commits:

- `a494e6838401e6fcd8f88f734f27dc4d5043487c`
- `15e04fd8e8d1de48e5e219c2acce430d9092e751`

Closure evidence:

- `cdc-verification.md`
