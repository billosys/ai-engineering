# Validation Evidence Map

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice02-top-level-compatibility-decision
artifact: validation-evidence-map
created-on: 2026-09-02
selected path: no-shim
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source_commit: 5b796c3
source-files-edited: false
```

## Validation Evidence

| Check | Command or review | Result |
|-------|-------------------|--------|
| Source status baseline | `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short` | Returned no output before and after validation. |
| Source diff hygiene | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --check` | Returned no output. Required even though no source files changed, to document clean source hygiene. |
| Skill description gate | `make check-skills` | Passed with `>> all skill descriptions within limit`. |
| Framework package gate | `make collab-framework` | Passed after sandbox escalation allowed ignored `build/` and `collaboration-framework.zip` writes. |
| Generated output handling | Git status after `make collab-framework` | Returned no output; generated zip output is ignored and no tracked source change was produced. |
| Route review | `SKILL.md`, `README.md`, `AGENTS.md`, `CLAUDE.md` | Current route remains top-level `SKILL.md` with `/collaboration-framework` documentation and `CLAUDE.md -> AGENTS.md` compatibility. |
| Package root review | `unzip -l collaboration-framework.zip` | Package root is `collaboration-framework/`. |
| Entrypoint review | `unzip -p collaboration-framework.zip collaboration-framework/SKILL.md` | Entrypoint frontmatter begins with `name: collaboration-framework`; entrypoint behavior is preserved. |
| Planning diff hygiene | `git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check` | Returned no output after planning artifact and ledger updates. |

## Package Behavior Evidence

`make collab-framework` produced `collaboration-framework.zip` with:

- package root: `collaboration-framework/`;
- entrypoint: `collaboration-framework/SKILL.md`;
- framework docs under `collaboration-framework/docs/`;
- project-management files under `collaboration-framework/docs/pm/`;
- templates under `collaboration-framework/templates/`.

The entrypoint frontmatter inside the zip begins:

```yaml
name: collaboration-framework
description: |
```

This validates that the no-shim path preserves route review, package root,
and entrypoint behavior for the current top-level authoritative `SKILL.md`.

## Source And Planning Status

Source checkout:

- Path: `/Users/oubiwann/lab/billosys/ai-engineering`
- Commit: `5b796c3`
- `status --short`: returned no output.
- Source commit: none; no source edits.

Planning checkout:

- Path: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`
- Baseline before Slice02 planning edits: `c7e25b9`
- Planning `diff --check`: returned no output after planning artifact and
  ledger updates.

## Boundary

The validation evidence supports the selected no-shim path only. It is not
source-edit authorization for later Arc03 slices. The re-entry condition in
the decision artifact must be applied before composer source moves.
