---
# === CORE IDENTIFICATION ===
concept: Block Scope
slug: block-scope

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
  - block-level scope

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scope
  - binding
extends:
  - scope
related:
  - local-scope
  - global-scope
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is scope?"
---

# Quick Definition

Block scope means that bindings declared with `let` and `const` are local to the block (curly-braced region) in which they are declared, invisible to code before and after that block.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 134-140 of 03-functions.md): "Bindings declared with `let` and `const` are in fact local to the *block* in which they are declared, so if you create one of those inside of a loop, the code before and after the loop cannot 'see' it. In pre-2015 JavaScript, only functions created new scopes, so old-style bindings, created with the `var` keyword, are visible throughout the whole function in which they appear -- or throughout the global scope, if they are not in a function."

# Prerequisites

- **scope**: Block scope is a specific type of scope.
- **binding**: Applies to `let` and `const` bindings.

# Key Properties

1. `let` and `const` are scoped to the nearest enclosing block.
2. `var` is NOT block-scoped -- it is scoped to the nearest function or global scope.
3. Blocks are delimited by curly braces (`{}`).
4. Block scope was introduced with ES2015 (`let` and `const`).

# Construction / Recognition

## To Construct/Create:
```javascript
if (true) {
  let y = 20; // only visible inside this block
  const z = 30; // only visible inside this block
}
// y and z are not accessible here
```

## To Identify/Recognize:
- A `let` or `const` declaration inside any `{}` block.

# Context & Application

Block scope provides finer-grained control over binding visibility than function scope alone. It is particularly useful in loops, where each iteration can have its own binding instance.

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
- **scope** -- Block scope is a type of scope.

## Enables
- Cleaner variable management in loops and conditionals.

## Related
- **local-scope** -- Block scope is a form of local scope.
- **global-scope** -- `var` bypasses block scope to reach function/global scope.

## Contrasts With
- None explicitly, but implicitly contrasts with `var` function-scoping behavior.

# Common Errors

- **Error**: Expecting `var` to be block-scoped.
  **Correction**: `var` is visible throughout the entire enclosing function or global scope, regardless of blocks.

# Common Confusions

- **Confusion**: All curly braces create identical scope behavior for all binding keywords.
  **Clarification**: Only `let` and `const` respect block scope. `var` ignores block boundaries and is scoped to the enclosing function.

# Source Reference

Chapter 3: Functions, Section "Bindings and scopes", lines 134-148 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 134-140)
- Confidence rationale: Explicit description with contrast to `var`
- Cross-reference status: verified within chapter
