---
# === CORE IDENTIFICATION ===
concept: CommonJS module.exports
slug: commonjs-module-exports

# === CLASSIFICATION ===
category: modules
subcategory: node-modules
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Modules"
chapter_number: 10
pdf_page: 270
section: "10.2.1 Node Exports"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Node exports"
  - "exports object"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - commonjs-require
extends: []
related:
  - es6-named-exports
  - es6-default-export
contrasts_with:
  - es6-named-exports
  - es6-default-export

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does CommonJS (`require`) relate to ES6 modules (`import`)?"
---

# Quick Definition

The mechanism in Node's CommonJS module system for defining a module's public API, using either the `exports` object for multiple exports or `module.exports` for a single exported value.

# Core Definition

Node provides two ways to export values. For multiple exports, assign properties to the global `exports` object. For a single export (typically a function or class), assign directly to `module.exports`. "The default value of module.exports is the same object that exports refers to" (p. 271).

# Prerequisites

- **commonjs-require** — Understanding Node's module system is required to understand its export mechanism

# Key Properties

1. `exports` is a pre-defined global object in every Node module
2. `module.exports` defaults to the same object as `exports`
3. Assigning to `module.exports` replaces the entire exported value
4. Properties set on `exports` become properties of the module's return value

# Construction / Recognition

Multiple exports via `exports`:
```js
exports.mean = data => data.reduce(sum)/data.length;
exports.stddev = function(d) { /* ... */ };
```

Single export via `module.exports`:
```js
module.exports = class BitSet extends AbstractWritableSet { /* ... */ };
```

Export object at end of module:
```js
module.exports = { mean, stddev };
```

# Context & Application

Used in all Node.js modules that follow the CommonJS pattern. The choice between `exports` and `module.exports` depends on whether the module exposes multiple named values or a single value.

# Examples

From the source text (p. 270-271): Setting individual exports: `exports.mean = data => ...`. Replacing the entire export: `module.exports = class BitSet ...`. Exporting an object at the end: `module.exports = { mean, stddev }`.

# Relationships

## Builds Upon
- **CommonJS Require** — The export mechanism is the counterpart to require()

## Enables
- **Module consumption** — Other modules use require() to access these exports

## Contrasts With
- **ES6 Named Exports** — ES6 uses `export` keyword declarations rather than property assignment
- **ES6 Default Export** — ES6 uses `export default` rather than `module.exports =`

# Common Errors

- **Error**: Writing `exports = someValue` instead of `module.exports = someValue`.
  **Correction**: Assigning to `exports` only changes the local variable binding, not the actual module export. Always use `module.exports` when replacing the entire export.

# Common Confusions

- **Confusion**: Thinking `exports` and `module.exports` are always interchangeable.
  **Clarification**: They reference the same object initially, but if you assign a new value to `module.exports`, the `exports` variable still points to the original object and is no longer useful.

# Source Reference

Chapter 10: Modules, Section 10.2.1, pages 270-272.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — clearly explained with examples
- Uncertainties: None
- Cross-reference status: Verified
