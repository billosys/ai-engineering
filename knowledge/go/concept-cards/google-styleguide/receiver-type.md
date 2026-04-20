---
concept: Receiver Type
slug: receiver-type
category: language
subcategory: method-design
tier: intermediate
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Receiver type"
extraction_confidence: high
aliases:
  - value receiver vs pointer receiver
  - method receiver choice
prerequisites:
  - go-method-basics
  - copying-decisions
related:
  - pass-values
  - interfaces-decisions
contrasts_with: []
answers_questions:
  - "When should Go methods use pointer receivers?"
  - "When should Go methods use value receivers?"
  - "Should all methods on a type use the same receiver type?"
---

# Quick Definition

Use pointer receivers when the method mutates the receiver, when the type contains non-copyable fields (e.g., `sync.Mutex`), or when the type is large. Use value receivers for small immutable types, built-in types, maps, functions, and channels. When in doubt, use a pointer receiver. Prefer consistency: make all methods on a type either pointer or value receivers.

# Core Definition

> "Correctness wins over speed or simplicity. There are cases where you must use a pointer value. In other cases, pick pointers for large types or as future-proofing if you don't have a good sense of how the code will grow, and use values for simple plain old data." -- Google Go Style Guide, "Receiver type"

> "As a general guideline, prefer to make the methods for a type either all pointer methods or all value methods." -- Google Go Style Guide, "Receiver type"

# Prerequisites

- Understanding of Go method sets and receiver types
- Knowledge of when types are safe to copy

# Key Properties

1. **Mutation requires pointer**: If the method modifies the receiver, use `*T`.
2. **Non-copyable fields require pointer**: Types with `sync.Mutex` or similar fields must use `*T`.
3. **Large types use pointer**: Passing a struct is like passing all its fields; if that is too much, use a pointer.
4. **Slices that don't reslice use value**: A slice receiver that only reads uses value (`func (b Buffer) Len() int`).
5. **Built-in types use value**: Integers, strings, etc. that do not need mutation use value receivers.
6. **Maps, functions, channels use value**: These are already reference types.
7. **Small immutable structs use value**: Types like `time.Time` are naturally value types.
8. **Concurrent modification**: Use value if concurrent modifications should not be visible to the method.
9. **Pointer elements hint at pointer receiver**: If struct fields are pointers to mutable data, use a pointer receiver.
10. **When in doubt, use pointer**: The default recommendation when unsure.

# Construction / Recognition

**Value receiver -- slice that doesn't reslice:**

```go
type Buffer []byte

func (b Buffer) Len() int { return len(b) }
```

**Pointer receiver -- mutation required:**

```go
type Counter int

func (c *Counter) Inc() { *c++ }
```

**Pointer receiver -- non-copyable field (sync.Mutex):**

```go
type Counter struct {
    mu    sync.Mutex
    total int
}

func (c *Counter) Inc() {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.total++
}
```

**Pointer receiver -- struct with mutable pointer field:**

```go
type Counter struct {
    m *Metric
}

func (c *Counter) Inc() {
    c.m.Add(1)
}
```

**Value receiver -- built-in type wrapper:**

```go
type User string

func (u User) String() { return string(u) }
```

**Value receiver -- map type:**

```go
type Header map[string][]string

func (h Header) Add(key, value string) { /* omitted */ }
```

**Value receiver -- small immutable struct:**

```go
type Time struct { /* omitted */ }

func (t Time) Add(d Duration) Time { /* omitted */ }
```

# Context & Application

The choice between pointer and value receivers affects not only correctness but also which interfaces a type satisfies. A value receiver method is in the method set of both `T` and `*T`, while a pointer receiver method is only in the method set of `*T`. This means a value type cannot satisfy an interface that requires a pointer-receiver method. The performance difference is usually negligible; profile before optimizing.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **pass-values**: Parallel guidance for function parameters.
- **copying-decisions**: Non-copyable types must use pointer receivers.
- **interfaces-decisions**: Receiver type affects which interfaces a type satisfies.

# Common Errors

1. Using value receivers on types with `sync.Mutex` fields.
2. Mixing pointer and value receivers on the same type without reason.
3. Using pointer receivers on maps, channels, or functions.
4. Choosing receiver type based on performance assumptions without benchmarks.

# Common Confusions

- **Performance is not the main concern**: The compiler can optimize both approaches. Focus on correctness and clarity.
- **Method set implications**: A `T` value cannot call `*T` methods through an interface, even though Go auto-takes the address for direct method calls.
- **Queue example**: `func (q *Queue) Push(x Item) { *q = append([]Item{x}, *q...) }` -- reslicing requires a pointer receiver.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Receiver type" section.

# Verification Notes

Confidence: high. All rules and code examples are directly from the source text.
