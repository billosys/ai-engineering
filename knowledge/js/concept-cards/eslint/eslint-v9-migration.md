---
# === CORE IDENTIFICATION ===
concept: ESLint v9 Migration
slug: eslint-v9-migration

# === CLASSIFICATION ===
category: migration
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/migrate-to-9.0.0.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "migrate to ESLint v9"
  - "ESLint 9 breaking changes"
  - "ESLint v9.0.0 migration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - configuration-files
extends: []
related:
  - flat-config-migration
  - eslint-v10-migration
  - plugin-migration-flat-config
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the breaking changes in ESLint v9?"
  - "How do I migrate from ESLint v8 to v9?"
  - "What happened to eslintrc in v9?"
  - "What Node.js versions does ESLint v9 support?"
  - "What context methods were removed in v9?"
---

# Quick Definition
ESLint v9 is a major release that makes flat config (`eslint.config.js`) the default configuration format, drops Node.js < v18.18 support, removes several deprecated features, and introduces breaking changes for users, plugin developers, and integration developers.

# Core Definition
ESLint v9.0.0 is a major release with breaking changes across three audiences: users, plugin developers, and integration developers. The most significant change is making `eslint.config.js` (flat config) the default configuration format, deprecating eslintrc. Other major user-facing changes include: dropping Node.js < v18.18 and v19 support; removing formatters (checkstyle, compact, jslint-xml, junit, tap, unix, visualstudio) to separate packages; removing `require-jsdoc` and `valid-jsdoc` rules; updating `eslint:recommended` (adding `no-constant-binary-expression`, `no-empty-static-block`, `no-new-native-nonconstructor`, `no-unused-private-class-members`; removing `no-extra-semi`, `no-inner-declarations`, `no-mixed-spaces-and-tabs`, `no-new-symbol`); and making `--quiet` skip execution of warn-level rules for performance.

For plugin developers, v9 removes several `context` methods (replaced by properties), removes `sourceCode.getComments()`, removes `CodePath#currentSegments`, requires `meta.schema` for rules with options, renames `FlatRuleTester` to `RuleTester`, and drops function-style rules.

For integration developers, `FlatESLint` becomes `ESLint`, and `Linter` expects flat config format.

# Prerequisites
- eslint: Basic ESLint knowledge
- configuration-files: Understanding of ESLint configuration

# Key Properties
1. **Flat config default** -- `eslint.config.js` is the new default; eslintrc is deprecated (set `ESLINT_USE_FLAT_CONFIG=false` to keep using it)
2. **Node.js v18.18+ required** -- Drops support for Node.js < v18.18 and v19
3. **Formatters externalized** -- Seven formatters moved to separate npm packages
4. **Context methods deprecated** -- `context.getSourceCode()`, `context.getFilename()`, etc. deprecated in favor of properties
5. **eslint:recommended updated** -- Four rules added, four removed
6. **--quiet optimization** -- Rules set to "warn" are no longer executed when using `--quiet`
7. **Stricter rule schemas** -- `meta.schema` is now required for rules with options
8. **Function-style rules removed** -- Rules must use object format with `create()` method

# Construction / Recognition
- Update Node.js to v18.18.0 or above
- Migrate configuration following the Configuration Migration Guide
- Replace removed formatters with npm packages (e.g., `eslint-formatter-checkstyle`)
- Replace `require-jsdoc`/`valid-jsdoc` with `eslint-plugin-jsdoc`
- Update custom rules: replace `context.getSourceCode()` with `context.sourceCode`, etc.
- Update custom rules: ensure `meta.schema` is present if the rule accepts options
- Fix or disable newly-enabled `eslint:recommended` rules

# Context & Application
The v9 migration is a critical transition point for the ESLint ecosystem, as it begins the shift from the eslintrc configuration system to flat config. While eslintrc is still available via an environment variable, all new development targets flat config. Plugin authors and integration developers face the most significant API changes.

# Examples
From use/migrate-to-9.0.0.md:

Removed formatters and their replacements:
| Removed Formatter | Replacement Package |
|---|---|
| `checkstyle` | `eslint-formatter-checkstyle` |
| `compact` | `eslint-formatter-compact` |
| `junit` | `eslint-formatter-junit` |

Context method replacements for plugin developers:
- `context.getSourceCode()` -> `context.sourceCode`
- `context.getFilename()` -> `context.filename`
- `context.getCwd()` -> `context.cwd`

# Relationships
## Precedes
- eslint-v10-migration

## Related
- flat-config-migration
- plugin-migration-flat-config

## Contrasts With
- ESLint v8 (eslintrc default, function-style rules allowed, older Node.js support)

# Common Errors
1. Running ESLint v9 on Node.js < v18.18 -- will fail immediately
2. Not realizing `--quiet` now skips warn-level rule execution -- rules with side effects (e.g., `markVariableAsUsed()`) at "warn" level may not run
3. Having custom rules without `meta.schema` that accept options -- now produces an error

# Common Confusions
1. **eslintrc is deprecated, not removed** -- In v9, eslintrc still works with `ESLINT_USE_FLAT_CONFIG=false`; it is fully removed in v10
2. **FlatESLint vs ESLint** -- In v9, `FlatESLint` was renamed to `ESLint`; the old `ESLint` became `LegacyESLint`

# Source Reference
- use/migrate-to-9.0.0.md: Comprehensive v9 migration guide with all breaking changes

# Verification Notes
- High confidence: Detailed, official migration guide with categorized breaking changes
- Breaking change lists taken directly from the table of contents and individual sections
