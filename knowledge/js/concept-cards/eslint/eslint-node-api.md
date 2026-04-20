---
# === CORE IDENTIFICATION ===
concept: ESLint Node.js API
slug: eslint-node-api

# === CLASSIFICATION ===
category: integration
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "integrate/nodejs-api.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint programmatic API"
  - "ESLint JS API"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint-getting-started
extends: []
related:
  - eslint-class
  - eslint-linter-class
  - eslint-integration-tutorial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use ESLint programmatically from Node.js?"
  - "What is the difference between the ESLint class and the Linter class?"
  - "What other exports does the eslint package provide?"
---

# Quick Definition
The ESLint Node.js API provides programmatic access to linting via three main exports: the `ESLint` class (file-system-dependent), the `Linter` class (browser-compatible), and utility classes like `SourceCode`, `RuleTester`, and `loadESLint()`.

# Core Definition
The Node.js API is designed for plugin and tool authors who need ESLint functionality without the CLI. The package exports several key classes: `ESLint` (the primary class for Node.js, depends on `fs` and the file system), `Linter` (a lightweight class that parses and reports without filesystem access, suitable for browsers), `SourceCode` (represents parsed source code with AST), and `RuleTester` (utility for writing rule tests). The `loadESLint()` function supports integrations that need to handle both flat config and legacy config systems, returning the appropriate `ESLint` constructor based on options. Only documented API surfaces are considered stable.

# Prerequisites
- eslint-getting-started -- Must have ESLint installed

# Key Properties
1. **ESLint class** -- Primary class for Node.js; depends on filesystem; supports `lintFiles()`, `lintText()`, `loadFormatter()`, `calculateConfigForFile()`, `outputFixes()`
2. **Linter class** -- Lightweight, browser-compatible; no filesystem access; uses `verify()` and `verifyAndFix()`
3. **SourceCode** -- Represents parsed source code with AST; can be passed to `Linter#verify()`
4. **RuleTester** -- Utility for writing tests for ESLint rules
5. **loadESLint()** -- Returns the correct ESLint class for flat config (`useFlatConfig: true`) or legacy config (`useFlatConfig: false`)
6. **Stability guarantee** -- Only documented parts of the API are stable; undocumented parts may change without notice

# Construction / Recognition
```js
// ESLint class (file-system-dependent)
const { ESLint } = require("eslint");
const eslint = new ESLint({ fix: true });
const results = await eslint.lintFiles(["lib/**/*.js"]);

// Linter class (browser-compatible)
const { Linter } = require("eslint");
const linter = new Linter();
const messages = linter.verify("var foo;", { rules: { semi: 2 } });

// loadESLint for version-agnostic integrations
const { loadESLint } = require("eslint");
const DefaultESLint = await loadESLint();
```

# Context & Application
The Node.js API powers editor integrations, custom linter tools, code review automation, learning platforms, and bundler plugins. The `ESLint` class is the standard choice for server-side tools; the `Linter` class enables browser-based linting (e.g., eslint.org/demo). The `loadESLint()` function is essential for integrations that must support multiple ESLint versions.

# Examples
From integrate/nodejs-api.md:
- Basic linting with `ESLint` class: create instance, call `lintFiles()`, load formatter, output results
- Autofix workflow: create `ESLint({ fix: true })`, call `lintFiles()`, then `ESLint.outputFixes(results)`
- `lintText()`: lint a string of code with `eslint.lintText(code)`
- `Linter#verify()`: `linter.verify("var foo;", { rules: { semi: 2 } }, { filename: "foo.js" })`

# Relationships
## Builds Upon
- eslint-getting-started (ESLint must be installed)
## Contains
- eslint-class (file-system API)
- eslint-linter-class (browser-compatible API)
## Related
- eslint-integration-tutorial (walkthrough of building an integration)
- eslint-built-in-formatters (loaded via `eslint.loadFormatter()`)

# Common Errors
1. Using the `ESLint` class in the browser -- it depends on Node.js `fs`; use `Linter` instead
2. Relying on undocumented API surfaces -- these may change without notice between versions

# Common Confusions
1. **ESLint class vs Linter class** -- `ESLint` is for Node.js (reads config files, accesses filesystem); `Linter` is for in-memory linting (no filesystem, browser-compatible)
2. **loadESLint() necessity** -- Only needed if your integration must support both flat config and legacy eslintrc systems

# Source Reference
- integrate/nodejs-api.md: Complete API reference for ESLint class, Linter class, SourceCode, RuleTester, and loadESLint()
- integrate/index.md: Overview of integration approaches

# Verification Notes
Comprehensive source documentation with full type signatures and examples. High confidence.
