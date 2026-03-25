---
# === CORE IDENTIFICATION ===
concept: Language Options
slug: language-options

# === CLASSIFICATION ===
category: configuration
subcategory: language settings
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/configure/language-options.md"
chapter_number: null
pdf_page: null
section: "Specify JavaScript Options"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - languageOptions
  - ecmaVersion
  - sourceType
  - parser options

# === TYPED RELATIONSHIPS ===
prerequisites:
  - configuration-objects
extends: []
related:
  - global-declarations
  - parser-configuration
  - rule-configuration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I set the ECMAScript version for ESLint?"
  - "What is the difference between module, commonjs, and script source types?"
  - "How do I enable JSX parsing in ESLint?"
  - "What parser options does the default ESLint parser support?"
---

# Quick Definition
Language options (`languageOptions`) configure how ESLint interprets JavaScript source code, including the ECMAScript version, module type, parser, parser options, and global variable declarations.

# Core Definition
The `languageOptions` property of a configuration object controls JavaScript-specific parsing settings. Its key sub-properties are `ecmaVersion` (which ECMAScript standard to support, defaulting to `"latest"`), `sourceType` (whether code is `"module"`, `"commonjs"`, or `"script"`, defaulting to `"module"` for `.js`/`.mjs` and `"commonjs"` for `.cjs`), `globals` (declared global variables), `parser` (the parser object, defaulting to Espree), and `parserOptions` (parser-specific options passed through to the parser).

# Prerequisites
- configuration-objects (languageOptions lives inside config objects)

# Key Properties
1. `ecmaVersion`: defaults to `"latest"`, can be a year (2015-present) or version number (3, 5)
2. `sourceType`: `"module"` (ESM, strict mode), `"commonjs"` (require, non-strict), `"script"` (shared global scope, non-strict)
3. `globals`: object mapping variable names to `"writable"`, `"readonly"`, or `"off"`
4. `parser`: parser object with `parse()` or `parseForESLint()` method (default: Espree)
5. `parserOptions`: parser-specific options; for Espree, includes `ecmaFeatures` (`jsx`, `globalReturn`, `impliedStrict`) and `allowReserved`
6. ESLint automatically passes `ecmaVersion` and `sourceType` to all parsers

# Construction / Recognition
Configuring ECMAScript 5 with script mode:
```js
export default defineConfig([{
  languageOptions: {
    ecmaVersion: 5,
    sourceType: "script",
  },
}]);
```

Enabling JSX parsing:
```js
export default defineConfig([{
  languageOptions: {
    parserOptions: {
      ecmaFeatures: { jsx: true },
    },
  },
}]);
```

# Context & Application
Language options are essential when linting projects that target older ECMAScript versions, use CommonJS modules, or need JSX support. They are also the entry point for configuring custom parsers like `@typescript-eslint/parser` or `@babel/eslint-parser`.

# Examples
From `use/configure/language-options.md`: JSX support does not imply React support -- `eslint-plugin-react` is needed for React-specific semantics.

From `use/configure/parser.md`: Custom parsers are set via `languageOptions.parser`, with parser-specific options in `languageOptions.parserOptions`.

# Relationships
## Builds Upon
- configuration-objects (languageOptions is a property of config objects)

## Enables
- global-declarations (globals are set within languageOptions)
- parser-configuration (parser and parserOptions within languageOptions)

## Related
- rule-configuration (rules depend on correct language options for accurate analysis)

# Common Errors
1. Setting `ecmaVersion` to 5 while using `sourceType: "module"` (modules require ES6+)
2. Thinking JSX support means React support (need eslint-plugin-react separately)
3. Not setting `sourceType: "commonjs"` for Node.js require()-based code

# Common Confusions
1. Confusing `ecmaVersion` (syntax/globals support) with `sourceType` (module system)
2. Not realizing that `parserOptions` content depends entirely on which parser is being used

# Source Reference
- `sources-md/eslint/use/configure/language-options.md`, sections "Specify JavaScript Options", "Specify Parser Options"
- `sources-md/eslint/use/configure/configuration-files.md`, section "Configuration Objects" (languageOptions property listing)

# Verification Notes
Extracted from language options and configuration files documentation. Default values confirmed against docs.
