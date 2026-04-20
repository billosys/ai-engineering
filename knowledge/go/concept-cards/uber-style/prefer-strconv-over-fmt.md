---
# === CORE IDENTIFICATION ===
concept: Prefer strconv over fmt
slug: prefer-strconv-over-fmt

# === CLASSIFICATION ===
category: performance
subcategory: string-conversion
tier: intermediate

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton (and Uber Go team)"
chapter: "Performance"
chapter_number: 3
pdf_page: null
section: "Prefer strconv over fmt"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "strconv vs fmt"
  - "strconv.Itoa vs fmt.Sprint"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - avoid-repeated-string-to-byte-conversions
  - prefer-specifying-container-capacity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does strconv compare to fmt for string conversion performance?"
  - "Why is strconv faster than fmt for converting primitives to strings?"
  - "When should I use strconv instead of fmt?"
---

# Quick Definition

When converting primitives to/from strings, use `strconv` instead of `fmt` because `strconv` is significantly faster (roughly 2x) and allocates less memory.

# Core Definition

The `fmt` package uses reflection to determine types at runtime, making it slower for simple type conversions. The `strconv` package provides type-specific conversion functions that avoid this overhead. On hot paths, preferring `strconv` over `fmt` can provide meaningful performance improvements.

This guidance applies specifically to the hot path -- performance-critical code that runs frequently.

# Prerequisites

Familiarity with Go's `fmt` and `strconv` standard library packages.

# Key Properties

1. **~2x speed improvement** -- Benchmarks show `strconv.Itoa` at ~64.2 ns/op vs `fmt.Sprint` at ~143 ns/op.
2. **Fewer allocations** -- `strconv.Itoa` requires 1 allocation vs 2 allocations for `fmt.Sprint`.
3. **No reflection** -- `strconv` functions are type-specific and avoid the reflection overhead of `fmt`.
4. **Hot path guidance** -- This optimization matters on hot paths; for infrequent conversions, readability may take priority.

# Construction / Recognition

## To Construct/Create:
1. Replace `fmt.Sprint(intVal)` with `strconv.Itoa(intVal)` for int-to-string conversion.
2. Replace `fmt.Sprintf("%d", intVal)` with `strconv.Itoa(intVal)`.
3. Use `strconv.FormatFloat`, `strconv.FormatBool`, etc. for other primitive types.

## To Identify/Recognize:
1. Look for `fmt.Sprint`, `fmt.Sprintf("%d", ...)`, `fmt.Sprintf("%v", ...)` calls on primitive types.
2. Check if these appear in hot paths (loops, request handlers, serialization code).

# Context & Application

- **Typical contexts**: High-throughput request handling, serialization code, logging on hot paths, data processing loops.
- **Common applications**: Converting IDs to strings for map keys, building query parameters, formatting numeric output in tight loops.

# Examples

**Example 1** (source: Uber Go Style Guide, Ch 3):

Bad:
```go
for i := 0; i < b.N; i++ {
  s := fmt.Sprint(rand.Int())
}
```

```plain
BenchmarkFmtSprint-4    143 ns/op    2 allocs/op
```

Good:
```go
for i := 0; i < b.N; i++ {
  s := strconv.Itoa(rand.Int())
}
```

```plain
BenchmarkStrconv-4    64.2 ns/op    1 allocs/op
```

# Relationships

- **Related to** `avoid-repeated-string-to-byte-conversions`: Both are hot-path performance optimizations that reduce allocations and conversion overhead.
- **Related to** `prefer-specifying-container-capacity`: All three concepts are part of the Performance chapter's guidance on reducing allocations.

# Common Errors

1. **Using fmt.Sprintf for simple int-to-string** -- `fmt.Sprintf("%d", n)` is slower than `strconv.Itoa(n)` and provides no formatting advantage for simple cases.
2. **Premature optimization on cold paths** -- Applying this guidance to code that runs infrequently adds no meaningful benefit.

# Common Confusions

1. **"Always use strconv"** vs. **"Prefer strconv on hot paths"** -- The guidance is specifically for performance-sensitive code. For complex formatting with multiple values, `fmt.Sprintf` remains the right tool.
2. **strconv vs. fmt capability** -- `strconv` handles primitive-to-string and string-to-primitive conversions. `fmt` handles arbitrary formatting with format verbs, multiple arguments, and custom formatters. They serve different purposes.

# Source Reference

- Source: "Uber Go Style Guide"
- Chapter: "Performance" (Ch 3)
- Section: "Prefer strconv over fmt"

# Verification Notes

- Extraction confidence: high -- Explicitly defined section with benchmark data and clear Bad/Good examples.
