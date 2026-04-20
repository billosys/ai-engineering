---
# === CORE IDENTIFICATION ===
concept: Renaming Imports and Exports
slug: renaming-imports-exports

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
pdf_page: 277
section: "10.3.3 Imports and Exports with Renaming"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "import as"
  - "export as"
  - "module aliasing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - es6-import-statement
  - es6-named-exports
extends: []
related:
  - re-exports
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes named exports from default exports in ES6 modules?"
---

# Quick Definition

The `as` keyword in ES6 `import` and `export` statements that allows renaming identifiers to avoid naming conflicts or provide more descriptive names.

# Core Definition

When two modules export values with the same name, or when an imported name conflicts with a local identifier, the `as` keyword allows renaming. On import: `import { render as renderImage } from "./imageutils.js"`. On export: `export { layout as calculateLayout }`. The keyword `default` can be used as a placeholder: `import { default as Histogram } from "./hist.js"`.

# Prerequisites

- **es6-import-statement** — Renaming applies to import statements
- **es6-named-exports** — Renaming applies to named exports

# Key Properties

1. Import renaming: `import { name as localName } from ...`
2. Export renaming: `export { localName as exportedName }`
3. Default exports can be imported via renaming: `import { default as Name } from ...`
4. Only single identifiers allowed before `as` (not expressions)

# Construction / Recognition

```js
import { render as renderImage } from "./imageutils.js";
import { render as renderUI } from "./ui.js";
export { layout as calculateLayout, render as renderLayout };
import { default as Histogram, mean, stddev } from "./histogram-stats.js";
```

# Context & Application

Essential when consuming modules that export conflicting names, or when a module's internal names are too terse for external use.

# Examples

From the source text (p. 277): Disambiguating two `render` functions from different modules by renaming them to `renderImage` and `renderUI`. Also shows `import { default as Histogram, mean, stddev }` as an alternative way to import both default and named exports.

# Relationships

## Builds Upon
- **ES6 Import Statement** — Renaming is a feature of the import syntax
- **ES6 Named Exports** — Renaming is a feature of the export syntax

## Related
- **Re-exports** — Re-exports frequently use renaming with `as`

# Common Errors

- **Error**: Attempting `export { Math.sin as sin }` — using an expression instead of an identifier.
  **Correction**: Only simple identifiers are allowed before `as` in export statements.

# Common Confusions

- **Confusion**: Thinking `as` in import/export works like `as` in Python imports.
  **Clarification**: They are similar in purpose (aliasing), but JavaScript requires the `as` keyword inside curly braces, while Python uses it directly after the module name.

# Source Reference

Chapter 10: Modules, Section 10.3.3, pages 277-278.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — clearly explained with examples
- Uncertainties: None
- Cross-reference status: Verified
