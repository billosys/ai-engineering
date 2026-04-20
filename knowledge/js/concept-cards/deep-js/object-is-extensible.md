---
# === CORE IDENTIFICATION ===
concept: Object.isExtensible()
slug: object-is-extensible

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
section: "11.2.1 Checking whether an object is extensible"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "isExtensible"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object-prevent-extensions
extends: []
related:
  - object-is-sealed
  - object-is-frozen
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.preventExtensions() from Object.seal() from Object.freeze()?"
---

# Quick Definition

`Object.isExtensible(obj)` returns `true` if new properties can be added to `obj`, `false` otherwise. It returns `false` for objects that have been passed to `preventExtensions()`, `seal()`, or `freeze()`.

# Core Definition

As described in "Deep JavaScript" Ch 11, `Object.isExtensible()` has the signature `(obj: any): boolean`. It "checks whether `obj` is extensible."

# Prerequisites

- **Object.preventExtensions()** — this is the check for that operation's effect

# Key Properties

1. Returns `true` for normal objects
2. Returns `false` after `preventExtensions()`, `seal()`, or `freeze()`
3. Accepts any value (non-objects return `false`)

# Construction / Recognition

## To Construct/Create:
1. Not applicable — this is a check, not a constructor

## To Identify/Recognize:
1. `Object.isExtensible(obj)` — returns boolean

# Context & Application

Used to check whether an object can accept new properties before attempting to add them.

# Examples

**Example 1** (Ch 11):
```js
const obj = {};
assert.equal(Object.isExtensible(obj), true);
Object.preventExtensions(obj);
assert.equal(Object.isExtensible(obj), false);
```

# Relationships

## Builds Upon
- **object-prevent-extensions** — checks the effect of this method

## Enables
- Runtime checks before property addition

## Related
- **object-is-sealed** — similar check for sealing
- **object-is-frozen** — similar check for freezing

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `isExtensible` to return `true` for sealed or frozen objects.
  **Correction**: Both `seal()` and `freeze()` also prevent extensions, so `isExtensible()` returns `false`.

# Common Confusions

- **Confusion**: Thinking `isExtensible() === false` means the object is frozen.
  **Clarification**: Non-extensible only means no new properties can be added. The object may or may not be sealed or frozen.

# Source Reference

Chapter 11: Protecting objects from being changed, Section 11.2.1, lines 99-117.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with API signature and example.
- Cross-reference status: verified
