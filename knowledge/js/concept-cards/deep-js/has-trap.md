---
# === CORE IDENTIFICATION ===
concept: Has Trap
slug: has-trap

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
  - "handler.has()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
  - proxy-trap
extends:
  - proxy-trap
related:
  - get-trap
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a Proxy with handler traps?"
---

# Quick Definition

The `has` trap intercepts the `in` operator on a Proxy, determining whether a property exists.

# Core Definition

From "Deep JavaScript" (Ch 20.7.2): "`has(target, propKey): boolean` -- Triggered by `propKey in proxy`." Returns a boolean indicating property existence. Invariants: non-configurable own properties of the target can't be reported as non-existent; if the target is non-extensible, no own property can be reported as non-existent.

# Prerequisites

- **Proxy** — The `has` trap works on Proxy objects
- **Proxy handler** — The trap is a method on the handler
- **Proxy trap** — `has` is one of the available traps

# Key Properties

1. Signature: `has(target, propKey)`
2. Returns a boolean (the result of the `in` operation)
3. Propagates through the prototype chain
4. Subject to invariants regarding non-configurable and non-extensible targets

# Construction / Recognition

## To Construct/Create:
1. Define a `has` method on the handler object

## To Identify/Recognize:
1. Triggered by `propKey in proxy`

# Context & Application

The `has` trap allows customization of property existence checks, useful for virtual objects that want to report properties they don't actually have, or for hiding certain properties from the `in` operator.

# Examples

**Example 1** (Ch 20):
```js
const handler = {
  has(target, propKey) {
    logged.push(`HAS ${propKey}`);
    return true;
  }
};
const proxy = new Proxy(target, handler);
assert.equal('hello' in proxy, true);
```

# Relationships

## Builds Upon
- **Proxy trap** — `has` is a specific trap type

## Related
- **Get trap** — Both propagate through the prototype chain

# Common Errors

- **Error**: Reporting a non-configurable own property as non-existent
  **Correction**: The invariant prevents this; a `TypeError` is thrown

# Common Confusions

- **Confusion**: The `has` trap is triggered by `Object.hasOwnProperty()`
  **Clarification**: `has` is triggered by the `in` operator, which checks the full prototype chain. `hasOwnProperty` is a regular method call, not intercepted by `has`.

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.7.2, lines 9133+.

# Verification Notes

- Definition source: direct from source API reference
- Confidence rationale: Explicitly listed with examples
- Cross-reference status: verified
