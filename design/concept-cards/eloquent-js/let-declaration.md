---
# === CORE IDENTIFICATION ===
concept: Let Declaration
slug: let-declaration

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
  - let keyword
  - let binding

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binding
extends: []
related:
  - const-declaration
  - var-declaration
contrasts_with:
  - const-declaration
  - var-declaration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes let, const, and var?"
  - "What is a binding (variable)?"
---

# Quick Definition

The `let` keyword creates a binding that can be reassigned to point at different values over its lifetime.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 113-116 of 02-program-structure.md): "The special word (*keyword*) `let` indicates that this sentence is going to define a binding. It is followed by the name of the binding and, if we want to immediately give it a value, by an `=` operator and an expression."

# Prerequisites

- **Binding** -- `let` is one way to create a binding.

# Key Properties

1. The `let` keyword **defines a binding** (line 113).
2. Optionally followed by `=` and an expression to give an **initial value** (lines 115-116).
3. Can be **reassigned** -- the `=` operator changes what value the binding grasps (lines 136-138).
4. Without an initial value, the binding holds `undefined` (lines 172-174).
5. Multiple bindings can be defined in one `let` statement, separated by commas (lines 177-178).
6. Introduced in ES2015 (2015) as the modern replacement for `var`.

# Construction / Recognition

## To Construct/Create:
1. `let caught = 5 * 5;` -- with initial value.
2. `let x;` -- without initial value (holds `undefined`).
3. `let one = 1, two = 2;` -- multiple bindings.

## To Identify/Recognize:
1. A declaration starting with the keyword `let`.

# Context & Application

`let` is the standard way to declare bindings in modern JavaScript. It is preferred over `var` because it has clearer scoping rules (explained in later chapters). The source uses `let` throughout for mutable bindings.

# Examples

**Example 1** (Ch 2, lines 107-109): Basic let declaration:
```js
let caught = 5 * 5;
```

**Example 2** (Ch 2, lines 128-132): Using a let binding:
```js
let ten = 10;
console.log(ten * ten);
// → 100
```

**Example 3** (Ch 2, lines 180-184): Multiple bindings:
```js
let one = 1, two = 2;
console.log(one + two);
// → 3
```

# Relationships

## Builds Upon
- **Binding** -- `let` creates bindings.

## Enables
- Mutable state tracking in programs.
- Loop counters and accumulators.

## Related
- **Const Declaration** -- For bindings that should not be reassigned.
- **Var Declaration** -- The older, pre-2015 alternative.

## Contrasts With
- **Const Declaration** -- `const` bindings cannot be reassigned; `let` bindings can.
- **Var Declaration** -- `var` "behaves oddly in some situations" (line 203); `let` has clearer semantics.

# Common Errors

- **Error**: Forgetting that `let` without assignment yields `undefined`.
  **Correction**: `let x;` creates a binding whose value is `undefined` until assigned.

# Common Confusions

- **Confusion**: `let` and `var` are interchangeable.
  **Clarification**: While similar, `var` "behaves oddly in some situations" (line 203). The precise differences involve scoping and are explained in Chapter 3.

# Source Reference

Chapter 2: Program Structure, Section "Bindings", lines 107-184 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition as keyword for binding creation
- Cross-reference status: verified within chapter
