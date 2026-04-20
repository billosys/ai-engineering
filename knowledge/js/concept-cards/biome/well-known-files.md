---
# === CORE IDENTIFICATION ===
concept: Well-Known Files
slug: well-known-files

# === CLASSIFICATION ===
category: configuration
subcategory: file parsing
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "guides/configure-biome.mdx"
chapter_number: null
pdf_page: null
section: "Well-known files"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "well known files"
  - "special JSON files"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-configuration
extends: []
related:
  - file-includes-and-excludes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does biome.json configuration relate to CLI options?"
---

# Quick Definition
Files that Biome recognizes by name rather than extension and parses with specific JSON settings (comments and/or trailing commas allowed or disallowed).

# Core Definition
Biome maintains a list of "well-known files" -- files identified by their filename rather than their extension -- that receive special JSON parsing treatment. These files fall into three categories based on their parsing tolerance: (1) strict JSON (no comments, no trailing commas), such as `.all-contributorsrc` and `.nycrc`; (2) JSON with comments only, such as `.eslintrc.json`, `tslint.json`, and `turbo.json`; (3) JSON with both comments and trailing commas, such as `tsconfig.json`, `jsconfig.json`, `deno.json`, and `.babelrc`. Additionally, all `.json` files under `.vscode/`, `.zed/`, and `.cursor/` project directories are parsed with full comment and trailing comma support.

# Prerequisites
- biome-configuration: Must understand how Biome handles different file types.

# Key Properties
1. Recognition is by exact filename, not by extension.
2. Three parsing tiers: strict JSON, comments-only JSON, and comments-plus-trailing-commas JSON.
3. Currently limited to JSON-like files, though the list may expand.
4. Editor configuration directories (`.vscode/`, `.zed/`, `.cursor/`) receive permissive parsing.
5. The parsing settings correspond to `json.parser.allowComments` and `json.parser.allowTrailingCommas`.

# Construction / Recognition
Well-known files are automatically recognized -- no user configuration is needed. If a file matches a known name, Biome applies the appropriate parsing rules. Users cannot add custom well-known files.

# Context & Application
This feature prevents parse errors when Biome encounters common ecosystem files that use non-standard JSON features. For example, `tsconfig.json` uses comments and trailing commas by convention, and Biome handles this automatically.

# Examples
From the source:
- Strict JSON: `.bowerrc`, `.nycrc`, `mcmod.info`
- Comments only: `.eslintrc.json`, `tslint.json`, `turbo.json`
- Comments and trailing commas: `tsconfig.json`, `jsconfig.json`, `deno.json`, `.babelrc`, `nx.json`

(From guides/configure-biome.mdx, "Well-known files" section)

# Relationships
## Builds Upon
- biome-configuration
## Enables
None directly.
## Related
- file-includes-and-excludes (well-known files interact with file selection)
## Contrasts With
None.

# Common Errors
1. Expecting Biome to parse a custom JSON-with-comments file correctly when it is not on the well-known list -- use `biome.jsonc` naming or configure `json.parser` options instead.

# Common Confusions
1. Assuming all `.json` files allow comments -- only specific well-known files and editor config directories do.

# Source Reference
- guides/configure-biome.mdx, "Well-known files" section

# Verification Notes
Complete list of well-known files is enumerated in the source. High confidence.
