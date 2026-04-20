---
# === CORE IDENTIFICATION ===
concept: Proxy this Binding
slug: proxy-this-binding

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
section: "20.3.7.1 Wrapping an object affects this"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Proxy this behavior"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-target
extends: []
related:
  - method-call-interception
  - internal-slots
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Proxy in JavaScript?"
---

# Quick Definition

When a method is called on a Proxy, `this` points to the Proxy (not the target), which keeps the Proxy in the loop for internal method calls but can cause issues with objects that associate data with `this` via mechanisms not controlled by Proxies.

# Core Definition

From "Deep JavaScript" (Ch 20.3.7.1): "If we invoke that method via the Proxy, `this` points to `proxy`. [...] if the Proxy forwards a method call to the target, `this` is not changed. As a consequence, the Proxy continues to be in the loop if the target uses `this`, e.g., to make a method call."

This has consequences: objects using WeakMap-based private data or internal slots associate data with `this`, and since `this === proxy` (not `target`), the data lookup fails.

# Prerequisites

- **Proxy** — This binding is a Proxy behavior
- **Proxy target** — The target is what `this` might be expected to be

# Key Properties

1. `this` in a method called via Proxy points to the Proxy
2. This keeps tracing/interception active for internal method calls (useful for tracing)
3. This breaks objects using WeakMap-based private data (different `this` = different key)
4. This breaks built-in objects with internal slots (e.g., Date, Map)

# Construction / Recognition

## To Construct/Create:
1. Call any method on a Proxy -- `this` will be the Proxy

## To Identify/Recognize:
1. `this === proxy` inside a method called via the Proxy

# Context & Application

This behavior is a double-edged sword: it enables transparent method tracing (all `this.method()` calls go through the Proxy) but breaks objects that store private data by `this` identity.

# Examples

**Example 1** (Ch 20):
```js
const target = {
  myMethod() {
    return {
      thisIsTarget: this === target,
      thisIsProxy: this === proxy,
    };
  }
};
const proxy = new Proxy(target, {});

assert.deepEqual(proxy.myMethod(), {
  thisIsTarget: false,
  thisIsProxy: true,
});
```

**Example 2** (Ch 20): WeakMap private data failure:
```js
const _name = new WeakMap();
class Person {
  constructor(name) { _name.set(this, name); }
  get name() { return _name.get(this); }
}
const jane = new Person('Jane');
const proxy = new Proxy(jane, {});
assert.equal(proxy.name, undefined); // WeakMap has no entry for proxy
```

# Relationships

## Builds Upon
- **Proxy** — A fundamental behavior of Proxy method calls

## Related
- **Method call interception** — Tracing works because `this` stays as Proxy
- **Internal slots** — Built-in objects fail because slots are on target, not Proxy

# Common Errors

- **Error**: Wrapping objects with WeakMap-based private data in Proxies
  **Correction**: Use regular properties (via `this._name`) or handle the `this` rebinding in the get trap

# Common Confusions

- **Confusion**: `this` inside a method called on a Proxy points to the target
  **Clarification**: `this` points to the Proxy, not the target

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.3.7.1, lines 9133+.

# Verification Notes

- Definition source: direct from source with examples
- Confidence rationale: Extensively demonstrated with multiple scenarios
- Cross-reference status: verified
