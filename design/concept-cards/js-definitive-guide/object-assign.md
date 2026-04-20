---
# === CORE IDENTIFICATION ===
concept: Object.assign()
slug: object-assign

# === CLASSIFICATION ===
category: objects
subcategory: property-operations
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 159
section: "6.7 Extending Objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "extending objects"
  - "copying properties"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - own-vs-inherited-properties
  - enumerating-properties
extends: []
related:
  - spread-operator-in-object-literals
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes shallow copy from deep copy of objects?"
---

# Quick Definition

`Object.assign()` copies enumerable own properties (including Symbols) from one or more source objects into a target object, modifying and returning the target. It performs a shallow copy.

# Core Definition

"Object.assign() expects two or more objects as its arguments. It modifies and returns the first argument, which is the target object, but does not alter the second or any subsequent arguments, which are the source objects. For each source object, it copies the enumerable own properties of that object (including those whose names are Symbols) into the target object." (Ch. 6, §6.7)

# Prerequisites

- **own-vs-inherited-properties** — Only own properties are copied.
- **enumerating-properties** — Only enumerable properties are copied.

# Key Properties

1. Modifies and returns the target object (first argument).
2. Copies enumerable own properties, including Symbols.
3. Later source objects override earlier ones and the target for same-named properties.
4. Uses ordinary get/set operations — invokes getters on sources and setters on target.
5. Does not copy getters/setters themselves as methods.
6. Performs a shallow copy — nested objects are shared by reference.
7. Overrides pattern: `o = Object.assign({}, defaults, o)`.

# Construction / Recognition

```js
Object.assign(target, source1, source2, ...)
```

# Context & Application

`Object.assign()` is used for merging objects, applying defaults, and creating shallow copies. It is the ES6 standard version of the `extend()` utility common in frameworks.

# Examples

From the source text (§6.7, pp. 159-161):

```js
let target = {x: 1}, source = {y: 2, z: 3};
for(let key of Object.keys(source)) {
    target[key] = source[key];
}
target   // => {x: 1, y: 2, z: 3}

// Using Object.assign():
Object.assign({x: 1}, {x: 2, y: 2}, {y: 3, z: 4})  // => {x: 2, y: 3, z: 4}

// Defaults pattern:
o = Object.assign({}, defaults, o);
// Or equivalently with spread:
o = {...defaults, ...o};
```

# Relationships

## Builds Upon
- **own-vs-inherited-properties** — Only copies own properties
- **enumerating-properties** — Only copies enumerable properties

## Enables
- Shallow copy and merge patterns

## Related
- **spread-operator-in-object-literals** — `{...obj}` achieves similar results for object literals

## Contrasts With
- No direct contrast (deep copy requires other techniques)

# Common Errors

- **Error**: Expecting `Object.assign()` to perform a deep copy.
  **Correction**: Nested objects are copied by reference, not cloned. Use `structuredClone()` or recursive copying for deep copies.

- **Error**: Using `Object.assign(o, defaults)` for defaults (overwrites o's existing properties).
  **Correction**: Use `Object.assign({}, defaults, o)` so o's properties override defaults.

# Common Confusions

- **Confusion**: Expecting getter/setter methods to be copied as-is.
  **Clarification**: `Object.assign()` invokes getters on the source and setters on the target — it copies values, not accessor definitions.

# Source Reference

Chapter 6: Objects, Section 6.7, pages 159-161.

# Verification Notes

- Definition source: Direct quote from §6.7
- Confidence rationale: High — detailed with multiple patterns
- Uncertainties: None
- Cross-reference status: Verified
