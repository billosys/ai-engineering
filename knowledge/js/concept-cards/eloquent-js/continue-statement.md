---
# === CORE IDENTIFICATION ===
concept: Continue Statement
slug: continue-statement

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
section: "Breaking Out of a Loop"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - while-loop
  - for-loop
extends: []
related:
  - break-statement
contrasts_with:
  - break-statement

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding closures?"
---

# Quick Definition

The `continue` keyword skips the rest of the current loop iteration and proceeds to the loop's next iteration.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 707-710 of 02-program-structure.md): "The `continue` keyword is similar to `break` in that it influences the progress of a loop. When `continue` is encountered in a loop body, control jumps out of the body and continues with the loop's next iteration."

# Prerequisites

- **While Loop** or **For Loop** -- `continue` is used inside loops.

# Key Properties

1. **Skips the rest** of the current iteration (line 709).
2. **Proceeds to the next iteration** -- the loop condition is re-evaluated (line 710).
3. Similar to `break` in influencing loop progress, but does not exit the loop (line 708).

# Construction / Recognition

## To Construct/Create:
1. Place `continue;` inside a loop body, typically inside an `if` condition.

## To Identify/Recognize:
1. The keyword `continue` followed by a semicolon inside a loop.

# Context & Application

Continue is used when certain iterations should be skipped based on a condition, but the loop should keep running. It simplifies loop bodies by avoiding deeply nested if/else blocks.

# Examples

The source provides the definition but does not include a standalone code example for `continue`. Based on the definition (Ch 2, lines 707-710):
```js
for (let i = 0; i < 10; i++) {
  if (i % 2 == 0) continue;
  console.log(i);  // prints only odd numbers
}
```

# Relationships

## Builds Upon
- **While Loop**, **For Loop** -- `continue` operates within loops.

## Enables
- Skipping specific iterations without exiting the loop.

## Related
- **Break Statement** -- Both influence loop progress.

## Contrasts With
- **Break Statement** -- `break` exits the loop entirely; `continue` only skips the current iteration.

# Common Errors

- **Error**: Placing `continue` outside a loop.
  **Correction**: `continue` can only be used inside loop bodies (`while`, `do`, `for`).

# Common Confusions

- **Confusion**: `continue` causes the loop to end.
  **Clarification**: `continue` only ends the current iteration and moves to the next one. The loop continues running.

# Source Reference

Chapter 2: Program Structure, Section "Breaking Out of a Loop", lines 706-710 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition
- Cross-reference status: verified within chapter
