---
concept: Use go.uber.org/atomic
slug: use-uber-atomic
category: concurrency
subcategory: atomic-operations
tier: intermediate
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Use go.uber.org/atomic"
extraction_confidence: high
aliases:
  - uber atomic
  - type-safe atomics
prerequisites:
  - go-concurrency-basics
related:
  - avoid-mutable-globals
contrasts_with: []
answers_questions:
  - "Why use go.uber.org/atomic instead of sync/atomic?"
  - "What are the risks of using raw sync/atomic operations?"
---

# Quick Definition

Use `go.uber.org/atomic` instead of the standard `sync/atomic` package for atomic operations. The standard package operates on raw types (`int32`, `int64`), making it easy to accidentally perform non-atomic reads or writes. The `go.uber.org/atomic` package wraps these in type-safe structs like `atomic.Bool`.

# Core Definition

> "Atomic operations with the sync/atomic package operate on the raw types (`int32`, `int64`, etc.) so it is easy to forget to use the atomic operation to read or modify the variables." -- Uber Go Style Guide, "Use go.uber.org/atomic"

> "go.uber.org/atomic adds type safety to these operations by hiding the underlying type. Additionally, it includes a convenient `atomic.Bool` type." -- Uber Go Style Guide, "Use go.uber.org/atomic"

# Prerequisites

- Understanding of concurrent access and data races in Go
- Familiarity with atomic operations and why they are needed
- Basic knowledge of the `sync/atomic` standard library package

# Key Properties

1. **Type safety**: The underlying primitive type is hidden, so all access must go through atomic methods.
2. **Prevents accidental non-atomic access**: With raw `int32`, a direct read like `f.running == 1` is a data race. With `atomic.Bool`, you must call `f.running.Load()`.
3. **Convenient types**: Provides `atomic.Bool`, `atomic.Int32`, `atomic.Int64`, `atomic.String`, etc.
4. **Method-based API**: Uses `.Load()`, `.Store()`, `.Swap()`, `.CAS()` instead of package-level functions.

# Construction / Recognition

**Bad -- raw sync/atomic with race condition:**

```go
type foo struct {
  running int32  // atomic
}

func (f *foo) start() {
  if atomic.SwapInt32(&f.running, 1) == 1 {
     // already running...
     return
  }
  // start the Foo
}

func (f *foo) isRunning() bool {
  return f.running == 1  // race!
}
```

**Good -- go.uber.org/atomic with type safety:**

```go
type foo struct {
  running atomic.Bool
}

func (f *foo) start() {
  if f.running.Swap(true) {
     // already running...
     return
  }
  // start the Foo
}

func (f *foo) isRunning() bool {
  return f.running.Load()
}
```

# Context & Application

In the bad example, the `isRunning()` method reads `f.running` directly (`f.running == 1`) without using `atomic.LoadInt32`, creating a data race. The comment `// atomic` on the field is the only hint that atomic access is required, but the compiler does not enforce it. With `atomic.Bool`, the type itself enforces that all access goes through atomic methods -- there is no way to read the value without calling `.Load()`.

# Examples

See Construction / Recognition above for the source examples.

# Relationships

- **avoid-mutable-globals**: Both address safe concurrent access patterns; mutable globals compound the risk of non-atomic access.

# Common Errors

1. Using a raw `int32` field with a `// atomic` comment but then reading it directly elsewhere in the code.
2. Mixing atomic and non-atomic access to the same variable.
3. Using `sync/atomic` functions inconsistently across a codebase when `go.uber.org/atomic` would enforce correctness.

# Common Confusions

- **`sync/atomic` is not wrong per se**: It works correctly when used consistently. The problem is that it relies on developer discipline rather than type system enforcement. `go.uber.org/atomic` makes misuse a compile error.

# Source Reference

Uber Go Style Guide, "Guidelines" chapter, "Use go.uber.org/atomic" section.

# Verification Notes

Confidence: high. The rationale, the race condition in the bad example, and the type-safe alternative are all explicitly presented in the source with code examples.
