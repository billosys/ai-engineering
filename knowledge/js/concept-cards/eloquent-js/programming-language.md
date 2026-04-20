---
# === CORE IDENTIFICATION ===
concept: Programming Language
slug: programming-language

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
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - computer language

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - programming
  - program
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a programming language?"
  - "What must I know before understanding closures?"
---

# Quick Definition

A programming language is an artificially constructed language used to instruct computers, allowing words and phrases to be combined in new ways to express new concepts.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 0, lines 63-68): "A *programming language* is an artificially constructed language used to instruct computers. It is interesting that the most effective way we've found to communicate with a computer borrows so heavily from the way we communicate with each other. Like human languages, computer languages allow words and phrases to be combined in new ways, making it possible to express ever new concepts."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Programming languages are **artificially constructed**, not natural languages.
2. They borrow from human language -- combining words and phrases to express concepts.
3. A good programming language allows the programmer to **talk about actions at a higher level**, omitting low-level details (lines 324-329).
4. Programming languages provide **convenient building blocks** (like `while` and `console.log`) and allow defining **your own building blocks** (like `sum` and `range`).
5. JavaScript is one such language, built into every modern web browser (line 77).

# Construction / Recognition

## To Identify/Recognize:
1. A formal notation system designed for writing instructions that a computer can execute.
2. Has defined syntax and semantics for expressing computations.

# Context & Application

Programming languages are the medium through which all programming occurs. The source uses the evolution from binary machine code to assembly-like pseudocode to JavaScript to illustrate how programming languages abstract away low-level details and enable programmers to express intent more clearly.

# Examples

**Example 1** (Ch 0, lines 171-181): Binary machine code -- the earliest "programs" before programming languages:
```
00110001 00000000 00000000
00110001 00000001 00000001
00110011 00000001 00000010
```

**Example 2** (Ch 0, lines 309-312): The same computation in a high-level language:
```js
console.log(sum(range(1, 10)));
// → 55
```
The moral: programming languages let us express the same program in readable, composable ways.

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- **All JavaScript concepts** -- JavaScript is the programming language taught in this source.

## Related
- **Programming** -- Programming is done using programming languages.
- **Program** -- Programs are written in programming languages.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Assuming JavaScript and Java are related because of their similar names.
  **Correction**: "JavaScript has almost nothing to do with the programming language named Java. The similar name was inspired by marketing considerations rather than good judgment" (lines 343-349).

# Common Confusions

- **Confusion**: ECMAScript and JavaScript are different things.
  **Clarification**: "The terms ECMAScript and JavaScript can be used interchangeably -- they are two names for the same language" (lines 358-359).

# Source Reference

Chapter 0: Introduction, lines 62-329 of 00-introduction.md (book.md line 69).

# Verification Notes

- Definition source: direct (quoted from source, line 63)
- Confidence rationale: Explicit definition provided with italicized term
- Cross-reference status: verified within chapter
