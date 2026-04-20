---
# === CORE IDENTIFICATION ===
concept: OwnKeys Trap
slug: own-keys-trap

# === CLASSIFICATION ===
category: metaprogramming
subcategory: traps
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Metaprogramming with Proxies"
chapter_number: 20
section: "20.7.2 Handler methods"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "handler.ownKeys()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
  - proxy-trap
extends:
  - proxy-trap
related:
  - get-own-property-descriptor-trap
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a Proxy with handler traps?"
---

# Quick Definition

The `ownKeys` trap intercepts operations that list an object's own property keys, including `Object.keys()`, `Object.getOwnPropertyNames()`, and `Object.getOwnPropertySymbols()`.

# Core Definition

From "Deep JavaScript" (Ch 20.7.2): "`ownKeys(target): Array<PropertyKey>` -- Triggered by `Object.getOwnPropertyPropertyNames(proxy)`, `Object.getOwnPropertyPropertySymbols(proxy)`, `Object.keys(proxy)`." A fundamental operation. Invariants include: no duplicate entries, elements must be strings or symbols, must include keys of all non-configurable own properties, and for non-extensible targets must include exactly the target's own keys.

# Prerequisites

- **Proxy** — The `ownKeys` trap works on Proxy objects
- **Proxy handler** — The trap is a method on the handler
- **Proxy trap** — `ownKeys` is one of the available traps

# Key Properties

1. Signature: `ownKeys(target)`
2. Returns an Array of PropertyKey (string | symbol)
3. A fundamental operation
4. Subject to multiple invariants regarding non-configurable and non-extensible targets

# Construction / Recognition

## To Construct/Create:
1. Define an `ownKeys` method on the handler object

## To Identify/Recognize:
1. Triggered by `Object.keys()`, `Object.getOwnPropertyNames()`, `Object.getOwnPropertySymbols()`

# Context & Application

The `ownKeys` trap controls property enumeration, useful for hiding internal properties or virtualizing the list of properties an object appears to have.

# Examples

**Example 1** (Ch 20): Triggered by various operations:
```js
// Object.keys(proxy) uses ownKeys trap
// then filters for enumerable string keys via getOwnPropertyDescriptor
```

# Relationships

## Builds Upon
- **Proxy trap** — `ownKeys` is a fundamental trap

## Related
- **getOwnPropertyDescriptor trap** — `Object.keys()` uses both `ownKeys` and `getOwnPropertyDescriptor`

# Common Errors

- **Error**: Omitting non-configurable own property keys from the returned array
  **Correction**: The invariant requires all non-configurable own property keys to be present

# Common Confusions

- **Confusion**: `ownKeys` only affects `Object.keys()`
  **Clarification**: It affects `Object.getOwnPropertyNames()`, `Object.getOwnPropertySymbols()`, and `Object.keys()` (which further filters by enumerability)

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.7.2, lines 9133+.

# Verification Notes

- Definition source: direct from source API reference
- Confidence rationale: Explicitly listed with invariants
- Cross-reference status: verified
