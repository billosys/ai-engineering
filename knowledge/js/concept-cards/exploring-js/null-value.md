---
# === CORE IDENTIFICATION ===
concept: Null Value
slug: null-value

# === CLASSIFICATION ===
category: primitive-types
subcategory: non-values
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "The non-values undefined and null"
chapter_number: 16
pdf_page: null
section: "undefined vs. null"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - undefined-value
  - falsy-and-truthy-values
  - nullish-coalescing-operator
contrasts_with:
  - undefined-value

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is `undefined` and how does it differ from `null`?"
  - "What distinguishes `null` from `undefined`?"
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

`null` is a primitive value that means "the intentional absence of any object value" -- it is used by programmers to explicitly indicate that a variable holds no meaningful value.

# Core Definition

`null` means "the intentional absence of any object value" (quoting the language specification). Programmers use `null` to mean "explicitly switched off" -- it helps implement option types (also called maybe types) where a variable can hold either a meaningful value or a meta-value meaning "no meaningful value" (Ch. 16, Section 16.1).

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. `typeof null` is `'object'` (a historical bug in JavaScript)
2. `null` is falsy
3. Accessing properties on `null` throws a `TypeError`
4. JSON supports `null` but not `undefined`
5. `null` is the end of prototype chains: `Object.getPrototypeOf(Object.prototype)` is `null`
6. Regex non-matches return `null`: `/a/.exec('x')` is `null`

# Construction / Recognition

`null` appears in these contexts:
- End of prototype chain: `Object.getPrototypeOf(Object.prototype)`
- Failed regex match: `/a/.exec('x')`
- JSON representation: `JSON.stringify({a: undefined, b: null})` produces `'{"b":null}'`

# Context & Application

`null` is the conventional "no object" value in JavaScript, borrowed from Java. Use it when you want to explicitly indicate that a reference or variable intentionally has no object value.

# Examples

From the source text:

```js
// End of prototype chain
> Object.getPrototypeOf(Object.prototype)
null

// Failed regex match
> /a/.exec('x')
null

// JSON supports null but not undefined
> JSON.stringify({a: undefined, b: null})
'{"b":null}'
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **nullish-coalescing-operator** — triggers the default value
- **falsy-and-truthy-values** — `null` is falsy

## Related
- **undefined-value** — the other non-value in JavaScript

## Contrasts With
- **undefined-value** — `undefined` means "not initialized/not existing"; `null` means "intentionally no value"

# Common Errors

- **Error**: Using `typeof null === 'null'` to check for null
  **Correction**: `typeof null` is `'object'` (a historical bug). Use `x === null` instead.

# Common Confusions

- **Confusion**: Thinking `null` and `undefined` are the same
  **Clarification**: They are distinct values with different semantics. `null` is programmer-chosen; `undefined` is language-chosen.

# Source Reference

Chapter 16: The non-values undefined and null, Sections 16.1-16.2.2, lines 56-150.

# Verification Notes

- Definition source: direct (quotes the ECMAScript specification)
- Confidence rationale: Explicit definition with spec quote
- Cross-reference status: verified
