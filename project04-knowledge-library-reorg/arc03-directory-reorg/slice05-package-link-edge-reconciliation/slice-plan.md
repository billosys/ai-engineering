# Slice 05: Package, Link, and Edge-Case Reconciliation

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice05-package-link-edge-reconciliation
status: open
opened-by: CDC
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: conditional
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Reconcile package lists, package-local links, package-path exceptions, Biome
multi-entrypoint behavior, and CCDP separation after the accepted Arc03
directory moves.

## Scope

In scope:

- Start from source commit `873a5502acef9c087cefd78d468cf6d123a27341`.
- Treat package-local link repair as the first reconciliation pattern before
  adding, widening, or accepting exceptions.
- Inspect `Makefile`, `package-path-exceptions.tsv`, `SKILL.md`, package-local
  links, generated zip roots, and install zip lists after the Slice03/Slice04
  moves.
- Preserve `knowledge/biome/` as a multi-entrypoint source root that produces
  distinct generated package roots.
- Preserve `protocols/ccdp/` as a separate protocol package surface, outside
  installable skill packages unless a later operator-approved project changes
  that policy.
- Record every persistent warning, explicit exception, or no-op with owner,
  reason, validation command, and re-entry condition.
- Make narrow source repairs only where validation exposes broken package
  paths or route links.

Out of scope:

- README decomposition and end-user documentation prose; Arc04 owns this.
- Final public skill-kind or atomic/composite vocabulary; Arc05 owns this.
- Moving more source material unless required by a package/link defect.
- Broad package-path exceptions or accepted warnings without operator approval.
- Folding CCDP into installable skill packages.
- Committing generated zips.

## Expected Artifacts

- `artifacts/package-link-repair-inventory.md`
- `artifacts/biome-and-ccdp-edge-case-validation.md`
- `artifacts/package-path-exception-register.md`
- `artifacts/source-change-and-validation-evidence.md`

## Verification Approach

CC will close the slice by committing any source edits first, then committing
the planning close packet. If no source edits are needed, explicitly record
that no source commit was created.

Required validation includes:

- source `git status --short --untracked-files=all`;
- source `git diff --check`;
- `make check-skills`;
- `make collab-framework`;
- `make check-package-paths`;
- `make all`;
- generated package inspection for `collaboration-framework.zip`, Biome
  packages, and CCDP packages or package lists as applicable;
- package-path exception review;
- planning `git diff --check`.

If a persistent package-path exception or accepted warning is required, stop
and record the operator gate instead of broadening exceptions silently.

## Exit Criteria

- Package-local link repair has been attempted before exceptions.
- Package/list surfaces agree with the moved source layout.
- Biome multi-entrypoint behavior is preserved with generated package evidence.
- CCDP remains separate with package/list evidence.
- Persistent exceptions or warnings are either unchanged and justified, removed
  by repair, or recorded as operator-gated.
- Source and planning worktrees finish clean.
- CC commits source and planning changes using explicit file lists.
- `closing-report.md` walks all six ledger rows and bubbles findings up to
  Slice06.
