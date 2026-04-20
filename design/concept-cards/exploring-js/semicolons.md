---
# === CORE IDENTIFICATION ===
concept: Semicolons
slug: semicolons

# === CLASSIFICATION ===
category: syntax-fundamentals
subcategory: basic-syntax
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Syntax"
chapter_number: 9
pdf_page: null
section: "9.7 Semicolons"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - statements
extends: []
related:
  - automatic-semicolon-insertion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Where do semicolons go in JavaScript code?"
---

# Quick Definition

Semicolons terminate statements in JavaScript, except for statements that end with a block (`{}`). While mostly optional due to ASI, they are recommended for clarity.

# Core Definition

"Each statement is terminated by a semicolon" except "statements ending with blocks" (Ch. 9, &sect;9.7.1). A subtle case: `const func = () => {};` has a semicolon because the entire `const` declaration is the statement (even though it contains a block). Control statement bodies are themselves statements, so a block body doesn't need a trailing semicolon.

# Prerequisites

- **statements** -- semicolons terminate statements

# Key Properties

1. Statements end with semicolons: `const x = 3;`
2. Statements ending with blocks do not: `function foo() { }` (no semicolon)
3. Exception: when a block is inside a larger statement, the statement's semicolon applies
4. Example: `const func = () => {};` -- semicolon for the `const` statement
5. Author recommends always writing semicolons

# Construction / Recognition

```js
const x = 3;          // semicolon
someFunction('abc');   // semicolon
i++;                   // semicolon

function foo() { }    // no semicolon
if (y > 0) { }       // no semicolon

const func = () => {}; // semicolon (for const, not the arrow)
```

# Context & Application

Semicolon usage is a stylistic choice, but the author recommends always using them. Tools like Prettier and ESLint can enforce a consistent style.

# Examples

From the source text (Ch. 9, &sect;9.7.1):
```js
const x = 3;
someFunction('abc');

function foo() {
  // ...
}  // no semicolon

const func = () => {}; // semicolon!
```

# Relationships

## Builds Upon
- **statements** -- semicolons terminate statements

## Enables
- **automatic-semicolon-insertion** -- what happens when semicolons are omitted

## Related
- No additional

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Omitting semicolons without understanding ASI pitfalls.
  **Correction**: Either always use semicolons, or use tools (Prettier/ESLint) to handle edge cases.

# Common Confusions

- **Confusion**: Thinking `const func = () => {};` shouldn't have a semicolon because it ends with `}`.
  **Clarification**: The `}` belongs to the arrow function expression inside the `const` statement; the `const` statement needs a semicolon.

# Source Reference

Chapter 9: Syntax, Section 9.7, lines 863-898.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Detailed rules with subtle cases explained
- Cross-reference status: verified
