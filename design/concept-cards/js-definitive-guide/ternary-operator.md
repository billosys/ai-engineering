---
# === CORE IDENTIFICATION ===
concept: Ternary Operator (?:)
slug: ternary-operator

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 108
section: "4.13.1 The Conditional Operator (?:)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "conditional operator"
  - "?: operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
  - operator-precedence
extends: []
related:
  - short-circuit-evaluation
  - if-else-statement
contrasts_with:
  - if-else-statement

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The ternary operator (`?:`) is JavaScript's only three-operand operator: it evaluates the first operand as a boolean, then returns the second operand if truthy or the third if falsy.

# Core Definition

"The conditional operator is the only ternary operator (three operands) in JavaScript... The first operand is evaluated and interpreted as a boolean. If the value of the first operand is truthy, then the second operand is evaluated, and its value is returned. Otherwise, if the first operand is falsy, then the third operand is evaluated and its value is returned." (Ch. 4, §4.13.1)

# Prerequisites

- **primary-expressions** — Each of the three operands is an expression.
- **operator-precedence** — The ternary operator has right-to-left associativity and low precedence.

# Key Properties

1. Only one of the second or third operands is evaluated — never both.
2. Operands may be of any type.
3. Right-to-left associativity: `a?b:c?d:e?f:g` is `a?b:(c?d:(e?f:g))`.
4. Provides an expression-level alternative to `if/else` statements.

# Construction / Recognition

```js
condition ? valueIfTruthy : valueIfFalsy
```

# Context & Application

The ternary operator is used for inline conditional expressions, especially in variable assignments and template literals where an `if/else` statement cannot appear.

# Examples

From the source text (§4.13.1, pp. 108-109):

```js
x > 0 ? x : -x     // The absolute value of x

greeting = "hello " + (username ? username : "there");

// Equivalent if/else:
greeting = "hello ";
if (username) {
    greeting += username;
} else {
    greeting += "there";
}
```

# Relationships

## Builds Upon
- **operator-precedence** — Low precedence, right-to-left associativity

## Enables
- Inline conditional expressions in assignments, return values, and template literals

## Related
- **short-circuit-evaluation** — Alternative conditional patterns using `&&` and `||`

## Contrasts With
- **if-else-statement** — `if/else` is a statement; `?:` is an expression that produces a value

# Common Errors

- **Error**: Omitting parentheses around the ternary when used inside a larger expression.
  **Correction**: Use parentheses for clarity: `"hello " + (username ? username : "there")`.

# Common Confusions

- **Confusion**: Believing both the second and third operands are evaluated.
  **Clarification**: Only one branch is evaluated, similar to short-circuit behavior in `&&`/`||`.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.13.1, pages 108-109.

# Verification Notes

- Definition source: Direct quote from §4.13.1
- Confidence rationale: High — clearly defined
- Uncertainties: None
- Cross-reference status: Verified
