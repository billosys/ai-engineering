* **Date:** 2026-08-26
* **Previous:** `0.4.0` (2026-08-09)
* **Commits:** 2 first-parent project commits
* **Diff:** 4 files changed, +221 / -81 lines

## Headline

Collaboration Framework v1.3.0 — a project-management cleanup release that
moves planning artifacts out of implementation-branch `docs/` trees and into a
dedicated planning Git worktree, with project directories named like arcs and
slices.

## Planning Worktree Default

The project-management default changed from version-looking directories such as
`docs/design-v0.1.0/` to a dedicated orphan `planning` branch mounted as a Git
worktree.

The new default is:

- Reuse the repository's existing worktree convention when one is present.
- Otherwise use `$PROJECT_DIR/.worktrees`.
- Use a `planning` branch and `.worktrees/planning` worktree by default.
- Keep the planning branch orphaned, with no inherited implementation files.
- Store project plans under `projectNN-<slug>/`.

This makes the planning tree the official source of truth for project plans,
arc plans, slice ledgers, prompts, close reports, and CDC verification, without
mixing those records into product or release documentation.

## Project Naming and Metadata

Project directories now follow the same naming pattern as arcs and slices:
`projectNN-<slug>`, for example `project01-vault-split`.

Ordering and relationships are no longer inferred from release-looking
directory names. `project-plan.md` now carries explicit metadata for:

- `project`
- `status`
- `depends-on`
- `blocks`
- `related`

This gives humans and LLMs the sortable filesystem shape without encoding
dependency semantics in path names.

## Slice Plan Naming

The slice plan-of-record was renamed from `slice-doc.md` to `slice-plan.md`, so
all three planning scales now use the same pattern:

- `project-plan.md`
- `arc-plan.md`
- `slice-plan.md`

The old name remains only in version-history notes that explain the rename.

## Framework Document Updates

The release updates the collaboration-framework entry point and the two
operational specs that carry the planning/verification mechanics:

- `SKILL.md` bumped to `1.3.0` and now routes planning work to the new
  planning-worktree default.
- `docs/PROJECT-MANAGEMENT.md` bumped to `2.2` and now owns the new substrate,
  naming rules, metadata fields, confirmation protocol, and related
  anti-patterns.
- `docs/AI-ENGINEERING-METHODOLOGY.md` bumped to `1.6` and now summarizes the
  worktree-based planning model rather than the old `docs/design-vX.Y.Z` tree.
- `templates/LEDGER-DISCIPLINE.md` bumped to `2.1` and now uses the
  planning-worktree path and `slice-plan.md` terminology.

## Verification

- `git diff --check` passed before the cleanup commit.
- Remaining `docs/design-vX.Y.Z` and `docs/design-v0.1.0` mentions are
  historical, explicitly superseded, or anti-pattern examples.
- The installed `collaboration-framework` skill was checked after install and
  reports `version: 1.3.0` with the new planning-worktree and `slice-plan.md`
  guidance visible.
