---
# === CORE IDENTIFICATION ===
concept: Global Scope
slug: global-scope

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
  - global bindings
  - global environment

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scope
  - binding
extends:
  - scope
related:
  - local-scope
  - block-scope
contrasts_with:
  - local-scope

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is scope?"
---

# Quick Definition

Global scope is the scope of bindings defined outside of any function, block, or module, making them visible throughout the entire program.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 3, lines 119-122 of 03-functions.md): "For bindings defined outside of any function, block, or module, the scope is the whole program -- you can refer to such bindings wherever you want. These are called *global*."

# Prerequisites

- **scope**: Global scope is a type of scope.
- **binding**: Global bindings are accessible throughout the program.

# Key Properties

1. Global bindings are visible from anywhere in the program.
2. `var` bindings not inside a function end up in the global scope.
3. Too many global bindings "pollute" the namespace (Ch 4, line 1111).
4. The `Math` object exists to avoid putting math functions in global scope.

# Construction / Recognition

## To Construct/Create:
- Declare a binding outside any function, block, or module.
- Use `var` outside of a function.

## To Identify/Recognize:
- A binding accessible from any part of the program.

# Context & Application

Global scope is necessary for certain shared values, but overuse leads to namespace pollution and accidental overwrites. The `Math` object (Ch 4) demonstrates the pattern of using objects as namespaces to avoid excess globals.

# Examples

**Example 1** (Ch 3, lines 142-148 of 03-functions.md):
```javascript
let x = 10;   // global
if (true) {
  let y = 20; // local to block
  var z = 30; // also global
}
```

# Relationships

## Builds Upon
- **scope** -- Global scope is a specific type of scope.

## Enables
- All code can reference global bindings.

## Related
- **local-scope** -- Provides isolation from global scope.
- **block-scope** -- `let`/`const` are block-scoped, not global even at top of a block.

## Contrasts With
- **local-scope** -- Local bindings are restricted to their function/block; global bindings are not.

# Common Errors

- **Error**: Using `var` inside a block and expecting it to be block-scoped.
  **Correction**: `var` is visible throughout the enclosing function or, if not in a function, the global scope.

# Common Confusions

- **Confusion**: Thinking `let` at the top level of a file is the same as `var` at the top level.
  **Clarification**: While both may be accessible widely, `let` is block-scoped and `var` is function/global-scoped, which matters inside blocks.

# Source Reference

Chapter 3: Functions, Section "Bindings and scopes", lines 118-140 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 119-122)
- Confidence rationale: Explicit definition with italicized term "global"
- Cross-reference status: verified within chapter
