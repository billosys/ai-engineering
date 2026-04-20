---
# === CORE IDENTIFICATION ===
concept: Verify Interface Compliance
slug: verify-interface-compliance

# === CLASSIFICATION ===
category: interfaces
subcategory: interface-compliance
tier: intermediate

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Verify Interface Compliance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "compile-time interface check"
  - "interface satisfaction assertion"
  - "static interface assertion"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - pointers-to-interfaces
  - receivers-and-interfaces
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I verify interface compliance at compile time?"
  - "What does `var _ Interface = (*Type)(nil)` do?"
  - "When should I use compile-time interface assertions?"
---

# Quick Definition

Use compile-time assertions like `var _ Interface = (*Type)(nil)` to verify that a type implements an interface, catching violations at compile time rather than runtime.

# Core Definition

The Uber Go Style Guide recommends verifying interface compliance at compile time where appropriate. The statement `var _ http.Handler = (*Handler)(nil)` will fail to compile if `*Handler` ever stops matching the `http.Handler` interface. The right-hand side of the assignment should be the zero value of the asserted type: `nil` for pointer types, slices, and maps, and an empty struct literal for struct types (Uber Go Style Guide, "Verify Interface Compliance").

# Prerequisites

- **Go interfaces** -- Must understand how interfaces and interface satisfaction work in Go
- **Zero values** -- Understanding Go's zero values for different types (nil for pointers, slices, maps; empty struct for structs)

# Key Properties

1. The pattern uses blank identifier (`_`) assignment to avoid creating an unused variable
2. For pointer receivers, use `(*Type)(nil)` as the zero value on the right-hand side
3. For value receivers, use `Type{}` (empty struct literal) as the zero value
4. The assertion triggers a compile error if the type does not implement the interface
5. Should be used for exported types with API contracts, types in interface collections, and cases where violations would break users

# Construction / Recognition

## To Apply:
1. Identify the interface your type must satisfy
2. Determine if your type uses pointer or value receivers for the interface methods
3. For pointer receivers: add `var _ InterfaceName = (*TypeName)(nil)`
4. For value receivers: add `var _ InterfaceName = TypeName{}`
5. Place the assertion near the type declaration

## To Recognize:
1. Look for `var _ SomeInterface = (*SomeType)(nil)` or `var _ SomeInterface = SomeType{}`
2. These lines serve solely as compile-time checks and produce no runtime code

# Context & Application

This pattern is most valuable when:
- Exported types are required to implement specific interfaces as part of their API contract
- Types are part of a collection implementing the same interface (exported or unexported)
- Violating an interface would break users of the package

The assertion acts as documentation and a safety net: it communicates the intent that a type implements an interface and catches regressions if someone later removes or changes a method signature.

# Examples

**Example 1** (Guidelines, "Verify Interface Compliance"): Pointer receiver assertion

```go
type Handler struct {
  // ...
}

var _ http.Handler = (*Handler)(nil)

func (h *Handler) ServeHTTP(
  w http.ResponseWriter,
  r *http.Request,
) {
  // ...
}
```

The statement `var _ http.Handler = (*Handler)(nil)` will fail to compile if `*Handler` ever stops matching the `http.Handler` interface.

**Example 2** (Guidelines, "Verify Interface Compliance"): Value receiver assertion

```go
type LogHandler struct {
  h   http.Handler
  log *zap.Logger
}

var _ http.Handler = LogHandler{}

func (h LogHandler) ServeHTTP(
  w http.ResponseWriter,
  r *http.Request,
) {
  // ...
}
```

Since `LogHandler` uses a value receiver, the zero value is an empty struct literal `LogHandler{}`.

# Relationships

## Builds Upon
- **Go interface satisfaction rules** -- The assertion relies on Go's compile-time interface checking

## Enables
- Safer API evolution by catching interface regressions early
- Self-documenting code that declares which interfaces a type satisfies

## Related
- **pointers-to-interfaces** -- Understanding pointer vs value types is relevant to choosing the correct zero value
- **receivers-and-interfaces** -- Whether you use pointer or value receivers determines the assertion form

## Contrasts With
- Runtime interface checks using type assertions, which only catch errors at runtime

# Common Errors

- **Error**: Using `(*Type)(nil)` when the type satisfies the interface with value receivers
  **Correction**: Use `Type{}` for value receivers; `(*Type)(nil)` for pointer receivers. Both work for value receivers, but `Type{}` is more idiomatic when all methods have value receivers.

- **Error**: Omitting the compile-time check for exported types that implement interfaces
  **Correction**: Always add the assertion for exported types that are part of an API contract

# Common Confusions

- **Confusion**: Believing the assertion creates runtime overhead
  **Clarification**: The blank identifier assignment is purely a compile-time check; it produces no runtime code and has zero performance impact

- **Confusion**: Thinking `var _ Interface = (*Type)(nil)` instantiates a Type
  **Clarification**: `(*Type)(nil)` is a nil pointer of type `*Type` -- no allocation or instantiation occurs

# Source Reference

Chapter 2: Guidelines, Section "Verify Interface Compliance".

# Verification Notes

- Definition source: Directly from the "Verify Interface Compliance" section with explicit code examples
- Confidence rationale: HIGH -- the source provides detailed explanation, multiple examples, and clear guidance on when to apply
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
