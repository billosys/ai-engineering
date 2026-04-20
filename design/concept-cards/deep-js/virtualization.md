---
# === CORE IDENTIFICATION ===
concept: Virtualization
slug: virtualization

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
section: "20.5.2 Virtual objects versus wrappers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "virtual object"
  - "transparent virtualization"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
extends: []
related:
  - proxy-invariants
  - transparent-virtualization
contrasts_with:
  - proxy-wrapper

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Proxy in JavaScript?"
---

# Quick Definition

Virtualization is the use of a Proxy as a standalone object with custom behavior, where the target is incidental -- the Proxy *is* the object rather than wrapping another.

# Core Definition

From "Deep JavaScript" (Ch 20.5.2): "Proxies are used in two roles: As *wrappers*, they *wrap* their targets, they control access to them. [...] As *virtual objects*, they are simply objects with special behavior and their targets don't matter." Examples of virtual objects include a Proxy that forwards method calls to a remote object. The target still serves a purpose: enforcing invariants and providing fallback behavior.

# Prerequisites

- **Proxy** — Virtualization is a Proxy usage pattern
- **Proxy handler** — The handler defines the virtual behavior

# Key Properties

1. The Proxy *is* the object, not a wrapper around another object
2. The target exists for invariant enforcement and fallback behavior
3. It is impossible to determine whether an object is a Proxy (transparent virtualization)
4. Useful for remote objects, web service clients, lazy-loading proxies

# Construction / Recognition

## To Construct/Create:
1. Create a Proxy with a minimal target (e.g., `{}` or `function(){}`)
2. Implement desired behavior entirely in handler traps

## To Identify/Recognize:
1. A Proxy where the handler defines all meaningful behavior, not the target

# Context & Application

Virtual objects enable creating objects with completely custom semantics -- dynamic property generation, remote method dispatch, or API abstractions -- without any real backing object.

# Examples

**Example 1** (Ch 20): Web service client as virtual object:
```js
function createWebService(baseUrl) {
  return new Proxy({}, {
    get(target, propKey, receiver) {
      return () => httpGet(baseUrl + '/' + propKey);
    }
  });
}
```

# Relationships

## Builds Upon
- **Proxy** — Virtualization is one of two main Proxy usage patterns

## Related
- **Proxy invariants** — Constrain virtual objects to maintain consistency

## Contrasts With
- **Proxy wrapper** — Wrappers control access to the target; virtual objects define standalone behavior

# Common Errors

- **Error**: Creating a virtual object without considering invariants
  **Correction**: Even virtual objects must respect invariants; the target's state affects what the handler can report

# Common Confusions

- **Confusion**: Virtual objects don't need a target
  **Clarification**: Every Proxy requires a target for invariant checking and fallback behavior, even if the target is minimal

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.5.2, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined and contrasted with wrappers
- Cross-reference status: verified
