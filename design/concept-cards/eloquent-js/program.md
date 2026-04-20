---
# === CORE IDENTIFICATION ===
concept: Program
slug: program

# === CLASSIFICATION ===
category: fundamentals
subcategory: core-concepts
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Introduction"
chapter_number: 0
pdf_page: null
section: "On programming"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - programming
  - programming-language
  - statement
  - expression
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a program?"
  - "What must I know before understanding closures?"
---

# Quick Definition

A program is a set of precise instructions telling a computer what to do, built from statements that may contain expressions.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 0, line 48): a *program* is "a set of precise instructions telling a computer what to do." The source elaborates (lines 121-129): "A program is many things. It is a piece of text typed by a programmer, it is the directing force that makes the computer do what it does, it is data in the computer's memory, and, at the same time, it controls the actions performed on this memory." Chapter 2 (line 64) adds: "A program is a list of statements."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A program is simultaneously **text**, **data in memory**, and a **directing force** for computation.
2. A program is **a list of statements** (Ch 2).
3. Programs grow in complexity as they grow in size -- managing this complexity is the core skill of programming.
4. A program is analogous to a machine with interconnected parts.
5. Programs are "costless to build" and "weightless" -- they are buildings of thought.

# Construction / Recognition

## To Construct/Create:
1. Write statements in a programming language.
2. Combine statements into a coherent sequence of instructions.

## To Identify/Recognize:
1. A piece of text that can be executed by a computer to perform actions.

# Context & Application

The concept of a program is the foundational unit of all software. In JavaScript, a program is a list of statements executed from top to bottom, with control flow structures allowing branching and looping.

# Examples

**Example 1** (Ch 0, lines 277-285): A simple JavaScript program:
```js
let total = 0, count = 1;
while (count <= 10) {
  total += count;
  count += 1;
}
console.log(total);
// → 55
```

**Example 2** (Ch 2, lines 70-73): The simplest possible program -- expression statements:
```js
1;
!false;
```
This is a valid program (a list of statements), though a useless one since it produces no observable side effects.

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- **Statement** -- Programs are composed of statements.
- **Expression** -- Statements contain expressions.
- All control flow and data concepts.

## Related
- **Programming** -- The activity that produces programs.
- **Programming Language** -- The medium in which programs are written.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Thinking of a program only as text.
  **Correction**: A program is simultaneously text, data in memory, and a controlling force for computation.

# Common Confusions

- **Confusion**: A program and a script are fundamentally different things.
  **Clarification**: In JavaScript, the terms are often used interchangeably. The source treats a program as any list of statements that can be executed.

# Source Reference

Chapter 0: Introduction, "On programming", lines 120-145 of 00-introduction.md; Chapter 2: Program Structure, line 64 of 02-program-structure.md (book.md lines 69, 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term; reinforced in Ch 2
- Cross-reference status: verified across Ch 0 and Ch 2
