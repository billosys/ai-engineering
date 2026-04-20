---
# === CORE IDENTIFICATION ===
concept: Statement
slug: statement

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
section: "Expressions and statements"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expression
extends: []
related:
  - side-effect
  - program
  - binding
contrasts_with:
  - expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an expression vs. a statement?"
  - "What must I know before understanding closures?"
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition

A statement corresponds to a full sentence in a program -- it stands on its own, may produce side effects, and a program is a list of statements.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 2, lines 62-64 of 02-program-structure.md): "If an expression corresponds to a sentence fragment, a JavaScript *statement* corresponds to a full sentence. A program is a list of statements."

# Prerequisites

- **Expression** -- Statements contain expressions; the simplest statement is an expression with a semicolon.

# Key Properties

1. A statement **stands on its own** -- unlike expressions, it does not just produce a value (lines 78-79).
2. The simplest statement is **an expression followed by a semicolon**: `1;` (lines 67-73).
3. Statements can produce **side effects** -- displaying something, changing machine state (lines 79-82).
4. A statement without side effects is **useless** (lines 76-85).
5. Statements often **contain expressions** (Ch 2 summary, lines 880-883).
6. **Semicolons** terminate most statements; rules for omission are complex (lines 88-95).

# Construction / Recognition

## To Construct/Create:
1. Expression statement: `1;`, `console.log("hello");`.
2. Declaration: `let x = 5;`.
3. Control flow: `if (condition) { ... }`, `while (condition) { ... }`.

## To Identify/Recognize:
1. A complete instruction that can stand on its own in a program.
2. Usually terminated by a semicolon or enclosed in braces.

# Context & Application

Statements are the fundamental units from which programs are built. Understanding the distinction between statements (which do things) and expressions (which produce values) is essential for understanding program structure.

# Examples

**Example 1** (Ch 2, lines 70-73): Expression statements:
```js
1;
!false;
```
"It is a useless program, though" -- these statements produce values but have no side effects.

**Example 2** (Ch 2, summary lines 880-883): "You now know that a program is built out of statements, which themselves sometimes contain more statements. Statements tend to contain expressions, which themselves can be built out of smaller expressions."

# Relationships

## Builds Upon
- **Expression** -- The simplest statement is an expression with a semicolon.

## Enables
- **Program** -- Programs are lists of statements.
- All control flow constructs (if, while, for) are statements.

## Related
- **Side Effect** -- Useful statements produce side effects.
- **Binding** -- Binding declarations are statements.

## Contrasts With
- **Expression** -- Expressions produce values; statements perform actions.

# Common Errors

- **Error**: Omitting semicolons inconsistently.
  **Correction**: "Every statement that needs a semicolon will always get one. I recommend you do the same" (lines 92-94).

# Common Confusions

- **Confusion**: All statements produce values.
  **Clarification**: While expression statements produce values (which are immediately discarded), many statements (like `if`, `while`) do not produce values -- they control program flow.

# Source Reference

Chapter 2: Program Structure, Section "Expressions and statements", lines 38-95 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term
- Cross-reference status: verified within chapter and summary
