---
# === CORE IDENTIFICATION ===
concept: Const Declaration
slug: const-declaration

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
  - const keyword
  - constant binding

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binding
extends: []
related:
  - let-declaration
  - var-declaration
contrasts_with:
  - let-declaration
  - var-declaration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes let, const, and var?"
  - "What is a binding (variable)?"
---

# Quick Definition

The `const` keyword defines a constant binding that points at the same value for as long as it lives, useful for giving permanent names to values.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 206-209 of 02-program-structure.md): "The word `const` stands for *constant*. It defines a constant binding, which points at the same value for as long as it lives. This is useful for bindings that just give a name to a value so that you can easily refer to it later."

# Prerequisites

- **Binding** -- `const` is one way to create a binding.

# Key Properties

1. Stands for **constant** (line 206).
2. The binding **cannot be reassigned** -- it points at the same value for its lifetime (lines 207-208).
3. Useful for **naming values** for later reference (lines 208-209).
4. Must be **initialized** at declaration (unlike `let`).

# Construction / Recognition

## To Construct/Create:
1. `const greeting = "Hello ";` -- always with an initial value.

## To Identify/Recognize:
1. A declaration starting with the keyword `const`.

# Context & Application

`const` is used when a binding should never be reassigned. It communicates intent to other programmers that this name will always refer to the same value. Note that `const` prevents reassignment of the binding, not mutation of the value itself (relevant for objects and arrays in later chapters).

# Examples

**Example 1** (Ch 2, lines 190-195): Const declaration:
```js
const greeting = "Hello ";
console.log(greeting + name);
// → Hello Ayda
```

**Example 2** (Ch 2, lines 867-875): Const for a meaningful number:
```js
const myNumber = 11213;
```

# Relationships

## Builds Upon
- **Binding** -- `const` creates bindings.

## Enables
- Clear communication of programmer intent for immutable references.

## Related
- **Let Declaration** -- For reassignable bindings.
- **Var Declaration** -- The older alternative.

## Contrasts With
- **Let Declaration** -- `let` allows reassignment; `const` does not.
- **Var Declaration** -- `var` allows reassignment and has different scoping.

# Common Errors

- **Error**: Trying to reassign a `const` binding.
  **Correction**: `const` bindings cannot be reassigned. Use `let` if reassignment is needed.

# Common Confusions

- **Confusion**: `const` makes the value immutable.
  **Clarification**: `const` prevents the *binding* from being reassigned, but if the value is an object or array, its contents can still be modified. This distinction becomes important in later chapters.

# Source Reference

Chapter 2: Program Structure, Section "Bindings", lines 206-209 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term
- Cross-reference status: verified within chapter
