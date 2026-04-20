---
# === CORE IDENTIFICATION ===
concept: Symbols as Values for Constants
slug: symbols-as-constants

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
section: "Symbols as values for constants"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symbol-type
extends: []
related:
  - symbols-as-property-keys
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Symbol and when would you use one?"
---

# Quick Definition

Symbols can serve as unique values for constants (like enum values), preventing accidental collisions between unrelated constants that happen to have the same string value.

# Core Definition

When using strings as constant values, there is a risk of collision: `COLOR_BLUE = 'Blue'` and `MOOD_BLUE = 'Blue'` are equal even though they represent different concepts. Symbols solve this: `COLOR_BLUE = Symbol('Blue')` and `MOOD_BLUE = Symbol('Blue')` are guaranteed to be different (Ch. 24, Section 24.3.1).

# Prerequisites

- **symbol-type** -- symbols provide unique identities

# Key Properties

1. Each `Symbol()` call produces a unique value
2. Prevents accidental equality between unrelated constants
3. Description aids debugging but does not affect identity
4. Works well with `switch` statements

# Construction / Recognition

```js
const COLOR_RED    = Symbol('Red');
const COLOR_BLUE   = Symbol('Blue');
const MOOD_BLUE    = Symbol('Blue');

assert.notEqual(COLOR_BLUE, MOOD_BLUE); // different symbols!
```

# Context & Application

Use symbols for enum-like constants where uniqueness matters more than serializability. Note that symbols cannot be serialized to JSON.

# Examples

From the source text:

```js
const COLOR_RED    = Symbol('Red');
const COLOR_ORANGE = Symbol('Orange');
const COLOR_YELLOW = Symbol('Yellow');
const COLOR_GREEN  = Symbol('Green');
const COLOR_BLUE   = Symbol('Blue');
const COLOR_VIOLET = Symbol('Violet');

function getComplement(color) {
  switch (color) {
    case COLOR_RED: return COLOR_GREEN;
    case COLOR_ORANGE: return COLOR_BLUE;
    case COLOR_YELLOW: return COLOR_VIOLET;
    case COLOR_GREEN: return COLOR_RED;
    case COLOR_BLUE: return COLOR_ORANGE;
    case COLOR_VIOLET: return COLOR_YELLOW;
    default: throw new Exception('Unknown color: '+color);
  }
}
assert.equal(getComplement(COLOR_YELLOW), COLOR_VIOLET);
```

# Relationships

## Builds Upon
- **symbol-type** — uses unique identity property

## Enables
- Type-safe enum patterns

## Related
- **symbols-as-property-keys** — the other main use case for symbols

## Contrasts With
- None

# Common Errors

- **Error**: Trying to serialize symbol constants to JSON
  **Correction**: Symbols are not JSON-serializable. Use strings for serializable constants.

# Common Confusions

- **Confusion**: Thinking symbol-based constants can be reconstructed from descriptions
  **Clarification**: There is no way to reconstruct a specific symbol from its description. Each `Symbol()` call creates a new unique symbol.

# Source Reference

Chapter 24: Symbols, Section 24.3.1, lines 138-199.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete example with use case
- Cross-reference status: verified
