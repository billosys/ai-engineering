---
# === CORE IDENTIFICATION ===
concept: BigInt and JSON
slug: bigint-json

# === CLASSIFICATION ===
category: primitive-types
subcategory: bigints
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Bigints -- arbitrary-precision integers (advanced)"
chapter_number: 20
pdf_page: null
section: "Bigints and JSON"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bigint-type
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JSON does not support bigints. `JSON.stringify(123n)` throws a `TypeError`. The recommended workaround is to store bigints as strings using custom replacer/reviver functions.

# Core Definition

"The JSON standard is fixed and won't change." JSON cannot represent bigints, so `JSON.stringify()` throws `TypeError` for bigint values. The recommended approach is using a custom replacer to serialize bigints as prefixed strings and a reviver to parse them back (Ch. 20, Section 20.8).

# Prerequisites

- **bigint-type** -- the type that JSON cannot represent

# Key Properties

1. `JSON.stringify(123n)` throws `TypeError`
2. Workaround: store bigints as prefixed strings
3. Use custom replacer/reviver functions for round-tripping

# Construction / Recognition

```js
// Throws
> JSON.stringify(123n)
TypeError: Do not know how to serialize a BigInt

// Workaround with replacer
function bigintReplacer(_key, value) {
  if (typeof value === 'bigint') {
    return '[[bigint]]' + value;
  }
  return value;
}
```

# Context & Application

When transmitting bigint values over JSON APIs, encode them as strings. Common approaches include string encoding with a prefix or wrapping in an object.

# Examples

From the source text:

```js
const bigintPrefix = '[[bigint]]';

function bigintReplacer(_key, value) {
  if (typeof value === 'bigint') {
    return bigintPrefix + value;
  }
  return value;
}

const data = { value: 9007199254740993n };
assert.equal(
  JSON.stringify(data, bigintReplacer),
  '{"value":"[[bigint]]9007199254740993"}'
);

function bigintReviver(_key, value) {
  if (typeof value === 'string' && value.startsWith(bigintPrefix)) {
    return BigInt(value.slice(bigintPrefix.length));
  }
  return value;
}
```

# Relationships

## Builds Upon
- **bigint-type** — the type in question

## Enables
- JSON serialization patterns for bigints

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Including bigint values in objects passed to `JSON.stringify()` without a replacer
  **Correction**: Always use a custom replacer function when objects may contain bigints.

# Common Confusions

- **Confusion**: Thinking JSON.stringify silently converts bigints to numbers
  **Clarification**: It throws a `TypeError`, unlike its behavior with `undefined` (which is silently omitted).

# Source Reference

Chapter 20: Bigints, Section 20.8, lines 879-936.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete replacer/reviver pattern provided
- Cross-reference status: verified
