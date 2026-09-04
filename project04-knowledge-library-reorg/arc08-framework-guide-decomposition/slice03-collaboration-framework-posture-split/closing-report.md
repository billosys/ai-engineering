# Slice 03 Closing Report: Collaboration-Framework Posture Split

Status: proposed-done pending CDC verification
Date: 2026-09-04

Source commit: `e7ba785bf8c48ef061f69f9d90d176030b62dfc4`
Planning commit: `5de33d7fcd49d6de80737f730d3e92f69ea4089b`

## Summary

Slice03 split the collaboration-framework posture monolith into four approved numbered guides, removed the old monolith as a live source/package route, updated the collaboration-framework source entrypoint and public route docs, and normalized collaboration-framework component history to a sibling `version-history.md`.

## Explicit File List

Source files changed in `e7ba785bf8c48ef061f69f9d90d176030b62dfc4`:

- `Makefile`
- `docs/ORIGINS.md`
- `docs/collaboration-framework.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md` removed as the old live route through a tracked rename to `01-posture-and-ethics.md`
- `knowledge/collaboration-framework/guides/01-posture-and-ethics.md`
- `knowledge/collaboration-framework/guides/02-structural-pulls.md`
- `knowledge/collaboration-framework/guides/03-collaborative-rights.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md`

Planning files changed for close:

- `arc08-framework-guide-decomposition/slice03-collaboration-framework-posture-split/artifacts/posture-split-map.md`
- `arc08-framework-guide-decomposition/slice03-collaboration-framework-posture-split/artifacts/source-route-repair-map.md`
- `arc08-framework-guide-decomposition/slice03-collaboration-framework-posture-split/artifacts/version-history-reconciliation.md`
- `arc08-framework-guide-decomposition/slice03-collaboration-framework-posture-split/artifacts/source-validation-results.md`
- `arc08-framework-guide-decomposition/slice03-collaboration-framework-posture-split/ledger.md`
- `arc08-framework-guide-decomposition/slice03-collaboration-framework-posture-split/closing-report.md`

## Validation

- `git diff --check`: pass.
- Focused Markdown link scan over 9 touched Markdown files: pass, `checked_files=9 missing_links=0`.
- `make check-skills`: pass, all skill descriptions within limit.
- `make collab-framework`: pass, built `target/skills/collaboration-framework.zip`.
- `scripts/check-package-paths --exceptions assets/packaging/path-exceptions.tsv target/skills/*.zip`: pass, `exit_code=0`, `hard failures: 0`, `warnings: 358`.
- `make check-package-paths`: pass, full target exited 0 after rebuilding all zips.
- `unzip -Z1 target/skills/collaboration-framework.zip`: contains the four numbered posture guides and `knowledge/collaboration-framework/version-history.md`; old `AI-CONSTITUTION-SUPPLEMENT.md` path absent.

The initial non-escalated package-build attempts failed only because the sandbox could not write `build/` and `target/skills/` in the source checkout. The same required commands passed with approved escalation.

## Ledger Row Walk

Rows: 8. Done: 8. Deferred: 0. No-op: 0.

- F-1 proposed-done: four numbered posture guides exist; old monolith path is absent as a live load target and retained only in provenance/disposition notes.
- F-2 proposed-done: original major sections and supplement lineage were preserved across the split guides and sibling history, with standalone guide introductions and guide-set navigation.
- F-3 proposed-done: collaboration-framework SKILL routes now point to the split guide set and retain Slice02 Expedited Mode guardrails.
- F-4 proposed-done: component history lives in `knowledge/collaboration-framework/version-history.md`; former monolith version history is reconciled there.
- F-5 proposed-done: public docs, SKILL routes, and methodology links were repaired or dispositioned; no release-note or AGENTS old-path repair was required by the scan.
- F-6 proposed-done: required source validation, local link scan, skill checks, framework build, and package-path validation passed.
- F-7 proposed-done: generated `collaboration-framework.zip` includes the four numbered posture guides and does not expose the old monolith path.
- F-8 proposed-done: this close report records source/planning commits, explicit file lists, validation evidence, row walk, and bubble-up.

## Bubble-Up To Arc08

Slice04 should reconcile the full framework-guide decomposition after Slice01, Slice02, and Slice03. It should explicitly verify:

- Project-management process/history routes still compose with the collaboration-framework posture split.
- `knowledge/collaboration-framework/SKILL.md` and `knowledge/collaboration-framework/guides/04-component-route-table.md` agree on the final component map.
- `knowledge/collaboration-framework/version-history.md` and `knowledge/project-management/version-history.md` are sibling component histories with no guide-local component-history drift.
- Generated `collaboration-framework.zip` remains package-valid and carries no old monolith live route.

## Final Status

Slice03 is proposed-done pending independent CDC verification. No `cdc-verification.md` was created by CC.
