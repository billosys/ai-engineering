---
# === CORE IDENTIFICATION ===
concept: Get Trap
slug: get-trap

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
  - "handler.get()"
  - "get handler method"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
  - proxy-trap
extends:
  - proxy-trap
related:
  - set-trap
  - reflect-api
contrasts_with:
  - set-trap

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes the get trap from the set trap in Proxy handlers?"
  - "How do I create a Proxy with handler traps?"
---

# Quick Definition

The `get` trap intercepts property read operations on a Proxy, triggered by `receiver[propKey]` or `receiver.someProp`.

# Core Definition

From "Deep JavaScript" (Ch 20.7.2): "`get(target, propKey, receiver): any` -- Triggered by `receiver[propKey]` or `receiver.someProp`." The `get` trap is a *derived* operation that can be implemented via `getPrototypeOf` and `getOwnPropertyDescriptor`. It propagates through the prototype chain: if a Proxy is in the prototype chain, its `get` trap is triggered for properties not found in earlier objects.

Invariant: If the target has an own, non-writable, non-configurable data property, the handler must return that property's value.

# Prerequisites

- **Proxy** — The `get` trap works on Proxy objects
- **Proxy handler** — The trap is a method on the handler
- **Proxy trap** — `get` is one of the available traps

# Key Properties

1. Signature: `get(target, propKey, receiver)`
2. `receiver` is the object on which the property access was originally performed
3. Returns any value (the value that the property access evaluates to)
4. A derived operation (not fundamental)
5. Subject to invariants for non-writable, non-configurable properties

# Construction / Recognition

## To Construct/Create:
1. Define a `get` method on the handler object

## To Identify/Recognize:
1. Triggered by any property read: `proxy.prop`, `proxy[key]`, `Reflect.get(proxy, key)`

# Context & Application

The `get` trap is the most commonly used trap. It enables property tracing, virtual properties, negative array indices, default values for missing properties, and intercepting method calls (by returning functions).

# Examples

**Example 1** (Ch 20): Tracing property access:
```js
function tracePropertyAccesses(obj, propKeys, log=console.log) {
  const propKeySet = new Set(propKeys);
  return new Proxy(obj, {
    get(target, propKey, receiver) {
      if (propKeySet.has(propKey)) {
        log('GET '+propKey);
      }
      return Reflect.get(target, propKey, receiver);
    },
  });
}
```

**Example 2** (Ch 20): Negative array indices:
```js
get(target, propKey, receiver) {
  if (typeof propKey === 'string') {
    const index = Number(propKey);
    if (index < 0) {
      propKey = String(target.length + index);
    }
  }
  return Reflect.get(target, propKey, receiver);
}
```

# Relationships

## Builds Upon
- **Proxy trap** — `get` is a specific trap type

## Enables
- **Method call interception** — Method calls start with a `get` to retrieve the function
- **Property tracing** — Log property reads
- **Virtual properties** — Return computed values for non-existent properties

## Contrasts With
- **Set trap** — `get` reads properties; `set` writes properties

# Common Errors

- **Error**: Returning a different value for a non-writable, non-configurable target property
  **Correction**: The invariant requires returning the actual property value; violating this throws `TypeError`

# Common Confusions

- **Confusion**: The `get` trap intercepts method calls
  **Clarification**: There is no method call trap. A method call is `get` (retrieve function) + `apply` (call it). The `get` trap only intercepts the retrieval step.

# Source Reference

Chapter 20: Metaprogramming with Proxies, Sections 20.4.1, 20.4.3, 20.7.2, lines 9133+.

# Verification Notes

- Definition source: direct from source text and API reference
- Confidence rationale: Extensively demonstrated with multiple use cases
- Cross-reference status: verified
