---
# === CORE IDENTIFICATION ===
concept: ES6 Named Exports
slug: es6-named-exports

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
  - "named module exports"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - es6-module-system
extends: []
related:
  - es6-default-export
  - es6-import-statement
  - renaming-imports-exports
contrasts_with:
  - es6-default-export
  - commonjs-module-exports

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes named exports from default exports in ES6 modules?"
---

# Quick Definition

ES6 module exports where each exported value has an explicit name, declared by prefixing `export` to a declaration or using `export { name1, name2 }` syntax.

# Core Definition

Named exports allow a module to export multiple values, each identified by name. "To export a constant, variable, function, or class from an ES6 module, simply add the keyword export before the declaration" (p. 274). Alternatively, all exports can be declared in a single statement at the end of the module: `export { Circle, degreesToRadians, PI }`.

# Prerequisites

- **es6-module-system** — Named exports are part of the ES6 module system

# Key Properties

1. Each export has an explicit name used by importers
2. Can be declared inline with `export` before a declaration
3. Can be declared in a single `export { ... }` statement (not an object literal)
4. A module can have any number of named exports
5. `export` can only appear at the top level of a module

# Construction / Recognition

Inline exports:
```js
export const PI = Math.PI;
export function degreesToRadians(d) { return d * PI / 180; }
export class Circle { constructor(r) { this.r = r; } }
```

Grouped export statement:
```js
export { Circle, degreesToRadians, PI };
```

# Context & Application

Used when a module needs to expose multiple values. Importers can selectively import only the names they need, enabling tree-shaking by bundlers.

# Examples

From the source text (p. 274): Both inline and grouped export forms are shown for a geometry module exporting `PI`, `degreesToRadians`, and `Circle`.

# Relationships

## Builds Upon
- **ES6 Module System** — Named exports are a fundamental part of ES6 modules

## Enables
- **ES6 Import Statement** — Named exports are consumed via `import { name } from ...`
- **Renaming Imports/Exports** — Named exports can be renamed with `as` keyword

## Contrasts With
- **ES6 Default Export** — Default exports are unnamed; named exports require explicit names
- **CommonJS module.exports** — CommonJS assigns to `exports.name`; ES6 uses `export` keyword

# Common Errors

- **Error**: Thinking `export { Circle, PI }` creates an object literal.
  **Correction**: The curly braces in export statements are special syntax, not object literal notation. You cannot use expressions or computed properties.

# Common Confusions

- **Confusion**: Attempting `export { Math.sin as sin }` — using expressions in export lists.
  **Clarification**: Export lists require single identifiers before `as`, not expressions. This is a SyntaxError.

# Source Reference

Chapter 10: Modules, Section 10.3.1, pages 274-275.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High — clearly defined with examples
- Uncertainties: None
- Cross-reference status: Verified
