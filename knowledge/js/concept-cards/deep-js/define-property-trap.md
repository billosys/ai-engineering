---
# === CORE IDENTIFICATION ===
concept: DefineProperty Trap
slug: define-property-trap

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
  - "handler.defineProperty()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
  - proxy-trap
extends:
  - proxy-trap
related:
  - get-own-property-descriptor-trap
contrasts_with:
  - get-own-property-descriptor-trap

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Proxy traps relate to property descriptor operations?"
---

# Quick Definition

The `defineProperty` trap intercepts `Object.defineProperty()` on a Proxy, controlling how properties are defined or modified.

# Core Definition

From "Deep JavaScript" (Ch 20.7.2): "`defineProperty(target, propKey, propDesc): boolean` -- Triggered by `Object.defineProperty(proxy, propKey, propDesc)`." A fundamental operation. Invariants: can't add properties to a non-extensible target; can't define a non-configurable property unless the target already has one; descriptor must be compatible with existing target property.

# Prerequisites

- **Proxy** — Works on Proxy objects
- **Proxy handler** — Trap is a method on the handler
- **Proxy trap** — A fundamental trap type

# Key Properties

1. Signature: `defineProperty(target, propKey, propDesc)`
2. Returns a boolean indicating success
3. A fundamental operation
4. Subject to invariants regarding extensibility and configurability

# Construction / Recognition

## To Construct/Create:
1. Define a `defineProperty` method on the handler

## To Identify/Recognize:
1. Triggered by `Object.defineProperty(proxy, propKey, propDesc)`

# Context & Application

This trap controls property definition, enabling validation or transformation of property descriptors before they are applied.

# Examples

**Example 1** (Ch 20): In the forwarding handler, a `set` operation triggers `defineProperty` internally:
```js
// Output of Proxy-based logging handler shows:
// 'SET distance'
// 'GETOWNPROPERTYDESCRIPTOR distance'
// 'DEFINEPROPERTY distance'
```

# Relationships

## Builds Upon
- **Proxy trap** — A fundamental trap

## Related
- **getOwnPropertyDescriptor trap** — Both work with property descriptors

## Contrasts With
- **getOwnPropertyDescriptor trap** — `defineProperty` writes descriptors; `getOwnPropertyDescriptor` reads them

# Common Errors

- **Error**: Defining a non-configurable property on a non-extensible target via the trap
  **Correction**: Multiple invariants constrain what can be defined; violations throw `TypeError`

# Common Confusions

- **Confusion**: `defineProperty` trap is only triggered by explicit `Object.defineProperty()` calls
  **Clarification**: Property assignments (`proxy.x = value`) can also trigger `defineProperty` internally, as shown by the forwarding handler output

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.7.2, lines 9133+.

# Verification Notes

- Definition source: direct from source API reference
- Confidence rationale: Explicitly listed with invariants
- Cross-reference status: verified
