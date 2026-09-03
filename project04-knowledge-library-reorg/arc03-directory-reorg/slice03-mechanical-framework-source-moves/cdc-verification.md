# CDC Verification: Arc03 Slice03 Mechanical Framework Source Moves

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice03-mechanical-framework-source-moves
status: verified-closed
verified-by: CDC
verified-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
cc_source_commit: 99cebae1e98004164e4ea6735c4a68bc60c233da
cdc_source_repair_commit: 27cc255
cc_planning_commit: c0221cc861dfbc8334b6e241e12facf80b08def7
source-files-edited: true
```

## Verification Summary

CDC independently reproduced all six Slice03 ledger rows against the committed
planning packet and reran the source-side validation gates after one narrow
CDC compatibility repair.

The CC source commit moved the collaboration-framework payload from old
`docs/` and `templates/` paths into
`knowledge/collaboration-framework/`, preserved package behavior, and kept the
top-level `SKILL.md` as the authoritative no-shim entrypoint.

During verification, CDC found one stale direct route in `AGENTS.md`: it still
pointed future assistants at `docs/PROJECT-MANAGEMENT.md` and `docs/pm/`, even
though those physical files had moved. CDC repaired only that route in source
commit `27cc255`, preserving the `CLAUDE.md -> AGENTS.md` compatibility
surface.

Slice03 is verified-closed after that repair.

## Ledger Reproduction

| ID | CDC result | Evidence |
|----|------------|----------|
| F-1 | reproduced | `rg -n "mechanical move manifest|docs/AI-CONSTITUTION-SUPPLEMENT.md|docs/AI-ENGINEERING-METHODOLOGY.md|docs/PROJECT-MANAGEMENT.md|docs/pm/|docs/CODE-AUDIT.md|docs/CODE-COVERAGE.md|docs/SUBAGENT-DELEGATION-POLICY.md|docs/CONTRIBUTION-STYLE.md|templates/LEDGER-DISCIPLINE.md|templates/CONTRIBUTION-TICKET.md|knowledge/collaboration-framework" artifacts/mechanical-move-manifest.md` returned matches for every planned old and new framework/template path. |
| F-2 | reproduced | `rg -n "source-prose preservation|pure move|route/link update|version history|git diff --name-status --find-renames|byte-for-byte|cmp|line-level disclosure|no prose rewrite" artifacts/source-prose-preservation-evidence.md` returned matches for rename-aware evidence, byte-for-byte `cmp` checks, and line-level disclosure for route/link/version edits. |
| F-3 | reproduced with CDC repair | `rg -n "compatibility route update|no-shim|top-level SKILL.md|validated shim|replacement route|README.md|AGENTS.md|CLAUDE.md|CLAUDE.md -> AGENTS.md|re-entry condition|route compatibility" artifacts/compatibility-route-update-record.md` reproduced the CC compatibility record. CDC additionally verified `AGENTS.md` and repaired its stale direct PM-doc path in source commit `27cc255`. |
| F-4 | reproduced | `rg -n "package validation|CF_FILES|make check-skills|make collab-framework|make check-package-paths|collaboration-framework.zip|package root|entrypoint|package-path-exceptions.tsv|existing exception|no new exception|generated zip not committed" artifacts/package-validation-evidence.md` returned matches for package lists, validation gates, generated package inspection, existing exception maintenance, and ignored generated zips. |
| F-5 | reproduced with CDC repair | `rg -n "source checkout|source commit|source-files-edited: true|git status --short|git diff --check|edited source paths|moved source paths|generated zip not committed|clean final source status" artifacts/*.md` returned matches for the CC source commit, moved/edited path classes, generated zip handling, and clean source status. CDC source repair commit `27cc255` is the only additional source commit. |
| F-6 | reproduced | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout|planning checkout|Bubble-Up to Arc03|silent-drop|Slice04" closing-report.md` returned matches for row count, closure count, source/planning checkout status, Bubble-Up to Arc03, silent-drop, and Slice04 implications. |

## Source Validation

CDC verified source state in
`/Users/oubiwann/lab/billosys/ai-engineering`:

- `git show --name-status --find-renames --oneline 99cebae1e98004164e4ea6735c4a68bc60c233da` showed the planned framework payload moves, mostly `R100`, with `R098` for `AI-ENGINEERING-METHODOLOGY.md` because of disclosed route/link and version-history edits.
- `git show --name-status --oneline 27cc255` showed only `AGENTS.md`.
- `git diff --check` returned no output.
- `make check-skills` passed with `>> all skill descriptions within limit`.
- `make collab-framework` passed when rerun standalone and produced a
  `collaboration-framework.zip` with package root `collaboration-framework/`,
  entrypoint `collaboration-framework/SKILL.md`, and moved payload under
  `collaboration-framework/knowledge/collaboration-framework/`.
- `make check-package-paths` exited `0`. Its output contained accepted warning
  families, but no hard failure.
- `test -f docs/PROJECT-MANAGEMENT.md` exited nonzero, confirming the old
  physical path is absent.
- `test -f knowledge/collaboration-framework/docs/PROJECT-MANAGEMENT.md`
  exited `0`, confirming the new physical path is present.
- `rg -n "docs/PROJECT-MANAGEMENT.md|docs/pm/|knowledge/collaboration-framework/docs/PROJECT-MANAGEMENT.md|knowledge/collaboration-framework/docs/pm/" AGENTS.md SKILL.md README.md` confirmed `AGENTS.md` now uses the new physical PM path. Remaining `SKILL.md` text uses old `docs/...` labels as link text while the links target `knowledge/...`; that is a later public-language cleanup, not a path-resolution blocker for this slice.
- `git status --short` returned no output after the package build because
  generated zip output is ignored.

## Bubble-Up Check

Slice03 delivered the transitional mechanical move into
`knowledge/collaboration-framework/` and preserved package behavior after CDC's
narrow `AGENTS.md` route repair.

Slice04 should now split ownership at the source-root level: accepted Project02
components should move out of the transitional
`knowledge/collaboration-framework/` payload where a mechanical move can
preserve prose. Large guide splitting, polished component entrypoint prose,
README decomposition, and final public skill-kind/topology vocabulary remain
later work unless a validation gate proves a narrow route wrapper is required
inside Slice04.

The concept-card-method root remains reserved rather than live unless Project03
or Project05 implementation evidence authorizes actual method material.

## Closure

Slice03 is verified-closed.

Rows: 6. Done: 6. Deferred: 0. No-op: 0.
