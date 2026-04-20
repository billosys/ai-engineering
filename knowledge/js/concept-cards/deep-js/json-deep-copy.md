---
# === CORE IDENTIFICATION ===
concept: Deep Copying via JSON Round-Tripping
slug: json-deep-copy

# === CLASSIFICATION ===
category: data-management
subcategory: copying
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Copying objects and Arrays"
chapter_number: 7
section: "Hack: generic deep copying via JSON"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "JSON.parse(JSON.stringify()) copy"
  - "JSON round-trip copy"
  - "JSON serialization copy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deep-copy
extends: []
related:
  - nested-spreading-deep-copy
  - generic-deep-copy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a deep copy of an object?"
---

# Quick Definition

Deep copying via JSON round-tripping serializes an object to a JSON string and parses it back, producing a deep copy -- but only for JSON-compatible values.

# Core Definition

As described in "Deep JavaScript" Ch 7, Section 7.3.2: "This is a hack, but, in a pinch, it provides a quick solution: In order to deep-copy an object `original`, we first convert it to a JSON string and parse that JSON string." The significant limitation is that only JSON-compatible keys and values are preserved. Symbol keys, functions, `undefined`, and BigInts are either silently dropped or cause exceptions.

# Prerequisites

- **Deep copy** -- understanding what a deep copy is and why it is needed
- **JSON** -- understanding JSON serialization and its value type limitations

# Key Properties

1. Produces a genuine deep copy (no shared references).
2. Only supports JSON-compatible keys (no Symbols) and values (no functions, undefined, BigInt).
3. Unsupported values are silently dropped (functions, undefined, Symbol keys) or throw exceptions (BigInt).
4. Does not preserve prototypes, property attributes, or special objects (Date, RegExp, Map, Set).
5. Called a "hack" by the source author -- use with awareness of limitations.

# Construction / Recognition

## To Construct/Create:
1. ```js
   function jsonDeepCopy(original) {
     return JSON.parse(JSON.stringify(original));
   }
   ```

## To Identify/Recognize:
1. The pattern `JSON.parse(JSON.stringify(x))`.

# Context & Application

Useful as a quick solution for deep-copying plain data objects with only JSON-compatible values (strings, numbers, booleans, null, arrays, plain objects). Not suitable for objects containing functions, Symbols, Dates, RegExps, or other non-JSON types.

# Examples

**Example 1** (Ch 7): Basic usage:
```js
const original = {name: 'Jane', work: {employer: 'Acme'}};
const copy = JSON.parse(JSON.stringify(original));
assert.deepEqual(original, copy);
```

**Example 2** (Ch 7): Unsupported values silently dropped:
```js
assert.deepEqual(
  JSON.parse(JSON.stringify({
    [Symbol('a')]: 'abc',  // Symbol key: ignored
    b: function () {},       // function: ignored
    c: undefined,            // undefined: ignored
  })),
  {}  // empty object
);
```

**Example 3** (Ch 7): BigInt throws:
```js
assert.throws(
  () => JSON.parse(JSON.stringify({a: 123n})),
  /^TypeError: Do not know how to serialize a BigInt$/);
```

# Relationships

## Builds Upon
- **Deep copy** -- JSON round-tripping is one approach to deep copying

## Enables
- **Quick deep copy for data objects** -- suitable for API responses and configuration objects

## Related
- **Nested spreading deep copy** -- manual alternative without JSON limitations
- **Generic deep copy** -- recursive alternative that handles more types

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Using JSON round-tripping on objects containing Dates (they become strings).
  **Correction**: Use a recursive deep copy function or `structuredClone()` for Date objects.

# Common Confusions

- **Confusion**: JSON round-tripping is a reliable, general-purpose deep copy method.
  **Clarification**: It is explicitly described as a "hack" with significant limitations. Many JavaScript value types are silently lost or cause errors.

# Source Reference

Chapter 7: "Copying objects and Arrays", Section 7.3.2, lines 3381-3425.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit implementation, limitations, and examples all provided in source.
- Cross-reference status: verified against Ch 7 section 7.3.2
