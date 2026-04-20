---
concept: Proxy Objects
slug: proxy-objects
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
  - "Proxy class"
  - "JavaScript Proxy"
prerequisites:
  - reflect-api
  - property-descriptors
extends: []
related:
  - proxy-traps
  - proxy-invariants
contrasts_with: []
answers_questions:
  - "What is a Proxy object?"
  - "How do I create and use a Proxy with handler traps?"
  - "What must I understand before learning about the Proxy API?"
---

# Quick Definition

ES6 objects that wrap a target object and intercept fundamental operations (property access, assignment, deletion, etc.) through a handlers object, enabling custom behaviors like validation, logging, read-only wrappers, and virtual properties.

# Core Definition

"The Proxy class, available in ES6 and later, is JavaScript's most powerful metaprogramming feature. It allows us to write code that alters the fundamental behavior of JavaScript objects" (p. 416). A Proxy is created with `new Proxy(target, handlers)`. Operations on the proxy are dispatched to handler methods if defined, or to the target object if not.

# Prerequisites

- **reflect-api** — Reflect methods match Proxy handler methods for delegation
- **property-descriptors** — Understanding attributes is needed for handler correctness

# Key Properties

1. Created with `new Proxy(target, handlers)`
2. Empty handlers = transparent wrapper (operations pass to target)
3. Handler methods match Reflect API: get, set, has, deleteProperty, defineProperty, etc.
4. `Proxy.revocable(target, handlers)` creates revocable proxies
5. Works with function targets (apply, construct traps)
6. Proxy enforces invariants to prevent inconsistent behavior

# Construction / Recognition

```js
let proxy = new Proxy(target, {
    get(target, property, receiver) { return Reflect.get(target, property, receiver); },
    set(target, prop, value, receiver) { return Reflect.set(target, prop, value, receiver); }
});

// Revocable proxy:
let {proxy, revoke} = Proxy.revocable(target, {});
revoke();  // proxy stops working
```

# Context & Application

Used for logging/debugging (logging proxies), access control (read-only wrappers), validation, virtual objects (infinite property objects), and code isolation (revocable proxies).

# Examples

From the source text (p. 417-421): Read-only proxy that throws TypeError on write attempts. Identity proxy with infinite properties where every property value equals its name. Logging proxy that records all operations and delegates via Reflect. Revocable proxy for third-party library isolation.

# Relationships

## Builds Upon
- **Reflect API** — Handler methods delegate to Reflect for default behavior
- **Property Descriptors** — Proxy handlers interact with property attributes

## Enables
- **Proxy Traps** — The individual handler methods
- **Proxy Invariants** — The rules Proxy enforces for consistency

# Common Errors

- **Error**: Creating a read-only proxy without isExtensible/getOwnPropertyDescriptor handlers, causing inconsistencies.
  **Correction**: If you restrict operations, consider adding handlers that report consistent state (e.g., isExtensible returning false).

# Common Confusions

- **Confusion**: Thinking Proxy can intercept operations on the target directly.
  **Clarification**: Proxy only intercepts operations performed on the proxy object itself. Direct access to the target bypasses the proxy.

# Source Reference

Chapter 14: Metaprogramming, Section 14.7, pages 416-424.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High — extensive section
- Uncertainties: None
- Cross-reference status: Verified
