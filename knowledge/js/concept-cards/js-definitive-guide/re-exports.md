---
# === CORE IDENTIFICATION ===
concept: Re-exports
slug: re-exports

# === CLASSIFICATION ===
category: modules
subcategory: es6-modules
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Modules"
chapter_number: 10
pdf_page: 278
section: "10.3.4 Re-Exports"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "export from"
  - "barrel exports"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - es6-named-exports
  - es6-import-statement
extends: []
related:
  - renaming-imports-exports
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes named exports from default exports in ES6 modules?"
---

# Quick Definition

A combined import-and-export syntax using `export ... from` that allows a module to re-export values from other modules without importing them into its own scope.

# Core Definition

Re-exports combine import and export into a single statement: `export { mean } from "./stats/mean.js"`. This allows creating "barrel" modules that aggregate exports from multiple sub-modules. Wildcard re-exports (`export * from ...`) export all named values. Default exports can be re-exported with renaming: `export { default as mean } from "./stats/mean.js"`.

# Prerequisites

- **es6-named-exports** — Understanding named exports
- **es6-import-statement** — Understanding import syntax

# Key Properties

1. Values are not imported into the re-exporting module's scope
2. Supports renaming with `as`
3. Wildcard `export *` re-exports all named exports (not defaults)
4. Can re-export a default as named: `export { default as name } from ...`
5. Can re-export a named as default: `export { name as default } from ...`

# Construction / Recognition

```js
export { mean } from "./stats/mean.js";
export { stddev } from "./stats/stddev.js";
export * from "./stats/mean.js";
export { default as mean } from "./stats/mean.js";
export { mean as default } from "./stats.js";
```

# Context & Application

Used to create aggregate "index" modules that provide a convenient single import point for a library split across multiple files. Common in package main entry points.

# Examples

From the source text (p. 278-279): A `./stats.js` module that re-exports from sub-modules: `export { mean } from "./stats/mean.js"` and `export { stddev } from "./stats/stddev.js"`. Wildcard form: `export * from "./stats/mean.js"`. Re-exporting with rename: `export { mean, mean as average } from "./stats/mean.js"`.

# Relationships

## Builds Upon
- **ES6 Named Exports** — Re-exports forward named exports
- **ES6 Import Statement** — Re-exports are a combined import+export form

## Related
- **Renaming Imports/Exports** — Re-exports support `as` for renaming

# Common Errors

- **Error**: Expecting `export *` to also re-export the default export.
  **Correction**: Wildcard re-exports only forward named exports, not default exports. Default exports must be re-exported explicitly.

# Common Confusions

- **Confusion**: Thinking re-exported names are available in the re-exporting module's own code.
  **Clarification**: Re-exports do not create local bindings. The names pass through without being accessible in the re-exporting module itself.

# Source Reference

Chapter 10: Modules, Section 10.3.4, pages 278-279.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — multiple forms shown with clear examples
- Uncertainties: None
- Cross-reference status: Verified
