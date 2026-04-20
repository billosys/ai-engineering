---
# === CORE IDENTIFICATION ===
concept: Meta Object Protocol
slug: meta-object-protocol

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
section: "20.5.4 The meta object protocol and Proxy traps"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "MOP"
  - "JavaScript MOP"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - metaprogramming
  - proxy
extends: []
related:
  - proxy-trap
  - reflect-api
  - fundamental-vs-derived-operations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Proxy traps relate to property descriptor operations?"
---

# Quick Definition

The meta object protocol (MOP) is the set of internal methods that all JavaScript objects have for handling fundamental operations like property access, assignment, and deletion.

# Core Definition

From "Deep JavaScript" (Ch 20.5.4): "The ECMAScript specification describes how to execute JavaScript code. It includes a protocol for handling objects. This protocol operates at a meta level and is sometimes called the *meta object protocol* (MOP). The JavaScript MOP consists of own internal methods that all objects have." Internal method names are written in double square brackets (e.g., `[[Get]]`, `[[Set]]`).

For normal objects, derived operations call other operations. For Proxies, "each operation (regardless of whether it is fundamental or derived) is either intercepted by a handler method or forwarded to the target."

# Prerequisites

- **Metaprogramming** — The MOP operates at the meta level
- **Proxy** — Proxy traps correspond to MOP operations

# Key Properties

1. Internal methods exist in the spec but may not exist in actual engines
2. Names written in double square brackets: `[[Get]]`, `[[Set]]`, `[[GetOwnProperty]]`
3. Fundamental operations are independent; derived operations call other MOP methods
4. Proxy traps correspond to MOP operations
5. Proxy MOP differs from normal object MOP -- each trap is independently interceptable

# Construction / Recognition

## To Construct/Create:
1. Not directly constructible -- the MOP is the spec-level description of how objects work

## To Identify/Recognize:
1. Internal methods referenced in the ECMAScript specification

# Context & Application

Understanding the MOP explains why certain traps exist and how they relate. For example, `[[Get]]` internally calls `[[GetOwnProperty]]` and `[[GetPrototypeOf]]`, which is why the `get` trap can be implemented via fundamental traps.

# Examples

**Example 1** (Ch 20): Pseudo-implementation of `[[Get]]`:
```js
__Get__(propKey, receiver) {
  const desc = this.__GetOwnProperty__(propKey);
  if (desc === undefined) {
    const parent = this.__GetPrototypeOf__();
    if (parent === null) return undefined;
    return parent.__Get__(propKey, receiver);
  }
  if ('value' in desc) {
    return desc.value;
  }
  const getter = desc.get;
  if (getter === undefined) return undefined;
  return getter.__Call__(receiver, []);
}
```

# Relationships

## Builds Upon
- **Metaprogramming** — The MOP is the meta-level protocol for objects

## Enables
- **Proxy traps** — Each trap corresponds to a MOP operation
- **Reflect API** — Implements MOP operations as callable functions

## Related
- **Fundamental vs. derived operations** — MOP operations are classified this way

# Common Confusions

- **Confusion**: Internal methods are real JavaScript methods you can call
  **Clarification**: They exist only in the specification; engines may implement them differently

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.5.4, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined with pseudo-implementation
- Cross-reference status: verified (references ECMAScript spec)
