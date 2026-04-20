---
# === CORE IDENTIFICATION ===
concept: Function
slug: function

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
section: "Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
  - environment
extends: []
related:
  - return-value
  - side-effect
  - console-log
  - expression
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding closures?"
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition

A function is a piece of program wrapped in a value, which can be applied (called/invoked) by putting parentheses after it with arguments between them.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 256-257 of 02-program-structure.md): "A function is a piece of program wrapped in a value. Such values can be *applied* in order to run the wrapped program." And (lines 269-271): "Executing a function is called *invoking*, *calling*, or *applying* it. You can call a function by putting parentheses after an expression that produces a function value."

# Prerequisites

- **Value** -- Functions are values.
- **Environment** -- Functions are available as bindings in the environment.

# Key Properties

1. A **piece of program wrapped in a value** (line 256).
2. Applied by putting **parentheses** after a function expression (line 271).
3. Values between parentheses are called **arguments** (line 276).
4. Can produce **side effects** (output, state changes) or **return values** or both (lines 310-312).
5. Function calls that produce values are **expressions** (lines 324-325).
6. Different functions may need different numbers or types of arguments (line 277).
7. Full function definition is covered in **Chapter 3** (line 336).

# Construction / Recognition

## To Construct/Create:
1. Chapter 2 introduces calling functions; defining custom functions is covered in Chapter 3.

## To Identify/Recognize:
1. A binding name followed by parentheses: `prompt("Enter passcode")`.
2. An expression that produces a function value followed by parentheses.

# Context & Application

Functions are one of the most important concepts in JavaScript. Chapter 2 introduces calling built-in functions; Chapter 3 covers defining your own. Understanding functions as values wrapped in programs is the foundation for closures, higher-order functions, and all advanced JavaScript patterns.

# Examples

**Example 1** (Ch 2, lines 262-264): Calling a function:
```js
prompt("Enter passcode");
```

**Example 2** (Ch 2, summary lines 900-903): "Functions are special values that encapsulate a piece of program. You can invoke them by writing `functionName(argument1, argument2)`. Such a function call is an expression and may produce a value."

# Relationships

## Builds Upon
- **Value** -- Functions are values.
- **Environment** -- Built-in functions come from the environment.

## Enables
- **Return Value** -- Functions can return values.
- **Side Effect** -- Functions can produce side effects.
- **Closures** (Chapter 3) -- Closures are functions that capture their environment.

## Related
- **Console.log** -- A specific function.
- **Expression** -- Function calls are expressions.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Forgetting parentheses when calling a function (referencing the function value instead of calling it).
  **Correction**: `console.log` refers to the function value; `console.log()` calls it.

# Common Confusions

- **Confusion**: Functions and methods are different things.
  **Clarification**: Methods are functions that are properties of objects. This distinction is explored in later chapters.

# Source Reference

Chapter 2: Program Structure, Section "Functions", lines 252-277 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized terms; full coverage deferred to Chapter 3
- Cross-reference status: verified within chapter
