---
# === CORE IDENTIFICATION ===
concept: Apply Trap
slug: apply-trap

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
section: "20.3.2 Function-specific traps"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "handler.apply()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
  - proxy-trap
extends:
  - proxy-trap
related:
  - construct-trap
  - get-trap
contrasts_with:
  - construct-trap

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a Proxy with handler traps?"
---

# Quick Definition

The `apply` trap intercepts function calls on a Proxy, triggered by `proxy(...)`, `proxy.call(...)`, or `proxy.apply(...)`. Only available when the target is a function.

# Core Definition

From "Deep JavaScript" (Ch 20.3.2): "`apply`: Making a function call. Triggered via: `proxy(···)`, `proxy.call(···)`, `proxy.apply(···)`." From (Ch 20.7.2): "`apply(target, thisArgument, argumentsList): any`." No invariants are enforced. Only active if the target is callable.

# Prerequisites

- **Proxy** — Works on Proxy objects
- **Proxy handler** — Trap is a method on the handler
- **Proxy trap** — A function-specific trap

# Key Properties

1. Signature: `apply(target, thisArgument, argumentsList)`
2. Returns any value (the function's return value)
3. Only available when the target is a function
4. A fundamental operation
5. No invariants enforced

# Construction / Recognition

## To Construct/Create:
1. Create a Proxy wrapping a function target
2. Define an `apply` method on the handler

## To Identify/Recognize:
1. Triggered by calling the Proxy as a function

# Context & Application

The `apply` trap enables intercepting function calls, useful for logging, profiling, argument transformation, or memoization.

# Examples

**Example 1** (Ch 20): From the API reference:
```js
// apply(target, thisArgument, argumentsList): any
// Triggered by:
//   proxy.apply(thisArgument, argumentsList)
//   proxy.call(thisArgument, ...argumentsList)
//   proxy(...argumentsList)
```

# Relationships

## Builds Upon
- **Proxy trap** — A function-specific fundamental trap

## Related
- **Get trap** — Method calls are `get` + `apply`

## Contrasts With
- **Construct trap** — `apply` intercepts calls; `construct` intercepts `new` operator

# Common Errors

- **Error**: Defining `apply` on a handler for a non-function target
  **Correction**: `apply` is only active when the target is callable

# Common Confusions

- **Confusion**: `apply` intercepts method calls on an object
  **Clarification**: Method calls are intercepted in two steps: `get` retrieves the function, then `apply` (or a normal call) invokes it. The `apply` trap only fires when calling the Proxy itself as a function.

# Source Reference

Chapter 20: Metaprogramming with Proxies, Sections 20.3.2, 20.7.2, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined with trigger conditions
- Cross-reference status: verified
