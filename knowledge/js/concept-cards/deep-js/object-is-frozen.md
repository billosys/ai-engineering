---
# === CORE IDENTIFICATION ===
concept: Object.isFrozen()
slug: object-is-frozen

# === CLASSIFICATION ===
category: object-protection
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Protecting objects from being changed"
chapter_number: 11
section: "11.4.1 Checking whether an object is frozen"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "isFrozen"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object-freeze
extends: []
related:
  - object-is-sealed
  - object-is-extensible
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.preventExtensions() from Object.seal() from Object.freeze()?"
---

# Quick Definition

`Object.isFrozen(obj)` returns `true` if `obj` is non-extensible and all its own properties are non-configurable and non-writable (for data properties) or non-configurable (for accessor properties).

# Core Definition

As described in "Deep JavaScript" Ch 11, `Object.isFrozen()` has the signature `(obj: any): boolean`. It "checks whether `obj` is frozen."

# Prerequisites

- **Object.freeze()** — this is the check for that operation's effect

# Key Properties

1. Returns `true` if the object meets all freezing criteria
2. An empty non-extensible object is considered frozen
3. The strongest protection check

# Construction / Recognition

## To Construct/Create:
1. Not applicable — this is a check

## To Identify/Recognize:
1. `Object.isFrozen(obj)` — returns boolean

# Context & Application

Used to verify an object has the strongest protection level before relying on its immutability.

# Examples

**Example 1** (Ch 11):
```js
const point = { x: 17, y: -5 };
assert.equal(Object.isFrozen(point), false);
Object.freeze(point);
assert.equal(Object.isFrozen(point), true);
```

# Relationships

## Builds Upon
- **object-freeze** — checks whether an object has been frozen

## Enables
- Runtime verification of full immutability

## Related
- **object-is-sealed** — weaker check
- **object-is-extensible** — weakest check

## Contrasts With
- None

# Common Errors

- **Error**: Assuming `isFrozen()` checks nested objects.
  **Correction**: It only checks the object itself, not its property values.

# Common Confusions

- **Confusion**: Thinking only explicitly frozen objects return `true`.
  **Clarification**: Any object that meets the criteria (non-extensible, all properties non-configurable and non-writable) returns `true`, regardless of how that state was achieved.

# Source Reference

Chapter 11: Protecting objects from being changed, Section 11.4.1, lines 252-270.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with API signature and example.
- Cross-reference status: verified
