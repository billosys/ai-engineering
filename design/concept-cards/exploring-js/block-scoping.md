---
# === CORE IDENTIFICATION ===
concept: Block Scoping
slug: block-scoping

# === CLASSIFICATION ===
category: variables-scope
subcategory: scoping
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Variables and assignment"
chapter_number: 13
pdf_page: null
section: "13.4 The scope of a variable"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - block-scoped variables

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable-scope
extends:
  - variable-scope
related:
  - let-declaration
  - const-declaration
contrasts_with:
  - var-declaration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I declare and use variables with proper scoping?"
  - "What distinguishes `let` from `const` from `var`?"
---

# Quick Definition

Block scoping means a variable's scope is the innermost enclosing block (`{}`). Variables declared with `const` and `let` are block-scoped.

# Core Definition

"The variables declared via `const` and `let` are called *block-scoped* because their scopes are always the innermost surrounding blocks." (Ch. 13, &sect;13.4). This contrasts with `var`, which is function-scoped. Block scoping provides tighter control over variable visibility and prevents accidental leakage.

# Prerequisites

- **variable-scope** -- block scoping is a specific type of scope

# Key Properties

1. ^ES6^: `let` and `const` introduced block scoping
2. Scope = innermost surrounding block (`{}`)
3. Includes `if`, `for`, `while` blocks, standalone blocks, etc.
4. Does not leak outside the block
5. Contrasts with `var`'s function scoping

# Construction / Recognition

```js
{
  const x = 1; // only accessible within this block
}
// x is not accessible here

if (true) {
  let y = 2; // only accessible within the if block
}
// y is not accessible here
```

# Context & Application

Block scoping is the modern standard for variable declarations. It prevents the common `var` pitfall of variables leaking out of blocks.

# Examples

From the source text (Ch. 13, &sect;13.4):
```js
{ // Scope A
  const x = 0;
  { // Scope B
    const y = 1;
  }
  // y not accessible here
}
// x not accessible here
```

# Relationships

## Builds Upon
- **variable-scope** -- block scoping is a type of scope

## Enables
- Proper variable isolation
- Preventing accidental variable leakage

## Related
- **let-declaration** -- block-scoped mutable variables
- **const-declaration** -- block-scoped immutable variables

## Contrasts With
- **var-declaration** -- function-scoped, not block-scoped

# Common Errors

- **Error**: Expecting `var` to be block-scoped like `let`/`const`.
  **Correction**: `var` is function-scoped; use `let`/`const` for block scoping.

# Common Confusions

- **Confusion**: Thinking all declarations are block-scoped.
  **Clarification**: `var` is function-scoped, `import` is module-scoped. Only `let`, `const`, and `class` are block-scoped.

# Source Reference

Chapter 13: Variables and assignment, Section 13.4, lines 230-233.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicitly stated with demonstrated scope examples
- Cross-reference status: verified against Ch. 13 &sect;13.8 declarations table
