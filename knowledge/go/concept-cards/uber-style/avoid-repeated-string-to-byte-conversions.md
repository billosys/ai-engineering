---
# === CORE IDENTIFICATION ===
concept: Avoid Repeated String-to-Byte Conversions
slug: avoid-repeated-string-to-byte-conversions

# === CLASSIFICATION ===
category: performance
subcategory: allocation-reduction
tier: intermediate

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton (and Uber Go team)"
chapter: "Performance"
chapter_number: 3
pdf_page: null
section: "Avoid repeated string-to-byte conversions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "cache byte slice conversion"
  - "string to byte slice reuse"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - prefer-strconv-over-fmt
  - prefer-specifying-container-capacity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why should I avoid converting a string to []byte repeatedly?"
  - "How much does repeated string-to-byte conversion cost?"
  - "How do I reuse a byte slice converted from a string?"
---

# Quick Definition

Do not create byte slices from a fixed string repeatedly in a loop. Perform the conversion once, capture the result in a variable, and reuse it.

# Core Definition

In Go, converting a string to `[]byte` allocates a new byte slice and copies the string data each time. When this conversion happens inside a loop with a fixed string, each iteration pays the allocation and copy cost unnecessarily. Instead, perform the conversion once before the loop and reuse the resulting byte slice.

This guidance applies specifically to hot paths -- performance-critical code where the same string is converted to bytes repeatedly.

# Prerequisites

Understanding of Go's string and `[]byte` types and the fact that `[]byte(str)` allocates a new slice each time.

# Key Properties

1. **~7x speed improvement** -- Benchmarks show the good pattern at ~3.25 ns/op vs the bad pattern at ~22.2 ns/op.
2. **Allocation elimination** -- Converting once and reusing eliminates per-iteration allocations.
3. **Fixed string requirement** -- This optimization applies when the string value does not change between iterations.
4. **Hot path guidance** -- This is a performance optimization for frequently executed code paths.

# Construction / Recognition

## To Construct/Create:
1. Identify `[]byte("constant string")` conversions inside loops.
2. Move the conversion before the loop: `data := []byte("constant string")`.
3. Use the `data` variable inside the loop.

## To Identify/Recognize:
1. Look for `[]byte(stringLiteral)` or `[]byte(stringVar)` inside loops where the string does not change.
2. Profile allocations in hot paths -- repeated string-to-byte conversions will show up as allocation hotspots.

# Context & Application

- **Typical contexts**: Writing to `io.Writer` in loops, sending repeated messages, benchmark code, high-throughput data processing.
- **Common applications**: HTTP response writing, log output, protocol message construction.

# Examples

**Example 1** (source: Uber Go Style Guide, Ch 3):

Bad:
```go
for i := 0; i < b.N; i++ {
  w.Write([]byte("Hello world"))
}
```

```plain
BenchmarkBad-4   50000000   22.2 ns/op
```

Good:
```go
data := []byte("Hello world")
for i := 0; i < b.N; i++ {
  w.Write(data)
}
```

```plain
BenchmarkGood-4  500000000   3.25 ns/op
```

# Relationships

- **Related to** `prefer-strconv-over-fmt`: Both are performance optimizations that reduce unnecessary allocations on hot paths.
- **Related to** `prefer-specifying-container-capacity`: All three concepts are part of the Performance chapter's guidance on reducing allocations.

# Common Errors

1. **Converting inside tight loops** -- The most common mistake is placing `[]byte("...")` inside a `for` loop when the string is constant.
2. **Not recognizing variable strings** -- If the string changes each iteration, the conversion must happen inside the loop. This optimization only applies to fixed strings.

# Common Confusions

1. **"Strings are immutable so conversion should be free"** -- While strings are immutable in Go, converting to `[]byte` must allocate a new mutable slice and copy the data. This is by design to prevent aliasing between the immutable string and the mutable byte slice.
2. **Compiler optimization** -- In some cases the Go compiler can optimize away the allocation (e.g., when the byte slice is used immediately and not retained), but this should not be relied upon in performance-critical code.

# Source Reference

- Source: "Uber Go Style Guide"
- Chapter: "Performance" (Ch 3)
- Section: "Avoid repeated string-to-byte conversions"

# Verification Notes

- Extraction confidence: high -- Explicitly defined section with benchmark data and clear Bad/Good examples.
