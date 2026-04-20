---
# === CORE IDENTIFICATION ===
concept: do/while Loop
slug: do-while-loop

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: statements
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Statements"
chapter_number: 5
pdf_page: 123
section: "5.4.2 do/while"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "do while loop"

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
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `do/while` loop executes its body at least once, then repeatedly executes it while the condition expression is truthy — the test occurs at the bottom of the loop.

# Core Definition

"The do/while loop is like a while loop, except that the loop expression is tested at the bottom of the loop rather than at the top. This means that the body of the loop is always executed at least once." (Ch. 5, §5.4.2)

# Prerequisites

- **while-loop** — `do/while` is a variant of the while loop.

# Key Properties

1. Body executes at least once before the condition is tested.
2. Must be terminated with a semicolon after the `while(expression)`.
3. Less commonly used than `while` — appropriate when at least one iteration is guaranteed.

# Construction / Recognition

```js
do
    statement
while (expression);
```

# Context & Application

Used when the loop body must execute at least once, such as prompting for user input or processing data that is known to exist.

# Examples

From the source text (§5.4.2, p. 123):

```js
function printArray(a) {
    let len = a.length, i = 0;
    if (len === 0) {
        console.log("Empty Array");
    } else {
        do {
            console.log(a[i]);
        } while(++i < len);
    }
}
```

# Relationships

## Builds Upon
- **while-loop** — Variant that tests condition after the body

## Enables
- At-least-once iteration patterns

## Related
- **for-loop** — Another structured loop

## Contrasts With
- **while-loop** — `while` may never execute its body; `do/while` always executes at least once

# Common Errors

- **Error**: Forgetting the semicolon after `while(expression)` in a `do/while`.
  **Correction**: The `do/while` statement must always end with a semicolon.

# Common Confusions

- **Confusion**: Forgetting that `do/while` always executes the body once.
  **Clarification**: Even if the condition is initially false, the body runs before the first test.

# Source Reference

Chapter 5: Statements, Section 5.4.2, page 123.

# Verification Notes

- Definition source: Direct quote from §5.4.2
- Confidence rationale: High — clearly explained
- Uncertainties: None
- Cross-reference status: Verified
