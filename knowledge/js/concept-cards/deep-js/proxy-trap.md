---
# === CORE IDENTIFICATION ===
concept: Proxy Trap
slug: proxy-trap

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
section: "20.3 Proxies explained"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "handler trap"
  - "interceptor method"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
extends: []
related:
  - get-trap
  - set-trap
  - has-trap
  - apply-trap
  - construct-trap
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a Proxy with handler traps?"
  - "How do Proxy traps relate to property descriptor operations?"
---

# Quick Definition

A trap is a handler method that intercepts a specific operation on a Proxy, borrowing its name from the domain of operating systems.

# Core Definition

From "Deep JavaScript" (Ch 20.3): "For each operation, there is a corresponding handler method that -- if present -- performs that operation. Such a method *intercepts* the operation (on its way to the target) and is called a *trap* -- a term borrowed from the domain of operating systems."

There are 13 traps total: `get`, `set`, `has`, `deleteProperty`, `ownKeys`, `getOwnPropertyDescriptor`, `defineProperty`, `getPrototypeOf`, `setPrototypeOf`, `isExtensible`, `preventExtensions`, `apply`, and `construct` (last two only for function targets).

# Prerequisites

- **Proxy** — Traps exist within the Proxy mechanism
- **Proxy handler** — Traps are methods defined on the handler object

# Key Properties

1. Named after the operation they intercept
2. Receive the target as first argument, plus operation-specific arguments
3. Some traps are *fundamental* (independent), others are *derived* (can be implemented via fundamental ones)
4. Return values are type-checked and may be subject to invariants
5. Several traps return booleans indicating operation success

# Construction / Recognition

## To Construct/Create:
1. Define a method on the handler object with the trap's name

## To Identify/Recognize:
1. A method on a handler object whose name matches one of the 13 interceptable operations

# Context & Application

Traps give Proxies their power: each trap corresponds to a fundamental or derived operation in the JavaScript meta object protocol. The choice to include derived traps (like `get`) alongside fundamental ones was a design tradeoff between performance/convenience and consistency.

# Examples

**Example 1** (Ch 20): Two traps -- `get` and `has`:
```js
const handler = {
  get(target, propKey, receiver) {
    return 123;
  },
  has(target, propKey) {
    return true;
  }
};
```

# Relationships

## Builds Upon
- **Proxy handler** — Traps are methods on the handler

## Enables
- **All specific traps** — `get`, `set`, `has`, `deleteProperty`, etc.

## Related
- **Meta object protocol** — Traps correspond to internal MOP methods
- **Reflect API** — Each trap has a corresponding `Reflect` method

# Common Errors

- **Error**: Assuming there is an `invoke` trap for method calls
  **Correction**: Method calls are a sequence of `get` (retrieve function) then `apply` (call it); there is no separate `invoke` trap

# Common Confusions

- **Confusion**: All traps are fundamental operations
  **Clarification**: Some traps (like `get`, `set`, `has`) are derived -- they can be implemented via fundamental operations like `getOwnPropertyDescriptor` and `getPrototypeOf`

# Source Reference

Chapter 20: Metaprogramming with Proxies, Sections 20.3 and 20.7.2, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined with etymology
- Cross-reference status: verified against trap list in 20.7.2
