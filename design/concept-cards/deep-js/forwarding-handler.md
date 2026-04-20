---
# === CORE IDENTIFICATION ===
concept: Forwarding Handler
slug: forwarding-handler

# === CLASSIFICATION ===
category: metaprogramming
subcategory: handlers
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Metaprogramming with Proxies"
chapter_number: 20
section: "20.3.6 Forwarding intercepted operations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "logging handler"
  - "intercepting forwarder"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
  - reflect-api
extends:
  - proxy-handler
related:
  - proxy-trap
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a Proxy with handler traps?"
---

# Quick Definition

A forwarding handler is a Proxy handler that intercepts operations (e.g., for logging) but still forwards them to the target, typically using `Reflect` methods.

# Core Definition

From "Deep JavaScript" (Ch 20.3.6): "Sometimes there is some task we want to perform in addition to forwarding the operation. For example, intercepting and logging all operations, without preventing them from reaching the target." An advanced technique implements the handler itself as a Proxy, using the `get` trap to dynamically return handler methods that log and forward via `Reflect`:

```js
const handler = new Proxy({}, {
  get(target, trapName, receiver) {
    return (...args) => {
      console.log(trapName.toUpperCase() + ' ' + args[1]);
      return Reflect[trapName](...args);
    };
  },
});
```

# Prerequisites

- **Proxy** — Forwarding handlers are Proxy handlers
- **Proxy handler** — The forwarding handler is a specific handler pattern
- **Reflect API** — Used to forward operations to the target

# Key Properties

1. Intercepts operations for side effects (logging, tracing, profiling)
2. Forwards every operation to the target via `Reflect.*` methods
3. Can be implemented concisely using a Proxy-as-handler technique
4. The Proxy-as-handler pattern was a design goal of the Proxy API

# Construction / Recognition

## To Construct/Create:
1. Define handler methods that call `Reflect.*` after performing side effects
2. Or use a Proxy as the handler itself, with a `get` trap returning forwarding functions

## To Identify/Recognize:
1. A handler where every trap calls the corresponding `Reflect.*` method

# Context & Application

Forwarding handlers demonstrate the power of combining Proxies with Reflect. The Proxy-as-handler technique enables "all of the handler methods can be implemented via the single meta-method `get`."

# Examples

**Example 1** (Ch 20): Proxy-as-handler for universal logging:
```js
const handler = new Proxy({}, {
  get(target, trapName, receiver) {
    return (...args) => {
      console.log(trapName.toUpperCase() + ' ' + args[1]);
      return Reflect[trapName](...args);
    };
  },
});
const proxy = new Proxy(target, handler);
proxy.distance = 450;
// Output:
// 'SET distance'
// 'GETOWNPROPERTYDESCRIPTOR distance'
// 'DEFINEPROPERTY distance'
```

# Relationships

## Builds Upon
- **Proxy handler** — A specific handler pattern
- **Reflect API** — Used for forwarding

## Enables
- **Tracing** — Log all operations on an object
- **Profiling** — Measure time spent in operations

# Common Errors

- **Error**: Forgetting to return the `Reflect.*` result from the handler method
  **Correction**: The return value must be forwarded for the operation to work correctly

# Common Confusions

- **Confusion**: A forwarding handler adds no overhead
  **Clarification**: Even forwarding Proxies have performance overhead; the source notes "Proxies themselves have an impact on performance"

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.3.6, lines 9133+.

# Verification Notes

- Definition source: direct from source text with implementation
- Confidence rationale: Extensively demonstrated with two approaches
- Cross-reference status: verified
