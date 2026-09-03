# Closing Report: Arc03 Slice03 Mechanical Framework Source Moves

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice03-mechanical-framework-source-moves
status: proposed-done
closed-by: CC
closed-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source_commit: 99cebae1e98004164e4ea6735c4a68bc60c233da
source-files-edited: true
```

## Capability Verdict

Slice03 delivered the mechanical collaboration-framework payload move assigned
by the Arc03 plan. The current selected-file collaboration-framework package
payload now lives under `knowledge/collaboration-framework/`, top-level
`SKILL.md` remains authoritative under the re-entered no-shim decision, and
package validation remains green.

## Source Commit And Path List

Source commit: `99cebae1e98004164e4ea6735c4a68bc60c233da`
(`Move collaboration-framework source payload under knowledge`).

Edited source paths:

- `SKILL.md`
- `Makefile`
- `package-path-exceptions.tsv`
- `knowledge/collaboration-framework/docs/AI-ENGINEERING-METHODOLOGY.md`

Moved source paths:

- `docs/AI-CONSTITUTION-SUPPLEMENT.md` to `knowledge/collaboration-framework/docs/AI-CONSTITUTION-SUPPLEMENT.md`
- `docs/AI-ENGINEERING-METHODOLOGY.md` to `knowledge/collaboration-framework/docs/AI-ENGINEERING-METHODOLOGY.md`
- `docs/PROJECT-MANAGEMENT.md` to `knowledge/collaboration-framework/docs/PROJECT-MANAGEMENT.md`
- `docs/pm/01-scales-of-work.md` to `knowledge/collaboration-framework/docs/pm/01-scales-of-work.md`
- `docs/pm/02-canonical-planning-worktree.md` to `knowledge/collaboration-framework/docs/pm/02-canonical-planning-worktree.md`
- `docs/pm/03-planning-top-down.md` to `knowledge/collaboration-framework/docs/pm/03-planning-top-down.md`
- `docs/pm/04-closing-slices.md` to `knowledge/collaboration-framework/docs/pm/04-closing-slices.md`
- `docs/pm/05-closing-arcs.md` to `knowledge/collaboration-framework/docs/pm/05-closing-arcs.md`
- `docs/pm/06-confirmation-protocol.md` to `knowledge/collaboration-framework/docs/pm/06-confirmation-protocol.md`
- `docs/pm/07-anti-patterns.md` to `knowledge/collaboration-framework/docs/pm/07-anti-patterns.md`
- `docs/pm/08-maintenance.md` to `knowledge/collaboration-framework/docs/pm/08-maintenance.md`
- `docs/pm/09-worked-example-odm.md` to `knowledge/collaboration-framework/docs/pm/09-worked-example-odm.md`
- `docs/pm/version-history.md` to `knowledge/collaboration-framework/docs/pm/version-history.md`
- `docs/CODE-AUDIT.md` to `knowledge/collaboration-framework/docs/CODE-AUDIT.md`
- `docs/CODE-COVERAGE.md` to `knowledge/collaboration-framework/docs/CODE-COVERAGE.md`
- `docs/SUBAGENT-DELEGATION-POLICY.md` to `knowledge/collaboration-framework/docs/SUBAGENT-DELEGATION-POLICY.md`
- `docs/CONTRIBUTION-STYLE.md` to `knowledge/collaboration-framework/docs/CONTRIBUTION-STYLE.md`
- `templates/LEDGER-DISCIPLINE.md` to `knowledge/collaboration-framework/templates/LEDGER-DISCIPLINE.md`
- `templates/CONTRIBUTION-TICKET.md` to `knowledge/collaboration-framework/templates/CONTRIBUTION-TICKET.md`

## Artifact Inventory

| Artifact | Purpose |
|----------|---------|
| `artifacts/mechanical-move-manifest.md` | Exact old-to-new path map for the moved collaboration-framework payload. |
| `artifacts/source-prose-preservation-evidence.md` | Rename-aware diff, `cmp` byte-for-byte checks, and line-level disclosure for route/link/version edits. |
| `artifacts/compatibility-route-update-record.md` | Re-enters the no-shim decision and records top-level `SKILL.md`, `README.md`, `AGENTS.md`, and `CLAUDE.md` behavior. |
| `artifacts/package-validation-evidence.md` | Records `CF_FILES`, validation commands, generated package inspection, existing exception maintenance, and generated zip handling. |

## Ledger Walk

| ID | Status | Evidence |
|----|--------|----------|
| F-1 | done | `rg -n "mechanical move manifest|docs/AI-CONSTITUTION-SUPPLEMENT.md|docs/AI-ENGINEERING-METHODOLOGY.md|docs/PROJECT-MANAGEMENT.md|docs/pm/|docs/CODE-AUDIT.md|docs/CODE-COVERAGE.md|docs/SUBAGENT-DELEGATION-POLICY.md|docs/CONTRIBUTION-STYLE.md|templates/LEDGER-DISCIPLINE.md|templates/CONTRIBUTION-TICKET.md|knowledge/collaboration-framework" artifacts/mechanical-move-manifest.md` returned matches for the manifest, all old payload path classes, and `knowledge/collaboration-framework`. |
| F-2 | done | `rg -n "source-prose preservation|pure move|route/link update|version history|git diff --name-status --find-renames|byte-for-byte|cmp|line-level disclosure|no prose rewrite" artifacts/source-prose-preservation-evidence.md` returned matches for preservation method, pure moves, route/link updates, version history, rename-aware diff evidence, `cmp`, and no prose rewrite. |
| F-3 | done | `rg -n "compatibility route update|no-shim|top-level SKILL.md|validated shim|replacement route|README.md|AGENTS.md|CLAUDE.md|CLAUDE.md -> AGENTS.md|re-entry condition|route compatibility" artifacts/compatibility-route-update-record.md` returned matches for no-shim re-entry, preserved top-level route, README/AGENTS/CLAUDE behavior, symlink behavior, and future re-entry condition. |
| F-4 | done | `rg -n "package validation|CF_FILES|make check-skills|make collab-framework|make check-package-paths|collaboration-framework.zip|package root|entrypoint|package-path-exceptions.tsv|existing exception|no new exception|generated zip not committed" artifacts/package-validation-evidence.md` returned matches for Makefile `CF_FILES`, validation gates, generated package inspection, existing exception maintenance, no new exception, and generated zip handling. |
| F-5 | done | `rg -n "source checkout|source commit|source-files-edited: true|git status --short|git diff --check|edited source paths|moved source paths|generated zip not committed|clean final source status" artifacts/*.md` returned matches for source checkout, source commit, source-edited status, source hygiene commands, edited/moved paths, generated zip handling, and clean final source status. |
| F-6 | done | This closing report records Rows: 6, Done: 6, source checkout status, planning checkout status, Bubble-Up to Arc03, silent-drop, and Slice04 follow-up notes. |

## Source Checkout Status

`git -C /Users/oubiwann/lab/billosys/ai-engineering status --short --untracked-files=all`
returned no output after the source commit and validation.

`git -C /Users/oubiwann/lab/billosys/ai-engineering diff --check` returned no
output before the source commit.

Validation run:

- `make check-skills` passed.
- `make collab-framework` passed.
- `./scripts/check-package-paths --exceptions package-path-exceptions.tsv collaboration-framework.zip` passed with `hard failures: 0`.
- `make check-package-paths` passed and exited 0.
- Generated package inspection showed `collaboration-framework/` package root
  and `collaboration-framework/SKILL.md` entrypoint.

Generated zip not committed: regenerated zip files are ignored release
artifacts.

## Planning Checkout Status

Planning checkout:
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`.

`git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check`
is part of the final planning close verification and returned no output after
the planning packet was written.

## Silent-Drop Check

Slice03 specified:

- the mechanical move manifest;
- source-prose preservation evidence;
- no-shim compatibility route re-entry;
- package validation evidence;
- source commit and exact path list;
- source and planning checkout status;
- Bubble-Up to Arc03, including Slice04 implications.

All specified outputs are present in the artifacts, ledger, and this closing
report. No planned Slice03 artifact was dropped. No `cdc-verification.md` was
created.

## Bubble-Up to Arc03

Slice03 delivered the mechanical framework source move assigned by the Arc03
slice breakdown. The no-shim route remains valid after re-entry: top-level
`SKILL.md` remains authoritative while its links route to the moved payload.

Slice04 must account for these facts:

- `knowledge/collaboration-framework/` now exists and contains the moved
  composer/framework payload.
- `docs/ORIGINS.md` remains in top-level `docs/`; `templates/GUIDE.md`
  remains in top-level `templates/`.
- Package-local validation passes, but the collaboration-framework package
  still reports non-fatal warnings for source-clone and repo-only examples;
  Slice04 should avoid broad exceptions and continue package-local repair
  before exceptions.
- The methodology file has a disclosed line-level repair for a historical
  concept-card extraction path whose target is not present in the source
  checkout or generated package.

No arc-plan scope change is required from this slice.

## Closure

Slice03 is proposed-done pending CDC verification.

Rows: 6. Done: 6. Deferred: 0. No-op: 0.
