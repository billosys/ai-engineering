---
# === CORE IDENTIFICATION ===
concept: Do Loop
slug: do-loop

# === CLASSIFICATION ===
category: control-flow
subcategory: iteration
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Program Structure"
chapter_number: 2
pdf_page: null
section: "while and do loops"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - do...while loop
  - do-while loop

# === TYPED RELATIONSHIPS ===
prerequisites:
  - while-loop
extends:
  - while-loop
related:
  - for-loop
contrasts_with:
  - while-loop

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding closures?"
---

# Quick Definition

A `do` loop always executes its body at least once, then repeats as long as the condition (tested after the body) remains true.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 560-564 of 02-program-structure.md): "A `do` loop is a control structure similar to a `while` loop. It differs only on one point: a `do` loop always executes its body at least once, and it starts testing whether it should stop only after that first execution. To reflect this, the test appears after the body of the loop."

# Prerequisites

- **While Loop** -- The do loop is a variant of the while loop.

# Key Properties

1. **Always executes at least once** -- the condition is checked after the body (lines 562-563).
2. The test appears **after** the body: `do { ... } while (condition);` (line 564).
3. Otherwise identical to a `while` loop in behavior.

# Construction / Recognition

## To Construct/Create:
1. `do { body } while (condition);`

## To Identify/Recognize:
1. The `do` keyword followed by a block body, then `while (condition);`.

# Context & Application

Do loops are used when the body must execute at least once before checking whether to continue -- such as prompting for input that must be validated.

# Examples

**Example 1** (Ch 2, lines 566-572): Prompting until valid input:
```js
let yourName;
do {
  yourName = prompt("Who are you?");
} while (!yourName);
console.log("Hello " + yourName);
```
"This program will force you to enter a name. It will ask again and again until it gets something that is not an empty string."

# Relationships

## Builds Upon
- **While Loop** -- A do loop is a variant of a while loop.

## Enables
- Input validation patterns where at least one attempt is needed.

## Related
- **For Loop** -- Another loop variant.

## Contrasts With
- **While Loop** -- `while` checks condition first (may execute zero times); `do` checks after (always executes at least once).

# Common Errors

- **Error**: Forgetting the semicolon after `while (condition)` in a do loop.
  **Correction**: `do { ... } while (condition);` -- the trailing semicolon is required.

# Common Confusions

- **Confusion**: `do...while` and `while` always produce the same results.
  **Clarification**: They differ when the condition is initially false. `while` would skip the body entirely; `do...while` executes it once.

# Source Reference

Chapter 2: Program Structure, Section "while and do loops", lines 559-580 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition in dedicated paragraph
- Cross-reference status: verified within chapter
