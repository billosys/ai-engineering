---
# === CORE IDENTIFICATION ===
concept: Collection Immutability via Wrapping
slug: collection-immutability

# === CLASSIFICATION ===
category: class-patterns
subcategory: wrapping
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Immutable wrappers for collections"
chapter_number: 16
section: "16.1.1 Making collections immutable via wrapping"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - immutable collection pattern
  - read-only collection

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - wrapper-pattern
extends: []
related:
  - immutable-wrapper
  - immutable-map-wrapper
  - proxy-based-immutable-array
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make a mutable collection immutable without copying it?"
---

# Quick Definition

Collection immutability via wrapping is the technique of making a mutable collection (Map, Array, etc.) appear immutable by wrapping it in an object that exposes only non-destructive operations, without copying the data.

# Core Definition

As explained in "Deep JavaScript" (Ch 16, Section 16.1.1): "One important use case for this technique is an object that has an internal mutable data structure that it wants to export safely without copying it. The export being 'live' may also be a goal." The wrapper removes destructive operations from the interface. The chapter notes two limitations: implementations are "sketches" needing "more work," and "they work shallowly" — the wrapped collection is immutable but returned data is not.

# Prerequisites

- **JavaScript classes** — Object composition.
- **Wrapper pattern** — The technique used to implement this.

# Key Properties

1. The collection is **not copied** — wrapping is O(1).
2. The wrapped view is **live** — changes to the internal collection are visible.
3. Only **non-destructive** methods are forwarded.
4. Works **shallowly** — returned values from the collection are not themselves immutable.
5. For Maps: use **class-based wrapping**. For Arrays: use **Proxy-based wrapping**.

# Construction / Recognition

## To Construct/Create:
1. Determine whether the collection is method-based (Map) or property-based (Array).
2. For method-based: create a wrapper class forwarding only read methods.
3. For property-based: create a Proxy with restricted get/set/delete traps.

## To Identify/Recognize:
1. A wrapper or Proxy around a collection.
2. Read operations succeed; write operations throw.
3. The original collection remains mutable.

# Context & Application

This technique is the central topic of Chapter 16. It provides a way to safely share internal data structures without the cost of defensive copying and with the benefit of live views.

# Examples

**Example 1** (Ch 16): Map immutability:
```js
const map = new Map([[false, 'no'], [true, 'yes']]);
const wrapped = new ImmutableMapWrapper(map);
wrapped.get(true); // 'yes' (works)
wrapped.set(false, 'x'); // TypeError (blocked)
```

**Example 2** (Ch 16): Array immutability:
```js
const arr = ['a', 'b', 'c'];
const wrapped = wrapArrayImmutably(arr);
wrapped[1]; // 'b' (works)
wrapped[1] = 'x'; // TypeError (blocked)
```

# Relationships

## Builds Upon
- **Wrapper pattern** — The general technique.
- **Proxy** — Required for Array wrapping.

## Enables
- **Safe internal state sharing** — Owner keeps mutability; consumers get read-only view.
- **Live views** — Unlike copying, changes are reflected through the wrapper.

## Related
- **Immutable Map wrapper** — Specific Map implementation.
- **Proxy-based immutable Array** — Specific Array implementation.

## Contrasts With
- **Defensive copying** — Copies the entire collection; independent but expensive.
- **Object.freeze()** — Makes the original immutable; wrapping preserves internal mutability.

# Common Errors

- **Error**: Assuming immutable wrappers make deeply nested data immutable.
  **Correction**: Wrappers are shallow. Values returned by `get()` or index access are not wrapped. "This could be fixed by wrapping some of the results that are returned by methods."

# Common Confusions

- **Confusion**: Thinking wrapping copies the data.
  **Clarification**: Wrapping stores a reference; no copying occurs. This is why the view is live.

# Source Reference

Chapter 16: Immutable wrappers for collections, Section 16.1.1, lines 7669-7689.

# Verification Notes

- Definition source: direct (from source explanation of use case and limitations)
- Confidence rationale: Explicitly described as the chapter's central concept
- Cross-reference status: verified against Map and Array implementations
