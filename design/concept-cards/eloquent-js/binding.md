---
# === CORE IDENTIFICATION ===
concept: Binding
slug: binding

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
  - variable

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
  - expression
  - statement
extends: []
related:
  - let-declaration
  - const-declaration
  - var-declaration
  - undefined-value
  - environment
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a binding (variable)?"
  - "What must I know before understanding closures?"
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition

A binding (also called a variable) is a named reference that grasps a value, allowing a program to keep internal state and remember things.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 2, lines 100-105 of 02-program-structure.md): "How does a program keep an internal state? How does it remember things? We have seen how to produce new values from old values, but this does not change the old values, and the new value must be used immediately or it will dissipate again. To catch and hold values, JavaScript provides a thing called a *binding*, or *variable*."

# Prerequisites

- **Value** -- Bindings hold references to values.
- **Expression** -- The right side of a binding definition is an expression.
- **Statement** -- Binding declarations are statements.

# Key Properties

1. Bindings **grasp values** -- they are like tentacles, not boxes (lines 150-155).
2. Two bindings can **refer to the same value** (line 152).
3. A binding defined without a value holds `undefined` (lines 172-174).
4. Bindings can be **reassigned** using `=` to point to new values (lines 136-138).
5. Binding names must start with a letter, `$`, or `_`; may contain digits but not start with one (lines 214-218).
6. **Keywords** cannot be used as binding names (lines 221-233).
7. Multiple bindings can be defined in a single statement separated by commas (lines 177-178).

# Construction / Recognition

## To Construct/Create:
1. `let caught = 5 * 5;` -- create a binding with `let`.
2. `const greeting = "Hello ";` -- create a constant binding.
3. `var name = "Ayda";` -- create a binding with `var`.
4. `let x;` -- create a binding without a value (holds `undefined`).

## To Identify/Recognize:
1. A name that holds a reference to a value.
2. Declared with `let`, `const`, or `var`.

# Context & Application

Bindings are fundamental to all programming -- they allow programs to track state, store intermediate results, and give meaningful names to values. They are a prerequisite for understanding scope, closures, and all higher-level programming concepts.

# Examples

**Example 1** (Ch 2, lines 107-109): Creating a binding:
```js
let caught = 5 * 5;
```

**Example 2** (Ch 2, lines 140-147): Reassigning a binding:
```js
let mood = "light";
console.log(mood);
// → light
mood = "dark";
console.log(mood);
// → dark
```

**Example 3** (Ch 2, lines 163-168): Using a binding to track state:
```js
let luigisDebt = 140;
luigisDebt = luigisDebt - 35;
console.log(luigisDebt);
// → 105
```

# Relationships

## Builds Upon
- **Value** -- Bindings reference values.
- **Expression** -- Binding definitions use expressions.
- **Statement** -- Binding declarations are statements.

## Enables
- **Let Declaration**, **Const Declaration**, **Var Declaration** -- Specific ways to create bindings.
- **Environment** -- The set of bindings and their values.
- **Closures** (later chapters) -- Closures capture bindings.

## Related
- **Undefined** -- The value of bindings not yet assigned.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Thinking bindings *contain* values like boxes.
  **Correction**: "You should imagine bindings as tentacles rather than boxes. They do not *contain* values; they *grasp* them" (lines 150-152).

- **Error**: Using a reserved keyword as a binding name.
  **Correction**: Words like `let`, `if`, `for`, `class`, etc. cannot be used as binding names (lines 221-233).

# Common Confusions

- **Confusion**: Reassigning a binding changes the value itself.
  **Clarification**: Reassignment makes the binding point to a different value. Other bindings that referenced the old value are unaffected.

# Source Reference

Chapter 2: Program Structure, Section "Bindings", lines 97-209 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized terms in dedicated section
- Cross-reference status: verified within chapter
