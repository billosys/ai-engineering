---
# === CORE IDENTIFICATION ===
concept: Side Effect
slug: side-effect

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
  - statement
extends: []
related:
  - expression
  - console-log
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an expression vs. a statement?"
  - "What must I know before understanding closures?"
---

# Quick Definition

A side effect is an observable change that a statement makes to the world, such as displaying something on the screen or modifying the machine's internal state for subsequent statements.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 79-82 of 02-program-structure.md): "A statement stands on its own, so if it doesn't affect the world, it's useless. It may display something on the screen, as with `console.log`, or change the state of the machine in a way that will affect the statements that come after it. These changes are called *side effects*."

# Prerequisites

- **Statement** -- Side effects are produced by statements.

# Key Properties

1. An **observable change** to the world or machine state (line 82).
2. Displaying output on screen is a side effect (line 80).
3. Changing machine state that affects later statements is a side effect (lines 81-82).
4. A statement without side effects is **useless** (line 79).
5. Functions can be useful for their side effects or for the values they return -- or both (Ch 2, lines 310-312).

# Construction / Recognition

## To Construct/Create:
1. Call `console.log()` -- displays output.
2. Assign a binding -- changes machine state.
3. Modify a data structure.

## To Identify/Recognize:
1. Any action that changes something observable beyond just producing a value.

# Context & Application

Side effects are what make programs useful -- without them, a program would compute values that are immediately discarded. Understanding side effects is foundational for understanding how programs interact with users and with their own state.

# Examples

**Example 1** (Ch 2, lines 70-85): Useless statements (no side effects):
```js
1;
!false;
```
"This leaves no impression on the world at all. When you run this program, nothing observable happens."

**Example 2** (Ch 2, lines 310-312): Side effects vs. return values:
"Showing a dialog box or writing text to the screen is a *side effect*. Many functions are useful because of the side effects they produce."

# Relationships

## Builds Upon
- **Statement** -- Statements are the vehicle for side effects.

## Enables
- Understanding the distinction between useful and useless statements.
- Understanding function purposes (side effects vs. return values).

## Related
- **Console.log** -- A primary example of a side-effect-producing function.
- **Expression** -- Expressions alone do not produce side effects; they only produce values.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Writing expression statements without side effects and expecting something to happen.
  **Correction**: `1 + 2;` on its own does nothing observable. You need a side effect like `console.log(1 + 2);` to see a result.

# Common Confusions

- **Confusion**: All function calls produce side effects.
  **Clarification**: Some functions (like `Math.max`) produce only values with no side effects. Others (like `console.log`) produce side effects. Some do both.

# Source Reference

Chapter 2: Program Structure, Section "Expressions and statements", lines 79-85 of 02-program-structure.md; also "Return values", lines 306-312 (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term
- Cross-reference status: verified within chapter
