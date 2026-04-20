---
# === CORE IDENTIFICATION ===
concept: Prefer Specifying Container Capacity
slug: prefer-specifying-container-capacity

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
section: "Prefer Specifying Container Capacity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "map capacity hints"
  - "slice capacity preallocation"
  - "make with capacity"
  - "container preallocation"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - prefer-strconv-over-fmt
  - avoid-repeated-string-to-byte-conversions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do map capacity hints differ from slice capacity specification?"
  - "Why should I specify capacity when creating maps and slices?"
  - "What is the performance impact of not preallocating container capacity?"
---

# Quick Definition

Specify container capacity where possible when using `make()` for maps and slices. This allocates memory up front, minimizing subsequent allocations from resizing as elements are added.

# Core Definition

Go's `make()` function accepts optional capacity parameters for maps and slices. Providing these capacity values reduces the number of dynamic allocations needed as elements are added to the container. The guide distinguishes between two cases:

**Map capacity hints** (`make(map[T1]T2, hint)`): The hint approximates the number of hashmap buckets required. It does not guarantee complete preemptive allocation -- allocations may still occur when adding elements, even up to the specified capacity. Map hints are advisory.

**Slice capacity** (`make([]T, length, capacity)`): Unlike maps, slice capacity is exact. The compiler allocates enough memory for the specified capacity. Subsequent `append()` operations incur zero allocations until the length reaches the capacity, after which a resize is required.

# Prerequisites

Understanding of Go's `make()` function, slice mechanics (length vs. capacity), and map internals at a basic level.

# Key Properties

1. **Map hints are approximate** -- Map capacity hints right-size the initial hashmap bucket allocation but do not guarantee zero allocations during element insertion.
2. **Slice capacity is exact** -- Slice capacity guarantees zero allocations for `append()` calls until length equals capacity.
3. **~12x speed improvement for slices** -- Benchmarks show preallocated slices at 0.21s vs non-preallocated at 2.48s for 100M iterations.
4. **Reduces GC pressure** -- Fewer allocations mean less work for the garbage collector.
5. **Use when size is known or estimable** -- The optimization is most effective when the final size is known or can be reasonably estimated.

# Construction / Recognition

## To Construct/Create:
1. For maps: `m := make(map[string]int, len(items))` when the number of items is known.
2. For slices: `s := make([]int, 0, len(items))` when appending a known number of items.
3. Use the length of an input collection as the capacity hint when transforming one collection into another.

## To Identify/Recognize:
1. Look for `make(map[K]V)` without a capacity hint when the approximate size is known.
2. Look for `make([]T, 0)` without a capacity argument when followed by a loop of `append()` calls with a known iteration count.

# Context & Application

- **Typical contexts**: Data transformation loops, building maps from slices, aggregation operations, ETL pipelines.
- **Common applications**: Converting a slice of objects into a lookup map, collecting results from a known number of operations, building response payloads.

# Examples

**Example 1** (source: Uber Go Style Guide, Ch 3): Map capacity hints:

Bad:
```go
files, _ := os.ReadDir("./files")

m := make(map[string]os.DirEntry)
for _, f := range files {
    m[f.Name()] = f
}
```

Good:
```go
files, _ := os.ReadDir("./files")

m := make(map[string]os.DirEntry, len(files))
for _, f := range files {
    m[f.Name()] = f
}
```

**Example 2** (source: Uber Go Style Guide, Ch 3): Slice capacity specification:

Bad:
```go
for n := 0; n < b.N; n++ {
  data := make([]int, 0)
  for k := 0; k < size; k++{
    data = append(data, k)
  }
}
```

```plain
BenchmarkBad-4    100000000    2.48s
```

Good:
```go
for n := 0; n < b.N; n++ {
  data := make([]int, 0, size)
  for k := 0; k < size; k++{
    data = append(data, k)
  }
}
```

```plain
BenchmarkGood-4   100000000    0.21s
```

# Relationships

- **Related to** `prefer-strconv-over-fmt`: All three Performance chapter concepts focus on reducing allocations in hot paths.
- **Related to** `avoid-repeated-string-to-byte-conversions`: Both optimize allocation patterns for better performance.

# Common Errors

1. **Omitting capacity when size is known** -- Creating `make([]T, 0)` inside a loop that appends a known number of elements wastes allocations on resizing.
2. **Treating map hints as guarantees** -- Unlike slices, map capacity hints do not guarantee zero allocations. Some allocation may still occur.
3. **Using length instead of capacity for slices** -- `make([]T, size)` creates a slice with `size` zero-valued elements (length = size). Use `make([]T, 0, size)` when you intend to `append()`.

# Common Confusions

1. **Map capacity hints vs. slice capacity** -- Map hints are approximate and advisory; slice capacity is exact and guaranteed. This is the key difference between the two.
2. **Length vs. capacity in make()** -- `make([]T, length, capacity)` has two meanings: `length` is the number of initialized elements, `capacity` is the allocated backing array size. For "append-style" usage, use length 0 with the desired capacity.

# Source Reference

- Source: "Uber Go Style Guide"
- Chapter: "Performance" (Ch 3)
- Section: "Prefer Specifying Container Capacity"

# Verification Notes

- Extraction confidence: high -- Explicitly defined section with benchmark data, separate sub-sections for maps and slices, and clear Bad/Good examples.
