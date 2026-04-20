---
# === CORE IDENTIFICATION ===
concept: Flat Config Migration
slug: flat-config-migration

# === CLASSIFICATION ===
category: migration
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/configure/migration-guide.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "eslintrc to flat config migration"
  - "configuration migration"
  - "flat config migration guide"
  - "eslint.config.js migration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - configuration-files
extends: []
related:
  - eslint-v9-migration
  - eslint-v10-migration
  - plugin-migration-flat-config
contrasts_with:
  - eslintrc-configuration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I migrate from .eslintrc to eslint.config.js?"
  - "What are the key differences between eslintrc and flat config?"
  - "How do I import plugins in flat config?"
  - "How do I handle ignores in flat config?"
  - "How do I use FlatCompat for unconverted shareable configs?"
---

# Quick Definition
The migration from eslintrc format (.eslintrc.js/.eslintrc.json) to flat config format (eslint.config.js) replaces string-based plugin references with JavaScript imports, removes environments in favor of explicit globals, and restructures configuration into an exported array of config objects.

# Core Definition
Flat config is ESLint's new configuration system, which became the default in v9 and the only supported format in v10. The migration involves converting `.eslintrc.*` files to `eslint.config.js`. Key changes include: plugins and parsers are now imported as JavaScript modules rather than referenced by string name; the `env` property is replaced by importing globals from the `globals` npm package; `overrides` are replaced by multiple config objects with `files` patterns in the exported array; `extends` is replaced by importing and spreading shared configs; `.eslintignore` files are replaced by `ignores` properties in config objects; linter options like `noInlineConfig` and `reportUnusedDisableDirectives` move under a `linterOptions` key; and the `root` option no longer exists since flat config files act as if `root: true` is always set.

# Prerequisites
- eslint: Basic understanding of ESLint
- configuration-files: Understanding of ESLint configuration concepts

# Key Properties
1. **JavaScript module imports** -- Plugins and parsers are imported as JS modules instead of string references
2. **No more environments** -- The `env` property is replaced by explicit `globals` under `languageOptions`
3. **Array-based configuration** -- Config is an exported array of objects; each object can target specific file patterns via `files`
4. **Inline ignores** -- `.eslintignore` is replaced by `ignores` property in config objects (no separate file)
5. **No root option** -- Flat config always behaves as `root: true`
6. **defineConfig helper** -- The `defineConfig()` function from `eslint/config` provides type checking and convenience
7. **FlatCompat bridge** -- The `@eslint/eslintrc` package provides `FlatCompat` to translate unconverted eslintrc configs
8. **eslint-env comments removed** -- `/* eslint-env */` comments are no longer recognized; reported as errors in v10

# Construction / Recognition
- Use `@eslint/migrate-config` tool: `npx @eslint/migrate-config .eslintrc.json`
- Replace `plugins: ["jsdoc"]` with `import jsdoc from "eslint-plugin-jsdoc"` and `plugins: { jsdoc }`
- Replace `env: { browser: true }` with `languageOptions: { globals: { ...globals.browser } }`
- Replace `extends: ["eslint:recommended"]` with `import js from "@eslint/js"` and include `js.configs.recommended`
- Replace `overrides` with separate config objects in the array, each with `files` patterns
- Replace `.eslintignore` with `{ ignores: ["**/temp.js", "config/*"] }`

# Context & Application
This migration is essential for all ESLint users because the eslintrc format is deprecated in v9 and completely removed in v10. The flat config system provides better transparency (JavaScript imports instead of magical string resolution), better composability (arrays of config objects), and eliminates several categories of configuration confusion (cascading configs, plugin resolution issues).

# Examples
From use/configure/migration-guide.md:

eslintrc plugin loading:
```javascript
// .eslintrc.js
module.exports = {
  plugins: ["jsdoc"],
  rules: { "jsdoc/require-description": "error" }
};
```

Flat config equivalent:
```javascript
// eslint.config.js
import { defineConfig } from "eslint/config";
import jsdoc from "eslint-plugin-jsdoc";
export default defineConfig([{
  files: ["**/*.js"],
  plugins: { jsdoc },
  rules: { "jsdoc/require-description": "error" }
}]);
```

Using FlatCompat for unconverted configs:
```javascript
import { FlatCompat } from "@eslint/eslintrc";
const compat = new FlatCompat({ baseDirectory: __dirname });
export default defineConfig([
  ...compat.extends("eslint-config-my-config")
]);
```

# Relationships
## Enables
- eslint-v9-migration
- eslint-v10-migration

## Related
- plugin-migration-flat-config
- configuration-files

## Contrasts With
- eslintrc-configuration: The legacy format with string-based imports, cascading, and .eslintignore files

# Common Errors
1. Forgetting to install the `globals` package when replacing `env` configurations
2. Using `temp.js` in ignores instead of `**/temp.js` -- flat config ignores are relative to the config file
3. Not realizing dotfiles are no longer ignored by default in flat config

# Common Confusions
1. **eslint-env comments** -- These are not supported in flat config and are reported as errors in v10; use `globals` in config or `/* global */` comments instead
2. **package.json configuration** -- The `eslintConfig` key in package.json is not supported in flat config
3. **CLI flag changes** -- `--env`, `--ignore-path`, `--no-eslintrc`, `--resolve-plugins-relative-to`, and `--rulesdir` are no longer supported

# Source Reference
- use/configure/migration-guide.md: Comprehensive migration guide covering all differences between formats

# Verification Notes
- High confidence: Migration guide is a dedicated, detailed document covering all aspects of the transition
- Code examples taken directly from the source documentation
