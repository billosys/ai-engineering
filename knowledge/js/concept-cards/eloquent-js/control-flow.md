---
# === CORE IDENTIFICATION ===
concept: Control Flow
slug: control-flow

# === CLASSIFICATION ===
category: control-flow
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Program Structure"
chapter_number: 2
pdf_page: null
section: "Control flow"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - flow of control

# === TYPED RELATIONSHIPS ===
prerequisites:
  - statement
extends: []
related:
  - conditional-execution
  - while-loop
  - for-loop
  - do-loop
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding closures?"
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition

Control flow is the order in which statements are executed in a program; by default top-to-bottom, but alterable through conditional and looping statements.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 341-345 of 02-program-structure.md): "When your program contains more than one statement, the statements are executed as though they were a story, from top to bottom." The chapter introduces conditional execution and loops as ways to create non-linear control flow, summarized (lines 886-890): "You can introduce disturbances in the flow of control by using conditional (`if`, `else`, and `switch`) and looping (`while`, `do`, and `for`) statements."

# Prerequisites

- **Statement** -- Control flow governs statement execution order.

# Key Properties

1. Default flow is **top-to-bottom**, like reading a story (line 342-343).
2. **Conditional execution** creates branching paths (lines 369-372).
3. **Loops** create repeated execution paths (lines 493-494).
4. The three forms of flow disturbance are: **conditional** (`if`/`else`/`switch`), **looping** (`while`/`do`/`for`), and **jumping** (`break`/`continue`).

# Construction / Recognition

## To Identify/Recognize:
1. Any deviation from simple top-to-bottom statement execution.
2. Presence of `if`, `while`, `for`, `do`, `switch`, `break`, or `continue`.

# Context & Application

Control flow is what makes programs dynamic and responsive -- without it, programs would simply execute a fixed sequence of operations. All non-trivial programs use some form of control flow.

# Examples

**Example 1** (Ch 2, lines 347-351): Straight-line flow:
```js
let theNumber = Number(prompt("Pick a number"));
console.log("Your number is the square root of " +
            theNumber * theNumber);
```

**Example 2** (Ch 2, summary lines 886-890): "You can introduce disturbances in the flow of control by using conditional (`if`, `else`, and `switch`) and looping (`while`, `do`, and `for`) statements."

# Relationships

## Builds Upon
- **Statement** -- Control flow structures are statements that govern other statements.

## Enables
- **Conditional Execution** -- Branching control flow.
- **While Loop**, **For Loop**, **Do Loop** -- Looping control flow.

## Related
- All loop and conditional constructs.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Assuming all code runs in every execution.
  **Correction**: Conditional branches and loop bodies may or may not execute depending on their conditions.

# Common Confusions

- **Confusion**: Control flow and data flow are the same thing.
  **Clarification**: Control flow is about the order of statement execution. Data flow is about how values move through a program. They are related but distinct concepts.

# Source Reference

Chapter 2: Program Structure, Section "Control flow", lines 338-364 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: synthesized (from section content and summary)
- Confidence rationale: Dedicated section with visual diagrams
- Cross-reference status: verified with chapter summary
