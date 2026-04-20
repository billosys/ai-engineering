---
# === CORE IDENTIFICATION ===
concept: Var Declaration
slug: var-declaration

# === CLASSIFICATION ===
category: fundamentals
subcategory: program-structure
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Program Structure"
chapter_number: 2
pdf_page: null
section: "Bindings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - var keyword

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binding
extends: []
related:
  - let-declaration
  - const-declaration
contrasts_with:
  - let-declaration
  - const-declaration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes let, const, and var?"
  - "What is a binding (variable)?"
---

# Quick Definition

The `var` keyword is the pre-2015 way to declare bindings in JavaScript; it mostly does the same thing as `let` but behaves oddly in some situations.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 198-203 of 02-program-structure.md): "The first of these, `var` (short for 'variable'), is the way bindings were declared in pre-2015 JavaScript, when `let` didn't exist yet. I'll get back to the precise way it differs from `let` in the next chapter. For now, remember that it mostly does the same thing, but we'll rarely use it in this book because it behaves oddly in some situations."

# Prerequisites

- **Binding** -- `var` is one way to create a binding.

# Key Properties

1. Short for **"variable"** (line 199).
2. The **pre-2015** way to declare bindings (line 199).
3. **Mostly does the same thing** as `let` (line 202).
4. **Behaves oddly** in some situations (line 203) -- differences explained in Chapter 3.
5. Rarely used in modern JavaScript code.

# Construction / Recognition

## To Construct/Create:
1. `var name = "Ayda";`

## To Identify/Recognize:
1. A declaration starting with the keyword `var`.

# Context & Application

`var` is encountered primarily in older JavaScript code written before ES2015. Understanding it is necessary for reading legacy codebases. The source deliberately avoids `var` in favor of `let` and `const` and warns that it behaves oddly.

# Examples

**Example 1** (Ch 2, lines 190-195): Var declaration:
```js
var name = "Ayda";
const greeting = "Hello ";
console.log(greeting + name);
// → Hello Ayda
```

# Relationships

## Builds Upon
- **Binding** -- `var` creates bindings.

## Enables
- Reading and understanding legacy JavaScript code.

## Related
- **Let Declaration** -- The modern replacement for `var`.
- **Const Declaration** -- For constant bindings.

## Contrasts With
- **Let Declaration** -- `let` has clearer scoping behavior; `var` "behaves oddly."
- **Const Declaration** -- `const` prevents reassignment; `var` allows it.

# Common Errors

- **Error**: Using `var` in new code without understanding its scoping quirks.
  **Correction**: Prefer `let` or `const` in modern code. The precise differences in scoping are covered in Chapter 3.

# Common Confusions

- **Confusion**: `var` and `let` are identical.
  **Clarification**: They mostly work the same way, but `var` has different scoping rules (function-scoped vs. block-scoped) and hoisting behavior, explained in Chapter 3.

# Source Reference

Chapter 2: Program Structure, Section "Bindings", lines 198-203 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit description, though full differences deferred to Chapter 3
- Cross-reference status: partial -- full explanation deferred to Chapter 3
