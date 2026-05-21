---
concept: Map Syntax Efficiency
slug: map-syntax-efficiency
category: performance
subcategory: maps
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Maps"
chapter_number: null
pdf_page: null
section: "Using the Map Syntax"
extraction_confidence: high
aliases:
  - "map update syntax"
  - "map matching syntax"
  - ":= operator efficiency"
  - "=> operator efficiency"
prerequisites:
  - small-map-implementation
extends: []
related:
  - maps-as-alternative-to-records
  - maps-module-functions
contrasts_with: []
answers_questions:
  - "How does `maps:get/2` compare to map matching syntax for efficiency?"
  - "What distinguishes `maps:update/3` from `maps:put/3`?"
  - "What distinguishes the `:=` operator from the `=>` operator in map updates?"
---

# Quick Definition

Map syntax (matching and updating with `#{}`) is usually slightly more efficient than the corresponding `maps` module functions. The efficiency gain is most significant when matching or updating multiple literal keys at once on small maps, where the operation is essentially constant-time.

# Core Definition

The Efficiency Guide states (Maps chapter, "Using the Map Syntax" section): "Using the map syntax is usually slightly more efficient than using the corresponding function in the `maps` module."

The gain is most noticeable for three operations achievable only with map syntax:

1. **Matching multiple literal keys** in one expression
2. **Updating multiple literal keys** in one expression
3. **Adding multiple literal keys** to a map in one expression

For small maps with compile-time constant keys, these multi-element operations run in essentially constant time. The `:=` operator is slightly more efficient than `=>` for small maps because it knows the key already exists and does not need to check for a new key insertion.

With variable keys, the compiler must rewrite multi-element updates to sequential single-element updates (left to right) because keys could be identical.

# Prerequisites

- **small-map-implementation** -- Understanding why multi-element operations on small maps are constant-time

# Key Properties

1. Map syntax is slightly more efficient than `maps` module functions
2. Multi-element operations with literal keys are essentially constant-time for small maps
3. `:=` is slightly more efficient than `=>` for small maps (key known to exist)
4. Variable keys force sequential left-to-right updates (keys could be identical)
5. The compiler rewrites `Map#{Key1 := X, Key2 := Y}` (variable keys) into sequential updates
6. The efficiency advantage is less noticeable for large maps
7. For large maps, multi-element operations have execution time proportional to the number of elements

# Construction / Recognition

## Applying Efficient Map Syntax

1. Use multi-element matching: `#{key1 := V1, key2 := V2} = Map`
2. Use multi-element updating: `Map#{key1 := V1, key2 := V2}`
3. Prefer `:=` over `=>` when the key is known to exist
4. Use literal keys (atoms, integers) rather than variables when possible

## Recognizing Compiler Rewrites

Variable key updates are rewritten by the compiler:
```erlang
%% This:
Map = Map1#{Key1 := X, Key2 := Y, Key3 := Z}
%% Becomes:
Map2 = Map1#{Key1 := X},
Map3 = Map2#{Key2 := Y},
Map = Map3#{Key3 := Z}
```

# Context & Application

Map syntax efficiency is a compiler-level optimization. The compiler can analyze map expressions with literal keys and generate optimized code that performs all updates in a single operation. This is analogous to how the compiler optimizes binary construction -- compile-time knowledge enables batch operations.

For the record-replacement use case, this optimization is critical: updating three fields at once is about three times faster than three sequential `maps:update/3` calls for small maps.

For the dictionary use case (where keys are typically variables), the optimization matters less because the compiler cannot determine if keys are distinct.

# Examples

**DO -- Multi-element update with literal keys** (Maps chapter):
```erlang
Map = Map1#{x := X, y := Y, z := Z}
```

**DO NOT -- Sequential maps:update/3 calls** (Maps chapter):
```erlang
Map2 = maps:update(x, X, Map1),
Map3 = maps:update(y, Y, Map2),
Map = maps:update(z, Z, Map3)
```

"If the map is a small map, the first example runs roughly three times as fast."

**Variable key rewrite** (Maps chapter):
```erlang
%% Variable keys -- compiler rewrites to sequential updates:
Map = Map1#{Key1 := X, Key2 := Y, Key3 := Z}
%% Becomes:
Map2 = Map1#{Key1 := X},
Map3 = Map2#{Key2 := Y},
Map = Map3#{Key3 := Z}
```

# Relationships

## Related

- **maps-as-alternative-to-records** -- Record-replacement usage benefits most from map syntax efficiency
- **maps-module-functions** -- Functions that are sometimes less efficient than map syntax equivalents

## Enables

- **maps-as-alternative-to-records** -- The efficiency of map syntax with literal keys is what makes record replacement practical

# Common Errors

- **Error**: Using `=>` to update an existing key, losing the slight efficiency of `:=`
  **Correction**: Use `:=` when the key is known to exist; it is both more efficient and provides a runtime check

- **Error**: Assuming multi-element syntax with variable keys is optimized as a single operation
  **Correction**: Variable keys are rewritten to sequential single-element updates by the compiler

# Common Confusions

- **Confusion**: Thinking `:=` and `=>` differ only in error behavior (`:=` requires key exists, `=>` does not)
  **Clarification**: They also differ in performance; `:=` is slightly more efficient for small maps because the runtime can skip the check for key insertion

- **Confusion**: Believing map syntax is always dramatically faster than `maps` module functions
  **Clarification**: The gain is "usually slightly more efficient"; the dramatic advantage (roughly 3x) only appears for multi-element operations with literal keys on small maps

- **Confusion**: Thinking that large maps benefit equally from multi-element syntax
  **Clarification**: For large maps, execution time is "roughly proportional to the number of elements matched or updated" -- the constant-time advantage is specific to small maps

# Source Reference

Maps chapter, "Using the Map Syntax" section. Includes DO/DO NOT code examples, the "roughly three times as fast" benchmark, and the variable key rewrite explanation.

# Verification Notes

- Definition: Directly extracted from the opening of the "Using the Map Syntax" section
- Three operations: Listed verbatim from the source bulleted list
- "Roughly three times as fast": Direct quote from source
- Variable key rewrite: Code example directly from source
- `:=` vs `=>`: Statement from source section
- Confidence: HIGH -- explicit performance comparisons with specific benchmarks in official documentation
