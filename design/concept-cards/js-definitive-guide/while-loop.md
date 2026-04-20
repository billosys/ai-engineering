---
# === CORE IDENTIFICATION ===
concept: while Loop
slug: while-loop

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
pdf_page: 122
section: "5.4.1 while"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expression-statements
  - compound-and-empty-statements
extends: []
related:
  - do-while-loop
  - for-loop
  - break-continue-statements
contrasts_with:
  - do-while-loop

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `while` loop is JavaScript's basic loop construct: it evaluates a condition expression before each iteration and executes the loop body repeatedly while the expression is truthy.

# Core Definition

"The while statement is JavaScript's basic loop. It has the following syntax: `while (expression) statement`. To execute a while statement, the interpreter first evaluates *expression*. If the value of the expression is falsy, then the interpreter skips over the *statement* that serves as the loop body and moves on to the next statement in the program. If, on the other hand, the *expression* is truthy, the interpreter executes the *statement* and repeats." (Ch. 5, §5.4.1)

# Prerequisites

- **expression-statements** — The condition is an expression; the body is a statement.
- **compound-and-empty-statements** — Block statements form multi-line loop bodies.

# Key Properties

1. Condition is tested *before* each iteration — the body may never execute.
2. `while(true)` creates an infinite loop.
3. Loop variables must be initialized before the loop and updated within the body.
4. `continue` in a while loop returns directly to the condition test.

# Construction / Recognition

```js
while (expression)
    statement
```

# Context & Application

The `while` loop is used when the number of iterations is not known in advance and depends on a condition. It is the most general loop form.

# Examples

From the source text (§5.4.1, pp. 122-123):

```js
let count = 0;
while(count < 10) {
    console.log(count);
    count++;
}
```

# Relationships

## Builds Upon
- **expression-statements** — Condition and body are expressions/statements

## Enables
- General-purpose looping

## Related
- **for-loop** — A more structured loop with init/test/increment
- **break-continue-statements** — Used to exit or skip iterations

## Contrasts With
- **do-while-loop** — `do/while` tests the condition after the body, guaranteeing at least one execution

# Common Errors

- **Error**: Forgetting to update the loop variable, creating an infinite loop.
  **Correction**: Ensure the loop body modifies the variable(s) tested in the condition.

# Common Confusions

- **Confusion**: Believing `continue` in a `while` loop works identically to `continue` in a `for` loop.
  **Clarification**: In a `while` loop, `continue` jumps directly to the condition test. In a `for` loop, `continue` first evaluates the increment expression before the test.

# Source Reference

Chapter 5: Statements, Section 5.4.1, pages 122-123.

# Verification Notes

- Definition source: Direct quote from §5.4.1
- Confidence rationale: High — clearly defined
- Uncertainties: None
- Cross-reference status: Verified
