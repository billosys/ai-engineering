---
# === CORE IDENTIFICATION ===
concept: Scope
slug: scope

# === CLASSIFICATION ===
category: functions
subcategory: binding-visibility
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Functions"
chapter_number: 3
pdf_page: null
section: "Bindings and scopes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - binding scope
  - variable scope

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binding
extends: []
related:
  - local-scope
  - global-scope
  - block-scope
  - nested-scope
  - lexical-scoping
  - closure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is scope?"
  - "What must I know before understanding closures?"
---

# Quick Definition

Scope is the part of a program in which a binding is visible and can be referenced.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 3, lines 118-119 of 03-functions.md): "Each binding has a *scope*, which is the part of the program in which the binding is visible." The chapter summary (lines 946-951) adds: "A key part of understanding functions is understanding scopes. Each block creates a new scope. Parameters and bindings declared in a given scope are local and not visible from the outside."

# Prerequisites

- **binding**: Scope governs the visibility of bindings.

# Key Properties

1. Each binding has a scope that determines where it can be referenced.
2. Scopes are determined by the structure of the program text (lexical scoping).
3. `let` and `const` bindings are local to the block in which they are declared.
4. `var` bindings are visible throughout the entire enclosing function or global scope.
5. Each scope can "look out" into the scope around it.

# Construction / Recognition

## To Construct/Create:
Scopes are created by:
- Function bodies
- Blocks (`if`, `for`, `while`, standalone `{}`)
- Modules (discussed in Chapter 10)

## To Identify/Recognize:
- Any set of curly braces creates a new scope for `let` and `const`.
- Function definitions always create a new scope.

# Context & Application

Understanding scope is essential for writing correct JavaScript programs. It determines which bindings are accessible at any given point, how name conflicts are resolved, and forms the foundation for closures.

# Examples

**Example 1** (Ch 3, lines 142-148 of 03-functions.md):
```javascript
let x = 10;   // global
if (true) {
  let y = 20; // local to block
  var z = 30; // also global
}
```

**Example 2** (Ch 3, lines 158-168 of 03-functions.md) -- scope shadowing:
```javascript
const halve = function(n) {
  return n / 2;
};
let n = 10;
console.log(halve(100));
// → 50
console.log(n);
// → 10
```

# Relationships

## Builds Upon
- **binding** -- Scope governs binding visibility.

## Enables
- **local-scope** -- A specific type of scope.
- **global-scope** -- The outermost scope.
- **block-scope** -- Scope created by blocks.
- **nested-scope** -- Scopes within scopes.
- **lexical-scoping** -- The rule for determining scope.
- **closure** -- Relies on scope for captured bindings.

## Related
- **function-definition** -- Functions create new scopes.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Assuming `var` is block-scoped like `let`.
  **Correction**: `var` bindings are visible throughout the whole function in which they appear, or globally if not in a function.

# Common Confusions

- **Confusion**: Thinking inner scopes cannot access outer bindings.
  **Clarification**: "Each scope can 'look out' into the scope around it" -- inner scopes can see all bindings from containing scopes.

# Source Reference

Chapter 3: Functions, Section "Bindings and scopes", lines 115-168 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from line 118-119)
- Confidence rationale: Explicit definition with italicized term
- Cross-reference status: verified against nested-scope and closure sections
