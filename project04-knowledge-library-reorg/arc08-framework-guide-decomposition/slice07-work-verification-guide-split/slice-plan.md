# Slice 07: Work-Verification Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice07-work-verification-guide-split
status: verified-closed
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: authorized
operating-mode: expedited
artifact_home: artifacts/
depends-on: slice06-project-management-example-layout-reconciliation/cdc-verification.md
```

## Goal

Split the current work-verification ledger-discipline material into the five
accepted numbered guides while preserving the full verification protocol,
package behavior, and sibling component version-history rule.

## Scope

In scope:

- Split or extract focused guide material from
  `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md` into:
  - `knowledge/work-verification/guides/01-ledger-discipline.md`
  - `knowledge/work-verification/guides/02-evidence-strength.md`
  - `knowledge/work-verification/guides/03-row-closure.md`
  - `knowledge/work-verification/guides/04-silent-drop-checks.md`
  - `knowledge/work-verification/guides/05-independent-verification.md`
- Preserve `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md` as a
  package-local support/template asset if it still carries useful complete
  protocol or copyable table material.
- Preserve the semantic substance of the current protocol while making the new
  guides independently loadable.
- Update `knowledge/work-verification/SKILL.md` to route to the new guides and
  retained template.
- Update `knowledge/work-verification/version-history.md` for the component
  change.
- Update collaboration-framework routes, project-management references,
  engineering-methods references, public docs, AGENTS, release notes, Makefile
  `CF_FILES`, package-path exceptions, and staging scripts when affected.
- Use explicit `git mv` path pairs for any source moves, and use `rmdir` as a
  precaution only if an empty directory must be removed.
- Create Slice07 planning evidence artifacts under `artifacts/` and close the
  slice with explicit source and planning commits.

Out of scope:

- Changing project-management layout beyond direct link repair.
- Splitting testing, code-auditing, agent-coordination, or contribution-style
  guide bodies; those belong to later Arc08 slices.
- Changing the evidence-strength vocabulary except where needed to preserve
  current meaning in the new guide structure.
- Reopening the sibling version-history rule.
- Committing generated zips, `build/`, or `target/skills`.

## Support Inputs

- `../slice06-project-management-example-layout-reconciliation/cdc-verification.md`
- `../slice05-component-version-history-normalization/cdc-verification.md`
- `../../artifacts/operator-accepted-architecture.md`
- `../../artifacts/component-file-layout-plan.md`
- Arc08 `arc-plan.md` and `ledger.md`
- Project04 `project-plan.md` and `ledger.md`

## Expected Artifacts

- `artifacts/current-work-verification-surface-map.md`
- `artifacts/work-verification-split-map.md`
- `artifacts/template-retention-disposition.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/source-validation-results.md`

## Verification Approach

CC should inspect the current work-verification entrypoint, template, and
sibling history before editing. The split should make common lookup paths
faster: ledger format and invariant spine, evidence strength, row closure,
silent-drop checks, and independent verification should each be reachable
without loading the whole template asset.

If `templates/LEDGER-DISCIPLINE.md` remains as a full protocol or copyable
support asset, record why it remains and how it relates to the new guides. If
it is narrowed, record what moved and how semantic preservation was checked.

Validation must cover local links, package paths, generated
collaboration-framework package shape, and absence or explicit disposition of
old live routes. Treat Expedited Mode as only the explicit process behavior
recorded in Arc08; do not infer source scope, reduce scope, skip checks,
weaken evidence, change review quality, or bypass approval gates.

## Exit Criteria

- The five accepted numbered work-verification guides exist.
- The split preserves the ledger protocol's semantic substance and makes the
  new guides independently loadable.
- `templates/LEDGER-DISCIPLINE.md` is retained as an explicitly dispositioned
  support/template asset or narrowed with a recorded semantic-preservation
  rationale.
- `knowledge/work-verification/SKILL.md` routes to the new guide set and any
  retained template.
- `knowledge/work-verification/version-history.md` records the component
  change.
- README/docs/AGENTS/SKILL/component/release-note references affected by the
  split are repaired or explicitly dispositioned.
- `make check-skills`, `make collab-framework`, and `make check-package-paths`
  pass with zero hard failures.
- Generated `collaboration-framework.zip` contains the five numbered
  work-verification guides, retains or omits `templates/LEDGER-DISCIPLINE.md`
  according to the recorded disposition, and has no stale live route to a
  replaced source path.
- Source and planning commits are created with explicit file lists and both
  required co-author trailers.

## CDC Closure

Slice07 was CDC-verified closed on 2026-09-04.

Verified source commit:

- `2a092d76090387a12e34d08e895084ee5389dbb2`

Verified planning commits:

- `b71f07916184344fd529cb3f8c07755938e074f5`
- `fa31b01ca8537ede9cbe23e51e7cc4e3254ad16d`

Closure evidence:

- `cdc-verification.md`
