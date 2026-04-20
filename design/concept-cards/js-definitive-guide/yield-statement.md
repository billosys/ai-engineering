---
# === CORE IDENTIFICATION ===
concept: yield Statement
slug: yield-statement

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: statements
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Statements"
chapter_number: 5
pdf_page: 134
section: "5.5.5 yield"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - return-statement
  - function-definition-expressions
extends: []
related: []
contrasts_with:
  - return-statement

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `yield` statement is used in generator functions (ES6) to produce the next value in a generated sequence without terminating the function. It is technically an operator.

# Core Definition

"The yield statement is much like the return statement but is used only in ES6 generator functions to produce the next value in the generated sequence of values without actually returning." (Ch. 5, §5.5.5)

# Prerequisites

- **return-statement** — `yield` is analogous to `return` but does not terminate the function.
- **function-definition-expressions** — `yield` is only valid inside `function*` generators.

# Key Properties

1. Only valid inside generator functions (`function*`).
2. Produces a value and suspends the generator until the next value is requested.
3. Technically an operator rather than a statement (see §12.4.2).

# Construction / Recognition

```js
function* range(from, to) {
    for(let i = from; i <= to; i++) {
        yield i;
    }
}
```

# Context & Application

`yield` enables generator functions that produce sequences of values lazily, on demand. Full coverage is in Chapter 12.

# Examples

From the source text (§5.5.5, p. 134):

```js
function* range(from, to) {
    for(let i = from; i <= to; i++) {
        yield i;
    }
}
```

# Relationships

## Builds Upon
- **return-statement** — `yield` is analogous to `return` for generators

## Enables
- Generator-based iteration (covered in Ch. 12)

## Related
- No related concepts within Chapters 4-6

## Contrasts With
- **return-statement** — `return` terminates the function; `yield` suspends it and can resume

# Common Errors

- **Error**: Using `yield` outside a generator function.
  **Correction**: `yield` is only valid inside `function*` declarations/expressions.

# Common Confusions

- **Confusion**: Believing `yield` terminates the function like `return`.
  **Clarification**: `yield` suspends the function — execution resumes from the `yield` point when the next value is requested.

# Source Reference

Chapter 5: Statements, Section 5.5.5, page 134.

# Verification Notes

- Definition source: Direct quote from §5.5.5
- Confidence rationale: Medium — brief coverage; full details deferred to Ch. 12
- Uncertainties: Complete semantics not covered until Ch. 12
- Cross-reference status: Unverified (Ch. 12 not in scope)
