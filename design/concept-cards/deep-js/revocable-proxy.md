---
# === CORE IDENTIFICATION ===
concept: Revocable Proxy
slug: revocable-proxy

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
section: "20.3.4 Revocable Proxies"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Proxy.revocable()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
extends:
  - proxy
related:
  - revocable-reference
  - membrane-pattern
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Proxy in JavaScript?"
---

# Quick Definition

A revocable Proxy is a Proxy that can be permanently switched off via a `revoke()` function, after which any operation on the Proxy throws a `TypeError`.

# Core Definition

From "Deep JavaScript" (Ch 20.3.4): "Proxies can be *revoked* (switched off): `const {proxy, revoke} = Proxy.revocable(target, handler);`. After we call the function `revoke` for the first time, any operation we apply to `proxy` causes a `TypeError`. Subsequent calls of `revoke` have no further effect."

# Prerequisites

- **Proxy** — Revocable Proxies extend the basic Proxy concept
- **Proxy handler** — Still requires a handler for interception

# Key Properties

1. Created via `Proxy.revocable(target, handler)` (not `new Proxy()`)
2. Returns an object with `proxy` and `revoke` properties
3. After `revoke()` is called, all operations on `proxy` throw `TypeError`
4. `revoke()` can be called multiple times; only the first call has effect
5. The revocation is permanent -- there is no way to "un-revoke"

# Construction / Recognition

## To Construct/Create:
1. `const {proxy, revoke} = Proxy.revocable(target, handler)`

## To Identify/Recognize:
1. A Proxy that throws `TypeError: Cannot perform '...' on a proxy that has been revoked`

# Context & Application

Revocable Proxies are the foundation of revocable references and the membrane pattern. They enable controlled access to resources that can be permanently cut off.

# Examples

**Example 1** (Ch 20):
```js
const target = {};
const handler = {};
const {proxy, revoke} = Proxy.revocable(target, handler);

proxy.city = 'Paris';
assert.equal(proxy.city, 'Paris');

revoke();

assert.throws(
  () => proxy.prop,
  /^TypeError: Cannot perform 'get' on a proxy that has been revoked$/
);
```

# Relationships

## Builds Upon
- **Proxy** — Extends the Proxy concept with revocability

## Enables
- **Revocable reference** — Access control pattern
- **Membrane pattern** — Security isolation using revocable references

# Common Errors

- **Error**: Trying to use a revoked Proxy
  **Correction**: Once revoked, all operations throw `TypeError`; ensure code handles this

# Common Confusions

- **Confusion**: Revoking a Proxy affects the target object
  **Clarification**: The target object is unchanged; only the Proxy becomes unusable

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.3.4, lines 9133+.

# Verification Notes

- Definition source: direct from source text with example
- Confidence rationale: Explicitly defined with complete example
- Cross-reference status: verified
