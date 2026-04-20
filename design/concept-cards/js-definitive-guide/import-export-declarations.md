---
# === CORE IDENTIFICATION ===
concept: import and export Declarations
slug: import-export-declarations

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: statements
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Statements"
chapter_number: 5
pdf_page: 143
section: "5.7.4 import and export"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - "ES6 modules"
  - "module declarations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expression-statements
  - use-strict
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `import` and `export` declarations are used to share values between ES6 modules. A module is a file with its own global namespace; `export` makes values available and `import` brings them into the current module.

# Core Definition

"The import and export declarations are used together to make values defined in one module of JavaScript code available in another module. A module is a file of JavaScript code with its own global namespace, completely independent of all other modules." (Ch. 5, §5.7.4)

# Prerequisites

- **expression-statements** — Declarations are statement-like constructs.
- **use-strict** — Module code is automatically strict.

# Key Properties

1. `import` brings values from other modules into the current scope.
2. `export` makes values from the current module available to others.
3. Modules have their own global namespace, independent of other modules.
4. `export default` exports a single primary value.
5. Named exports use `export { name1, name2 }` or `export` as a declaration modifier.
6. Module code is automatically strict mode.

# Construction / Recognition

```js
import Circle from './geometry/circle.js';
import { PI, TAU } from './geometry/constants.js';
import { magnitude as hypotenuse } from './vectors/utils.js';

export { PI, TAU };
export const TAU = 2 * Math.PI;
export default class Circle { /* ... */ }
```

# Context & Application

Modules are the standard way to organize modern JavaScript code. They enable code reuse, encapsulation, and dependency management.

# Examples

From the source text (§5.7.4, pp. 143-144):

```js
import Circle from './geometry/circle.js';
import { PI, TAU } from './geometry/constants.js';
import { magnitude as hypotenuse } from './vectors/utils.js';

// geometry/constants.js
const PI = Math.PI;
const TAU = 2 * PI;
export { PI, TAU };

export const TAU = 2 * Math.PI;
export function magnitude(x,y) { return Math.sqrt(x*x + y*y); }
export default class Circle { /* class definition omitted here */ }
```

# Relationships

## Builds Upon
- **use-strict** — Modules are automatically strict

## Enables
- Modular code organization

## Related
- No related concepts within Chapters 4-6

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `import`/`export` in non-module scripts.
  **Correction**: These declarations only work in JavaScript modules (files loaded with `type="module"` or `.mjs` extensions).

# Common Confusions

- **Confusion**: Confusing default exports with named exports.
  **Clarification**: A module can have one `export default` (imported without braces) and many named exports (imported with braces).

# Source Reference

Chapter 5: Statements, Section 5.7.4, pages 143-144.

# Verification Notes

- Definition source: Direct quote from §5.7.4
- Confidence rationale: Medium — brief coverage; full details in Ch. 10
- Uncertainties: Complete semantics deferred to Ch. 10
- Cross-reference status: Unverified (Ch. 10 not in scope)
