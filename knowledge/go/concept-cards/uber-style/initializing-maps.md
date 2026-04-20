---
concept: Initializing Maps
slug: initializing-maps
category: style
subcategory: initialization
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Initializing Maps"
extraction_confidence: high
aliases:
  - map initialization
  - "make(map) vs map literal"
prerequisites: []
extends: []
related:
  - initializing-structs
  - nil-is-a-valid-slice
contrasts_with: []
answers_questions:
  - "How do I initialize maps using make() vs. map literals?"
  - "What distinguishes `make(map)` from map literal initialization?"
  - "When should I use make() for maps vs map literals?"
---

# Quick Definition

Use `make()` for empty maps and maps populated programmatically; use map literals for maps with a fixed set of initial elements. This makes initialization visually distinct from declaration and allows adding size hints.

# Core Definition

The Uber Go Style Guide establishes a clear rule for map initialization: use `make(map[K]V)` for maps that start empty or are populated in a loop, and use map literals (`map[K]V{k1: v1, ...}`) for maps with a fixed, known set of elements at initialization time.

The key rationale is visual distinction: `make(map[T1]T2)` is visually distinct from a bare `var m map[T1]T2` declaration (which creates a nil map that panics on writes), while `map[T1]T2{}` looks confusingly similar to the declaration form.

# Prerequisites

- Understanding that a `var`-declared map is nil and panics on write operations
- Knowledge of `make()` built-in function

# Key Properties

1. **`make()` for empty/programmatic maps**: Visually distinct from nil map declaration; supports capacity hints.
2. **Map literals for fixed data**: When all elements are known at initialization, a literal is cleaner than sequential assignments.
3. **Visual distinction**: `make(map[T1]T2)` is clearly an initialization, while `map[T1]T2{}` looks similar to `map[T1]T2` (nil declaration).
4. **Capacity hints**: `make()` accepts an optional capacity hint for performance optimization.

# Construction / Recognition

**Good -- make() for empty maps:**

```go
var (
  // m1 is safe to read and write;
  // m2 will panic on writes.
  m1 = make(map[T1]T2)
  m2 map[T1]T2
)
```

**Bad -- empty literal for empty maps:**

```go
var (
  // m1 is safe to read and write;
  // m2 will panic on writes.
  m1 = map[T1]T2{}
  m2 map[T1]T2
)
```

**Good -- map literal for fixed data:**

```go
m := map[T1]T2{
  k1: v1,
  k2: v2,
  k3: v3,
}
```

**Bad -- make() with sequential assignment for fixed data:**

```go
m := make(map[T1]T2, 3)
m[k1] = v1
m[k2] = v2
m[k3] = v3
```

# Context & Application

This guideline applies to all map creation. The basic rule of thumb from the guide: "use map literals when adding a fixed set of elements at initialization time, otherwise use `make` (and specify a size hint if available)."

# Examples

See Construction / Recognition above for complete examples from the source.

# Relationships

- **initializing-structs**: Structs follow a parallel convention where `var` signals zero value and `T{...}` signals explicit initialization.
- **nil-is-a-valid-slice**: Slices have a similar nil vs empty distinction, but unlike maps, nil slices are safe to append to.

# Common Errors

1. Using `map[T1]T2{}` for empty maps -- visually confusing with nil map declaration.
2. Using `make()` with sequential assignments when a map literal would be cleaner for fixed data.
3. Forgetting that `var m map[T1]T2` creates a nil map that panics on write.

# Common Confusions

- **Nil map vs empty map**: A nil map (`var m map[K]V`) allows reads (returns zero values) but panics on writes. A `make`-created map is empty but safe for both reads and writes.
- **When to use capacity hints**: Provide a capacity hint to `make()` when you know the approximate number of elements to reduce rehashing. This is an optimization, not a requirement.

# Source Reference

Uber Go Style Guide, "Style" chapter, "Initializing Maps" section.

# Verification Notes

Confidence: high. The rules, rationale, and code examples are directly from the source text with explicit Bad/Good comparisons.
