---
# === CORE IDENTIFICATION ===
concept: Hoisting
slug: hoisting

# === CLASSIFICATION ===
category: functions
subcategory: execution-model
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Functions"
chapter_number: 3
pdf_page: null
section: "Declaration notation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - function hoisting

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declaration
  - scope
extends: []
related:
  - function-expression
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a function declaration from a function expression?"
---

# Quick Definition

Hoisting is the behavior where function declarations are conceptually moved to the top of their scope, allowing them to be called before they appear in the source code.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 277-284 of 03-functions.md): "The preceding code works, even though the function is defined *below* the code that uses it. Function declarations are not part of the regular top-to-bottom flow of control. They are conceptually moved to the top of their scope and can be used by all the code in that scope. This is sometimes useful because it offers the freedom to order code in a way that seems the clearest, without worrying about having to define all functions before they are used."

# Prerequisites

- **function-declaration**: Hoisting applies to function declarations.
- **scope**: Declarations are hoisted to the top of their scope.

# Key Properties

1. Only applies to function **declarations**, not function expressions or arrow functions.
2. The entire function (name and body) is available before the declaration in source order.
3. Allows flexible code ordering -- calling functions before defining them.
4. Does not apply to `let`/`const` bindings assigned function expressions.

# Construction / Recognition

## To Construct/Create:
Hoisting happens automatically for function declarations.

## To Identify/Recognize:
- A function being called before its declaration appears in the source code, with no error.

# Context & Application

Hoisting is useful for organizing code with high-level logic at the top and helper functions below, or for mutually recursive functions that need to reference each other.

# Examples

**Example 1** (Ch 3, lines 268-274 of 03-functions.md):
```javascript
console.log("The future says:", future());

function future() {
  return "You'll never have flying cars";
}
```
This works because the `future` declaration is hoisted.

# Relationships

## Builds Upon
- **function-declaration** -- Only declarations are hoisted.

## Enables
- Flexible code organization.
- Mutual recursion between declarations.

## Related
- **function-expression** -- Not hoisted, so order matters.

## Contrasts With
- None explicitly, but implicitly contrasts with function expression behavior.

# Common Errors

- **Error**: Expecting function expressions assigned to `let`/`const` to be hoisted.
  **Correction**: Only `function` declarations are hoisted. `const f = function() {}` is not available before the assignment.

# Common Confusions

- **Confusion**: All functions are hoisted.
  **Clarification**: Only function declarations (where `function` is the first word of a statement) are hoisted. Function expressions and arrow functions are not.

# Source Reference

Chapter 3: Functions, Section "Declaration notation", lines 265-284 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (paraphrased from lines 277-284)
- Confidence rationale: Explicit description of hoisting behavior
- Cross-reference status: verified against function-expression section
