# Slice 08: Testing Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice08-testing-guide-split
status: open
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: authorized
operating-mode: expedited
artifact_home: artifacts/
depends-on: slice07-work-verification-guide-split/cdc-verification.md
```

## Goal

Split the current testing coverage prompt into the three accepted numbered
guides while preserving the hard coverage-quality floor and making testing,
coverage hardening, and validation gates separately loadable.

## Scope

In scope:

- Split or extract focused guide material from
  `knowledge/testing/guides/CODE-COVERAGE.md` into:
  - `knowledge/testing/guides/01-testing-discipline.md`
  - `knowledge/testing/guides/02-coverage-hardening.md`
  - `knowledge/testing/guides/03-validation-gates.md`
- Use an explicit `git mv` for the old coverage prompt if it becomes one of
  the new accepted guide files.
- Preserve the semantic substance of the current coverage prompt: hard coverage
  threshold discipline, warnings/lint/format pressure, root-cause repair,
  anti-patterns, systematic coverage work, progress reporting, and adaptation
  from Rust/Cargo examples to the active repository's own tools.
- Broaden routing from "code coverage only" to testing discipline, coverage
  hardening, and validation gates without overclaiming future TDD material.
- Remove the old `knowledge/testing/guides/CODE-COVERAGE.md` path as a live
  route unless an explicit evidence-backed support-asset disposition is
  recorded.
- Update `knowledge/testing/SKILL.md` to route to the new guide set.
- Update `knowledge/testing/version-history.md` for the component change.
- Update collaboration-framework routes, work-verification references,
  engineering-methods references, project-management references, public docs,
  AGENTS, release notes, Makefile `CF_FILES`, package-path exceptions, and
  staging scripts when affected.
- Use explicit `git mv` path pairs for source moves. If an empty directory
  must be removed, use `rmdir` as a precaution only.
- Create Slice08 planning evidence artifacts under `artifacts/` and close the
  slice with explicit source and planning commits.

Out of scope:

- Splitting code-auditing, agent-coordination, or contribution-style guide
  bodies; those belong to later Arc08 slices.
- Changing test policy beyond what is needed to preserve and route the current
  coverage/testing discipline in the new guide structure.
- Adding a new TDD method, CI system, coverage tool, runtime harness, or
  package target not already required by existing package validation.
- Reopening the sibling version-history rule.
- Committing generated zips, `build/`, or `target/skills`.

## Support Inputs

- `../slice07-work-verification-guide-split/cdc-verification.md`
- `../slice06-project-management-example-layout-reconciliation/cdc-verification.md`
- `../../artifacts/operator-accepted-architecture.md`
- `../../artifacts/component-file-layout-plan.md`
- Arc08 `arc-plan.md` and `ledger.md`
- Project04 `project-plan.md` and `ledger.md`

## Expected Artifacts

- `artifacts/current-testing-surface-map.md`
- `artifacts/testing-split-map.md`
- `artifacts/legacy-code-coverage-disposition.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/source-validation-results.md`

## Verification Approach

CC should inspect the current testing entrypoint, `CODE-COVERAGE.md`, sibling
history, route references, and package list before editing. The split should
make common lookup paths faster: general testing discipline, coverage
hardening, and validation gates should each be reachable without loading the
whole old coverage prompt.

Record how `CODE-COVERAGE.md` was handled. If it is moved to
`02-coverage-hardening.md`, record that as a rename with semantic extraction
into the companion guides. If any copy of the old file is retained, record why
it remains support material rather than a stale live route.

Validation must cover local links, package paths, generated
collaboration-framework package shape, and absence or explicit disposition of
the old `CODE-COVERAGE.md` live route. Treat Expedited Mode as only the
explicit process behavior recorded in Arc08; do not infer source scope, reduce
scope, skip checks, weaken evidence, change review quality, or bypass approval
gates.

## Exit Criteria

- The three accepted numbered testing guides exist.
- The split preserves the current testing/coverage discipline and makes the new
  guides independently loadable.
- `knowledge/testing/guides/CODE-COVERAGE.md` is removed as a live route,
  renamed into an accepted guide, or retained only with explicit support-asset
  disposition.
- `knowledge/testing/SKILL.md` routes to the new guide set.
- `knowledge/testing/version-history.md` records the component change.
- README/docs/AGENTS/SKILL/component/release-note references affected by the
  split are repaired or explicitly dispositioned.
- `make check-skills`, `make collab-framework`, and `make check-package-paths`
  pass with zero hard failures.
- Generated `collaboration-framework.zip` contains the three numbered testing
  guides and follows the recorded legacy `CODE-COVERAGE.md` disposition.
- Source and planning commits are created with explicit file lists and both
  required co-author trailers.
