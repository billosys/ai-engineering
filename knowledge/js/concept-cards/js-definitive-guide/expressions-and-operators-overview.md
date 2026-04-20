---
# === CORE IDENTIFICATION ===
concept: Expressions and Operators Overview
slug: expressions-and-operators-overview

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
  - variables-overview
  - type-system-overview
extends: []
related:
  - strict-vs-loose-equality
  - type-coercion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes `==` from `===`?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

An expression is a phrase of JavaScript that can be evaluated to produce a value, while operators act on values (operands) to produce new values — including arithmetic, comparison, and logical operators.

# Core Definition

As introduced in Chapter 1: "An expression is a phrase of JavaScript that can be evaluated to produce a value." An initializer expression uses literal syntax. Operators "act on values (the operands) to produce a new value." JavaScript includes arithmetic operators (+, -, *, /, %, **), comparison operators (===, !==, <, <=, >, >=), and logical operators (&&, ||, !). (pp. 23-24)

# Prerequisites

- **javascript-language-overview** — Expressions are a fundamental language concept
- **variables-overview** — Variable names are expressions that evaluate to their values
- **type-system-overview** — Operators interact with the type system

# Key Properties

1. Expressions compute values; statements perform actions
2. Arithmetic operators: +, -, *, /, %, ** (exponentiation, ES2016)
3. The + operator adds numbers but concatenates strings
4. Comparison operators: ===, !==, <, <=, >, >=
5. Logical operators: && (AND), || (OR), ! (NOT)
6. Assignment operators: =, +=, -=, *=, /=, etc.

# Construction / Recognition

```javascript
3 + 2                    // => 5: addition
"3" + "2"                // => "32": string concatenation
x === y                  // strict equality comparison
(x === 2) && (y === 3)   // logical AND
```

# Context & Application

Expressions and operators are used in every JavaScript program to compute values, make comparisons, and combine boolean conditions. Understanding operator behavior with different types is essential for avoiding bugs.

# Examples

From the source text (pp. 23-24):
```javascript
3 + 2                        // => 5: addition
3 - 2                        // => 1: subtraction
3 * 2                        // => 6: multiplication
3 / 2                        // => 1.5: division
"3" + "2"                    // => "32": + adds numbers, concatenates strings
points[1].x - points[0].x   // => 1: more complicated operands also work

let x = 2, y = 3;
x === y                      // => false: equality
x !== y                      // => true: inequality
"two" === "three"            // => false: the two strings are different
(x === 2) && (y === 3)       // => true: both comparisons are true
(x > 3) || (y < 3)           // => false: neither comparison is true
!(x === y)                   // => true: ! inverts a boolean value
```

# Relationships

## Builds Upon
- **javascript-language-overview** — Expressions are fundamental to the language
- **type-system-overview** — Operator behavior depends on operand types

## Enables
- **strict-vs-loose-equality** — Detailed treatment of equality operators
- **type-coercion** — The + operator demonstrates type-dependent behavior

## Related
- **type-coercion** — Operators trigger implicit type conversions

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using `+` expecting numeric addition when one operand is a string.
  **Correction**: When either operand is a string, `+` performs concatenation: `"3" + "2"` produces `"32"`, not `5`.

# Common Confusions

- **Confusion**: The `=` operator tests equality.
  **Clarification**: `=` is assignment; `===` is strict equality; `==` is loose equality with type coercion.

# Source Reference

Chapter 1: Introduction to JavaScript, Section 1.3, pages 23-24.

# Verification Notes

- Definition source: Direct quotes from pp. 23-24
- Confidence rationale: High — clearly introduced with many examples
- Uncertainties: Full operator treatment deferred to Chapter 4
- Cross-reference status: Verified
