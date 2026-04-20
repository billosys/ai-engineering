---
# === CORE IDENTIFICATION ===
concept: JavaScript Naming Conventions
slug: naming-conventions

# === CLASSIFICATION ===
category: syntax-fundamentals
subcategory: naming
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Syntax"
chapter_number: 9
pdf_page: null
section: "9.1.6 Casing styles"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - casing conventions
  - naming styles

# === TYPED RELATIONSHIPS ===
prerequisites:
  - identifiers
extends: []
related:
  - reserved-words
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What naming conventions does JavaScript use?"
---

# Quick Definition

JavaScript uses camelCase for most names (variables, functions, methods), PascalCase for classes, ALL_CAPS for constants, and dash-case for module filenames and CSS.

# Core Definition

JavaScript follows specific casing conventions (Ch. 9, &sect;9.1.6-9.1.8): camelCase for functions, variables, and methods (`myFunction`, `obj.myMethod`); PascalCase for classes (`MyClass`); ALL_CAPS underscore case for shared constants (`MY_CONSTANT`); dash-case for CSS names and module filenames (`my-utility-class`, `the-special-library.mjs`). Underscore prefix (`_`) indicates unused parameters or private properties.

# Prerequisites

- **identifiers** -- naming conventions apply to identifiers

# Key Properties

1. camelCase: functions, variables, methods (`myFunction`)
2. PascalCase: classes (`MyClass`)
3. ALL_CAPS: constants shared between modules (`MY_CONSTANT`)
4. dash-case (kebab case): CSS names, module filenames
5. `_` prefix: unused parameters or private properties
6. `$` prefix: sometimes used for library variables (e.g., jQuery)

# Construction / Recognition

```js
const myVariable = 1;          // camelCase
function myFunction() {}       // camelCase
class MyClass {}               // PascalCase
const MY_CONSTANT = 42;        // ALL_CAPS
import * as lib from './the-special-library.mjs'; // dash-case file
arr.map((_x, i) => i);        // _ for unused params
```

# Context & Application

Following naming conventions makes code readable and consistent with the broader JavaScript community.

# Examples

From the source text (Ch. 9, &sect;9.1.6-9.1.8):
- `myFunction`, `obj.myMethod` (camelCase)
- `MyClass` (PascalCase)
- `MY_CONSTANT` (ALL_CAPS)
- `arr.map((_x, i) => i)` (underscore for unused params)
- `this._value` (underscore prefix for private properties)

# Relationships

## Builds Upon
- **identifiers** -- conventions for how to style identifiers

## Enables
- Code readability and community consistency

## Related
- **reserved-words** -- words to avoid when naming

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using PascalCase for regular functions or camelCase for classes.
  **Correction**: PascalCase is reserved for classes/constructors; regular functions use camelCase.

# Common Confusions

- **Confusion**: Not knowing when to use ALL_CAPS vs. camelCase for constants.
  **Clarification**: ALL_CAPS is for shared/module-level constants; local `const` variables use camelCase.

# Source Reference

Chapter 9: Syntax, Sections 9.1.6-9.1.8, lines 466-535.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit listing with examples
- Cross-reference status: verified
