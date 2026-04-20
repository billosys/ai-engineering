---
concept: Pass Values
slug: pass-values
category: language
subcategory: value-semantics
tier: intermediate
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Pass values"
extraction_confidence: high
aliases:
  - pass by value
  - avoid unnecessary pointers
prerequisites:
  - go-pointer-basics
related:
  - receiver-type
  - copying-decisions
contrasts_with: []
answers_questions:
  - "When should Go functions take pointers vs values?"
  - "Is passing a pointer for performance always correct in Go?"
  - "Should strings be passed by pointer in Go?"
---

# Quick Definition

Do not pass pointers as function arguments just to save a few bytes. If a function only reads its argument as `*x` throughout, the argument should not be a pointer. Pass strings, interface values, and small fixed-size types by value. Exception: large structs and protocol buffer messages should be passed by pointer.

# Core Definition

> "Do not pass pointers as function arguments just to save a few bytes. If a function reads its argument `x` only as `*x` throughout, then the argument shouldn't be a pointer. Common instances of this include passing a pointer to a string (`*string`) or a pointer to an interface value (`*io.Reader`). In both cases, the value itself is a fixed size and can be passed directly." -- Google Go Style Guide, "Pass values"

> "This advice does not apply to large structs, or even small structs that may increase in size. In particular, protocol buffer messages should generally be handled by pointer rather than by value." -- Google Go Style Guide, "Pass values"

# Prerequisites

- Understanding of Go's value vs. pointer semantics
- Knowledge of how Go passes arguments (always by copy)

# Key Properties

1. **No pointers for read-only small values**: If a function only dereferences a pointer to read, pass the value directly.
2. **Strings are fixed-size**: A `string` is a 16-byte header (pointer + length); pass it by value, not as `*string`.
3. **Interfaces are fixed-size**: An `io.Reader` is a two-word interface value; pass it directly, not as `*io.Reader`.
4. **Large structs use pointers**: Structs that are large or may grow (especially protocol buffer messages) should be passed by pointer.
5. **Proto messages**: Always handle by pointer -- they satisfy `proto.Message` interface and can be arbitrarily large.

# Construction / Recognition

**Bad -- unnecessary pointer for a string:**

```go
func process(name *string) {
    fmt.Println(*name)
}
```

**Good -- pass string by value:**

```go
func process(name string) {
    fmt.Println(name)
}
```

**Bad -- unnecessary pointer for an interface:**

```go
func read(r *io.Reader) { ... }
```

**Good -- pass interface by value:**

```go
func read(r io.Reader) { ... }
```

**Good -- pointer for large/growing struct:**

```go
func processMessage(msg *pb.Request) { ... }
```

# Context & Application

The motivation for passing pointers to save bytes is usually misguided for small types. A string is already a small header, and copying it is cheap. Passing a pointer adds indirection and can inhibit compiler optimizations like escape analysis. The exception for protocol buffers is practical: proto messages implement `proto.Message` via a pointer receiver and can grow to arbitrary sizes as schemas evolve.

# Examples

See Construction / Recognition above for illustrative examples.

# Relationships

- **receiver-type**: Parallel guidance for choosing pointer vs. value receivers on methods.
- **copying-decisions**: Related concern about when copying values is safe.

# Common Errors

1. Passing `*string` or `*io.Reader` "for performance."
2. Using pointers for all parameters regardless of size.
3. Passing protocol buffer messages by value (breaks `proto.Message` interface).

# Common Confusions

- **Performance assumptions**: The compiler can optimize value passing; don't assume pointers are faster without benchmarks.
- **Mutation vs. size**: The primary reason to use pointers is mutation or large size, not micro-optimization.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Pass values" section.

# Verification Notes

Confidence: high. All guidance is directly from the source text.
