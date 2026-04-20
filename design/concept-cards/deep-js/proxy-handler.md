---
# === CORE IDENTIFICATION ===
concept: Proxy Handler
slug: proxy-handler

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
section: "20.3 Proxies explained"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "handler object"
  - "trap handler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
extends: []
related:
  - proxy-trap
  - reflect-api
  - forwarding-handler
contrasts_with:
  - proxy-target

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a Proxy with handler traps?"
---

# Quick Definition

A Proxy handler is an object whose methods (called traps) intercept operations performed on the Proxy, defining custom behavior for those operations.

# Core Definition

From "Deep JavaScript" (Ch 20.3): "For each operation, there is a corresponding handler method that -- if present -- performs that operation. Such a method *intercepts* the operation (on its way to the target) and is called a *trap*." The handler is the second argument to `new Proxy(target, handler)`. If the handler doesn't implement a trap for an operation, that operation is forwarded to the target.

# Prerequisites

- **Proxy** — Handlers are used when creating Proxies

# Key Properties

1. A plain object with trap methods
2. Each method name corresponds to an interceptable operation (e.g., `get`, `set`, `has`)
3. Missing trap methods cause operations to be forwarded to the target
4. The handler is encapsulated -- it cannot be accessed via the Proxy

# Construction / Recognition

## To Construct/Create:
1. Create an object with methods named after the traps you want to intercept
2. Pass it as the second argument to `new Proxy(target, handler)`

## To Identify/Recognize:
1. The second argument to the `Proxy` constructor
2. An object with methods matching trap names

# Context & Application

The handler is the meta-level component of a Proxy. The design principle of *stratification* keeps the handler (meta level) separate from the Proxy object (base level), avoiding the problems of mixing levels.

# Examples

**Example 1** (Ch 20):
```js
const handler = {
  get(target, propKey, receiver) {
    logged.push(`GET ${propKey}`);
    return 123;
  },
  has(target, propKey) {
    logged.push(`HAS ${propKey}`);
    return true;
  }
};
const proxy = new Proxy(target, handler);
```

# Relationships

## Builds Upon
- **Proxy** — Handlers are required to create Proxies

## Enables
- **Proxy trap** — Traps are the individual methods on the handler

## Related
- **Reflect API** — Provides default implementations for forwarding operations
- **Forwarding handler** — A handler that logs then forwards all operations

## Contrasts With
- **Proxy target** — The handler intercepts; the target receives forwarded operations

# Common Errors

- **Error**: Defining a handler method with the wrong name
  **Correction**: Handler method names must exactly match trap names (e.g., `get`, `set`, `has`, `deleteProperty`)

# Common Confusions

- **Confusion**: The handler is accessible from the Proxy
  **Clarification**: Handler encapsulation means "We can't access a handler via its Proxy"

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.3, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined as a core Proxy concept
- Cross-reference status: verified
