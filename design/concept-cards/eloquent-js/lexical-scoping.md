---
# === CORE IDENTIFICATION ===
concept: Lexical Scoping
slug: lexical-scoping

# === CLASSIFICATION ===
category: functions
subcategory: binding-visibility
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Functions"
chapter_number: 3
pdf_page: null
section: "Nested scope"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - static scoping

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scope
  - nested-scope
extends:
  - scope
related:
  - closure
  - local-scope
  - global-scope
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does lexical scoping relate to closures?"
  - "What must I know before understanding closures?"
---

# Quick Definition

Lexical scoping means that the set of bindings visible inside a block is determined by the position of that block in the program text, not by when or how the code is called.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 3, lines 208-212 of 03-functions.md): "The set of bindings visible inside a block is determined by the place of that block in the program text. Each local scope can also see all the local scopes that contain it, and all scopes can see the global scope. This approach to binding visibility is called *lexical scoping*."

# Prerequisites

- **scope**: Lexical scoping is a rule for how scope works.
- **nested-scope**: Lexical scoping operates over nested scopes.

# Key Properties

1. Binding visibility is determined by the **textual position** of the code, not by runtime call patterns.
2. Each local scope can see all local scopes that **contain** it (outward only).
3. All scopes can see the global scope.
4. This is the foundation for closures in JavaScript.

# Construction / Recognition

## To Construct/Create:
Lexical scoping is not something you create -- it is a rule of the language. You leverage it by:
- Nesting functions inside functions.
- Referencing outer bindings from inner functions.

## To Identify/Recognize:
- Any time an inner function accesses a binding from an outer function, lexical scoping is at work.

# Context & Application

Lexical scoping is what makes closures possible. When a function references a binding from its enclosing scope, that reference is based on where the function is written (its lexical position), not where it is called. This is a fundamental design decision in JavaScript.

# Examples

**Example 1** (Ch 3, lines 183-205 of 03-functions.md):
```javascript
const hummus = function(factor) {
  const ingredient = function(amount, unit, name) {
    let ingredientAmount = amount * factor;
    // ...
  };
  // ...
};
```
The `ingredient` function can see `factor` because of lexical scoping -- `ingredient` is textually inside `hummus`.

# Relationships

## Builds Upon
- **scope** -- Lexical scoping defines how scope resolution works.
- **nested-scope** -- Lexical scoping operates across nested scopes.

## Enables
- **closure** -- Closures work because of lexical scoping: a function sees bindings from the scope where it was defined, not where it is called.

## Related
- **local-scope** -- Lexical scoping determines which local scopes are visible.
- **global-scope** -- All scopes can see the global scope under lexical scoping.

## Contrasts With
- None within this source (dynamic scoping is not discussed).

# Common Errors

- **Error**: Expecting a function to see bindings from the scope where it is called, not where it was defined.
  **Correction**: Under lexical scoping, a function sees the environment in which it was **created**, not the environment in which it is **called**.

# Common Confusions

- **Confusion**: Lexical scoping and closure are the same thing.
  **Clarification**: Lexical scoping is the rule; closure is the consequence. A closure is a function that uses lexical scoping to retain access to bindings from its enclosing scope.

# Source Reference

Chapter 3: Functions, Section "Nested scope", lines 208-212 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 208-212)
- Confidence rationale: Explicit definition with italicized term "lexical scoping"
- Cross-reference status: verified against closure section
