---
# === CORE IDENTIFICATION ===
concept: Defensive Copying of Output
slug: defensive-copying-output

# === CLASSIFICATION ===
category: data-management
subcategory: defensive-patterns
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The problems of shared mutable state and how to avoid them"
chapter_number: 9
section: "Copying exposed internal data"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "output defense"
  - "return value copying"
  - "encapsulation via copying"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - defensive-copying
  - shared-mutable-state
extends:
  - defensive-copying
related:
  - defensive-copying-input
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does defensive copying relate to immutability?"
  - "What is shared mutable state?"
---

# Quick Definition

Defensive copying of output means copying internal data before exposing it to external code, preventing external parties from mutating the object's internal state through the returned reference.

# Core Definition

As described in "Deep JavaScript" Ch 9, Section 9.2.1.2: "Copying internal data before exposing it to an outside party, means that that party can't disrupt our internal activity." This protects object encapsulation -- even if external code modifies the returned value, the object's internal state remains intact.

# Prerequisites

- **Defensive copying** -- output copying is one direction of defensive copying
- **Shared mutable state** -- the problem motivating the copy

# Key Properties

1. The copy is made in getter/accessor methods before returning internal data.
2. External code receives a copy, not a reference to internal state.
3. Protects internal state from external mutation.
4. Essential for maintaining object invariants.

# Construction / Recognition

## To Construct/Create:
1. In a method that exposes internal data, return a copy: `return [...this._data];`

## To Identify/Recognize:
1. A spread or copy operation in a return statement of a method that exposes internal collections.

# Context & Application

Critical for classes/objects that maintain internal state and expose it via getters. Without output defense, callers can break object invariants by mutating the returned reference.

# Examples

**Example 1** (Ch 9): Vulnerable StringBuilder (no output defense):
```js
class StringBuilder {
  _data = [];
  add(str) { this._data.push(str); }
  getParts() {
    return this._data; // Exposes internal reference!
  }
  toString() { return this._data.join(''); }
}

const sb = new StringBuilder();
sb.add('Hello');
sb.add(' world!');
sb.getParts().length = 0; // Destroys internal state!
assert.equal(sb.toString(), ''); // Broken!
```

**Example 2** (Ch 9): Fixed StringBuilder (with output defense):
```js
class StringBuilder {
  _data = [];
  add(str) { this._data.push(str); }
  getParts() {
    return [...this._data]; // Defensive copy
  }
  toString() { return this._data.join(''); }
}

const sb = new StringBuilder();
sb.add('Hello');
sb.add(' world!');
sb.getParts().length = 0; // Only affects the copy
assert.equal(sb.toString(), 'Hello world!'); // Still works!
```

# Relationships

## Builds Upon
- **Defensive copying** -- this is the output direction

## Enables
- **Safe encapsulation** -- internal state cannot be corrupted through returned values

## Related
- **Defensive copying input** -- the complementary direction

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Returning internal arrays/objects directly from getters.
  **Correction**: Always return a copy: `return [...this._data]` or `return {...this._state}`.

# Common Confusions

- **Confusion**: Private fields (`#field`) eliminate the need for output defense.
  **Clarification**: Private fields prevent direct access to the field, but if a method returns a reference to the private field's value, external code can still mutate that value.

# Source Reference

Chapter 9: "The problems of shared mutable state and how to avoid them", Section 9.2.1.2, lines 4050-4100.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit before/after example with the StringBuilder class showing both the vulnerability and the fix.
- Cross-reference status: verified against Ch 9 section 9.2.1.2
