---
# === CORE IDENTIFICATION ===
concept: GetOwnPropertyDescriptor Trap
slug: get-own-property-descriptor-trap

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
  - "handler.getOwnPropertyDescriptor()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
  - proxy-trap
extends:
  - proxy-trap
related:
  - define-property-trap
  - proxy-invariants
contrasts_with:
  - define-property-trap

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Proxy traps relate to property descriptor operations?"
---

# Quick Definition

The `getOwnPropertyDescriptor` trap intercepts `Object.getOwnPropertyDescriptor()` on a Proxy, controlling what property descriptor is reported.

# Core Definition

From "Deep JavaScript" (Ch 20.7.2): "`getOwnPropertyDescriptor(target, propKey): undefined|PropDesc` -- Triggered by `Object.getOwnPropertyDescriptor(proxy, propKey)`." A fundamental operation with multiple invariants: must return `undefined` or an object; non-configurable properties can't be reported as non-existent; for non-extensible targets, exactly the target's own properties must be reported.

# Prerequisites

- **Proxy** — Works on Proxy objects
- **Proxy handler** — Trap is a method on the handler
- **Proxy trap** — A fundamental trap type

# Key Properties

1. Signature: `getOwnPropertyDescriptor(target, propKey)`
2. Returns `undefined` or a property descriptor object
3. A fundamental operation
4. Central to the MOP -- `get` internally relies on `getOwnPropertyDescriptor`

# Construction / Recognition

## To Construct/Create:
1. Define a `getOwnPropertyDescriptor` method on the handler

## To Identify/Recognize:
1. Triggered by `Object.getOwnPropertyDescriptor(proxy, propKey)`

# Context & Application

This trap is fundamental to the meta object protocol. The internal `[[Get]]` operation calls `[[GetOwnProperty]]` to retrieve descriptors. Also used by `Object.keys()` to check enumerability after `ownKeys` provides the key list.

# Examples

**Example 1** (Ch 20): The MOP shows how `get` uses `getOwnPropertyDescriptor` internally:
```js
__Get__(propKey, receiver) {
  const desc = this.__GetOwnProperty__(propKey);
  if (desc === undefined) {
    const parent = this.__GetPrototypeOf__();
    if (parent === null) return undefined;
    return parent.__Get__(propKey, receiver);
  }
  if ('value' in desc) {
    return desc.value;
  }
  // ...
}
```

# Relationships

## Builds Upon
- **Proxy trap** — A fundamental trap in the MOP

## Enables
- **Get trap** — `get` internally depends on `getOwnPropertyDescriptor`

## Contrasts With
- **defineProperty trap** — Reads vs. writes property descriptors

# Common Errors

- **Error**: Reporting a non-configurable property as non-existent
  **Correction**: Invariant violation throws `TypeError`

# Common Confusions

- **Confusion**: `getOwnPropertyDescriptor` is rarely triggered
  **Clarification**: It is triggered during many operations internally, including `Object.keys()` which checks enumerability

# Source Reference

Chapter 20: Metaprogramming with Proxies, Sections 20.5.4, 20.7.2, lines 9133+.

# Verification Notes

- Definition source: direct from source API reference and MOP discussion
- Confidence rationale: Explicitly listed with invariants and MOP relationship
- Cross-reference status: verified
