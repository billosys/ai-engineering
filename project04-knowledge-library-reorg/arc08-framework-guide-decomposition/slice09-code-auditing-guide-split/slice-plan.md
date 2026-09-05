# Slice 09: Code-Auditing Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice09-code-auditing-guide-split
status: open
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: authorized
operating-mode: expedited
artifact_home: artifacts/
depends-on: slice08-testing-guide-split/cdc-verification.md
```

## Goal

Split the current code-auditing guide into the five accepted numbered guides
while preserving the diagnosis-only audit contract, evidence map, severity
discipline, file-line finding format, and modernization handoff.

## Scope

In scope:

- Split or extract focused guide material from
  `knowledge/code-auditing/guides/CODE-AUDIT.md` into:
  - `knowledge/code-auditing/guides/01-audit-scope-and-map.md`
  - `knowledge/code-auditing/guides/02-findings-and-severity.md`
  - `knowledge/code-auditing/guides/03-scale-aware-auditing.md`
  - `knowledge/code-auditing/guides/04-modernization-synthesis.md`
  - `knowledge/code-auditing/guides/05-audit-to-hardening-handoff.md`
- Use an explicit `git mv` for the old audit guide if it becomes one of the
  new accepted guide files.
- Preserve the semantic substance of the current audit guide: diagnosis-only
  audit posture, language/tool detection, audit map construction, all-scale
  review, severity classes, finding format with file:line evidence, per-language
  reports, top-level index, modernization synthesis, negative findings, and
  final verification checklist.
- Remove the old `knowledge/code-auditing/guides/CODE-AUDIT.md` path as a live
  route unless an explicit evidence-backed support-asset disposition is
  recorded.
- Update `knowledge/code-auditing/SKILL.md` to route to the new guide set.
- Update `knowledge/code-auditing/version-history.md` for the component change.
- Update collaboration-framework routes, work-verification references, testing
  references, engineering-methods references, project-management references,
  public docs, AGENTS, release notes, Makefile `CF_FILES`, package-path
  exceptions, and staging scripts when affected.
- Use explicit `git mv` path pairs for source moves. If an empty directory
  must be removed, use `rmdir` as a precaution only.
- Create Slice09 planning evidence artifacts under `artifacts/` and close the
  slice with explicit source and planning commits.

Out of scope:

- Splitting agent-coordination or contribution-style guide bodies; those belong
  to later Arc08 slices.
- Changing the audit from diagnosis-only to implementation or remediation work.
- Adding a new audit runner, report generator, CI system, or package target not
  already required by existing package validation.
- Weakening severity/file-line evidence, broadening the audit to unsupported
  skills, or accepting context-window sampling as a full audit.
- Reopening the sibling version-history rule.
- Committing generated zips, `build/`, or `target/skills`.

## Support Inputs

- `../slice08-testing-guide-split/cdc-verification.md`
- `../slice07-work-verification-guide-split/cdc-verification.md`
- `../../artifacts/operator-accepted-architecture.md`
- `../../artifacts/component-file-layout-plan.md`
- Arc08 `arc-plan.md` and `ledger.md`
- Project04 `project-plan.md` and `ledger.md`

## Expected Artifacts

- `artifacts/current-code-auditing-surface-map.md`
- `artifacts/code-auditing-split-map.md`
- `artifacts/legacy-code-audit-disposition.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/source-validation-results.md`

## Verification Approach

CC should inspect the current code-auditing entrypoint, `CODE-AUDIT.md`,
sibling history, route references, and package list before editing. The split
should make common lookup paths faster: audit scope/map, findings/severity,
scale-aware auditing, modernization synthesis, and audit-to-hardening handoff
should each be reachable without loading the whole old audit guide.

Record how `CODE-AUDIT.md` was handled. If it is moved to
`01-audit-scope-and-map.md` or another accepted guide, record that as a rename
with semantic extraction into the companion guides. If any copy of the old file
is retained, record why it remains support material rather than a stale live
route.

Validation must cover local links, package paths, generated
collaboration-framework package shape, and absence or explicit disposition of
the old `CODE-AUDIT.md` live route. Treat Expedited Mode as only the explicit
process behavior recorded in Arc08; do not infer source scope, reduce scope,
skip checks, weaken evidence, change review quality, or bypass approval gates.

## Exit Criteria

- The five accepted numbered code-auditing guides exist.
- The split preserves the current diagnosis-only audit contract and makes the
  new guides independently loadable.
- `knowledge/code-auditing/guides/CODE-AUDIT.md` is removed as a live route,
  renamed into an accepted guide, or retained only with explicit support-asset
  disposition.
- `knowledge/code-auditing/SKILL.md` routes to the new guide set.
- `knowledge/code-auditing/version-history.md` records the component change.
- README/docs/AGENTS/SKILL/component/release-note references affected by the
  split are repaired or explicitly dispositioned.
- `make check-skills`, `make collab-framework`, and `make check-package-paths`
  pass with zero hard failures.
- Generated `collaboration-framework.zip` contains the five numbered
  code-auditing guides and follows the recorded legacy `CODE-AUDIT.md`
  disposition.
- Source and planning commits are created with explicit file lists and both
  required co-author trailers.
