---
# === CORE IDENTIFICATION ===
concept: Set Trap
slug: set-trap

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
  - "handler.set()"
  - "set handler method"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
  - proxy-trap
extends:
  - proxy-trap
related:
  - get-trap
  - reflect-api
contrasts_with:
  - get-trap

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes the get trap from the set trap in Proxy handlers?"
  - "How do I create a Proxy with handler traps?"
---

# Quick Definition

The `set` trap intercepts property write operations on a Proxy, triggered by `receiver[propKey] = value` or `receiver.someProp = value`.

# Core Definition

From "Deep JavaScript" (Ch 20.7.2): "`set(target, propKey, value, receiver): boolean` -- Triggered by `receiver[propKey] = value` or `receiver.someProp = value`." Returns a boolean indicating whether the operation succeeded. The `set` trap propagates through the prototype chain similarly to `get`.

Invariant: The property can't be changed if the target has a non-writable, non-configurable data property with that key.

# Prerequisites

- **Proxy** — The `set` trap works on Proxy objects
- **Proxy handler** — The trap is a method on the handler
- **Proxy trap** — `set` is one of the available traps

# Key Properties

1. Signature: `set(target, propKey, value, receiver)`
2. Returns a boolean (whether the set succeeded)
3. `receiver` is the original object on which the assignment was performed
4. A derived operation (not fundamental)
5. Subject to invariants for non-writable, non-configurable properties

# Construction / Recognition

## To Construct/Create:
1. Define a `set` method on the handler object

## To Identify/Recognize:
1. Triggered by any property write: `proxy.prop = value`, `proxy[key] = value`

# Context & Application

The `set` trap is used for data binding (observing property changes), validation, preventing accidental property creation, and tracing property writes.

# Examples

**Example 1** (Ch 20): Data binding with `set`:
```js
function createObservedArray(callback) {
  const array = [];
  return new Proxy(array, {
    set(target, propertyKey, value, receiver) {
      callback(propertyKey, value);
      return Reflect.set(target, propertyKey, value, receiver);
    }
  });
}
const observedArray = createObservedArray(
  (key, value) => console.log(
    `${JSON.stringify(key)} = ${JSON.stringify(value)}`));
observedArray.push('a');
// Output:
// '"0" = "a"'
// '"length" = 1'
```

**Example 2** (Ch 20): Tracing property writes:
```js
set(target, propKey, value, receiver) {
  if (propKeySet.has(propKey)) {
    log('SET '+propKey+'='+value);
  }
  return Reflect.set(target, propKey, value, receiver);
},
```

# Relationships

## Builds Upon
- **Proxy trap** — `set` is a specific trap type

## Enables
- **Data binding** — Observe and react to property changes
- **Property validation** — Validate values before assignment
- **Property tracing** — Log property writes

## Contrasts With
- **Get trap** — `set` writes properties; `get` reads properties

# Common Errors

- **Error**: Forgetting to return `true` or calling `Reflect.set()` to actually perform the operation
  **Correction**: The `set` trap must return a boolean and should forward the operation via `Reflect.set()` if the property should actually be set

# Common Confusions

- **Confusion**: The `set` trap only triggers on explicit assignments
  **Clarification**: It also triggers on inherited property sets (via prototype chain) and internal operations like `Array.push()` setting indexed properties

# Source Reference

Chapter 20: Metaprogramming with Proxies, Sections 20.4.1, 20.4.4, 20.7.2, lines 9133+.

# Verification Notes

- Definition source: direct from source text and API reference
- Confidence rationale: Demonstrated with multiple use cases
- Cross-reference status: verified
