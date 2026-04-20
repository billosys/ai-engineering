---
# === CORE IDENTIFICATION ===
concept: ES6 Default Export
slug: es6-default-export

# === CLASSIFICATION ===
category: modules
subcategory: es6-modules
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Modules"
chapter_number: 10
pdf_page: 274
section: "10.3.1 ES6 Exports"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "default module export"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - es6-module-system
extends: []
related:
  - es6-named-exports
  - es6-import-statement
contrasts_with:
  - es6-named-exports

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes named exports from default exports in ES6 modules?"
---

# Quick Definition

An ES6 module export using `export default` that designates a single primary value for the module, which importers can assign any local name to without curly braces.

# Core Definition

"It is common to write modules that export only one value (typically a function or class), and in this case, we usually use export default instead of export" (p. 274). Default exports are "slightly easier to import than non-default exports." A module can have at most one default export. Unlike named exports, `export default` can export anonymous expressions including anonymous functions and object literals.

# Prerequisites

- **es6-module-system** — Default exports are part of the ES6 module system

# Key Properties

1. A module can have only one default export
2. The exported value does not need a name in the exporting module
3. Importers choose the local name: `import MyName from './module.js'`
4. Can export anonymous functions, classes, or object literals
5. Can coexist with named exports (uncommon)

# Construction / Recognition

```js
export default class BitSet {
    // implementation omitted
}
```

# Context & Application

Used when a module has a single primary purpose — one class, one function, or one value. Makes imports simpler since no curly braces or name matching is required.

# Examples

From the source text (p. 274): `export default class BitSet { ... }`. When importing: `import BitSet from './bitset.js'` — the importer chooses the name `BitSet`.

# Relationships

## Builds Upon
- **ES6 Module System** — Default exports are part of ES6 module syntax

## Enables
- **ES6 Import Statement** — Simplified import syntax without curly braces

## Contrasts With
- **ES6 Named Exports** — Named exports require matching names and curly braces when importing; default exports let the importer choose any name

# Common Errors

- **Error**: Having more than one `export default` in a module.
  **Correction**: A module can only have one default export. Use named exports for additional values.

# Common Confusions

- **Confusion**: Thinking curly braces after `export default` work like the `export { }` grouping syntax.
  **Clarification**: With `export default`, curly braces create an actual object literal. With plain `export`, curly braces are special export syntax listing identifiers.

# Source Reference

Chapter 10: Modules, Section 10.3.1, pages 274-275.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High — clearly explained
- Uncertainties: None
- Cross-reference status: Verified
