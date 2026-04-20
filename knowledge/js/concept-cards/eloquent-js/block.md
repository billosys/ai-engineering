---
# === CORE IDENTIFICATION ===
concept: Block
slug: block

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
section: "Conditional execution"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - code block
  - brace-delimited block

# === TYPED RELATIONSHIPS ===
prerequisites:
  - statement
extends: []
related:
  - conditional-execution
  - while-loop
  - for-loop
  - indentation-and-style
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an expression vs. a statement?"
  - "What must I know before understanding closures?"
---

# Quick Definition

A block is a sequence of statements wrapped in braces (`{` and `}`), which groups them into a single statement for use in control flow structures.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 410-413 of 02-program-structure.md): "The braces can be used to group any number of statements into a single statement, called a *block*."

# Prerequisites

- **Statement** -- Blocks contain statements.

# Key Properties

1. Delimited by **braces** `{` and `}` (line 411).
2. Groups **any number of statements** into a single statement (line 411-412).
3. Used with `if`, `while`, `for`, and other control structures that expect a single statement.
4. Can be omitted for single-statement bodies, but the source recommends **always using them** (lines 413-417).

# Construction / Recognition

## To Construct/Create:
1. Wrap statements in `{ ... }`.

## To Identify/Recognize:
1. Matched curly braces containing statements.

# Context & Application

Blocks are the basic grouping mechanism in JavaScript. They are used everywhere control structures need to execute multiple statements. Understanding blocks is prerequisite to understanding block scoping (with `let` and `const`).

# Examples

**Example 1** (Ch 2, lines 383-389): Block in an if statement:
```js
if (!Number.isNaN(theNumber)) {
  console.log("Your number is the square root of " +
              theNumber * theNumber);
}
```

**Example 2** (Ch 2, lines 419-422): Single-statement without a block:
```js
if (1 + 1 == 2) console.log("It's true");
// → It's true
```

# Relationships

## Builds Upon
- **Statement** -- A block groups statements.

## Enables
- **Conditional Execution** -- if/else bodies use blocks.
- **Loops** -- while/for/do bodies use blocks.
- Block scoping (later chapters).

## Related
- **Indentation and Style** -- Proper indentation reflects block structure.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Omitting braces for a block and later adding a second statement that appears to be in the block but is not.
  **Correction**: Always use braces, even for single-statement bodies.

# Common Confusions

- **Confusion**: Blocks create a new scope in all cases.
  **Clarification**: With `let` and `const`, blocks do create scope. With `var`, they do not (covered in Chapter 3).

# Source Reference

Chapter 2: Program Structure, Section "Conditional execution", lines 410-417 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term
- Cross-reference status: verified within chapter
