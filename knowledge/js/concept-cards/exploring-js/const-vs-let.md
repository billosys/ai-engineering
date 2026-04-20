---
# === CORE IDENTIFICATION ===
concept: Choosing const vs let
slug: const-vs-let

# === CLASSIFICATION ===
category: variables-scope
subcategory: variable-declarations
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Variables and assignment"
chapter_number: 13
pdf_page: null
section: "13.3 Deciding between const and let"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - const-declaration
  - let-declaration
extends: []
related:
  - const-immutability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes `let` from `const` from `var`?"
  - "How do I declare and use variables with proper scoping?"
---

# Quick Definition

The recommended rule: prefer `const` (immutable binding, signals the value never changes); use `let` only when you need to reassign the variable.

# Core Definition

"I recommend the following rules to decide between `const` and `let`: `const` indicates an immutable binding and that a variable never changes its value. Prefer it. `let` indicates that the value of a variable changes. Use it only when you can't use `const`." (Ch. 13, &sect;13.3).

# Prerequisites

- **const-declaration** -- understanding what const provides
- **let-declaration** -- understanding when let is needed

# Key Properties

1. Default to `const`
2. Use `let` only when reassignment is needed
3. `const` communicates intent: this value won't change
4. `let` communicates intent: this value will change
5. `const` in `for-of` loops: fresh binding per iteration
6. `let` needed in `for` loops with changing counter

# Construction / Recognition

```js
const name = 'Jane';     // won't change -- use const
let counter = 0;         // will change -- use let
counter++;

for (const elem of arr) { }  // const OK (fresh binding per iteration)
for (let i = 0; i < n; i++) { }  // let needed (i changes)
```

# Context & Application

This is a widely adopted best practice in the JavaScript community. It makes code more readable by signaling intent.

# Examples

From the source text (Ch. 13, &sect;13.2.2, 13.3):
```js
// const with for-of (fresh binding each iteration)
const arr = ['hello', 'world'];
for (const elem of arr) {
  console.log(elem);
}

// let needed in plain for loop
for (let i = 0; i < arr.length; i++) {
  const elem = arr[i];
  console.log(elem);
}
```

# Relationships

## Builds Upon
- **const-declaration** -- const is the preferred default
- **let-declaration** -- let is the fallback

## Enables
- Clear communication of intent in code

## Related
- **const-immutability** -- understanding what const actually prevents

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `let` everywhere out of habit.
  **Correction**: Default to `const`; only use `let` when the variable needs to be reassigned.

# Common Confusions

- **Confusion**: Thinking `const` is only for "true constants" like `PI`.
  **Clarification**: `const` is for any variable that won't be reassigned, including objects and arrays.

# Source Reference

Chapter 13: Variables and assignment, Section 13.3, lines 171-189.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit recommendation with rationale
- Cross-reference status: verified
