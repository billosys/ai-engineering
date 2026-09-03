# Slice 04: Component, Method, and Template Ownership Moves

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice04-component-method-template-ownership-moves
status: verified-closed
opened-by: CDC
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: true
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Mechanically place accepted Project02 component substrate, authorized method
material, and owner-local templates under their owning `knowledge/` roots while
preserving source prose, package behavior, and the Arc04/Arc05 separation.

## Scope

In scope:

- Start from the current source checkout after Slice03 source commits
  `99cebae1e98004164e4ea6735c4a68bc60c233da` and CDC repair commit
  `27cc255`.
- Move source material out of the transitional
  `knowledge/collaboration-framework/` payload into accepted Project02
  component roots where the move can be mechanical and ownership is clear.
- Preserve source prose during moves. Rename paths when ownership is clear, but
  do not split large documents into newly authored guide sets in this slice.
- Move owner-local templates under owning component roots when accepted:
  ledger discipline under `knowledge/work-verification/` and contribution
  ticket workflow under `knowledge/contribution-style/`.
- Preserve top-level `templates/GUIDE.md` as a cross-cutting support exception
  unless evidence proves a single owning root.
- Record the planned `knowledge/concept-card-method/` root as reserved unless
  already-authorized Project03/Project05 source material exists in the current
  checkout.
- Update only route links, package payload paths, and existing exception paths
  required by the mechanical ownership moves.

Out of scope:

- Final component guide decomposition or polished component entrypoint prose.
- Public skill-kind or atomic/composite vocabulary; Arc05 owns that language.
- README decomposition and end-user docs prose; Arc04 owns that work.
- Moving domain/tooling skill roots, Biome entrypoints, CCDP source, or
  top-level compatibility files except for narrow route updates.
- Creating broad package-path exceptions or persistent accepted warnings
  without operator approval.
- Committing generated zip artifacts.

## Expected Target Direction

The expected ownership direction is:

```text
knowledge/collaboration-framework/     daily-driver composer/posture material
knowledge/engineering-methods/         methodology, substrate, process, gates
knowledge/project-management/          planning and close lifecycle
knowledge/work-verification/           ledger/evidence discipline and template
knowledge/testing/                     coverage and validation-gate discipline
knowledge/code-auditing/               diagnosis-only audit discipline
knowledge/agent-coordination/          CC/CDC/operator and delegation material
knowledge/contribution-style/          contribution prose and ticket template
knowledge/concept-card-method/         reserved until authorized live material
templates/GUIDE.md                     top-level cross-cutting support exception
```

This slice may choose conservative file names such as preserving original
document names under owner roots when final guide decomposition would require
prose rewriting.

## Expected Artifacts

- `artifacts/component-ownership-move-manifest.md`
- `artifacts/method-and-template-ownership-record.md`
- `artifacts/source-prose-preservation-evidence.md`
- `artifacts/validation-and-package-impact-evidence.md`

## Verification Approach

CC will commit source edits first, then commit the planning close packet. Both
commits must use explicit file lists or pathspecs for every changed file. Do
not stage broad directories.

Required validation includes:

- source `git status --short` before edits;
- source `git diff --check`;
- rename-aware source move review with `git diff --name-status --find-renames`;
- source-prose preservation evidence, using byte comparison where possible and
  explicit disclosure for any route/link/version edits;
- `make check-skills`;
- `make collab-framework`;
- `make check-package-paths`;
- generated package inspection for affected package roots;
- planning `git diff --check`.

## Exit Criteria

- Accepted Project02 component ownership is reflected in source-root placement
  for the moved substrate this slice can handle mechanically.
- The concept-card-method root is either populated only by authorized live
  material or explicitly recorded as reserved/not live.
- Owner-local templates are moved or explicitly retained with evidence-backed
  exception rationale.
- Top-level compatibility surfaces remain valid after route updates.
- Package behavior remains valid and generated zips remain uncommitted.
- CC commits the source change and planning close packet separately, each with
  explicit file lists.
- `closing-report.md` walks all six ledger rows and bubbles package/link
  implications up to Slice05.
