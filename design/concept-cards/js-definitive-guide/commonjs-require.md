---
# === CORE IDENTIFICATION ===
concept: CommonJS Modules (require/exports)
slug: commonjs-require

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
section: "10.2 Modules in Node"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Node modules"
  - "require() modules"
  - "CJS modules"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - module-pattern-iife
extends:
  - module-pattern-iife
related:
  - es6-module-system
  - commonjs-module-exports
contrasts_with:
  - es6-module-system

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does CommonJS (`require`) relate to ES6 modules (`import`)?"
  - "How do I implement the module pattern in JavaScript?"
---

# Quick Definition

Node's built-in module system where each file is an independent module that imports dependencies with `require()` and exports its public API through the `exports` object or `module.exports`.

# Core Definition

In Node's CommonJS module system, "each file is an independent module with a private namespace. Constants, variables, functions, and classes defined in one file are private to that file unless the file exports them. And values exported by one module are only visible in another module if that module explicitly imports them" (p. 270). Modules import with `require()` and export by setting properties on `exports` or replacing `module.exports`.

# Prerequisites

- **module-pattern-iife** — CommonJS is an automated, standardized version of the IIFE module pattern

# Key Properties

1. Each file has a private namespace — top-level declarations are not global
2. `require()` is synchronous and returns the exported value
3. `exports` object for exporting multiple values; `module.exports` for exporting a single value
4. Module specifiers use filesystem paths (relative with `./` or absolute)
5. The `.js` suffix can be omitted in require() calls

# Construction / Recognition

Exporting multiple values:
```js
exports.mean = data => data.reduce(sum)/data.length;
exports.stddev = function(d) { /* ... */ };
```

Exporting a single class or function:
```js
module.exports = class BitSet extends AbstractWritableSet { /* ... */ };
```

Importing:
```js
const fs = require("fs");           // Built-in module
const stats = require('./stats.js'); // Local module
const { stddev } = require('./stats.js'); // Destructured import
```

# Context & Application

CommonJS is the dominant module system in Node.js. While ES6 modules are now supported in Node, the vast majority of existing Node code uses require(). Bundling tools like webpack also support this format for browser code.

# Examples

From the source text (p. 270-272): Importing a built-in Node module: `const fs = require("fs")`. Importing a local module with destructuring: `const { stddev } = require('./stats.js')`. Exporting a single object at end of module: `module.exports = { mean, stddev }`.

# Relationships

## Builds Upon
- **Module Pattern (IIFE + Closure)** — CommonJS automates the IIFE pattern at the file level

## Enables
- **CommonJS module.exports** — The mechanism for defining what a module exports

## Related
- **ES6 Module System** — The newer, standardized alternative now part of the language

## Contrasts With
- **ES6 Module System** — ES6 uses static `import`/`export` declarations; CommonJS uses dynamic `require()` calls

# Common Errors

- **Error**: Using `exports = { mean, stddev }` instead of `module.exports = { mean, stddev }`.
  **Correction**: Assigning to `exports` directly replaces the local variable reference, not the actual exports object. Use `module.exports` to replace the entire exported value.

# Common Confusions

- **Confusion**: Thinking `require()` works in web browsers without a bundler.
  **Clarification**: `require()` is a Node-specific function. Browser code needs a bundler like webpack to use CommonJS modules, or should use ES6 import/export instead.

# Source Reference

Chapter 10: Modules, Section 10.2, pages 270-273.

# Verification Notes

- Definition source: Direct quotes and synthesis from source text
- Confidence rationale: High — thoroughly described with clear examples
- Uncertainties: None
- Cross-reference status: Verified against section 10.1 and 10.3
