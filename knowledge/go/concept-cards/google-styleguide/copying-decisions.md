---
concept: Copying
slug: copying-decisions
category: language
subcategory: value-semantics
tier: intermediate
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Copying"
extraction_confidence: high
aliases:
  - struct copying
  - copy safety
prerequisites:
  - go-struct-basics
  - receiver-type
related:
  - pass-values
  - receiver-type
contrasts_with: []
answers_questions:
  - "When is it unsafe to copy a struct in Go?"
  - "Why shouldn't you copy a sync.Mutex?"
  - "How do pointer receivers relate to copy safety?"
---

# Quick Definition

Be careful when copying structs from other packages. Types whose methods use pointer receivers (like `sync.Mutex` and `bytes.Buffer`) must not be copied by value. When authoring APIs with non-copyable fields, use pointer types for parameters and returns to prevent accidental copying.

# Core Definition

> "To avoid unexpected aliasing and similar bugs, be careful when copying a struct from another package. For example, synchronization objects such as `sync.Mutex` must not be copied." -- Google Go Style Guide, "Copying"

> "In general, do not copy a value of type `T` if its methods are associated with the pointer type, `*T`." -- Google Go Style Guide, "Copying"

# Prerequisites

- Understanding of Go value vs. pointer semantics
- Knowledge of `sync.Mutex` and similar types

# Key Properties

1. **Sync types are non-copyable**: `sync.Mutex`, `sync.WaitGroup`, etc. must never be copied.
2. **Buffer aliasing**: Copying `bytes.Buffer` causes the copy's slice to alias the original's internal array, leading to surprising behavior.
3. **Pointer receiver = non-copyable hint**: If a type's methods use `*T`, copying `T` by value is likely wrong.
4. **Use pointer types in APIs**: Take and return `*T` for structs with non-copyable fields.

# Construction / Recognition

**Bad -- copying a bytes.Buffer:**

```go
b1 := bytes.Buffer{}
b2 := b1
```

**Good -- struct with non-copyable field uses pointer throughout:**

```go
type Record struct {
    buf bytes.Buffer
    // other fields omitted
}

func New() *Record {...}

func (r *Record) Process(...) {...}

func Consumer(r *Record) {...}
```

**Bad -- value receiver and value parameter copy non-copyable field:**

```go
type Record struct {
    buf bytes.Buffer
    // other fields omitted
}

func (r Record) Process(...) {...} // Makes a copy of r.buf

func Consumer(r Record) {...} // Makes a copy of r.buf
```

# Context & Application

Value receivers on types with `sync.Mutex` fields silently copy the mutex, which can lead to unguarded concurrent access -- a data race that is invisible at the call site. The `bytes.Buffer` case is equally insidious: the copy appears to work but modifying one buffer can corrupt the other through the shared backing array. The `go vet` tool catches some of these issues, but the safest approach is to use pointer receivers and pointer parameters consistently for types with non-copyable internals.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **receiver-type**: Choosing pointer vs. value receivers is directly related to copy safety.
- **pass-values**: Complements this guidance by describing when passing by value is appropriate.

# Common Errors

1. Assigning a `sync.Mutex`-containing struct to another variable.
2. Using value receivers on types with `bytes.Buffer` or mutex fields.
3. Passing non-copyable structs by value to functions.

# Common Confusions

- **Value receivers hide the copy**: Calling a value-receiver method on a pointer still copies the value for the method call, which can silently copy a mutex.
- **Not just sync types**: Any type with internal pointers to shared state (e.g., `bytes.Buffer`) has copy-safety concerns.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Copying" section.

# Verification Notes

Confidence: high. All guidance and code examples are directly from the source text.
