---
status: proposed-done
closed: 2026-08-29
implementation_checkout: /Users/oubiwann/lab/billosys/ai-engineering
implementation_diff_state: uncommitted working-tree diff
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
---

# Slice 04 Closing Report

## Summary

Slice 04 tightened the package-path warning policy after the Slice 03 entrypoint
burn-down. The implementation diff is limited to `package-path-exceptions.tsv`:
five stale `transitional-warning` rows with `expires=after-arc02` were converted
to ordinary `warning` rows with concrete later-maintenance expiry labels.

The warning total remains visible at 295. This is intentional: unresolved package
usability issues were not hidden behind broad exceptions. The post-change gate
reports 0 hard failures, 295 warnings, and 3 explicit exceptions.

## Implementation Scope

- Changed: `package-path-exceptions.tsv`.
- Not changed: checker code, mature guide prose, mature guide directories,
  package staging transforms, URL policy, and CCDP package targets.
- No implementation commit exists yet; the current implementation state is an
  uncommitted working-tree diff.

## Verification

| Command | Evidence | Result |
|---------|----------|--------|
| `make check-package-paths` before policy change | `artifacts/current-warning-baseline.txt` | Pass: 0 hard failures, 295 warnings, 3 explicit exceptions. |
| `make check-package-paths` after policy change | `artifacts/post-warning-policy-check.txt` | Pass: 0 hard failures, 295 warnings, 3 explicit exceptions. |
| `scripts/check-package-paths --check-exceptions-only` | `artifacts/check-exceptions-only.txt` | Pass: exception schema ok. |
| `make check-skills` | `artifacts/make-check-skills.txt` | Pass. |
| `make all` | `artifacts/make-all.txt` | Pass. |
| `git diff --check` in implementation checkout | `artifacts/git-diff-check-implementation.txt` | Pass. |
| `git -C .worktrees/planning diff --check` | `artifacts/git-diff-check-planning.txt` | Pass. |

## Artifacts

Artifacts are under
`project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice04-warning-policy-tightening/artifacts/`.

- Baseline and post-change transcripts: `current-warning-baseline.txt`, `post-warning-policy-check.txt`.
- Extracted inventories: `current-warning-inventory.tsv`, `post-warning-policy-inventory.tsv`.
- Count summaries: `current-warning-counts.tsv`, `post-warning-counts.tsv`.
- Classification and policy notes: `warning-policy-classification.md`, `transitional-exception-disposition.md`, `exception-diff-scope.md`, `implementation-diff-scope.md`, `later-arc-backlog.md`.
- Gate transcripts: `check-exceptions-only.txt`, `make-check-skills.txt`, `make-all.txt`, `git-diff-check-implementation.txt`, `git-diff-check-planning.txt`, `git-status-implementation.txt`.
- Full generated inventory: `artifact-inventory.txt`.

## Ledger Walk

- F-1: Done. Current warning baseline was generated from `make check-package-paths` and recorded in `current-warning-baseline.txt`, `current-warning-inventory.tsv`, and `current-warning-counts.tsv`.
- F-2: Done. `warning-policy-classification.md` classifies `bundled-reference`, `repo-only/provenance`, `source-clone-reference`, `example-project path`, and parser false-positive findings.
- F-3: Done. `transitional-exception-disposition.md` records the disposition of every stale `expires=after-arc02` row.
- F-4: Done. `exception-diff-scope.md` records that no broad suppressions or new explicit exceptions were added.
- F-5: Done. `later-arc-backlog.md` keeps real unresolved package usability issues visible for later work.
- F-6: Done. `post-warning-policy-check.txt` records the passing post-change package-path gate.
- F-7: Done. `check-exceptions-only.txt`, `make-check-skills.txt`, and `make-all.txt` all record passing gates.
- F-8: Done. `implementation-diff-scope.md`, `git-status-implementation.txt`, and `git-diff-check-implementation.txt` show implementation scope stayed inside the slice boundary.
- F-9: Done. `artifact-inventory.txt` records the durable artifact set under this slice's `artifacts/` directory.
- F-10: Done. This close report walks F-1 through F-10, names the implementation diff state, inventories artifacts, and bubbles the result to Arc 02.

## Bubble-up to Arc 02

Arc 02 now has a tightened warning policy after entrypoint burn-down. The stale
Arc 02 transitional warning rows no longer remain as `after-arc02` debt; each
remaining affected package issue is visible as an ordinary warning with a later
maintenance disposition.

Remaining warning classes are documented as later-arc or later-maintenance
backlog rather than package-path gate defects for Arc 02. On CC evidence, Arc 02
is ready for CDC close review. CDC still owns independent verification and any
arc close decision.
