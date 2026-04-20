---
# === CORE IDENTIFICATION ===
concept: DeleteProperty Trap
slug: delete-property-trap

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
  - "handler.deleteProperty()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
  - proxy-trap
extends:
  - proxy-trap
related:
  - reflect-api
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a Proxy with handler traps?"
---

# Quick Definition

The `deleteProperty` trap intercepts the `delete` operator on a Proxy, controlling whether a property can be removed.

# Core Definition

From "Deep JavaScript" (Ch 20.7.2): "`deleteProperty(target, propKey): boolean` -- Triggered by `delete proxy[propKey]` or `delete proxy.someProp`." A fundamental operation. Invariant: a property can't be reported as deleted if the target has a non-configurable own property with that key, or if the target is non-extensible and has an own property with that key.

# Prerequisites

- **Proxy** — The `deleteProperty` trap works on Proxy objects
- **Proxy handler** — The trap is a method on the handler
- **Proxy trap** — `deleteProperty` is one of the available traps

# Key Properties

1. Signature: `deleteProperty(target, propKey)`
2. Returns a boolean indicating whether deletion succeeded
3. A fundamental operation (not derived)
4. Subject to invariants regarding non-configurable properties

# Construction / Recognition

## To Construct/Create:
1. Define a `deleteProperty` method on the handler object

## To Identify/Recognize:
1. Triggered by `delete proxy.prop` or `delete proxy[key]`

# Context & Application

Used to control or log property deletion, or to prevent deletion of certain properties.

# Examples

**Example 1** (Ch 20): Forwarding with logging:
```js
const handler = {
  deleteProperty(target, propKey) {
    console.log('DELETE ' + propKey);
    return Reflect.deleteProperty(target, propKey);
  },
}
```

# Relationships

## Builds Upon
- **Proxy trap** — `deleteProperty` is a fundamental trap

## Related
- **Reflect API** — `Reflect.deleteProperty()` is the function form of `delete`

# Common Errors

- **Error**: Reporting deletion success for a non-configurable property
  **Correction**: The invariant prevents this and throws `TypeError`

# Common Confusions

- **Confusion**: `deleteProperty` and `Reflect.deleteProperty()` behave identically to the `delete` operator
  **Clarification**: `Reflect.deleteProperty()` returns `false` for non-configurable properties; `delete` in strict mode throws `TypeError`

# Source Reference

Chapter 20: Metaprogramming with Proxies, Sections 20.3.6, 20.7.2, lines 9133+.

# Verification Notes

- Definition source: direct from source API reference
- Confidence rationale: Explicitly listed and demonstrated
- Cross-reference status: verified
