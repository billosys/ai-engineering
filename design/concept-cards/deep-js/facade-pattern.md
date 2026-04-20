---
# === CORE IDENTIFICATION ===
concept: Facade Pattern
slug: facade-pattern

# === CLASSIFICATION ===
category: class-patterns
subcategory: wrapping
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Immutable wrappers for collections"
chapter_number: 16
section: "16.1 Wrapping objects"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - Facade

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
extends: []
related:
  - wrapper-pattern
  - delegation-via-forwarding
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What design pattern is wrapping related to?"
---

# Quick Definition

The Facade pattern (Gang of Four) provides a simplified interface to a complex subsystem or object; wrapping is related to this pattern because it reduces the interface of the wrapped object.

# Core Definition

As referenced in "Deep JavaScript" (Ch 16, Section 16.1): "Wrapping is related to the Gang of Four design pattern Facade." A Facade provides a simpler, more focused interface to a more complex underlying object or system. In the context of Chapter 16, immutable wrappers act as facades by presenting only the read-only portion of a collection's interface.

# Prerequisites

- **JavaScript classes** — Object-oriented design.

# Key Properties

1. Provides a **simplified interface** to a complex object or subsystem.
2. Hides **complexity** and irrelevant operations from the consumer.
3. The wrapped object's full interface is still available **internally**.
4. Implemented via **delegation/forwarding** of selected methods.

# Construction / Recognition

## To Construct/Create:
1. Identify the subset of operations consumers need.
2. Create a new class that wraps the original and exposes only those operations.
3. Forward selected method calls to the underlying object.

## To Identify/Recognize:
1. A class that simplifies or restricts access to another object.
2. The wrapper has fewer methods than the wrapped object.

# Context & Application

The Facade pattern is mentioned as the design pattern context for the wrapping technique. In Chapter 16, the "facade" is specifically a read-only facade over a mutable collection, but the Facade pattern applies more broadly to any interface simplification.

# Examples

**Example 1** (Ch 16): ImmutableMapWrapper as a Facade:
```js
// The Map has methods: get, has, keys, size, set, delete, clear, ...
// The wrapper (facade) only exposes: get, has, keys, size
const wrapped = new ImmutableMapWrapper(map);
```

# Relationships

## Builds Upon
- **Object composition** — The facade contains a reference to the complex object.

## Enables
- **Interface simplification** — Consumers see only what they need.
- **Immutable wrappers** — Immutable wrappers are facades that hide mutating methods.

## Related
- **Wrapper pattern** — The implementation technique used to build facades.
- **Delegation via forwarding** — The mechanism facades use to delegate work.

## Contrasts With
- **Adapter pattern** — Adapters convert interfaces; facades simplify them.

# Common Errors

- **Error**: Creating a facade that is too thin and doesn't add value.
  **Correction**: A facade should meaningfully simplify or restrict the interface, not just add an indirection layer.

# Common Confusions

- **Confusion**: Thinking a Facade must wrap multiple objects.
  **Clarification**: While the classic Facade pattern often wraps a subsystem, it can also wrap a single complex object, as shown in Chapter 16.

# Source Reference

Chapter 16: Immutable wrappers for collections, Section 16.1, lines 7659-7662.

# Verification Notes

- Definition source: synthesized (referenced by name in source, definition drawn from standard GoF knowledge)
- Confidence rationale: Named but not fully defined in source; standard pattern definition applied
- Cross-reference status: verified as referenced in source text
