---
# === CORE IDENTIFICATION ===
concept: Size Hints (Best Practices)
slug: size-hints-bp

# === CLASSIFICATION ===
category: performance
subcategory: memory-allocation
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Size hints"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "capacity preallocation"
  - "make with capacity"
  - "slice preallocation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable-declarations-bp
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I provide capacity hints to make()?"
  - "Is preallocation always a good idea?"
  - "How do I size hints for maps and slices?"
---

# Quick Definition

Provide capacity hints to `make([]T, len, cap)` and `make(map[K]V, size)` when sizes are known from empirical analysis. Most code does not need preallocation. Preallocating too much can waste memory or harm performance.

# Core Definition

Size hints via `make` preallocate capacity for slices and maps, avoiding repeated reallocations during growth. This is important when combined with empirical analysis showing the code is performance-sensitive. However, most code does not need size hints and can let the runtime grow the data structure as needed. Preallocation is acceptable when the final size is known (e.g., converting between a map and a slice), but is not a readability requirement and may not be worth the clutter in small cases. Preallocating more memory than needed can waste memory fleet-wide or even harm performance. When in doubt, benchmark and default to zero initialization or composite literal declaration.

# Prerequisites

- **variable-declarations-bp** -- Understanding the three declaration forms

# Key Properties

1. Use `make([]T, 0, cap)` when the final slice capacity is known or can be estimated
2. Use `make(map[K]V, size)` when the number of map entries is known
3. Only preallocate when empirical analysis shows it matters
4. Most code does not need size hints
5. Over-preallocation wastes memory and can harm performance
6. When in doubt, benchmark first

# Construction / Recognition

## To Apply:
1. Profile and benchmark before adding size hints
2. Provide hints when sizes are known (e.g., `make([]byte, 131072)` for filesystem block sizes)
3. Comment why the size was chosen
4. Default to zero initialization if size impact is unclear

## To Recognize:
1. `make` calls with capacity arguments accompanied by comments explaining the sizing rationale
2. Size hints justified by profiling data, not guesswork

# Context & Application

Size hints are a performance optimization, not a readability requirement. They should be guided by profiling data. The standard pattern includes a comment explaining the reasoning: a preferred buffer size, a typical element count, or a shard size. Over-optimization without data can be counterproductive.

# Examples

**Example 1 -- Size hints with rationale**:

```go
// Good:
var (
    // Preferred buffer size for target filesystem: st_blksize.
    buf = make([]byte, 131072)
    // Typically process up to 8-10 elements per run (16 is a safe assumption).
    q = make([]Node, 0, 16)
    // Each shard processes shardSize (typically 32000+) elements.
    seen = make(map[string]bool, shardSize)
)
```

# Relationships

## Related
- **variable-declarations-bp** -- The broader context of variable declaration forms

## Contrasts With
(none)

# Common Errors

- **Error**: Preallocating large capacities without profiling data
  **Correction**: Benchmark first; over-preallocation wastes memory

- **Error**: Adding size hints to every make call
  **Correction**: Most code does not need preallocation; only add when profiling shows benefit

# Common Confusions

- **Confusion**: Thinking preallocation is always an improvement
  **Clarification**: Preallocating more than needed can waste memory or even harm performance

- **Confusion**: Treating size hints as a readability requirement
  **Clarification**: They are a performance optimization; zero initialization is the default

# Source Reference

Chapter 4: Best Practices, Section "Variable declarations" > "Size hints".

# Verification Notes

- Definition source: Directly from "Size hints" subsection of Variable declarations
- Confidence rationale: HIGH -- explicit guidance with examples and warnings
- Uncertainties: None
- Cross-reference status: References GoTip #3: Benchmarking Go Code
