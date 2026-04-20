---
# === CORE IDENTIFICATION ===
concept: Symbol Descriptions
slug: symbol-descriptions

# === CLASSIFICATION ===
category: primitive-types
subcategory: symbols
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Symbols"
chapter_number: 24
pdf_page: null
section: "The descriptions of symbols"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symbol-type
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Symbol and when would you use one?"
---

# Quick Definition

A symbol's description is the optional string passed to `Symbol()`, accessible via `.toString()` (returns `'Symbol(desc)'`) or the `.description` property (returns `'desc'`, since ES2019).

# Core Definition

The parameter passed to `Symbol()` provides a description primarily useful for debugging. It is accessed in two ways: `.toString()` returns `'Symbol(mySymbol)'`, and `.description` (ES2019) returns just the description string `'mySymbol'` (Ch. 24, Section 24.2).

# Prerequisites

- **symbol-type** -- descriptions are attached to symbols

# Key Properties

1. Optional parameter to `Symbol()`: `Symbol('mySymbol')`
2. `.toString()` returns `'Symbol(mySymbol)'`
3. `.description` property returns `'mySymbol'` (ES2019)
4. Descriptions do not affect identity: two symbols with the same description are still different

# Construction / Recognition

```js
const mySymbol = Symbol('mySymbol');
assert.equal(mySymbol.toString(), 'Symbol(mySymbol)');
assert.equal(mySymbol.description, 'mySymbol');
```

# Context & Application

Descriptions improve debuggability by making symbols identifiable in logs and error messages.

# Examples

From the source text:

```js
const mySymbol = Symbol('mySymbol');
assert.equal(mySymbol.toString(), 'Symbol(mySymbol)');
assert.equal(mySymbol.description, 'mySymbol');
```

# Relationships

## Builds Upon
- **symbol-type** — descriptions are a property of symbols

## Enables
- Better debugging and logging

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Using the description to identify or compare symbols
  **Correction**: Descriptions are for debugging only. Compare symbols by reference, not by description.

# Common Confusions

- **Confusion**: Thinking `.description` was always available
  **Clarification**: `.description` was added in ES2019. Before that, only `.toString()` was available.

# Source Reference

Chapter 24: Symbols, Section 24.2, lines 104-130.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit examples of both access methods
- Cross-reference status: verified
