---
# === CORE IDENTIFICATION ===
concept: switch/case Statement
slug: switch-case-statement

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
pdf_page: 120
section: "5.3.3 switch"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "switch statement"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - if-else-statement
  - strict-equality-operator
extends: []
related:
  - break-continue-statements
contrasts_with:
  - if-else-statement

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes == from ===? (operator side)"
---

# Quick Definition

The `switch` statement evaluates an expression and then transfers control to a matching `case` label, using `===` (strict equality) for comparison. Without `break`, execution falls through to subsequent cases.

# Core Definition

"The switch statement handles exactly this situation [multiway branching on one expression]. The switch keyword is followed by an expression in parentheses and a block of code in curly braces." Case matching uses the `===` identity operator, not `==`. Case expressions are evaluated at runtime (unlike C/C++). (Ch. 5, §5.3.3)

# Prerequisites

- **if-else-statement** — `switch` is an alternative to chained `if/else if`.
- **strict-equality-operator** — `switch` uses `===` for case matching.

# Key Properties

1. Case matching uses `===` — no type conversion.
2. Case expressions are evaluated at runtime (not compile-time constants).
3. Without `break`, execution falls through to the next case.
4. `default:` label handles the no-match case; can appear anywhere in the block.
5. Avoid side effects in case expressions (they are evaluated sequentially until a match).

# Construction / Recognition

```js
switch(expression) {
    case value1: statements; break;
    case value2: statements; break;
    default: statements; break;
}
```

# Context & Application

`switch` is preferred over chained `if/else if` when all branches depend on the value of a single expression. It is commonly used for dispatching on type, status codes, or enumerated values.

# Examples

From the source text (§5.3.3, pp. 120-122):

```js
function convert(x) {
    switch(typeof x) {
        case "number": return x.toString(16);
        case "string": return '"' + x + '"';
        default:       return String(x);
    }
}
```

# Relationships

## Builds Upon
- **strict-equality-operator** — `switch` uses `===` for matching
- **if-else-statement** — `switch` replaces chained `if/else if` on a single expression

## Enables
- Multiway branching patterns, dispatch tables

## Related
- **break-continue-statements** — `break` is essential to prevent fall-through

## Contrasts With
- **if-else-statement** — `if/else` can test arbitrary conditions; `switch` tests one expression against multiple values

# Common Errors

- **Error**: Forgetting `break` statements, causing unintended fall-through.
  **Correction**: End every `case` with `break` or `return` unless fall-through is intentional.

# Common Confusions

- **Confusion**: Expecting `switch` to use `==` for comparison.
  **Clarification**: `switch` uses strict equality `===` — no type coercion occurs during case matching.

# Source Reference

Chapter 5: Statements, Section 5.3.3, pages 120-122.

# Verification Notes

- Definition source: Direct quote from §5.3.3
- Confidence rationale: High — detailed explanation with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
