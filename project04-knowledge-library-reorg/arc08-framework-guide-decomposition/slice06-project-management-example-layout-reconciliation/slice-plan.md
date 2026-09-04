# Slice 06: Project-Management Example Layout Reconciliation

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice06-project-management-example-layout-reconciliation
status: verified-closed
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: authorized
operating-mode: expedited
artifact_home: artifacts/
depends-on: slice05-component-version-history-normalization/cdc-verification.md
```

## Goal

Reconcile the current project-management component layout against the
operator-accepted architecture, especially the current worked-example guide
route versus the accepted `examples/01-worked-example-odm.md` target, while
preserving the eight numbered project-management guide routes.

## Scope

In scope:

- Compare the current `knowledge/project-management/` source tree with the
  accepted architecture in:
  - `../../artifacts/operator-accepted-architecture.md`
  - `../../artifacts/component-file-layout-plan.md`
- Decide and implement the accepted disposition for
  `knowledge/project-management/guides/09-worked-example-odm.md`, with the
  expected target:
  - `knowledge/project-management/examples/01-worked-example-odm.md`
- Preserve the current eight numbered project-management guides:
  - `01-scales-of-work.md`
  - `02-canonical-planning-worktree.md`
  - `03-planning-top-down.md`
  - `04-closing-slices.md`
  - `05-closing-arcs.md`
  - `06-confirmation-protocol.md`
  - `07-anti-patterns.md`
  - `08-maintenance.md`
- Keep `knowledge/project-management/guides/PROJECT-MANAGEMENT.md` as the
  wayfinder unless source evidence requires a separately recorded decision.
- Update project-management `SKILL.md`, `version-history.md`, Makefile
  `CF_FILES`, collaboration-framework routes, public docs, AGENTS, release
  notes, staging scripts, and package-path exceptions when affected.
- Use explicit `git mv` path pairs for any source move, and use `rmdir` as a
  precaution only if an empty directory must be removed.
- Create Slice06 planning evidence artifacts under `artifacts/` and close the
  slice with explicit source and planning commits.

Out of scope:

- Splitting or rewriting the eight project-management numbered guides.
- Splitting work-verification, testing, code-auditing, agent-coordination, or
  contribution-style guide bodies; those belong to later Arc08 slices.
- Changing Expedited Mode wording except for direct route/link repair required
  by this slice.
- Changing project-management planning mechanics beyond the accepted
  example-layout reconciliation.
- Committing generated zips, `build/`, or `target/skills`.

## Support Inputs

- `../slice05-component-version-history-normalization/cdc-verification.md`
- `../slice05-component-version-history-normalization/artifacts/deferred-guide-decomposition-register.md`
- `../../artifacts/operator-accepted-architecture.md`
- `../../artifacts/component-file-layout-plan.md`
- Arc08 `arc-plan.md` and `ledger.md`
- Project04 `project-plan.md` and `ledger.md`

## Expected Artifacts

- `artifacts/current-project-management-layout-map.md`
- `artifacts/accepted-layout-delta-map.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/source-validation-results.md`

## Verification Approach

CC should inspect the current project-management tree before editing, then
compare it to the accepted target. If the worked example can move cleanly to
`examples/01-worked-example-odm.md`, use `git mv` and repair all local links
and package routes. If source evidence shows the accepted target should be
adjusted, record the contradiction and proposed disposition before applying a
narrow repair.

Validation must cover local links, project-management package routes inside
`collaboration-framework.zip`, skill-description limits, and package-path hard
failures. Treat Expedited Mode as only the explicit process behavior recorded
in Arc08; do not infer source scope, reduce scope, skip checks, weaken
evidence, change review quality, or bypass approval gates.

## Exit Criteria

- Current project-management layout is compared against the accepted
  architecture.
- `guides/09-worked-example-odm.md` is moved to
  `examples/01-worked-example-odm.md`, or an explicit exception/disposition is
  recorded with evidence.
- The eight numbered project-management guides remain intact.
- Project-management `SKILL.md`, `version-history.md`, Makefile/package routes,
  public docs, AGENTS, release notes, and collaboration-framework route
  surfaces are repaired or explicitly dispositioned.
- `make check-skills`, `make collab-framework`, and `make check-package-paths`
  pass with zero hard failures.
- Generated `collaboration-framework.zip` contains the accepted
  project-management example path and does not expose the old worked-example
  guide path as a live route unless explicitly retained.
- Source and planning commits are created with explicit file lists and both
  required co-author trailers.

## CDC Closure

Slice06 was CDC-verified closed on 2026-09-04.

Verified source commit:

- `df2c33e0d882aa89dbd42da3b87737a822903979`

Verified planning commits:

- `96d41b25b6c16f0559eedcc9adf8135fd9828b3f`
- `75c0801ca2fc3404274878f82ec109044ba90119`

Closure evidence:

- `cdc-verification.md`
