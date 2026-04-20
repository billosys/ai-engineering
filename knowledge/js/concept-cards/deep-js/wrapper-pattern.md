---
# === CORE IDENTIFICATION ===
concept: Wrapper Pattern
slug: wrapper-pattern

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
  - object wrapping
  - wrapper object

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
extends: []
related:
  - facade-pattern
  - delegation-via-forwarding
  - immutable-wrapper
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a wrapper pattern for reducing an object's interface?"
---

# Quick Definition

The wrapper pattern creates a new object that stores an original object in a private field and selectively forwards only some method calls, effectively reducing the original's interface.

# Core Definition

As described in "Deep JavaScript" (Ch 16, Section 16.1): "If there is an object whose interface we'd like to reduce, we can take the following approach: Create a new object that stores the original in a private field. The new object is said to wrap the original object. The new object is called wrapper, the original object wrapped object. The wrapper only forwards some of the method calls it receives to the wrapped object."

# Prerequisites

- **JavaScript classes** — Class syntax with private fields.

# Key Properties

1. The original object is stored in a **private field** of the wrapper.
2. The wrapper **selectively forwards** method calls to the wrapped object.
3. Methods not forwarded are **effectively hidden** from users of the wrapper.
4. The wrapper controls what **operations are accessible**.
5. Related to the **Facade** design pattern (Gang of Four).

# Construction / Recognition

## To Construct/Create:
1. Create a wrapper class with a private field for the wrapped object.
2. Accept the wrapped object in the constructor.
3. Define methods that forward calls to the wrapped object.
4. Omit methods you want to hide.

## To Identify/Recognize:
1. A class that stores another object in a private field.
2. The class's methods delegate to the stored object.
3. The class exposes fewer methods than the original.

# Context & Application

Wrapping is used to create restricted views of objects. The primary use case in Chapter 16 is making collections immutable by wrapping them and only forwarding non-destructive methods. It is also useful for exporting internal data structures safely.

# Examples

**Example 1** (Ch 16): Generic wrapper structure:
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
- **Private fields** — The wrapped object is hidden from external access.

## Enables
- **Immutable wrapper** — A specific application that hides mutating methods.
- **Interface restriction** — Controls what operations are available.

## Related
- **Facade pattern** — The GoF pattern that wrapping is related to.
- **Delegation via forwarding** — The mechanism used to implement wrapping.

## Contrasts With
- **Inheritance** — Subclassing adds or modifies behavior; wrapping restricts it.
- **Proxy** — Proxies intercept all operations dynamically; wrappers are explicit.

# Common Errors

- **Error**: Exposing the wrapped object via a getter.
  **Correction**: Keep the wrapped object in a private field with no public accessor, otherwise the restriction can be bypassed.

# Common Confusions

- **Confusion**: Thinking a wrapper must expose the same interface as the wrapped object.
  **Clarification**: The whole point of wrapping is to expose a reduced interface. The wrapper chooses which methods to forward.

# Source Reference

Chapter 16: Immutable wrappers for collections, Section 16.1, lines 7640-7690.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicitly defined with structural code example
- Cross-reference status: verified against Facade/delegation references in source
