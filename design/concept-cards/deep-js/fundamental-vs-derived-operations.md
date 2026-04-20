---
# === CORE IDENTIFICATION ===
concept: Fundamental vs. Derived Operations
slug: fundamental-vs-derived-operations

# === CLASSIFICATION ===
category: metaprogramming
subcategory: reflection
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Metaprogramming with Proxies"
chapter_number: 20
section: "20.7.2.1 Fundamental operations versus derived operations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - meta-object-protocol
  - proxy-trap
extends: []
related:
  - reflect-api
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Proxy traps relate to property descriptor operations?"
---

# Quick Definition

Fundamental operations are MOP operations that work independently, while derived operations are implemented by calling other MOP operations.

# Core Definition

From "Deep JavaScript" (Ch 20.7.2.1): "The following operations are *fundamental*, they don't use other operations to do their work: `apply`, `defineProperty`, `deleteProperty`, `getOwnPropertyDescriptor`, `getPrototypeOf`, `isExtensible`, `ownKeys`, `preventExtensions`, `setPrototypeOf`. All other operations are *derived*, they can be implemented via fundamental operations. For example, `get` can be implemented by iterating over the prototype chain via `getPrototypeOf` and calling `getOwnPropertyDescriptor` for each chain member."

# Prerequisites

- **Meta object protocol** — Fundamental/derived is a classification of MOP operations
- **Proxy trap** — Traps include both fundamental and derived operations

# Key Properties

1. 9 fundamental operations: `apply`, `defineProperty`, `deleteProperty`, `getOwnPropertyDescriptor`, `getPrototypeOf`, `isExtensible`, `ownKeys`, `preventExtensions`, `setPrototypeOf`
2. 4 derived operations: `get`, `set`, `has`, `construct`
3. Including derived traps increases performance and convenience
4. Including derived traps can lead to inconsistency (e.g., `get` returning different value than `getOwnPropertyDescriptor`)

# Construction / Recognition

## To Construct/Create:
1. Not constructible -- this is a classification

## To Identify/Recognize:
1. Fundamental: operations that don't call other MOP methods
2. Derived: operations that internally call fundamental operations

# Context & Application

The distinction explains the Proxy API design tradeoff: providing only fundamental traps would be simpler but less convenient; including derived traps allows better performance at the cost of potential inconsistency.

# Examples

**Example 1** (Ch 20): `get` is derived -- implemented via fundamentals:
```js
// get can be implemented by iterating over the prototype chain
// via getPrototypeOf and calling getOwnPropertyDescriptor
// for each chain member until an own property is found
```

# Relationships

## Builds Upon
- **Meta object protocol** — Classifies MOP operations

## Related
- **Reflect API** — Provides both fundamental and derived operations as methods

# Common Confusions

- **Confusion**: All traps are equally independent
  **Clarification**: Derived traps like `get` could theoretically be implemented via fundamental traps like `getOwnPropertyDescriptor` and `getPrototypeOf`

# Source Reference

Chapter 20: Metaprogramming with Proxies, Sections 20.5.4, 20.7.2.1, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly listed with classifications
- Cross-reference status: verified
