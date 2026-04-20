---
# === CORE IDENTIFICATION ===
concept: File Ignoring
slug: file-ignoring

# === CLASSIFICATION ===
category: configuration
subcategory: file targeting
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/configure/ignore.md"
chapter_number: null
pdf_page: null
section: "Ignore Files"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - ignoring files
  - global ignores
  - globalIgnores
  - eslint ignore patterns

# === TYPED RELATIONSHIPS ===
prerequisites:
  - configuration-objects
extends: []
related:
  - define-config-helper
  - combining-configurations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I ignore files and directories in ESLint flat config?"
  - "What is the difference between global and non-global ignores?"
  - "How do I use globalIgnores()?"
  - "How do I include .gitignore patterns in ESLint?"
  - "How do I unignore a previously ignored file?"
---

# Quick Definition
File ignoring in ESLint is configured via the `ignores` property in config objects or the `globalIgnores()` helper, using glob patterns to exclude files and directories from linting.

# Core Definition
ESLint supports two types of ignore patterns: global ignores and non-global ignores. Global ignores apply to every configuration object and are created either by a config object with only `ignores` (and optionally `name`) or via the `globalIgnores()` helper function. Non-global ignores are `ignores` patterns within a config object that also has other keys (like `rules`), applying only to that specific config object. Default ignores are `["**/node_modules/", ".git/"]`. Global ignores can match directories (e.g., `dir/`); non-global ignores can only match files or files within directories.

# Prerequisites
- configuration-objects (ignores is a property of config objects)

# Key Properties
1. `globalIgnores()` helper imported from `"eslint/config"` for clear global ignore intent
2. Default patterns: `["**/node_modules/", ".git/"]`
3. Global ignores: config object with only `ignores` (+ optional `name`), or `globalIgnores([...])`
4. Non-global ignores: `ignores` alongside other keys like `rules`, scoped to that config object only
5. Negation patterns (`!pattern`) can unignore previously ignored files
6. `includeIgnoreFile()` from `@eslint/compat` imports `.gitignore` patterns
7. `--ignore-pattern` CLI flag for command-line ignore patterns
8. Directory ignore uses trailing `/` (e.g., `dist/`); file ignore uses `**` (e.g., `dist/**`)
9. Pattern `dir/**` ignores entire directory and prevents unignoring contents; use `dir/**/*` to allow unignoring specific files

# Construction / Recognition
Global ignores with helper:
```js
import { defineConfig, globalIgnores } from "eslint/config";

export default defineConfig([
  globalIgnores([".config/", "dist/", "tsconfig.json"]),
]);
```

Unignoring specific files:
```js
globalIgnores([
  "build/**/*",        // ignore contents
  "!build/test.js",    // but keep this file
])
```

Including `.gitignore`:
```js
import { includeIgnoreFile } from "@eslint/compat";
const gitignorePath = fileURLToPath(new URL(".gitignore", import.meta.url));

export default defineConfig([
  includeIgnoreFile(gitignorePath),
]);
```

# Context & Application
File ignoring is used to exclude build artifacts, vendor directories, generated files, and other non-source files from linting. The `globalIgnores()` helper is the recommended approach for clarity, replacing the older pattern of a bare `{ ignores: [...] }` object.

# Examples
From `use/configure/ignore.md`: To ignore a directory except specific files at any depth, combine `dir/**/*` (ignore contents), `!dir/**/*/` (unignore subdirectories), and `!dir/**/test.js` (unignore specific files).

Unlike `.gitignore`, a pattern like `.config` only matches in the config file's directory. Use `**/.config/` for recursive matching.

# Relationships
## Builds Upon
- configuration-objects (ignores is a config object property)

## Enables
- Clean linting runs without noise from generated/vendor code

## Related
- define-config-helper (globalIgnores is a companion export)
- combining-configurations (ignores interact with config merging)

# Common Errors
1. Using `dir/**` instead of `dir/**/*` when wanting to unignore specific files inside the directory
2. Expecting `.gitignore`-style pattern behavior (ESLint uses minimatch, not gitignore syntax)
3. Using non-global ignores (with other keys) and expecting them to apply to all config objects

# Common Confusions
1. Thinking a bare `ignores` pattern like `.config` recursively matches (it only matches in the config file's directory)
2. Not understanding the `dir/**` vs `dir/**/*` distinction for unignoring nested files

# Source Reference
- `sources-md/eslint/use/configure/ignore.md`, all sections
- `sources-md/eslint/use/configure/configuration-files.md`, section "Globally ignore files with ignores"

# Verification Notes
Extracted from the ignore files documentation and configuration files documentation. The global vs non-global distinction and unignoring patterns verified against examples.
