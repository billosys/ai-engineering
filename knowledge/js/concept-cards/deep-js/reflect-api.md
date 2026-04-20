---
# === CORE IDENTIFICATION ===
concept: Reflect API
slug: reflect-api

# === CLASSIFICATION ===
category: metaprogramming
subcategory: reflection
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Metaprogramming with Proxies"
chapter_number: 20
section: "20.7.5 Reflect"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Reflect object"
  - "Reflect module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-trap
extends: []
related:
  - proxy-handler
  - forwarding-handler
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Proxy in JavaScript?"
  - "How do I create a Proxy with handler traps?"
---

# Quick Definition

The Reflect API is a global object that provides methods mirroring every Proxy trap, enabling clean forwarding of intercepted operations from handlers to targets.

# Core Definition

From "Deep JavaScript" (Ch 20.7.5): "The global object `Reflect` implements all interceptable operations of the JavaScript meta object protocol as methods. The names of those methods are the same as those of the handler methods, which [...] helps with forwarding operations from the handler to the target."

From (Ch 20.3.6.1): "For each trap `handler.trap(target, arg_1, ..., arg_n)`, `Reflect` has a method `Reflect.trap(target, arg_1, ..., arg_n)`."

# Prerequisites

- **Proxy** — Reflect is designed to work with Proxies
- **Proxy trap** — Each Reflect method corresponds to a trap

# Key Properties

1. One method for each of the 13 traps (same names and signatures)
2. Provides operators as functions: `Reflect.has()` for `in`, `Reflect.deleteProperty()` for `delete`
3. Returns booleans for success/failure instead of throwing (unlike some `Object.*` methods)
4. Going forward, `Reflect` hosts low-level operations; `Object` hosts application-level operations

# Construction / Recognition

## To Construct/Create:
1. Use `Reflect.methodName(target, ...args)` in handler methods

## To Identify/Recognize:
1. Any `Reflect.*` method call, typically inside a Proxy handler

# Context & Application

Reflect methods are the standard way to forward operations in Proxy handlers. They also provide safer alternatives to operators (e.g., `Reflect.deleteProperty()` returns `false` instead of throwing in strict mode).

# Examples

**Example 1** (Ch 20): Using Reflect for forwarding:
```js
const handler = {
  deleteProperty(target, propKey) {
    console.log('DELETE ' + propKey);
    return Reflect.deleteProperty(target, propKey);
  },
  has(target, propKey) {
    console.log('HAS ' + propKey);
    return Reflect.has(target, propKey);
  },
}
```

**Example 2** (Ch 20): Safe `apply()`:
```js
// Unsafe:
func.apply(thisArg, argArray)
// Safe but verbose:
Function.prototype.apply.call(func, thisArg, argArray)
// Safe and concise:
Reflect.apply(func, thisArg, argArray)
```

# Relationships

## Builds Upon
- **Proxy trap** — Each Reflect method mirrors a trap

## Enables
- **Forwarding handler** — Reflect makes forwarding operations concise
- **Safe metaprogramming** — Operators as functions, boolean returns

## Related
- **Proxy handler** — Reflect is typically used inside handlers

# Common Errors

- **Error**: Using `Object.*` methods inside handlers when `Reflect.*` equivalents are more appropriate
  **Correction**: `Reflect.*` methods have the same signatures as trap methods, making forwarding simpler

# Common Confusions

- **Confusion**: `Reflect` and `Object` methods do the same thing
  **Clarification**: `Reflect` methods return booleans; `Object.defineProperty()` returns the object or throws. Going forward, `Reflect` is for low-level operations, `Object` for application-level ones.

# Source Reference

Chapter 20: Metaprogramming with Proxies, Sections 20.3.6.1, 20.7.5, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Extensively covered with all methods listed
- Cross-reference status: verified
