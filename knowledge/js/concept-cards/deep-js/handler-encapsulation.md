---
# === CORE IDENTIFICATION ===
concept: Handler Encapsulation
slug: handler-encapsulation

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
section: "20.5.3 Transparent virtualization and handler encapsulation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - proxy-handler
extends: []
related:
  - transparent-virtualization
  - stratification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Proxy in JavaScript?"
---

# Quick Definition

Handler encapsulation is the principle that a Proxy's handler object cannot be accessed through the Proxy itself, keeping the meta-level implementation hidden.

# Core Definition

From "Deep JavaScript" (Ch 20.5.3): "Proxies are shielded in two ways: [...] We can't access a handler via its Proxy (*handler encapsulation*)." Together with transparent virtualization, this gives "Proxies considerable power for impersonating other objects."

# Prerequisites

- **Proxy** — Handler encapsulation is a design property of Proxies
- **Proxy handler** — The handler is what is encapsulated

# Key Properties

1. No API to retrieve the handler from a Proxy
2. Complements transparent virtualization
3. Prevents external code from discovering or modifying interception behavior

# Construction / Recognition

## To Construct/Create:
1. Inherent property of all Proxies -- no construction needed

## To Identify/Recognize:
1. Attempting to retrieve a handler from a Proxy yields no result

# Context & Application

Handler encapsulation ensures that code interacting with a Proxy cannot discover what operations are being intercepted or how. This is essential for security patterns like membranes.

# Examples

**Example 1** (Ch 20): No built-in way to access the handler:
```js
const proxy = new Proxy({}, { get() { return 42; } });
// There is no proxy.handler, proxy.__handler__, or similar
```

# Relationships

## Builds Upon
- **Proxy** — A design property

## Related
- **Transparent virtualization** — The other shielding principle
- **Stratification** — Keeping meta and base levels separate

# Common Confusions

- **Confusion**: You can inspect a Proxy's traps from outside
  **Clarification**: Handler encapsulation prevents any external access to the handler

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.5.3, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
