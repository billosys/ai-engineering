---
# === CORE IDENTIFICATION ===
concept: Proxy Target
slug: proxy-target

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
section: "20.3 Proxies explained"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "target object"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
extends: []
related:
  - proxy-handler
  - proxy-invariants
contrasts_with:
  - proxy-handler

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Proxy in JavaScript?"
---

# Quick Definition

The target is the object that a Proxy wraps; unintercepted operations are forwarded to it, and its state is used to enforce invariants.

# Core Definition

From "Deep JavaScript" (Ch 20.3): "`target`: If the handler doesn't intercept an operation, then it is performed on the target. That is, it acts as a fallback for the handler. In a way, the Proxy wraps the target." The target also serves as bookkeeping for invariant enforcement -- handler return values are checked against the target's actual state.

# Prerequisites

- **Proxy** — The target is a required parameter when creating a Proxy

# Key Properties

1. First argument to `new Proxy(target, handler)`
2. Acts as fallback for unintercepted operations
3. Used for invariant enforcement (non-extensibility, non-configurability)
4. For function-specific traps (`apply`, `construct`), the target must be a function
5. Some objects (Date, WeakMap-based private data) cannot be transparently wrapped

# Construction / Recognition

## To Construct/Create:
1. Any JavaScript object can be a target

## To Identify/Recognize:
1. The first argument to the `Proxy` constructor

# Context & Application

The target is essential even for virtual objects -- it enforces invariants and provides fallback behavior. For wrapper Proxies, the target is the "real" object being wrapped.

# Examples

**Example 1** (Ch 20):
```js
const target = {size: 0};
const handler = {
  get(target, propKey, receiver) {
    return 123;
  }
};
const proxy = new Proxy(target, handler);

// set is not intercepted, so it goes to target:
proxy.age = 99;
assert.equal(target.age, 99);
```

# Relationships

## Related
- **Proxy handler** — Handler intercepts; target receives unintercepted operations
- **Proxy invariants** — Target state is used for invariant checks

## Contrasts With
- **Proxy handler** — The handler intercepts; the target stores/receives

# Common Errors

- **Error**: Wrapping a Date instance and expecting methods to work
  **Correction**: Date uses internal slots not intercepted by Proxies; `.getFullYear()` etc. throw `TypeError`

# Common Confusions

- **Confusion**: The Proxy and target are the same object
  **Clarification**: They are separate objects; `this` inside a method called via the Proxy points to the Proxy, not the target

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.3, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
