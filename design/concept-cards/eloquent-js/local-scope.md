---
# === CORE IDENTIFICATION ===
concept: Local Scope
slug: local-scope

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
  - local bindings
  - local variables
  - local environment

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scope
  - binding
extends:
  - scope
related:
  - global-scope
  - block-scope
  - closure
contrasts_with:
  - global-scope

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is scope?"
  - "What must I know before understanding closures?"
---

# Quick Definition

Local scope refers to bindings that are visible only within the function or block where they are created, providing isolation between different parts of a program.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 125-131 of 03-functions.md): "Bindings created for function parameters or declared inside a function can be referenced only in that function, so they are known as *local* bindings. Every time the function is called, new instances of these bindings are created. This provides some isolation between functions -- each function call acts in its own little world (its local environment) and can often be understood without knowing a lot about what's going on in the global environment."

# Prerequisites

- **scope**: Local scope is a type of scope.
- **binding**: Local scope governs the visibility of bindings within functions and blocks.

# Key Properties

1. Local bindings are created for function parameters and declarations inside functions/blocks.
2. They can only be referenced within their enclosing function or block.
3. **New instances** are created every time a function is called.
4. Each function call has its own independent local environment.
5. Local bindings provide isolation between functions.

# Construction / Recognition

## To Construct/Create:
- Declare a binding with `let` or `const` inside a function or block.
- Function parameters are automatically local.

## To Identify/Recognize:
- Any binding declared inside a function body or block that is not accessible outside.

# Context & Application

Local scope is essential for writing modular, predictable code. It ensures that functions can operate independently without interfering with each other's bindings.

# Examples

**Example 1** (Ch 3, lines 158-168 of 03-functions.md):
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
The `n` inside `halve` is local and does not affect the global `n`.

# Relationships

## Builds Upon
- **scope** -- Local scope is a specific type of scope.

## Enables
- **closure** -- Closures reference local bindings from enclosing scopes.

## Related
- **block-scope** -- Block-level locality for `let` and `const`.

## Contrasts With
- **global-scope** -- Global bindings are visible everywhere; local bindings are not.

# Common Errors

- **Error**: Expecting a local binding to persist between function calls.
  **Correction**: New instances of local bindings are created each time a function is called.

# Common Confusions

- **Confusion**: Thinking that a local binding with the same name as a global one modifies the global.
  **Clarification**: The local binding shadows the global one. Modifying the local has no effect on the global.

# Source Reference

Chapter 3: Functions, Section "Bindings and scopes", lines 125-131 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 125-131)
- Confidence rationale: Explicit definition with italicized term "local"
- Cross-reference status: verified within chapter
