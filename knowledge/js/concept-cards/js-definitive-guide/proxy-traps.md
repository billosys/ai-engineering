---
concept: Proxy Traps (Handler Methods)
slug: proxy-traps
category: metaprogramming
subcategory: proxies
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Metaprogramming"
chapter_number: 14
pdf_page: 416
section: "14.7 Proxy Objects"
extraction_confidence: high
aliases:
  - "handler methods"
  - "Proxy handlers"
prerequisites:
  - proxy-objects
extends: []
related:
  - reflect-api
  - proxy-invariants
contrasts_with: []
answers_questions:
  - "How do I create and use a Proxy with handler traps?"
---

# Quick Definition

The individual methods on a Proxy's handler object that intercept specific operations — including `get`, `set`, `has`, `deleteProperty`, `apply`, `construct`, and others — each corresponding to a Reflect API function.

# Core Definition

Proxy handler methods correspond one-to-one with Reflect API functions. Key traps include: `get(target, property, receiver)` for property reads, `set(target, prop, value, receiver)` for writes, `has(target, name)` for `in` operator, `deleteProperty(target, name)` for `delete`, `apply(target, thisArg, args)` for function calls, `construct(target, args)` for `new`, plus `defineProperty`, `getOwnPropertyDescriptor`, `ownKeys`, `getPrototypeOf`, `setPrototypeOf`, `isExtensible`, `preventExtensions`.

# Prerequisites

- **proxy-objects** — Traps are methods on Proxy handler objects

# Key Properties

1. `get(target, property, receiver)` — intercept property reads
2. `set(target, prop, value, receiver)` — intercept property writes (return boolean)
3. `has(target, name)` — intercept `in` operator
4. `deleteProperty(target, name)` — intercept `delete`
5. `apply(target, thisArg, args)` — intercept function calls
6. `construct(target, args, newTarget)` — intercept `new`
7. `ownKeys(target)` — intercept Object.keys(), Object.getOwnPropertyNames(), etc.
8. Each trap can delegate to Reflect for default behavior

# Construction / Recognition

```js
function readOnlyProxy(o) {
    function readonly() { throw new TypeError("Readonly"); }
    return new Proxy(o, {
        set: readonly,
        defineProperty: readonly,
        deleteProperty: readonly,
        setPrototypeOf: readonly,
    });
}
```

# Context & Application

Each trap intercepts a specific "fundamental operation" on the proxy. Use Reflect methods within traps to delegate to default behavior after custom logic.

# Examples

From the source text (p. 418-421): Read-only proxy using set/defineProperty/deleteProperty/setPrototypeOf traps. Identity proxy using get/has/ownKeys/getOwnPropertyDescriptor/set/deleteProperty/defineProperty/isExtensible/getPrototypeOf/setPrototypeOf traps. Logging proxy using get/set/apply/construct traps plus auto-generated delegation for the rest.

# Relationships

## Builds Upon
- **Proxy Objects** — Traps are the mechanism for customizing proxy behavior

## Related
- **Reflect API** — Each trap corresponds to a Reflect function
- **Proxy Invariants** — Invariants constrain what traps can return

# Common Errors

- **Error**: Forgetting to return a boolean from the `set` trap.
  **Correction**: The set trap should return `true` on success and `false` on failure (which causes TypeError in strict mode).

# Common Confusions

- **Confusion**: Thinking all traps must be defined.
  **Clarification**: Only define traps you need. Missing traps cause the operation to be performed directly on the target object.

# Source Reference

Chapter 14: Metaprogramming, Section 14.7, pages 416-422.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
