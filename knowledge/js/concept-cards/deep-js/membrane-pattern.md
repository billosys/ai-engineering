---
# === CORE IDENTIFICATION ===
concept: Membrane Pattern
slug: membrane-pattern

# === CLASSIFICATION ===
category: metaprogramming
subcategory: membranes
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Metaprogramming with Proxies"
chapter_number: 20
section: "20.4.6.1 Membranes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "membrane"
  - "security membrane"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - revocable-proxy
  - revocable-reference
extends:
  - revocable-reference
related:
  - proxy-handler
  - transparent-virtualization
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a membrane pattern?"
  - "What must I understand before learning about the membrane pattern?"
---

# Quick Definition

A membrane is a security pattern that wraps revocable Proxy references around all objects crossing a trust boundary, enabling complete isolation of untrusted code that can be permanently cut off.

# Core Definition

From "Deep JavaScript" (Ch 20.4.6.1): "*Membranes* build on the idea of revocable references: Libraries for safely running untrusted code wrap a membrane around that code to isolate it and to keep the rest of the system safe." Objects pass the membrane in two directions: untrusted code receives "dry objects" from outside, and hands "wet objects" to outside. "In both cases, revocable references are wrapped around the objects. Objects returned by wrapped functions or methods are also wrapped. Additionally, if a wrapped wet object is passed back into a membrane, it is unwrapped."

"Once the untrusted code is done, all of the revocable references are revoked."

# Prerequisites

- **Proxy** — Membranes are built with Proxies
- **Revocable Proxy** — The revocability mechanism enables shutting down the membrane
- **Revocable reference** — The building block for membranes

# Key Properties

1. Wraps all objects crossing the trust boundary (both directions)
2. Objects returned by wrapped functions/methods are also wrapped (transitive wrapping)
3. Objects passed back through the membrane are unwrapped (identity preservation)
4. All revocable references can be revoked at once, completely cutting off untrusted code
5. Used by the Caja Compiler for safe embedding of third-party HTML/CSS/JS

# Construction / Recognition

## To Construct/Create:
1. Create revocable Proxies for all objects crossing the boundary
2. Intercept function returns and method calls to wrap their results
3. Track wrapped objects to unwrap when they cross back
4. Provide a master `revoke` function to disable all references at once

## To Identify/Recognize:
1. A system where all cross-boundary object references are Proxy-wrapped and revocable

# Context & Application

Membranes are the gold standard for JavaScript sandboxing. They allow untrusted code to interact with trusted objects through controlled interfaces that can be permanently disabled.

# Examples

**Example 1** (Ch 20): Conceptual description:
```
// Untrusted code receives "dry objects" from the outside
// Untrusted code hands "wet objects" to the outside
// In both cases, revocable references wrap the objects
// When untrusted code is done, all references are revoked
```

# Relationships

## Builds Upon
- **Revocable reference** — Membranes extend revocable references to all cross-boundary objects
- **Revocable Proxy** — The underlying mechanism

## Enables
- **JavaScript sandboxing** — Safe execution of untrusted code
- **Resource isolation** — Complete cutoff of untrusted code's access

## Related
- **Transparent virtualization** — Membrane-wrapped objects should appear normal to untrusted code

# Common Errors

- **Error**: Only wrapping objects in one direction
  **Correction**: Both incoming ("dry") and outgoing ("wet") objects must be wrapped

# Common Confusions

- **Confusion**: A membrane is just a single Proxy wrapper
  **Clarification**: A membrane transitively wraps all objects, function returns, and method results crossing the boundary. It maintains identity so objects passed back are unwrapped.

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.4.6.1, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined with dry/wet terminology
- Cross-reference status: verified (references Caja Compiler)
