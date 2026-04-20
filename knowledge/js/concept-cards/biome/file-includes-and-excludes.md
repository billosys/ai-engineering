---
# === CORE IDENTIFICATION ===
concept: File Includes and Excludes
slug: file-includes-and-excludes

# === CLASSIFICATION ===
category: configuration
subcategory: file selection
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "guides/configure-biome.mdx"
chapter_number: null
pdf_page: null
section: "Specifying files to process"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "files.includes"
  - "file filtering"
  - "negated patterns"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-configuration
extends: []
related:
  - vcs-integration
  - biome-cli
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I configure Biome to process only changed files?"
  - "How does VCS integration relate to file processing?"
---

# Quick Definition
The mechanism for controlling which files Biome processes, using `files.includes` glob patterns, tool-specific includes, negated patterns with `!`, and double-negated patterns with `!!` for indexed-file control.

# Core Definition
Biome provides three strategies for specifying which files to process: CLI arguments (explicit file/folder paths), configuration-based patterns (`files.includes` and `<tool>.includes` in `biome.json`), and VCS integration (ignore files). The `files.includes` field accepts glob patterns and applies globally across all tools. Individual tools can further refine their scope with `<tool>.includes`. Negated patterns prefixed with `!` exclude files from linting/formatting but keep them "indexed" (available for project analysis). Double-negated patterns prefixed with `!!` exclude files from all operations including indexing.

# Prerequisites
- biome-configuration: Must understand the structure of biome.json.

# Key Properties
1. `files.includes` applies to all tools (formatter, linter, assist).
2. Tool-specific `<tool>.includes` can only narrow -- never widen -- what `files.includes` permits.
3. Single negation `!` excludes from formatting/linting but keeps files indexed for project analysis.
4. Double negation `!!` excludes from all operations, including indexing.
5. Negated globs must be preceded by the `**` pattern in the includes array.
6. Paths in configuration are resolved relative to the config file's location.
7. Biome always ignores "protected files" like `package-lock.json`, `yarn.lock`, etc.
8. CLI glob patterns are expanded by the shell, not by Biome.

# Construction / Recognition
To configure file selection:
1. Set `files.includes` with positive globs for files to process: `["src/**/*.js", "test/**/*.js"]`.
2. Add `!` prefixed patterns to exclude from tools but keep indexed: `["**", "!**/*.generated.js"]`.
3. Add `!!` prefixed patterns to fully exclude: `["**", "!!**/dist"]`.
4. Use `<tool>.includes` for per-tool refinement: `"linter": { "includes": ["**", "!test/**"] }`.

# Context & Application
Essential for projects that need fine-grained control over which files are formatted, linted, or included in project analysis (e.g., type inference, import resolution). The indexing distinction (`!` vs `!!`) matters for type-aware lint rules that need to resolve imports from files that should not themselves be linted.

# Examples
From the source:

```json
{
  "files": {
    "includes": [
      "**",
      "!**/*.generated.js",
      "!!**/dist"
    ]
  }
}
```

This includes all files, excludes `*.generated.js` from formatting/linting (but keeps them indexed), and fully excludes the `dist/` folder from all operations.

A tool-specific refinement:

```json
{
  "files": {
    "includes": ["src/**/*.js", "test/**/*.js", "!**/*.min.js"]
  },
  "linter": {
    "includes": ["**", "!test/**"]
  }
}
```

Here, `biome lint test/` would lint nothing because `test/` is excluded by the linter's includes.

(From guides/configure-biome.mdx, "Specifying files to process" section)

# Relationships
## Builds Upon
- biome-configuration
## Enables
- vcs-integration (VCS ignore is another file-selection strategy)
## Related
- biome-cli (CLI file arguments are an alternative selection method)
## Contrasts With
None.

# Common Errors
1. Using `<tool>.includes` to include files not matched by `files.includes` -- this has no effect.
2. Forgetting the leading `**` pattern before negated globs.
3. Using `!` when `!!` is needed, leaving unwanted files in the project index.

# Common Confusions
1. Confusing `!` (exclude from tools but still indexed) with `!!` (exclude from everything).
2. Thinking CLI glob expansion is handled by Biome -- it is handled by the shell.
3. Assuming `files.includes` only affects one tool; it is global.

# Source Reference
- guides/configure-biome.mdx, "Specifying files to process" section

# Verification Notes
Explicitly documented with examples and semantic distinctions. High confidence.
