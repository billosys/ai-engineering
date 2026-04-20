---
# === CORE IDENTIFICATION ===
concept: '"use strict" Directive'
slug: use-strict

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
pdf_page: 139
section: '5.6.3 "use strict"'

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "strict mode"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expression-statements
extends: []
related:
  - eval-function
  - delete-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `"use strict"` directive enables strict mode, a restricted subset of JavaScript that fixes language deficiencies, provides stronger error checking, and increases security. Code in ES6 modules and class bodies is automatically strict.

# Core Definition

"'use strict' is a *directive* introduced in ES5. Directives are not statements (but are close enough)." "The purpose of a 'use strict' directive is to indicate that the code that follows (in the script or function) is *strict code*." "Any code in a class body or in an ES6 module is automatically strict code." (Ch. 5, §5.6.3)

# Prerequisites

- **expression-statements** — The directive looks like an expression statement (a string literal).

# Key Properties

1. Must appear at the start of a script or function body, before any real statements.
2. In strict mode: `with` is forbidden, all variables must be declared, functions invoked as functions have `this` of `undefined`.
3. Assignments to non-writable properties and creation of properties on non-extensible objects throw TypeError.
4. `eval()` gets a private variable environment in strict mode.
5. `delete` on unqualified identifiers throws SyntaxError.
6. Duplicate property names in object literals and duplicate parameter names are SyntaxErrors.
7. Octal integer literals (0-prefixed) are not allowed.
8. `eval` and `arguments` cannot be reassigned.

# Construction / Recognition

```js
"use strict";   // At top of script or function body
```

# Context & Application

Strict mode is the recommended way to write JavaScript. In modern development, ES6 modules are automatically strict, so explicit `"use strict"` is mainly needed in non-module scripts.

# Examples

From the source text (§5.6.3, pp. 139-141):

```js
"use strict";
// All code in this script is strict

function f() {
    "use strict";
    // Code in this function is strict
}
```

Key strict mode behaviors:
- Assigning to undeclared variables throws ReferenceError (no implicit globals).
- `this` in plain function calls is `undefined` (not the global object).
- Deleting non-configurable properties throws TypeError.

# Relationships

## Builds Upon
- **expression-statements** — The directive is syntactically a string expression statement

## Enables
- Safer, more optimizable JavaScript execution

## Related
- **eval-function** — Strict mode restricts `eval()` behavior
- **delete-operator** — Strict mode changes `delete` error behavior

## Contrasts With
- No direct contrast — strict mode is a mode, not a concept to contrast

# Common Errors

- **Error**: Placing `"use strict"` after other statements in a function body.
  **Correction**: The directive must appear before any real statements to take effect.

# Common Confusions

- **Confusion**: Believing you always need `"use strict"` in modern code.
  **Clarification**: ES6 modules and class bodies are automatically strict. The directive is needed only in non-module scripts and legacy function bodies.

# Source Reference

Chapter 5: Statements, Section 5.6.3, pages 139-141.

# Verification Notes

- Definition source: Direct quote from §5.6.3
- Confidence rationale: High — comprehensive list of strict mode differences
- Uncertainties: None
- Cross-reference status: Verified
