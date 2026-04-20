---
# === CORE IDENTIFICATION ===
concept: Ambiguous Syntax
slug: ambiguous-syntax

# === CLASSIFICATION ===
category: syntax-fundamentals
subcategory: syntax-categories
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Syntax"
chapter_number: 9
pdf_page: null
section: "9.6 Ambiguous syntax"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - syntactic ambiguity

# === TYPED RELATIONSHIPS ===
prerequisites:
  - statements
  - expressions
  - expression-statements
extends: []
related:
  - function-declarations
  - arrow-function-expressions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why does the same syntax sometimes behave differently in JavaScript?"
---

# Quick Definition

JavaScript has syntactically ambiguous constructs where the same code means different things depending on whether it appears in statement or expression context -- notably `function` (declaration vs. expression) and `{}` (block vs. object literal).

# Core Definition

"JavaScript has several programming constructs that are syntactically ambiguous: the same syntax is interpreted differently, depending on whether it is used in statement context or in expression context." (Ch. 9, &sect;9.6). The two main cases are: `function` at the start of a statement is a function declaration, not a function expression; `{` at the start of a statement is a code block, not an object literal. Resolution: "statements starting with `function` or `{` are never interpreted as expressions." To force expression interpretation, wrap in parentheses.

# Prerequisites

- **statements** -- one side of the ambiguity
- **expressions** -- the other side
- **expression-statements** -- where ambiguity arises

# Key Properties

1. `function` at statement start = function declaration; in expression context = function expression
2. `{` at statement start = code block; in expression context = object literal
3. Resolution rule: statements starting with `function` or `{` are never expressions
4. Parentheses force expression interpretation: `(function(x) { ... })('abc')`

# Construction / Recognition

```js
// Function declaration (statement)
function id(x) { return x; }

// Function expression (expression context, via assignment)
const id = function me(x) { return x; };

// Object literal (expression context)
const obj = {};

// Code block (statement context)
{ }
```

# Context & Application

This ambiguity affects IIFEs, arrow functions returning objects, and object destructuring assignments.

# Examples

From the source text (Ch. 9, &sect;9.6.3):
```js
(function (x) { console.log(x) })('abc');
// Output: abc
// Parentheses force function expression interpretation
```

# Relationships

## Builds Upon
- **statements** -- statement context triggers one interpretation
- **expressions** -- expression context triggers another

## Enables
- Understanding IIFEs (Immediately Invoked Function Expressions)

## Related
- **function-declarations** -- one side of the function ambiguity
- **arrow-function-expressions** -- can trigger the object literal ambiguity when returning objects

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Starting a statement with `{` intending an object literal.
  **Correction**: Wrap in parentheses: `({prop: value})`.

# Common Confusions

- **Confusion**: Getting unexpected results when returning object literals from arrow functions.
  **Clarification**: `() => {a: 1}` is a code block with a label, not an object. Use `() => ({a: 1})`.

# Source Reference

Chapter 9: Syntax, Section 9.6, lines 768-861.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit explanation with disambiguation rules
- Cross-reference status: verified
