---
# === CORE IDENTIFICATION ===
concept: Symbol-Keyed Method Names
slug: symbol-keyed-method-names

# === CLASSIFICATION ===
category: functions
subcategory: naming
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The property .name of functions (bonus)"
chapter_number: 21
section: "21.2.7.1 Methods whose keys are symbols"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-name-property
  - method-naming
extends:
  - method-naming
related:
  - function-naming-rules
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a named function expression from an anonymous function?"
---

# Quick Definition

Methods with Symbol keys have string `.name` properties: the symbol's description in square brackets if present, or an empty string if the symbol has no description.

# Core Definition

From "Deep JavaScript" (Ch 21.2.7.1): "The key of a method can be a symbol. The `.name` property of such a method is still a string: If the symbol has a description, the method's name is the description in square brackets. Otherwise, the method's name is the empty string (`''`)."

# Prerequisites

- **Function .name property** — Symbol-keyed methods have specific naming behavior
- **Method naming** — Builds on general method naming rules

# Key Properties

1. Symbol with description: `.name` is `'[description]'`
2. Symbol without description: `.name` is `''`
3. The `.name` is always a string, even though the key is a Symbol

# Construction / Recognition

## To Construct/Create:
1. Define a method with a Symbol key: `{ [mySymbol]() {} }`

## To Identify/Recognize:
1. A `.name` value in square brackets like `'[keyWithDesc]'`

# Context & Application

This is an edge case of function naming. Symbol-keyed methods appear in various built-in protocols (e.g., `Symbol.iterator`), so understanding their naming helps with debugging.

# Examples

**Example 1** (Ch 21):
```js
const keyWithDesc = Symbol('keyWithDesc');
const keyWithoutDesc = Symbol();

const obj = {
  [keyWithDesc]() {},
  [keyWithoutDesc]() {},
};
assert.equal(obj[keyWithDesc].name, '[keyWithDesc]');
assert.equal(obj[keyWithoutDesc].name, '');
```

# Relationships

## Builds Upon
- **Method naming** — Special case for Symbol keys

# Common Confusions

- **Confusion**: The `.name` of a Symbol-keyed method is a Symbol
  **Clarification**: `.name` is always a string; Symbol descriptions are converted to strings in square brackets

# Source Reference

Chapter 21: The property .name of functions (bonus), Section 21.2.7.1, lines 11437+.

# Verification Notes

- Definition source: direct from source with assertions
- Confidence rationale: Explicitly demonstrated
- Cross-reference status: verified
