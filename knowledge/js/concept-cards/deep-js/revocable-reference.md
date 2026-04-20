---
# === CORE IDENTIFICATION ===
concept: Revocable Reference
slug: revocable-reference

# === CLASSIFICATION ===
category: metaprogramming
subcategory: proxies
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Metaprogramming with Proxies"
chapter_number: 20
section: "20.4.6 Revocable references"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "revocable wrapper"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - revocable-proxy
extends:
  - revocable-proxy
related:
  - membrane-pattern
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about the membrane pattern?"
---

# Quick Definition

A revocable reference is an intermediate object (implemented as a Proxy) that forwards operations to a resource and can be permanently switched off to prevent further access.

# Core Definition

From "Deep JavaScript" (Ch 20.4.6): "*Revocable references* work as follows: A client is not allowed to access an important resource (an object) directly, only via a reference (an intermediate object, a wrapper around the resource). Normally, every operation applied to the reference is forwarded to the resource. After the client is done, the resource is protected by *revoking* the reference, by switching it off."

The simplest implementation uses `Proxy.revocable()`:
```js
function createRevocableReference(target) {
  const handler = {}; // forward everything
  const { proxy, revoke } = Proxy.revocable(target, handler);
  return { reference: proxy, revoke };
}
```

# Prerequisites

- **Proxy** — Revocable references are implemented with Proxies
- **Revocable Proxy** — The underlying mechanism for revocation

# Key Properties

1. Acts as a transparent wrapper around the resource
2. Forwards all operations to the resource while active
3. Can be permanently revoked, after which all operations throw `TypeError`
4. The resource itself is unaffected by revocation

# Construction / Recognition

## To Construct/Create:
1. Use `Proxy.revocable(target, handler)` with an empty handler for full forwarding

## To Identify/Recognize:
1. An object that transparently wraps another and can be disabled

# Context & Application

Revocable references are the building block for the membrane pattern. They enable access control where a resource can be made available temporarily and then permanently protected.

# Examples

**Example 1** (Ch 20):
```js
const resource = { x: 11, y: 8 };
const {reference, revoke} = createRevocableReference(resource);

// Access granted
assert.equal(reference.x, 11);

revoke();

// Access denied
assert.throws(
  () => reference.x,
  /^TypeError: Cannot perform 'get' on a proxy that has been revoked/
);
```

# Relationships

## Builds Upon
- **Revocable Proxy** — The underlying mechanism

## Enables
- **Membrane pattern** — Membranes use revocable references for all cross-boundary objects

# Common Errors

- **Error**: Assuming revocation affects the underlying resource
  **Correction**: The resource is unchanged; only the reference (Proxy) is disabled

# Common Confusions

- **Confusion**: A revocable reference requires a complex handler
  **Clarification**: The simplest implementation uses an empty handler (all operations forwarded) with `Proxy.revocable()`

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.4.6, lines 9133+.

# Verification Notes

- Definition source: direct from source text with three implementations
- Confidence rationale: Extensively covered with multiple implementations shown
- Cross-reference status: verified
