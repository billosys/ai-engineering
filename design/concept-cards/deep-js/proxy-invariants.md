---
# === CORE IDENTIFICATION ===
concept: Proxy Invariants
slug: proxy-invariants

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
section: "20.5.5 Enforcing invariants for Proxies"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "handler invariants"
  - "Proxy safety constraints"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
  - proxy-trap
  - proxy-target
extends: []
related:
  - transparent-virtualization
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about Proxy invariants?"
---

# Quick Definition

Proxy invariants are safety constraints enforced by the Proxy API that ensure handlers cannot violate fundamental JavaScript guarantees about non-extensibility and non-configurability.

# Core Definition

From "Deep JavaScript" (Ch 20.5.5.2): "These and other characteristics that remain unchanged in the face of language operations are called *invariants*. It is easy to violate invariants via Proxies because they are not intrinsically bound by non-extensibility etc. The Proxy API prevents that from happening by checking the target object and the results of handler methods."

Invariants are traditionally: universal (work for all objects) and monotonic (once enabled, can't be disabled). The Proxy API enforces them by checking handler return values against the target's actual state, throwing `TypeError` on violations.

# Prerequisites

- **Proxy** — Invariants constrain Proxy behavior
- **Proxy handler** — Invariants are checked against handler return values
- **Proxy trap** — Each trap has specific invariants
- **Proxy target** — Target state is used for bookkeeping/enforcement

# Key Properties

1. Prevent misrepresentation of non-extensible or non-configurable properties
2. Enforced by checking handler results against the target object
3. Violations throw `TypeError`
4. Two enforcement mechanisms: checking against target state, and checking return value types
5. Each of the 13 traps has specific invariants (exhaustively listed in 20.7.3)

# Construction / Recognition

## To Construct/Create:
1. Invariants are automatically enforced -- they cannot be created or removed

## To Identify/Recognize:
1. A `TypeError` thrown from a Proxy operation that violates a constraint

# Context & Application

Invariants protect against both bugs and malicious code. Without them, a Proxy wrapping a protected object could misrepresent the object's state, breaking the guarantees of `Object.freeze()`, `Object.preventExtensions()`, and non-configurable properties.

# Examples

**Example 1** (Ch 20): Non-writable, non-configurable property must be faithfully represented:
```js
const handler = {
  get(target, propKey) {
    return 'abc';
  }
};
const target = Object.defineProperties({}, {
  model: { value: 'Isetta', writable: false, configurable: false },
});
const proxy = new Proxy(target, handler);

assert.throws(
  () => proxy.model,
  {
    name: 'TypeError',
    message: "'get' on proxy: property 'model' is a read-only and"
      + " non-configurable data property on the proxy target but"
      + " the proxy did not return its actual value (expected"
      + " 'Isetta' but got 'abc')",
  });
```

**Example 2** (Ch 20): Non-extensible target prototype must be faithfully reported:
```js
const nonExtensibleTarget = {};
Object.preventExtensions(nonExtensibleTarget);
const handler = { getPrototypeOf(t) { return fakeProto; } };
const proxy = new Proxy(nonExtensibleTarget, handler);

assert.throws(
  () => Object.getPrototypeOf(proxy),
  /proxy target is non-extensible but the trap did not return its actual prototype/);
```

# Relationships

## Builds Upon
- **Proxy target** — Target state used for bookkeeping
- **All traps** — Each trap has specific invariants

## Enables
- **Safe metaprogramming** — Proxies can't break fundamental guarantees
- **Transparent virtualization** — Invariants keep Proxy impersonation power in check

# Common Errors

- **Error**: Assuming a handler can return anything from any trap
  **Correction**: Invariants constrain return values based on the target's state

# Common Confusions

- **Confusion**: Invariants only apply to non-extensible objects
  **Clarification**: Invariants apply broadly -- for example, `construct` must always return an object, `isExtensible` must always return a boolean, and many traps have constraints related to non-configurable properties

# Source Reference

Chapter 20: Metaprogramming with Proxies, Sections 20.5.5, 20.7.3, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Extensively covered with examples and exhaustive list
- Cross-reference status: verified against ECMAScript spec reference
