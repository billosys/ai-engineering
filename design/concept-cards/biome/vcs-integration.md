---
# === CORE IDENTIFICATION ===
concept: VCS Integration
slug: vcs-integration

# === CLASSIFICATION ===
category: integration
subcategory: version control
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "guides/integrate-in-vcs.mdx"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Git integration"
  - "VCS support"
  - "version control integration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-configuration
extends: []
related:
  - file-includes-and-excludes
  - biome-ci-command
  - git-hooks-integration
  - biome-cli
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I configure Biome to process only changed files?"
  - "How does VCS integration relate to file processing?"
---

# Quick Definition
Biome's opt-in integration with Git that enables using VCS ignore files for file exclusion and processing only changed or staged files.

# Core Definition
Biome's VCS integration is an opt-in feature configured via the `vcs` section of `biome.json`. It currently supports only Git (`clientKind: "git"`). Once enabled (`vcs.enabled: true`), it provides two capabilities: (1) respecting the project's `.gitignore` and `.ignore` files for file exclusion (`vcs.useIgnoreFile: true`), and (2) processing only changed or staged files via the CLI flags `--changed` and `--staged`. The `--changed` flag processes files that differ from the configured `vcs.defaultBranch`, while `--since` allows specifying an arbitrary branch. The `--staged` flag limits processing to files in the Git index.

# Prerequisites
- biome-configuration: Must understand how to configure biome.json.

# Key Properties
1. Opt-in: requires both `vcs.enabled: true` and `vcs.clientKind: "git"`.
2. Enabling VCS alone does nothing -- individual features must also be enabled.
3. `vcs.useIgnoreFile: true` respects `.gitignore` and `.ignore` files.
4. `--changed` processes files that differ from `vcs.defaultBranch`.
5. `--since=<branch>` overrides `vcs.defaultBranch` for change detection.
6. `--staged` processes only files in the Git index (staged files).
7. `--staged` is not available with the `biome ci` command.
8. "Changed" is defined broadly -- even whitespace changes qualify.

# Construction / Recognition
To set up VCS integration:
1. Enable in config: `{ "vcs": { "enabled": true, "clientKind": "git" } }`.
2. For ignore files: add `"useIgnoreFile": true`.
3. For changed files: add `"defaultBranch": "main"`, then run `biome check --changed`.
4. For staged files: run `biome check --staged` (useful in pre-commit hooks).

# Context & Application
VCS integration is particularly useful in two scenarios: (1) ensuring Biome skips files already excluded by `.gitignore` (build outputs, dependencies), and (2) running Biome only on changed or staged files for faster feedback in development workflows and pre-commit hooks.

# Examples
From the source, full VCS configuration:

```json
{
  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": true,
    "defaultBranch": "main"
  }
}
```

Processing only changed files:
```shell
biome check --changed
```

Processing changes against a specific branch:
```shell
biome check --changed --since=next
```

Processing only staged files:
```shell
biome check --staged
```

(From guides/integrate-in-vcs.mdx)

# Relationships
## Builds Upon
- biome-configuration
## Enables
- git-hooks-integration (staged file processing is key to git hooks)
- biome-ci-command (CI uses --changed automatically with VCS)
## Related
- file-includes-and-excludes (VCS ignore is an alternative file exclusion method)
- biome-cli (--changed and --staged are CLI flags)
## Contrasts With
None.

# Common Errors
1. Enabling `vcs.enabled` without setting `vcs.clientKind`, which results in no VCS functionality.
2. Using `--staged` with `biome ci` -- it is not supported because CI has no concept of staged files.
3. Expecting `--changed` to detect only meaningful code changes -- any modification including whitespace triggers it.

# Common Confusions
1. Thinking VCS integration is enabled by default -- it requires explicit opt-in.
2. Confusing `--changed` (diff against a branch) with `--staged` (files in the Git index).

# Source Reference
- guides/integrate-in-vcs.mdx, all sections

# Verification Notes
Thoroughly documented with configuration and CLI examples. High confidence.
