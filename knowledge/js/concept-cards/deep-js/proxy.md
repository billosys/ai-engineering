---
# === CORE IDENTIFICATION ===
concept: Proxy
slug: proxy

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
section: "20.1 Overview"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Proxy object"
  - "ES6 Proxy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - metaprogramming
extends: []
related:
  - proxy-handler
  - proxy-trap
  - reflect-api
  - proxy-target
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Proxy in JavaScript?"
  - "How do I create a Proxy with handler traps?"
---

# Quick Definition

A Proxy is a special JavaScript object that intercepts and customizes operations performed on a target object, enabling metaprogramming through handler traps.

# Core Definition

From "Deep JavaScript" (Ch 20.1): "Proxies enable us to intercept and customize operations performed on objects (such as getting properties). They are a *metaprogramming* feature." A Proxy is created with two parameters: a `handler` (which intercepts operations via trap methods) and a `target` (which serves as fallback when the handler doesn't intercept an operation).

From (Ch 20.3): "Proxies are special objects that allow us to customize some of these operations. A Proxy is created with two parameters: `handler` [...] and `target`."

# Prerequisites

- **Metaprogramming** — Proxies are a metaprogramming feature (intercession)

# Key Properties

1. Created via `new Proxy(target, handler)`
2. Operations not intercepted by the handler are forwarded to the target
3. Each interceptable operation corresponds to a trap method on the handler
4. Proxies are transparent -- it is impossible to determine whether an object is a Proxy
5. Proxies slow down code; performance may be a consideration

# Construction / Recognition

## To Construct/Create:
1. `const proxy = new Proxy(target, handler)`
2. Or `const {proxy, revoke} = Proxy.revocable(target, handler)` for revocable Proxies

## To Identify/Recognize:
1. Cannot be detected externally (transparent virtualization)
2. Must track Proxies explicitly (e.g., via a WeakSet) if detection is needed

# Context & Application

Proxies are used for tracing, validation, data binding, access control, virtual objects, and implementing the membrane pattern. They bring intercession (redefining language operation semantics) to JavaScript.

# Examples

**Example 1** (Ch 20): Basic Proxy with a get trap:
```js
const target = {size: 0};
const handler = {
  get(target, propKey, receiver) {
    logged.push('GET ' + propKey);
    return 123;
  }
};
const proxy = new Proxy(target, handler);

assert.equal(proxy.size, 123);
```

# Relationships

## Builds Upon
- **Metaprogramming** — Proxies implement intercession

## Enables
- **Proxy handler** — The handler defines which operations to intercept
- **Revocable Proxy** — Proxies can be made revocable
- **Membrane pattern** — Uses Proxies for security isolation

## Related
- **Reflect API** — Mirror API for forwarding intercepted operations

# Common Errors

- **Error**: Wrapping objects with internal slots (e.g., Date) in a Proxy with empty handler
  **Correction**: Built-in objects using internal slots cannot be transparently wrapped; methods that depend on `[[DateValue]]` etc. will throw `TypeError`

# Common Confusions

- **Confusion**: A Proxy replaces its target
  **Clarification**: The Proxy wraps the target; unintercepted operations are forwarded to the target. The target itself is unchanged.

# Source Reference

Chapter 20: Metaprogramming with Proxies, Sections 20.1 and 20.3, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Central concept of the entire chapter
- Cross-reference status: verified
