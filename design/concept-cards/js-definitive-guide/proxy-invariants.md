---
concept: Proxy Invariants
slug: proxy-invariants
category: metaprogramming
subcategory: proxies
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Metaprogramming"
chapter_number: 14
pdf_page: 422
section: "14.7.1 Proxy Invariants"
extraction_confidence: high
aliases: []
prerequisites:
  - proxy-objects
  - proxy-traps
  - object-freeze
extends: []
related:
  - reflect-api
contrasts_with: []
answers_questions: []
---

# Quick Definition

Sanity checks enforced by the Proxy class after handler methods return, ensuring that proxy behavior cannot violate fundamental JavaScript invariants like the immutability of frozen properties or the non-extensibility of sealed objects.

# Core Definition

"After forwarding an operation, the Proxy class performs some sanity checks on the result to ensure important JavaScript invariants are not being violated. If it detects a violation, the proxy will throw a TypeError instead of letting the operation proceed" (p. 423). For example, a non-extensible target cannot have an isExtensible() handler that returns true, and a frozen property cannot have a get() handler that returns a different value.

# Prerequisites

- **proxy-objects** — Invariants constrain proxy behavior
- **proxy-traps** — Invariants check trap return values
- **object-freeze** — Frozen/sealed state triggers invariant checks

# Key Properties

1. Proxy checks handler results against target state
2. Non-extensible targets: isExtensible() must return false
3. Frozen properties: get() must return actual value
4. Non-extensible targets: getPrototypeOf() must return actual prototype
5. Violations throw TypeError
6. Most invariants involve non-extensible targets and non-configurable properties

# Construction / Recognition

```js
let target = Object.freeze({x: 1});
let proxy = new Proxy(target, { get() { return 99; }});
proxy.x;  // !TypeError: value returned by get() doesn't match target

let target2 = Object.preventExtensions({});
let proxy2 = new Proxy(target2, { isExtensible() { return true; }});
Reflect.isExtensible(proxy2);  // !TypeError: invariant violation
```

# Context & Application

Invariants prevent proxies from creating fundamentally inconsistent objects. They ensure that code relying on freeze/seal/preventExtensions guarantees is not subverted by a malicious or buggy proxy.

# Examples

From the source text (p. 422-424): A get() handler returning 99 for a frozen property with value 1 throws TypeError. An isExtensible() handler returning true for a non-extensible target throws TypeError.

# Relationships

## Builds Upon
- **Proxy Objects** — Invariants are enforced by the Proxy class
- **Proxy Traps** — Invariants check trap return values
- **Object.freeze()** — Frozen state triggers stricter invariant checking

## Related
- **Reflect API** — Invariant checks apply when Reflect methods are used on proxies

# Common Errors

- **Error**: Creating a read-only proxy without matching isExtensible/getOwnPropertyDescriptor handlers.
  **Correction**: While this doesn't always throw, it creates an inconsistent proxy. Add handlers for isExtensible and getOwnPropertyDescriptor for full consistency.

# Common Confusions

- **Confusion**: Thinking proxy invariants only matter for frozen objects.
  **Clarification**: Invariants apply to any non-extensible object or non-configurable property, not just frozen ones.

# Source Reference

Chapter 14: Metaprogramming, Section 14.7.1, pages 422-424.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
