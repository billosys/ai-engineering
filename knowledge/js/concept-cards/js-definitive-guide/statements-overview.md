---
# === CORE IDENTIFICATION ===
concept: Statements Overview
slug: statements-overview

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: language-overview
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Introduction to JavaScript"
chapter_number: 1
pdf_page: 24
section: "1.3 A Tour of JavaScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - control structures

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
  - expressions-and-operators-overview
extends: []
related:
  - variables-overview
  - automatic-semicolon-insertion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

Statements are instructions that perform actions and alter program state (such as variable declarations, assignments, and control structures like conditionals and loops), as opposed to expressions which compute values.

# Core Definition

As introduced in Chapter 1: "If JavaScript expressions are like phrases, then JavaScript statements are like full sentences." "An expression is something that computes a value but doesn't do anything: it doesn't alter the program state in any way. Statements, on the other hand, don't have a value, but they do alter the state." The broad categories of statements include "variable declarations and assignment statements" and "control structures, such as conditionals and loops." (p. 24)

# Prerequisites

- **javascript-language-overview** — Statements are a fundamental language concept
- **expressions-and-operators-overview** — Must understand the distinction between expressions and statements

# Key Properties

1. Statements alter program state; expressions compute values
2. Variable declarations (`let`, `const`, `var`) are statements
3. Assignment (`x = 5;`) is a statement
4. Control structures: `if/else`, `while`, `for`, `for/of`, `for/in`
5. Statements are separated by semicolons (which may be automatically inserted)

# Construction / Recognition

```javascript
if (x >= 0) { return x; } else { return -x; }   // conditional
for (let x of array) { sum += x; }                // for/of loop
while (n > 1) { product *= n; n--; }              // while loop
```

# Context & Application

Statements form the backbone of JavaScript programs, controlling flow of execution. Understanding the distinction between expressions and statements is essential for writing correct code.

# Examples

From the source text (pp. 26-27):
```javascript
function abs(x) {
    if (x >= 0) { return x; }
    else { return -x; }
}

function sum(array) {
    let sum = 0;
    for (let x of array) { sum += x; }
    return sum;
}

function factorial(n) {
    let product = 1;
    while (n > 1) { product *= n; n--; }
    return product;
}
```

# Relationships

## Builds Upon
- **expressions-and-operators-overview** — Statements contain and use expressions

## Enables
- Control flow patterns (covered in Chapter 5)

## Related
- **automatic-semicolon-insertion** — How statements are terminated
- **variables-overview** — Variable declarations are statements

## Contrasts With
- Expressions — expressions compute values, statements perform actions

# Common Errors

- **Error**: Expecting a statement to produce a value that can be assigned.
  **Correction**: Statements alter state but do not produce values; use expressions when you need a value.

# Common Confusions

- **Confusion**: All lines of JavaScript code are statements.
  **Clarification**: JavaScript has both statements (which do things) and expressions (which compute values). Some constructs like assignments are both.

# Source Reference

Chapter 1: Introduction to JavaScript, Section 1.3, pages 24-27.

# Verification Notes

- Definition source: Direct quote from p. 24
- Confidence rationale: High — clearly introduced
- Uncertainties: Full statement treatment deferred to Chapter 5
- Cross-reference status: Verified
