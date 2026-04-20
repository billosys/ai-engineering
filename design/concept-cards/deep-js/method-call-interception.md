---
# === CORE IDENTIFICATION ===
concept: Method Call Interception
slug: method-call-interception

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
section: "20.3.3 Intercepting method calls"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "intercepting methods via Proxy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - get-trap
extends:
  - get-trap
related:
  - apply-trap
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a Proxy with handler traps?"
---

# Quick Definition

Method call interception uses the `get` trap to return a wrapper function that logs or modifies the method call, since there is no dedicated method-call trap in the Proxy API.

# Core Definition

From "Deep JavaScript" (Ch 20.3.3): "If we want to intercept method calls via a Proxy, we are facing a challenge: There is no trap for method calls. Instead, a method call is viewed as a sequence of two operations: A `get` to retrieve a function, An `apply` to call that function." The pattern: intercept `get` to return a wrapped version of the original method.

# Prerequisites

- **Proxy** — Method call interception uses Proxies
- **Get trap** — The `get` trap retrieves the method before it's called

# Key Properties

1. No dedicated `invoke` trap exists in the Proxy API
2. Method calls are `get` + `apply` (two operations)
3. The `get` trap returns a wrapper function that calls the original method
4. `this` in the proxied method refers to the Proxy, keeping tracing active for internal calls

# Construction / Recognition

## To Construct/Create:
1. Implement a `get` trap that returns a wrapper function around the original method

## To Identify/Recognize:
1. A `get` trap that returns functions wrapping `target[propKey]`

# Context & Application

This pattern enables method tracing, profiling, and logging. Because `this` refers to the Proxy during method execution, internal method calls (e.g., `this.multiply()`) are also traced.

# Examples

**Example 1** (Ch 20):
```js
function traceMethodCalls(obj) {
  const handler = {
    get(target, propKey, receiver) {
      const origMethod = target[propKey];
      return function (...args) {
        const result = origMethod.apply(this, args);
        traced.push(propKey + JSON.stringify(args)
          + ' -> ' + JSON.stringify(result));
        return result;
      };
    }
  };
  return new Proxy(obj, handler);
}
```

# Relationships

## Builds Upon
- **Get trap** — Uses `get` to intercept method retrieval

## Related
- **Apply trap** — An alternative that intercepts function calls directly (when the Proxy itself is a function)

# Common Errors

- **Error**: Using an arrow function for the wrapper (losing dynamic `this`)
  **Correction**: Use a regular function to preserve `this` pointing to the Proxy

# Common Confusions

- **Confusion**: There should be an `invoke` trap for method calls
  **Clarification**: The design intentionally omits `invoke` -- extracting a method and calling it later should be equivalent to calling via dispatch

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.3.3, lines 9133+.

# Verification Notes

- Definition source: direct from source text with implementation
- Confidence rationale: Extensively demonstrated with example
- Cross-reference status: verified
