# CDC Verification: Arc03 Slice04 Component Method Template Ownership Moves

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice04-component-method-template-ownership-moves
status: verified-closed
verified-by: CDC
verified-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
cc_source_commit: 873a5502acef9c087cefd78d468cf6d123a27341
cc_planning_commit: a5dbc6a3077b7ea031ac0a3f63499b8eff635407
source-files-edited: true
```

## Verification Summary

CDC independently reproduced all six Slice04 ledger rows against the committed
planning packet and reran the source-side validation gates.

Slice04 mechanically moved accepted Project02 specialist component substrate
from the transitional `knowledge/collaboration-framework/` root into accepted
`knowledge/<component>/` owner roots, preserved source prose where pure moves
were expected, kept `concept-card-method` reserved rather than live, moved
owner-local templates under owning component roots, and preserved package
behavior.

Slice04 is verified-closed.

## Ledger Reproduction

| ID | CDC result | Evidence |
|----|------------|----------|
| F-1 | reproduced | `rg -n "component ownership move manifest|knowledge/<component>|knowledge/collaboration-framework|knowledge/engineering-methods|knowledge/project-management|knowledge/work-verification|knowledge/testing|knowledge/code-auditing|knowledge/agent-coordination|knowledge/contribution-style|mechanical move" artifacts/component-ownership-move-manifest.md` returned matches for every accepted owner root and the mechanical move claim. Source `git show --name-status --find-renames --oneline 873a5502acef9c087cefd78d468cf6d123a27341` reproduced the component move set. |
| F-2 | reproduced | `rg -n "method and template ownership|concept-card-method|reserved|authorized live material|templates/GUIDE.md|cross-cutting support|LEDGER-DISCIPLINE.md|CONTRIBUTION-TICKET.md|owner-local template|exception" artifacts/method-and-template-ownership-record.md` returned matches for the reserved method root, owner-local templates, and top-level `templates/GUIDE.md` cross-cutting support exception. CDC confirmed `test -d knowledge/concept-card-method` exited nonzero and `test -f templates/GUIDE.md` exited `0`. |
| F-3 | reproduced | `rg -n "source-prose preservation|pure move|route/link update|version history|git diff --name-status --find-renames|byte-for-byte|cmp|line-level disclosure|no prose rewrite" artifacts/source-prose-preservation-evidence.md` returned matches for rename-aware evidence, byte-for-byte `cmp` checks, line-level route/link/version disclosure, and no prose rewrite. CDC reran all five pure-move `cmp` commands and each exited `0`. |
| F-4 | reproduced | `rg -n "validation and package impact|git status --short|git diff --check|make check-skills|make collab-framework|make check-package-paths|generated package inspection|package root|entrypoint|package-path-exceptions.tsv|generated zip not committed" artifacts/validation-and-package-impact-evidence.md` returned matches for source hygiene, package gates, generated package inspection, package-path exception handling, and generated zip handling. CDC reran the relevant gates successfully. |
| F-5 | reproduced | `rg -n "compatibility|top-level SKILL.md|AGENTS.md|CLAUDE.md|CLAUDE.md -> AGENTS.md|README.md|Biome|CCDP|Arc04|Arc05|route update|scope boundary" artifacts/*.md` returned matches for top-level route surfaces, README/Biome/CCDP preservation, and Arc04/Arc05 boundaries. CDC confirmed `CLAUDE.md` still resolves to `AGENTS.md`. |
| F-6 | reproduced | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout|planning checkout|Bubble-Up to Arc03|Slice05|package-local link|exception" closing-report.md` returned matches for row count, closure count, source/planning status, Bubble-Up to Arc03, Slice05 link-repair guidance, and exception policy. |

## Source Validation

CDC verified source state in
`/Users/oubiwann/lab/billosys/ai-engineering`:

- `git status --short --untracked-files=all` returned no output before CDC
  verification and after package validation.
- `git show --name-status --find-renames --oneline 873a5502acef9c087cefd78d468cf6d123a27341` showed the planned owner-root moves plus narrow route/package edits to `AGENTS.md`, `Makefile`, `SKILL.md`, and `package-path-exceptions.tsv`.
- `git show -s --format=full 873a5502acef9c087cefd78d468cf6d123a27341` showed both required co-author trailers.
- `git diff --check` returned no output.
- `make check-skills` passed with `>> all skill descriptions within limit`.
- `make collab-framework` passed and produced a
  `collaboration-framework.zip` with package root `collaboration-framework/`,
  entrypoint `collaboration-framework/SKILL.md`, and the affected component
  owner roots under the package root.
- `./scripts/check-package-paths --exceptions package-path-exceptions.tsv collaboration-framework.zip` exited `0` with `hard failures: 0`, `warnings: 65`, and `explicit exceptions: 2`.
- `make check-package-paths` exited `0`; output remained warning-only for known
  package-path families.
- `unzip -l collaboration-framework.zip` showed the affected owner-root
  package paths, including `knowledge/project-management/`,
  `knowledge/work-verification/`, `knowledge/code-auditing/`, and
  `knowledge/contribution-style/`.

## Bubble-Up Check

Slice04 delivered the Arc03 piece assigned to it: accepted specialist component
substrate and owner-local templates now live under accepted
`knowledge/<component>/` roots where the move could remain mechanical.

The slice also surfaced a concrete Slice05 planning rule: package-local link
repair must be the first reconciliation pattern before package-path exceptions.
CC reported initial affected-package hard failures during implementation;
narrow package-local link repair cleared them without adding a broad
exception. The existing code-audit exception moved with its owner path to
`knowledge/code-auditing/docs/CODE-AUDIT.md`.

The silent-drop diff is complete. `concept-card-method` remains reserved
because no authorized live source root was present; `templates/GUIDE.md`
remains a narrow cross-cutting support exception; README, Biome, CCDP, Arc04
docs prose, and Arc05 public vocabulary stayed outside this slice.

## Closure

Slice04 is verified-closed.

Rows: 6. Done: 6. Deferred: 0. No-op: 0.
