---
# === CORE IDENTIFICATION ===
concept: Conditional Execution
slug: conditional-execution

# === CLASSIFICATION ===
category: control-flow
subcategory: branching
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Program Structure"
chapter_number: 2
pdf_page: null
section: "Conditional execution"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - if statement
  - if/else statement
  - branching

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean
  - expression
  - statement
  - control-flow
extends: []
related:
  - switch-statement
  - block
  - ternary-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding closures?"
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition

Conditional execution uses the `if` keyword to execute or skip a statement depending on the value of a Boolean expression, optionally with `else` to handle the alternative case.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 2, lines 369-372 of 02-program-structure.md): "Not all programs are straight roads. We may, for example, want to create a branching road where the program takes the proper branch based on the situation at hand. This is called *conditional execution*." And (lines 396-399): "The `if` keyword executes or skips a statement depending on the value of a Boolean expression. The deciding expression is written after the keyword, between parentheses, followed by the statement to execute."

# Prerequisites

- **Boolean** -- The condition is evaluated as Boolean.
- **Expression** -- The condition is an expression.
- **Statement** -- The body to execute is a statement.
- **Control Flow** -- Conditional execution alters control flow.

# Key Properties

1. Created with the `if` keyword (line 378).
2. Condition appears in **parentheses** after `if` (line 398).
3. Can include an **`else` branch** for the alternative case (lines 425-429).
4. Can be **chained** with `else if` for multiple branches (lines 442-444).
5. The body is typically a **block** (braces), though single statements can omit braces (lines 410-417).
6. The source recommends **always using braces** to avoid mistakes (lines 414-417).

# Construction / Recognition

## To Construct/Create:
1. Simple: `if (condition) { ... }`.
2. With else: `if (condition) { ... } else { ... }`.
3. Chained: `if (c1) { ... } else if (c2) { ... } else { ... }`.

## To Identify/Recognize:
1. The `if` keyword followed by a parenthesized condition.

# Context & Application

Conditional execution is the fundamental mechanism for making decisions in programs. Every program that needs to respond differently to different inputs uses conditional execution.

# Examples

**Example 1** (Ch 2, lines 383-389): Simple if:
```js
let theNumber = Number(prompt("Pick a number"));
if (!Number.isNaN(theNumber)) {
  console.log("Your number is the square root of " +
              theNumber * theNumber);
}
```

**Example 2** (Ch 2, lines 447-456): Chained if/else if/else:
```js
let num = Number(prompt("Pick a number"));

if (num < 10) {
  console.log("Small");
} else if (num < 100) {
  console.log("Medium");
} else {
  console.log("Large");
}
```

# Relationships

## Builds Upon
- **Boolean** -- Conditions evaluate to Boolean.
- **Control Flow** -- Conditional execution is a form of control flow.

## Enables
- Decision-making in programs.
- Guard clauses and input validation.

## Related
- **Switch Statement** -- Alternative for dispatching on a single value.
- **Block** -- Braces group statements in conditional bodies.
- **Ternary Operator** -- Expression-level conditional.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Omitting braces and accidentally including extra statements in a branch.
  **Correction**: "Most JavaScript programmers use them in every wrapped statement like this" (lines 415-417). Always use braces.

# Common Confusions

- **Confusion**: `if`/`else` and the ternary operator are interchangeable.
  **Clarification**: `if`/`else` is a statement (for actions); the ternary operator is an expression (for choosing between values).

# Source Reference

Chapter 2: Program Structure, Section "Conditional execution", lines 366-470 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated section with explicit definition using italicized term
- Cross-reference status: verified within chapter
