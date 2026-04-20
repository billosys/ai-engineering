---
# === CORE IDENTIFICATION ===
concept: ESLint v10 Migration
slug: eslint-v10-migration

# === CLASSIFICATION ===
category: migration
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/migrate-to-10.0.0.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "migrate to ESLint v10"
  - "ESLint 10 breaking changes"
  - "ESLint v10.0.0 migration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - eslint-v9-migration
  - flat-config-migration
extends: []
related:
  - eslint-source-code-object
  - plugin-migration-flat-config
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the breaking changes in ESLint v10?"
  - "How do I migrate from ESLint v9 to v10?"
  - "What was removed in v10 that was deprecated in v9?"
  - "What Node.js versions does ESLint v10 support?"
---

# Quick Definition
ESLint v10 is a major release that removes eslintrc support entirely, drops Node.js < v20.19 support, introduces file-based config lookup, adds JSX reference tracking, and removes all deprecated v9 context methods and SourceCode methods.

# Core Definition
ESLint v10.0.0 completes the transition from eslintrc to flat config by removing all eslintrc support. Key user-facing changes include: dropping Node.js < v20.19, v21, and v23 (supporting v20.19+, v22.13+, v24+); updating `eslint:recommended` with three new rules (`no-unassigned-vars`, `no-useless-assignment`, `preserve-caught-error`); changing config file lookup to search from the linted file's directory upward (previously from cwd); making `eslint-env` comments report as errors; and dropping `FlatESLint`/`LegacyESLint` in favor of just `ESLint`.

For plugin developers, v10 removes all deprecated `context` members (`getCwd()`, `getFilename()`, `getPhysicalFilename()`, `getSourceCode()`, `parserOptions`, `parserPath`), removes deprecated `SourceCode` methods (`getTokenOrCommentBefore()`, `getTokenOrCommentAfter()`, `isSpaceBetweenTokens()`, `getJSDocComment()`), makes `Program` AST node range span the entire source text, requires fixer methods to accept string `text` arguments, adds JSX reference tracking to scope analysis, and adds new `ScopeManager` requirements including an `addGlobals()` method.

# Prerequisites
- eslint: Basic ESLint knowledge
- eslint-v9-migration: Understanding of v9 changes
- flat-config-migration: Must have already migrated to flat config

# Key Properties
1. **eslintrc fully removed** -- No more `.eslintrc` support; `ESLINT_USE_FLAT_CONFIG=false` no longer works
2. **Node.js v20.19+ required** -- Drops v18, v19, v21, v23
3. **File-based config lookup** -- Config files are found by searching from each linted file upward, not from cwd
4. **JSX reference tracking** -- `<Component>` in JSX is now tracked as a variable reference for scope analysis
5. **eslint-env comments are errors** -- `/* eslint-env */` comments are now reported as lint errors
6. **Deprecated context methods removed** -- All getter-style context methods removed; use property equivalents
7. **Deprecated SourceCode methods removed** -- Four methods removed with replacement patterns
8. **Program range expanded** -- `Program.range` now covers the entire source text including surrounding comments/whitespace
9. **Fixer text must be string** -- All fixer methods now throw `TypeError` for non-string text arguments
10. **eslint:recommended updated** -- Three new rules added

# Construction / Recognition
- Ensure Node.js v20.19.0+ is installed
- Remove all eslintrc files; use only `eslint.config.js`
- Remove all `eslint-env` comments from source files
- Replace deprecated context methods in custom rules:
  - `context.getCwd()` -> `context.cwd`
  - `context.getFilename()` -> `context.filename`
  - `context.getSourceCode()` -> `context.sourceCode`
- Replace deprecated SourceCode methods:
  - `getTokenOrCommentBefore()` -> `getTokenBefore(node, { includeComments: true })`
  - `isSpaceBetweenTokens()` -> `isSpaceBetween()`
- Use `eslint-transforms` utility for automated migration of context methods

# Context & Application
ESLint v10 represents the completion of the multi-version migration from eslintrc to flat config. It enforces the clean removal of all legacy APIs that were deprecated in v9. Teams that delayed their flat config migration must complete it before upgrading to v10.

# Examples
From use/migrate-to-10.0.0.md:

Context method replacements:
| Removed | Replacement |
|---|---|
| `context.getCwd()` | `context.cwd` |
| `context.getFilename()` | `context.filename` |
| `context.getSourceCode()` | `context.sourceCode` |
| `context.parserOptions` | `context.languageOptions` |
| `context.parserPath` | No replacement |

Automated migration:
```shell
npm install eslint-transforms -g
eslint-transforms v9-rule-migration rules/
```

JSX reference tracking example -- previously `Card` was "defined but never used":
```jsx
import { Card } from "./card.jsx";
export function createCard(name) {
  return <Card name={name} />;  // now correctly tracked as a reference
}
```

# Relationships
## Follows
- eslint-v9-migration

## Related
- flat-config-migration
- eslint-source-code-object
- plugin-migration-flat-config

## Contrasts With
- ESLint v9 (still supports eslintrc via env variable, deprecated methods still available)

# Common Errors
1. Upgrading to v10 without migrating to flat config -- eslintrc is completely removed
2. Not removing `eslint-env` comments -- they are now reported as errors, not silently ignored
3. Using `v10_config_lookup_from_file` feature flag -- it was a v9 feature flag that errors in v10

# Common Confusions
1. **Config lookup change** -- v10 searches for config from each file's directory upward, not from cwd; use `--config` to override
2. **JSX reference tracking** -- Rules like `no-unused-vars` may report differently for JSX components; remove workaround plugins like `@eslint-react/jsx-uses-vars`

# Source Reference
- use/migrate-to-10.0.0.md: Comprehensive v10 migration guide with all breaking changes

# Verification Notes
- High confidence: Detailed, official migration guide with categorized breaking changes by audience
- All breaking changes and replacements taken directly from the migration guide
