---
# === CORE IDENTIFICATION ===
concept: String Interpolation
slug: string-interpolation

# === CLASSIFICATION ===
category: primitive-types
subcategory: strings
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Using template literals and tagged templates"
chapter_number: 23
pdf_page: null
section: "Template literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "${} syntax"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - template-literal
extends: []
related:
  - string-concatenation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a template literal?"
---

# Quick Definition

String interpolation is the ability to embed expressions inside template literals using `${expression}` syntax. The expression is evaluated, converted to string, and inserted into the resulting string.

# Core Definition

"If we put a dynamically computed value inside a `${}`, it is converted to a string and inserted into the string returned by the literal" (Ch. 23, Section 23.2). Any JavaScript expression can appear inside `${}`, including function calls, arithmetic, and ternary operators.

# Prerequisites

- **template-literal** -- interpolation is a feature of template literals

# Key Properties

1. Syntax: `${expression}` inside backtick-delimited template literal (ES6)
2. Expression is evaluated and converted to string
3. Any valid JavaScript expression can be interpolated
4. Multiple interpolations allowed in one template literal

# Construction / Recognition

```js
const MAX = 100;
`At most ${MAX} allowed: ${x}!`

// Expressions
`Sum: ${1 + 2}`
`Upper: ${name.toUpperCase()}`
```

# Context & Application

String interpolation is the modern replacement for string concatenation with `+`. It produces more readable code, especially with multiple dynamic values.

# Examples

From the source text:

```js
const MAX = 100;
function doSomeWork(x) {
  if (x > MAX) {
    throw new Error(`At most ${MAX} allowed: ${x}!`);
  }
}
assert.throws(
  () => doSomeWork(101),
  {message: 'At most 100 allowed: 101!'}
);
```

# Relationships

## Builds Upon
- **template-literal** — interpolation requires template literal syntax

## Enables
- Readable dynamic string construction

## Related
- **string-concatenation** — the older approach to building strings with values

## Contrasts With
- None

# Common Errors

- **Error**: Using `${}` in single or double quoted strings
  **Correction**: Interpolation only works in template literals (backtick-delimited). `'${x}'` produces the literal string `${x}`.

# Common Confusions

- **Confusion**: Thinking interpolation calls `.toString()` directly
  **Clarification**: It uses the general string conversion mechanism, which may use `.valueOf()` and `.toString()` via ToPrimitive.

# Source Reference

Chapter 23: Using template literals and tagged templates, Section 23.2, lines 109-143.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with examples
- Cross-reference status: verified
