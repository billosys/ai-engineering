---
# === CORE IDENTIFICATION ===
concept: Delegation via Forwarding
slug: delegation-via-forwarding

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
extraction_confidence: high

# === VARIANTS ===
aliases:
  - forwarding
  - method delegation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
extends: []
related:
  - wrapper-pattern
  - facade-pattern
contrasts_with:
  - inheritance

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is delegation via forwarding in JavaScript?"
---

# Quick Definition

Delegation via forwarding is a technique where one object handles some of its work by forwarding method calls to another object (the delegate), serving as an alternative to inheritance for code sharing.

# Core Definition

As described in "Deep JavaScript" (Ch 16, Section 16.1): "We used forwarding to implement delegation. Delegation means that one object lets another object (the delegate) handle some of its work. It is an alternative to inheritance for sharing code."

# Prerequisites

- **JavaScript classes** — Method calling and object composition.

# Key Properties

1. The wrapper **forwards** method calls to the wrapped object.
2. Forwarding implements **delegation** — the wrapper delegates work to the wrapped object.
3. It is an **alternative to inheritance** for code reuse.
4. The wrapper can **selectively** choose which methods to forward.
5. The delegate (wrapped object) does not know it is being delegated to.

# Construction / Recognition

## To Construct/Create:
1. Store the delegate in a field (private preferred).
2. Define methods that call the corresponding method on the delegate.
3. Pass through arguments with `...args` and return the result.

## To Identify/Recognize:
1. A method body that consists of calling the same method on a stored object.
2. Pattern: `method(...args) { return this.#delegate.method(...args); }`.

# Context & Application

Forwarding-based delegation is the mechanism underlying the wrapper pattern. It provides composition-based code reuse, following the principle of "favor composition over inheritance." In Chapter 16, it is specifically used to create restricted (immutable) views of collections.

# Examples

**Example 1** (Ch 16): Forwarding methods:
```js
class Wrapper {
  #wrapped;
  constructor(wrapped) {
    this.#wrapped = wrapped;
  }
  allowedMethod1(...args) {
    return this.#wrapped.allowedMethod1(...args);
  }
  allowedMethod2(...args) {
    return this.#wrapped.allowedMethod2(...args);
  }
}
```

# Relationships

## Builds Upon
- **Object composition** — Storing one object inside another.

## Enables
- **Wrapper pattern** — Wrapping is implemented via forwarding.
- **Interface restriction** — Selective forwarding hides some methods.

## Related
- **Facade pattern** — Uses forwarding to simplify a complex interface.

## Contrasts With
- **Inheritance** — Inheritance shares code via the prototype chain; delegation shares code via explicit forwarding.

# Common Errors

- **Error**: Forgetting to return the delegate's return value.
  **Correction**: Use `return this.#delegate.method(...args)` — omitting `return` discards the result.

# Common Confusions

- **Confusion**: Thinking forwarding and prototypal delegation are the same.
  **Clarification**: Prototypal delegation uses the prototype chain automatically. Forwarding is explicit — you must write the forwarding code for each method.

# Source Reference

Chapter 16: Immutable wrappers for collections, Section 16.1, lines 7660-7668.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicitly defined with reference to delegation pattern
- Cross-reference status: verified against wrapper pattern implementation
