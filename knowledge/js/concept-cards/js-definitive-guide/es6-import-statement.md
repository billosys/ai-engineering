---
# === CORE IDENTIFICATION ===
concept: ES6 Import Statement
slug: es6-import-statement

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
pdf_page: 275
section: "10.3.2 ES6 Imports"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - es6-module-system
  - es6-named-exports
  - es6-default-export
extends: []
related:
  - renaming-imports-exports
  - dynamic-import
contrasts_with:
  - commonjs-require

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does CommonJS (`require`) relate to ES6 modules (`import`)?"
  - "What distinguishes named exports from default exports in ES6 modules?"
---

# Quick Definition

The ES6 `import` declaration that brings exported values from other modules into the current module's scope, supporting default imports, named imports, namespace imports, and side-effect-only imports.

# Core Definition

The `import` keyword supports multiple forms: importing a default export (`import X from './mod.js'`), importing named exports (`import { a, b } from './mod.js'`), namespace imports (`import * as mod from './mod.js'`), and side-effect imports (`import './mod.js'`). Imports are hoisted, act as constants, and can only appear at the top level.

# Prerequisites

- **es6-module-system** — Imports are part of the ES6 module system
- **es6-named-exports** — Understanding what named exports are
- **es6-default-export** — Understanding what default exports are

# Key Properties

1. Imported bindings behave as constants (cannot be reassigned)
2. Imports are hoisted to the top of the module
3. Module specifiers must be string literals (not expressions or template literals)
4. Must start with `/`, `./`, or `../` (no bare specifiers in the standard)
5. Can combine default and named imports: `import Default, { named } from './mod.js'`

# Construction / Recognition

```js
import BitSet from './bitset.js';                    // Default import
import { mean, stddev } from './stats.js';            // Named imports
import * as stats from './stats.js';                  // Namespace import
import './analytics.js';                               // Side-effect only
import Histogram, { mean, stddev } from './hist.js';  // Combined
```

# Context & Application

Used at the top of every ES6 module to declare dependencies. The static nature enables bundlers to perform tree-shaking (removing unused exports).

# Examples

From the source text (p. 275-277): Namespace import creates an object: `import * as stats from "./stats.js"` then use `stats.mean()` and `stats.stddev()`. Side-effect import: `import "./analytics.js"` runs the module without importing any values.

# Relationships

## Builds Upon
- **ES6 Module System** — Imports are a core part of ES6 modules
- **ES6 Named Exports** — Named imports consume named exports
- **ES6 Default Export** — Default imports consume default exports

## Enables
- **Renaming Imports/Exports** — Imports can be renamed with `as`

## Contrasts With
- **CommonJS Require** — `require()` is a runtime function call; `import` is a static declaration

# Common Errors

- **Error**: Using a variable or template literal as the module specifier: `import x from someVar`.
  **Correction**: Module specifiers must be string literals. Use `import()` for dynamic module specifiers.

# Common Confusions

- **Confusion**: Thinking `import { x }` is destructuring assignment.
  **Clarification**: While it looks like destructuring, import syntax has different semantics — it binds to the live export bindings of the other module, not to a snapshot of values.

# Source Reference

Chapter 10: Modules, Section 10.3.2, pages 275-277.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — thorough treatment with all forms shown
- Uncertainties: None
- Cross-reference status: Verified
