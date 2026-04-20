---
# === CORE IDENTIFICATION ===
concept: Immutable Wrapper
slug: immutable-wrapper

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
  - read-only wrapper
  - immutable collection wrapper

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - wrapper-pattern
extends:
  - wrapper-pattern
related:
  - immutable-map-wrapper
  - proxy-based-immutable-array
  - collection-immutability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make a mutable collection immutable without copying it?"
---

# Quick Definition

An immutable wrapper makes a collection immutable by wrapping it in a new object that only forwards non-destructive (read-only) operations, removing all mutating methods from the interface.

# Core Definition

As described in "Deep JavaScript" (Ch 16, Section 16.1.1): "To make a collection immutable, we can use wrapping and remove all destructive operations from its interface." The wrapper stores the mutable collection privately and only exposes read-only methods. A key use case is "an object that has an internal mutable data structure that it wants to export safely without copying it."

# Prerequisites

- **JavaScript classes** — Class syntax with private fields.
- **Wrapper pattern** — The general technique this specializes.

# Key Properties

1. Only **non-destructive** methods are forwarded (e.g., `get`, `has`, `keys`).
2. Destructive methods (e.g., `set`, `delete`, `clear`) are **not available** on the wrapper.
3. The wrapped collection remains **mutable internally** — only the wrapper view is immutable.
4. The export can be **"live"** — changes to the internal collection are reflected through the wrapper.
5. Current implementations are **shallow** — returned data is not itself wrapped.

# Construction / Recognition

## To Construct/Create:
1. Identify destructive vs. non-destructive methods on the collection.
2. Create a wrapper class that only forwards non-destructive methods.
3. Store the collection in a private field.

## To Identify/Recognize:
1. A class that wraps a collection and omits mutating methods.
2. Attempts to call mutating methods throw errors.
3. Read operations work normally.

# Context & Application

Immutable wrappers are useful when an object owns a mutable data structure but wants to share a read-only view of it. Unlike copying, wrapping is O(1) and provides a live view. The chapter demonstrates wrappers for Maps and Arrays.

# Examples

**Example 1** (Ch 16): Concept of an immutable wrapper:
```js
const map = new Map([[false, 'no'], [true, 'yes']]);
const wrapped = new ImmutableMapWrapper(map);

// Non-destructive operations work:
wrapped.get(true);    // 'yes'
wrapped.has(false);   // true

// Destructive operations are not available:
wrapped.set(false, 'never!');  // TypeError: wrapped.set is not a function
wrapped.clear();               // TypeError: wrapped.clear is not a function
```

# Relationships

## Builds Upon
- **Wrapper pattern** — Immutable wrapping is a specialization of the general wrapper pattern.

## Enables
- **Safe data export** — Share internal state without risk of external mutation.
- **Live read-only views** — Changes to the internal collection are visible through the wrapper.

## Related
- **Immutable Map wrapper** — Specific implementation for Maps.
- **Proxy-based immutable Array** — Specific implementation for Arrays using Proxies.

## Contrasts With
- **Object.freeze()** — Freezes the actual object; the wrapper approach preserves internal mutability.
- **Defensive copying** — Creates a separate copy; more expensive but fully independent.

# Common Errors

- **Error**: Assuming the immutable wrapper makes nested data immutable too.
  **Correction**: Current implementations "work shallowly: Each one makes the wrapped object immutable, but not the data it returns."

# Common Confusions

- **Confusion**: Thinking the original collection is made immutable.
  **Clarification**: The original collection remains fully mutable. Only the wrapper view restricts operations. The owner can still mutate through the original reference.

# Source Reference

Chapter 16: Immutable wrappers for collections, Section 16.1.1, lines 7669-7689.

# Verification Notes

- Definition source: direct (from source explanation)
- Confidence rationale: Explicitly defined concept with clear use case
- Cross-reference status: verified against Map and Array implementations
