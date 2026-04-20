---
# === CORE IDENTIFICATION ===
concept: String Concatenation
slug: string-concatenation

# === CLASSIFICATION ===
category: primitive-types
subcategory: strings
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Strings"
chapter_number: 22
pdf_page: null
section: "String concatenation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-type
  - plus-operator
extends: []
related:
  - template-literal
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Strings can be concatenated using the `+` operator (which converts non-strings), the `+=` operator for incremental building, or by joining array elements with `.join()`.

# Core Definition

"If at least one operand is a string, the plus operator (`+`) converts any non-strings to strings and concatenates the result." The `+=` operator builds strings incrementally. An alternative is collecting strings in an array and calling `.join()`, which is useful when a separator is needed (Ch. 22, Section 22.4).

# Prerequisites

- **string-type** -- concatenation produces new strings
- **plus-operator** -- the `+` operator in string mode

# Key Properties

1. `+` converts non-strings to strings when one operand is a string
2. `+=` is efficient for incremental building (engines optimize internally)
3. Array `.join()` is useful for separator-based concatenation
4. Strings are immutable -- concatenation always creates new strings

# Construction / Recognition

```js
assert.equal(3 + ' times ' + 4, '3 times 4');

let str = '';
str += 'Say it';
str += ' one more';
str += ' time';

['a', 'b', 'c'].join(', ') // 'a, b, c'
```

# Context & Application

Use `+` or template literals for simple concatenation. Use array `.join()` when building strings from collections with separators.

# Examples

From the source text:

```js
assert.equal(3 + ' times ' + 4, '3 times 4');

let str = '';
str += 'Say it';
str += ' one more';
str += ' time';
assert.equal(str, 'Say it one more time');

// Array join with separator
function getPackingList(isAbroad = false, days = 1) {
  const items = [];
  items.push('tooth brush');
  if (isAbroad) items.push('passport');
  if (days > 3) items.push('water bottle');
  return items.join(', ');
}
```

# Relationships

## Builds Upon
- **string-type** — produces new strings
- **plus-operator** — `+` in string mode

## Enables
- Building dynamic strings

## Related
- **template-literal** — modern alternative for string interpolation

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `+` to add numbers when one operand is a string
  **Correction**: `'3' + 4` is `'34'` (string concatenation), not `7`. Convert strings to numbers explicitly if needed.

# Common Confusions

- **Confusion**: Thinking `+=` is slow for string building
  **Clarification**: Modern JavaScript engines internally optimize `+=` for strings. It is quite efficient.

# Source Reference

Chapter 22: Strings, Section 22.4, lines 330-407.

# Verification Notes

- Definition source: direct
- Confidence rationale: Multiple approaches described with examples
- Cross-reference status: verified
