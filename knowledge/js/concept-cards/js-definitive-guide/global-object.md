---
# === CORE IDENTIFICATION ===
concept: The Global Object
slug: global-object

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: variables
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 59
section: "3.7 The Global Object"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - globalThis
  - window
  - global
  - self

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object-type-overview
  - host-environments
extends: []
related:
  - var-declarations
  - nan-and-infinity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

The global object is a regular JavaScript object whose properties serve as the globally defined identifiers available to a program, including global constants (`undefined`, `Infinity`, `NaN`), global functions (`isNaN()`, `parseInt()`), constructor functions (`Date`, `Array`), and global objects (`Math`, `JSON`).

# Core Definition

"The global object is a regular JavaScript object that serves a very important purpose: the properties of this object are the globally defined identifiers that are available to a JavaScript program." When the interpreter starts, "it creates a new global object and gives it an initial set of properties" including global constants, functions, constructors, and objects. "ES2020 finally defines globalThis as the standard way to refer to the global object in any context." (pp. 59-60)

# Prerequisites

- **object-type-overview** — The global object is an object
- **host-environments** — Different host environments have different global objects

# Key Properties

1. Contains global constants: `undefined`, `Infinity`, `NaN`
2. Contains global functions: `isNaN()`, `parseInt()`, `eval()`
3. Contains constructor functions: `Date()`, `RegExp()`, `String()`, `Object()`, `Array()`
4. Contains global objects: `Math`, `JSON`
5. In Node: accessible as `global`
6. In browsers: the Window object serves as the global object, accessible as `window`
7. Web workers: accessible as `self`
8. ES2020: `globalThis` is the standard cross-environment reference
9. Variables declared with `var` (not `let`/`const`) become properties of the global object

# Construction / Recognition

The global object is created automatically by the JavaScript interpreter. Access it via:
```javascript
globalThis    // ES2020 standard, works everywhere
window        // Browser
global        // Node.js
self          // Web workers
```

# Context & Application

The global object is where all built-in functions and constants live. Understanding it is important for understanding variable scoping (especially `var`), and for accessing platform-specific APIs.

# Examples

From the source text (pp. 59-60):
- Global constants: `undefined`, `Infinity`, `NaN`
- Global functions: `isNaN()`, `parseInt()`, `eval()`
- Constructor functions: `Date()`, `RegExp()`, `String()`, `Object()`, `Array()`
- Global objects: `Math`, `JSON`

```javascript
// In Node:
global       // references the global object

// In browsers:
window       // references the global object (Window)

// ES2020 standard:
globalThis   // works in any context
```

# Relationships

## Builds Upon
- **object-type-overview** — The global object is an object
- **host-environments** — Each host environment provides a different global object

## Enables
- **var-declarations** — `var` at top level creates global object properties

## Related
- **nan-and-infinity** — NaN and Infinity are properties of the global object
- **var-declarations** — Global `var` declarations become global object properties

## Contrasts With
- None within this source

# Common Errors

- **Error**: Assuming `let` and `const` at the top level create global object properties.
  **Correction**: Only `var` at the top level creates properties of the global object. `let` and `const` do not.

# Common Confusions

- **Confusion**: `window` is available in all JavaScript environments.
  **Clarification**: `window` is browser-specific. Use `globalThis` (ES2020) for cross-environment compatibility.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.7, pages 59-60.

# Verification Notes

- Definition source: Direct quotes from pp. 59-60
- Confidence rationale: High — clearly defined
- Uncertainties: None
- Cross-reference status: Verified
