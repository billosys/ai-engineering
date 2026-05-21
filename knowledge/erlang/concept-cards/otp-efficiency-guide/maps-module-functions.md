---
concept: Maps Module Functions
slug: maps-module-functions
category: compiler-optimization
subcategory: maps
tier: advanced
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Maps"
chapter_number: null
pdf_page: null
section: "Using the Functions in the maps Module"
extraction_confidence: high
aliases:
  - "maps module efficiency"
  - "maps module implementation"
prerequisites:
  - map-syntax-efficiency
  - small-map-implementation
extends:
  - map-syntax-efficiency
related:
  - maps-as-alternative-to-records
  - maps-as-dictionaries
contrasts_with: []
answers_questions:
  - "How does `maps:get/2` compare to map matching syntax for efficiency?"
  - "What distinguishes `maps:update/3` from `maps:put/3`?"
---

# Quick Definition

The `maps` module functions are implemented in either C (fast, hard to beat) or Erlang (potentially improvable for specific use cases). The compiler rewrites several functions (`maps:get/2`, `maps:get/3`, `maps:is_key/2`, `maps:size/1`, `maps:put/3`) into more efficient forms.

# Core Definition

The Efficiency Guide provides implementation details for most `maps` module functions (Maps chapter, "Using the Functions in the maps Module" section). The key distinction is whether each function is implemented in C or Erlang:

- **C-implemented functions** are "pretty much impossible to implement more efficiently in Erlang": `maps:find/2`, `maps:from_list/1`, `maps:from_keys/2`, `maps:merge/2`, `maps:put/3`, `maps:remove/2`, `maps:take/2`, `maps:update/3`, `maps:keys/1`, `maps:values/1`, `maps:to_list/1`
- **Erlang-implemented functions** "are generally implemented in a way that attempts to make the performance reasonable for all possible inputs" and may be beatable for specific workloads: `maps:filter/2`, `maps:filtermap/2`, `maps:map/2`, `maps:merge_with/3`, `maps:with/2`, `maps:without/2`, `maps:intersect/2`, `maps:intersect_with/3`
- **Mixed C/Erlang**: `maps:iterator/1`, `maps:next/1`

Several functions are rewritten by the compiler:
- `maps:get/2` -> `map_get/2` guard BIF (similar performance to map matching)
- `maps:get/3` -> inline `case` expression with map matching (since OTP 26.0)
- `maps:is_key/2` -> `is_map_key/2` guard BIF
- `maps:size/1` -> `map_size/1` guard BIF
- `maps:new/0` -> `#{}` syntax
- `maps:put/3` -> map update syntax when the argument is known to be a map (since OTP 28)

# Prerequisites

- **map-syntax-efficiency** -- Understanding why map syntax is the baseline for comparison
- **small-map-implementation** -- Understanding flatmap vs. HAMT affects which optimizations matter

# Key Properties

1. C-implemented functions cannot be beaten in pure Erlang
2. Erlang-implemented functions use `maps:from_list/1` to construct results, potentially improvable
3. `maps:get/2` is rewritten to a guard BIF, achieving performance similar to map matching
4. `maps:get/3` is rewritten to an inline case expression (OTP 26.0+), no longer traceable
5. `maps:put/3` is rewritten to map syntax when the compiler knows the argument is a map (OTP 28+)
6. Multiple `maps:put/3` calls can be combined into a single multi-key update expression
7. `maps:update/3` (C) is slightly more efficient than `maps:put/3` (C) when the key is known to exist
8. `maps:filter/2` creates a new map via `maps:from_list/1`; using `maps:remove/2` can be more efficient when few values are removed
9. `maps:map/2` creates a new map via `maps:from_list/1`; using `maps:update/3` for changed values only can be more efficient
10. `maps:merge/2` (C) can share key tuples with argument maps for small maps (OTP 26.0+)

# Construction / Recognition

## Choosing Between maps Functions and Map Syntax

1. For compile-time literal keys with small maps: always prefer map syntax
2. For `maps:get/2`: performance is similar to map matching (compiler rewrites it), but multi-key matching is still more efficient
3. For `maps:put/3`: compiler may rewrite and combine calls (OTP 28+), but explicit map syntax is still preferred
4. For `maps:update/3`: prefer `:=` syntax for multiple updates; single update is equivalent
5. For Erlang-implemented functions: consider custom implementations when workload has specific patterns (e.g., few removals for filter, few changes for map)

## maps:put/3 Compiler Rewrite Example

```erlang
%% Given (when Map0 is known to be a map):
add_to_known_map(Map0, A, B, C) when is_map(Map0) ->
    Map1 = maps:put(a, A, Map0),
    Map2 = maps:put(b, B, Map1),
    maps:put(c, C, Map2).

%% Compiler rewrites to:
add_to_known_map(Map0, A, B, C) when is_map(Map0) ->
    Map0#{a => A, b => B, c => C}.
```

# Context & Application

Understanding which `maps` functions are implemented in C vs. Erlang helps developers make informed choices about when to use the module directly versus writing custom implementations. The compiler rewrites are particularly important because they mean that idiomatic Erlang code using `maps:get/2` is automatically optimized.

The implementation details "can change in the future" (noted in the source), so this is best used as guidance for understanding current performance characteristics rather than as permanent optimization rules.

# Examples

**maps:get/2 rewrite** (Maps chapter): The compiler rewrites `maps:get(Key, Map)` to `map_get(Key, Map)`, a guard BIF. Performance is similar to `#{Key := Value} = Map`.

**maps:put/3 rewrite** (Maps chapter):
```erlang
%% When Map0 is not proven to be a map, first call is kept:
add_to_map(Map0, A, B, C) ->
    Map1 = maps:put(a, A, Map0),
    Map1#{b => B, c => C}.
```

**maps:filter/2 optimization** (Maps chapter): If only a minority of values will be removed, use `maps:remove/2` directly instead of `maps:filter/2` (which rebuilds from a list).

**maps:map/2 optimization** (Maps chapter): If only 1% of values change, update only the changed values with `maps:update/3` instead of rebuilding the entire map.

**maps:merge/2 key sharing** (Maps chapter): For small maps, `maps:merge/2` can share the key tuple with an argument map if that argument contains all the keys (OTP 26.0+).

# Relationships

## Builds Upon

- **map-syntax-efficiency** -- Map syntax is the baseline; this card details when module functions approach or differ from that baseline

## Related

- **maps-as-alternative-to-records** -- Record-replacement usage should prefer syntax over module functions
- **maps-as-dictionaries** -- Dictionary usage has less difference between syntax and module

# Common Errors

- **Error**: Using `maps:filter/2` to remove a small number of elements from a large map
  **Correction**: Use `maps:remove/2` in a loop, which avoids rebuilding the entire map from a list

- **Error**: Using `maps:map/2` when only a few values change
  **Correction**: Use `maps:update/3` on the specific changed values to avoid full map reconstruction

- **Error**: Assuming `maps:get/2` is slower than map matching
  **Correction**: The compiler rewrites `maps:get/2` to a guard BIF; performance is similar (though multi-key matching is still more efficient)

# Common Confusions

- **Confusion**: Thinking all `maps` module functions are implemented in C and are equally fast
  **Clarification**: Several important functions (`filter/2`, `map/2`, `filtermap/2`) are implemented in Erlang and may be suboptimal for specific workloads

- **Confusion**: Believing `maps:put/3` and `maps:update/3` are interchangeable
  **Clarification**: `maps:update/3` is slightly more efficient when the key is known to exist (it raises an error if the key is missing); `maps:put/3` inserts or updates

- **Confusion**: Thinking `maps:get/3` (with default) is as efficient as `maps:get/2`
  **Clarification**: `maps:get/3` is rewritten to a case expression (OTP 26.0+), which is reasonable but using defaults prevents key sharing in small maps

# Source Reference

Maps chapter, "Using the Functions in the maps Module" section. Covers individual function notes for: `filter/2`, `filtermap/2`, `find/2`, `get/2`, `get/3`, `intersect/2`, `intersect_with/3`, `from_list/1`, `from_keys/2`, `is_key/2`, `iterator/1`, `keys/1`, `map/2`, `merge/2`, `merge_with/3`, `new/0`, `next/1`, `put/3`, `remove/2`, `size/1`, `take/2`, `to_list/1`, `update/3`, `values/1`, `with/2`, `without/2`.

# Verification Notes

- Definition: Synthesized from the per-function notes in the source section
- C vs. Erlang classification: Each function's implementation language is explicitly stated in the source
- Compiler rewrites: Each rewrite is explicitly described in the source
- OTP version notes: OTP 26.0 and OTP 28 changes are explicitly noted in the source
- Confidence: HIGH -- implementation details are explicitly stated per function in official documentation
- Note: Source warns these implementation details "can change in the future"
