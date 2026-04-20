---
# === CORE IDENTIFICATION ===
concept: Comment
slug: comment

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
section: "Comments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - code comment

# === TYPED RELATIONSHIPS ===
prerequisites:
  - statement
extends: []
related:
  - indentation-and-style
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding closures?"
---

# Quick Definition

A comment is a piece of text that is part of a program but is completely ignored by the computer, used to include explanations or related thoughts.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 843-844 of 02-program-structure.md): "A comment is a piece of text that is part of a program but is completely ignored by the computer."

# Prerequisites

- **Statement** -- Comments exist alongside statements in programs.

# Key Properties

1. **Completely ignored** by the computer (line 844).
2. Two forms: **single-line** with `//` and **multi-line** with `/* ... */` (lines 845-863).
3. `//` comments extend to the **end of the line** (line 861).
4. `/* ... */` comments can **span multiple lines** (lines 862-863).
5. Used to convey information or thoughts that raw code does not express (lines 835-840).

# Construction / Recognition

## To Construct/Create:
1. Single-line: `// this is a comment`.
2. Multi-line: `/* this is a comment */`.

## To Identify/Recognize:
1. Text preceded by `//` or enclosed in `/* ... */`.

# Context & Application

Comments help programmers communicate with themselves and others about what code does and why. They are essential for maintaining code over time, especially for non-obvious design decisions.

# Examples

**Example 1** (Ch 2, lines 849-858): Single-line comments:
```js
let accountBalance = calculateBalance(account);
// It's a green hollow where a river sings
accountBalance.adjust();
// Madly catching white tatters in the grass.
```

**Example 2** (Ch 2, lines 867-875): Multi-line comment:
```js
/*
  I first found this number scrawled on the back of an old
  notebook. Since then, it has often dropped by, showing up in
  phone numbers and the serial numbers of products that I've
  bought. It obviously likes me, so I've decided to keep it.
*/
const myNumber = 11213;
```

# Relationships

## Builds Upon
- **Statement** -- Comments appear alongside statements.

## Enables
- Code documentation and readability.

## Related
- **Indentation and Style** -- Another aspect of code readability.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Forgetting to close a `/* ... */` comment, causing code to be ignored.
  **Correction**: Always close multi-line comments with `*/`.

# Common Confusions

- **Confusion**: Comments make programs run slower.
  **Clarification**: Comments are completely ignored by the computer and have no effect on program execution.

# Source Reference

Chapter 2: Program Structure, Section "Comments", lines 832-875 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated section with explicit definition
- Cross-reference status: verified within chapter
