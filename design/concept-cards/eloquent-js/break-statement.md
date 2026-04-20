---
# === CORE IDENTIFICATION ===
concept: Break Statement
slug: break-statement

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
  - continue-statement
  - switch-statement
contrasts_with:
  - continue-statement

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding closures?"
---

# Quick Definition

The `break` statement immediately jumps out of the enclosing loop (or switch statement), ending its execution regardless of the loop condition.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 672-674 of 02-program-structure.md): "The `break` statement has the effect of immediately jumping out of the enclosing loop."

# Prerequisites

- **While Loop** or **For Loop** -- `break` is used inside loops.

# Key Properties

1. **Immediately exits** the enclosing loop (line 672-673).
2. Can be used in `for`, `while`, `do`, and `switch` statements.
3. Allows a loop to terminate based on a **condition inside the body** rather than only the loop condition (lines 694-697).
4. Without `break` in appropriate places, a loop can become **infinite** (lines 700-704).
5. Also used in `switch` statements to prevent fall-through (lines 776-798).

# Construction / Recognition

## To Construct/Create:
1. Place `break;` inside a loop body, typically inside an `if` condition.

## To Identify/Recognize:
1. The keyword `break` followed by a semicolon inside a loop or switch.

# Context & Application

Break is essential for loops that need to terminate based on a condition discovered during execution, rather than a condition that can be expressed in the loop header. It is also critical in switch statements.

# Examples

**Example 1** (Ch 2, lines 678-686): Finding first number >= 20 divisible by 7:
```js
for (let current = 20; ; current = current + 1) {
  if (current % 7 == 0) {
    console.log(current);
    break;
  }
}
// → 21
```
The `for` construct has no end condition -- it relies entirely on `break`.

# Relationships

## Builds Upon
- **While Loop**, **For Loop** -- `break` exits loops.

## Enables
- Early loop termination based on complex conditions.
- Correct `switch` statement behavior.

## Related
- **Switch Statement** -- `break` prevents fall-through in switch cases.

## Contrasts With
- **Continue Statement** -- `continue` skips to the next iteration; `break` exits entirely.

# Common Errors

- **Error**: Forgetting `break` in a switch case, causing fall-through.
  **Correction**: "Be careful, though -- it is easy to forget such a `break`, which will cause the program to execute code you do not want executed" (lines 796-798).

# Common Confusions

- **Confusion**: `break` and `continue` both exit the loop.
  **Clarification**: `break` exits the loop entirely; `continue` skips to the next iteration.

# Source Reference

Chapter 2: Program Structure, Section "Breaking Out of a Loop", lines 668-710 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition in dedicated section
- Cross-reference status: verified with switch section
