---
# === CORE IDENTIFICATION ===
concept: Git Hooks Integration
slug: git-hooks-integration

# === CLASSIFICATION ===
category: integration
subcategory: git hooks
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "recipes/git-hooks.mdx"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "pre-commit hooks"
  - "Biome git hooks"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-cli
extends: []
related:
  - vcs-integration
  - biome-ci-command
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I integrate Biome with Git hooks?"
---

# Quick Definition
Biome integrates with Git hooks through hook management tools (Lefthook, Husky + lint-staged, pre-commit, git-format-staged) or custom shell scripts to automatically format and lint files before committing or pushing.

# Core Definition
Biome can be executed in Git hooks to enforce code quality at commit or push time. The documentation covers four hook management tools: **Lefthook** (fast, cross-platform, dependency-free), **Husky** with **lint-staged** or **git-format-staged** (widely-used in JavaScript), and **pre-commit** (multi-language, with four official Biome hooks: `biome-ci`, `biome-check`, `biome-format`, `biome-lint`). Common CLI flags for hook usage include `--files-ignore-unknown=true` (skip unsupported files), `--no-errors-on-unmatched` (suppress errors when no files match), `--staged` (process only staged files), and `--write` (apply fixes).

# Prerequisites
- biome-cli: Must understand Biome's commands and flags.

# Key Properties
1. **Lefthook**: Uses `{staged_files}` or `{push_files}` placeholders; `stage_fixed: true` re-stages fixed files.
2. **Husky + lint-staged**: lint-staged passes staged files automatically; configuration in `package.json`.
3. **Husky + git-format-staged**: Avoids `git stash` conflicts between staged and unstaged changes.
4. **pre-commit**: Four official hooks via `biomejs/pre-commit` repo; requires `additional_dependencies` to specify Biome version.
5. Key CLI flags: `--files-ignore-unknown=true`, `--no-errors-on-unmatched`, `--staged`, `--write`.
6. Custom shell scripts can use `biome check --staged` directly in `.git/hooks/pre-commit`.
7. When using `--write` in hooks, staged files with unstaged changes need special handling to avoid data loss.

# Construction / Recognition
To set up Git hooks with Biome:

**Lefthook** (recommended for simplicity):
```yaml
pre-commit:
  commands:
    check:
      glob: "*.{js,ts,jsx,tsx,json,jsonc}"
      run: npx @biomejs/biome check --write --no-errors-on-unmatched --files-ignore-unknown=true --colors=off {staged_files}
      stage_fixed: true
```

**Husky + lint-staged:**
```json
{
  "lint-staged": {
    "*.{js,ts,jsx,tsx,json,jsonc}": [
      "biome check --write --no-errors-on-unmatched"
    ]
  }
}
```

**pre-commit:**
```yaml
repos:
  - repo: https://github.com/biomejs/pre-commit
    rev: "v2.0.6"
    hooks:
      - id: biome-check
        additional_dependencies: ["@biomejs/biome@2.1.1"]
```

# Context & Application
Git hooks provide immediate feedback before code is committed, catching formatting and linting issues early. They complement CI checks by preventing non-conforming code from entering the repository.

# Examples
From the source, Lefthook configuration for checking before commit:

```yaml
pre-commit:
  commands:
    check:
      glob: "*.{js,ts,cjs,mjs,d.cts,d.mts,jsx,tsx,json,jsonc}"
      run: npx @biomejs/biome check --no-errors-on-unmatched --files-ignore-unknown=true --colors=off {staged_files}
```

Shell script alternative:
```shell
#!/bin/sh
set -eu
npx @biomejs/biome check --staged --files-ignore-unknown=true --no-errors-on-unmatched
```

Pre-commit local hook (avoids dual version management):
```yaml
repos:
  - repo: local
    hooks:
      - id: local-biome-check
        name: biome check
        entry: npx @biomejs/biome check --write --files-ignore-unknown=true --no-errors-on-unmatched
        language: system
        types: [text]
```

(From recipes/git-hooks.mdx)

# Relationships
## Builds Upon
- biome-cli
## Enables
None directly.
## Related
- vcs-integration (--staged flag requires VCS awareness)
- biome-ci-command (hooks and CI are complementary quality gates)
## Contrasts With
None.

# Common Errors
1. Forgetting `--no-errors-on-unmatched`, causing hook failures when no matching files are staged.
2. Using `--write` in hooks without handling files that have both staged and unstaged changes, risking data loss.
3. With pre-commit tool, forgetting `additional_dependencies` to specify the Biome version.
4. Using both `glob` and `--files-ignore-unknown=true` redundantly -- only one is needed.

# Common Confusions
1. Confusing the `pre-commit` tool (Python-based hook manager at pre-commit.com) with the Git `pre-commit` hook itself.
2. Thinking Husky alone handles staged files -- it needs lint-staged or git-format-staged for that.
3. Not realizing `{staged_files}` is Lefthook syntax, not a Biome feature.

# Source Reference
- recipes/git-hooks.mdx, all sections (Lefthook, Husky, pre-commit, Shell script)

# Verification Notes
Extensively documented with configuration examples for four tools plus shell scripts. High confidence.
