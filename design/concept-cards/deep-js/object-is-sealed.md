---
# === CORE IDENTIFICATION ===
concept: Object.isSealed()
slug: object-is-sealed

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
section: "11.3.1 Checking whether an object is sealed"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "isSealed"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object-seal
extends: []
related:
  - object-is-extensible
  - object-is-frozen
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.preventExtensions() from Object.seal() from Object.freeze()?"
---

# Quick Definition

`Object.isSealed(obj)` returns `true` if `obj` is non-extensible and all its own properties are non-configurable.

# Core Definition

As described in "Deep JavaScript" Ch 11, `Object.isSealed()` has the signature `(obj: any): boolean`. It "checks whether `obj` is sealed." A frozen object is also considered sealed.

# Prerequisites

- **Object.seal()** — this is the check for that operation's effect

# Key Properties

1. Returns `true` if non-extensible and all own properties are non-configurable
2. Returns `true` for frozen objects (since freezing implies sealing)
3. Returns `false` for merely non-extensible objects (unless all properties happen to be non-configurable)

# Construction / Recognition

## To Construct/Create:
1. Not applicable — this is a check

## To Identify/Recognize:
1. `Object.isSealed(obj)` — returns boolean

# Context & Application

Used to verify an object's protection level at runtime.

# Examples

**Example 1** (Ch 11):
```js
const obj = {};
assert.equal(Object.isSealed(obj), false);
Object.seal(obj);
assert.equal(Object.isSealed(obj), true);
```

# Relationships

## Builds Upon
- **object-seal** — checks whether an object has been sealed

## Enables
- Runtime verification of object protection level

## Related
- **object-is-extensible** — related check
- **object-is-frozen** — stronger check

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `isSealed()` to return `false` for frozen objects.
  **Correction**: Frozen objects are also sealed, so `isSealed()` returns `true`.

# Common Confusions

- **Confusion**: Thinking `isSealed()` returns `true` only for explicitly sealed objects.
  **Clarification**: It returns `true` whenever the conditions are met (non-extensible + all properties non-configurable), regardless of how that state was achieved.

# Source Reference

Chapter 11: Protecting objects from being changed, Section 11.3.1, lines 202-220.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with API signature and example.
- Cross-reference status: verified
