---
# === CORE IDENTIFICATION ===
concept: Construct Trap
slug: construct-trap

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
  - "handler.construct()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
  - proxy-trap
extends:
  - proxy-trap
related:
  - apply-trap
contrasts_with:
  - apply-trap

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a Proxy with handler traps?"
---

# Quick Definition

The `construct` trap intercepts `new` operator calls on a Proxy, triggered by `new proxy(...)`. Only available when the target is a constructor function.

# Core Definition

From "Deep JavaScript" (Ch 20.3.2): "`construct`: Making a constructor call. Triggered via: `new proxy(···)`." From (Ch 20.7.2): "`construct(target, argumentsList, newTarget): object`." Invariant: the result returned by the handler must be an object (not `null` or any other primitive). Only active if the target is constructible.

# Prerequisites

- **Proxy** — Works on Proxy objects
- **Proxy handler** — Trap is a method on the handler
- **Proxy trap** — A function-specific trap

# Key Properties

1. Signature: `construct(target, argumentsList, newTarget)`
2. Must return an object (not a primitive)
3. Only available when the target is constructible
4. `newTarget` points to the constructor that started the current chain of constructor calls

# Construction / Recognition

## To Construct/Create:
1. Create a Proxy wrapping a constructor function
2. Define a `construct` method on the handler

## To Identify/Recognize:
1. Triggered by `new proxy(...args)`

# Context & Application

The `construct` trap enables intercepting object creation, useful for instance tracking, argument validation, or returning different objects from constructors.

# Examples

**Example 1** (Ch 20): From the API reference:
```js
// construct(target, argumentsList, newTarget): object
// Triggered by: new proxy(..argumentsList)
```

# Relationships

## Builds Upon
- **Proxy trap** — A function-specific fundamental trap

## Contrasts With
- **Apply trap** — `construct` intercepts `new`; `apply` intercepts function calls

# Common Errors

- **Error**: Returning a primitive from the `construct` trap
  **Correction**: The invariant requires an object return value; primitives cause `TypeError`

# Common Confusions

- **Confusion**: `construct` and `apply` are interchangeable
  **Clarification**: `construct` is for `new` operator calls; `apply` is for regular function calls

# Source Reference

Chapter 20: Metaprogramming with Proxies, Sections 20.3.2, 20.7.2, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined with invariant
- Cross-reference status: verified
