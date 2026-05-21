---
concept: Maps as Alternative to Records
slug: maps-as-alternative-to-records
category: data-types
subcategory: maps
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Maps"
chapter_number: null
pdf_page: null
section: "Using Maps as an Alternative to Records"
extraction_confidence: high
aliases:
  - "maps as records"
  - "map-based records"
prerequisites:
  - maps-vs-records
  - small-map-implementation
extends:
  - maps-vs-records
related:
  - map-syntax-efficiency
  - maps-module-functions
contrasts_with: []
answers_questions:
  - "How do I efficiently use maps as an alternative to records?"
  - "What distinguishes the `:=` operator from the `=>` operator in map updates?"
---

# Quick Definition

When using maps as record replacements, follow specific practices: use map syntax (not the maps module), keep maps at most 32 elements, create maps with all keys upfront, always update with `:=`, and avoid default values.

# Core Definition

The Efficiency Guide provides a set of rules for using maps efficiently as record substitutes (Maps chapter, "Using Maps as an Alternative to Records" section):

1. Use the map syntax instead of `maps` module functions
2. Keep element count at most 32 (to remain a small/flat map)
3. Always create maps with all keys that will ever be used
4. Always update using the `:=` operator (requiring the key already exists)
5. Match and update multiple elements at once whenever possible
6. Avoid default values and `maps:get/3`
7. Use `maps:merge/2` to apply defaults when needed

These rules maximize key sharing between map instances and enable the compiler to optimize operations on small maps.

# Prerequisites

- **maps-vs-records** -- Understanding why maps might be chosen over records
- **small-map-implementation** -- Understanding the flat map representation explains why these rules matter (key tuple sharing, 32-element threshold)

# Key Properties

1. Map syntax (`:=`, `=>`) is more efficient than `maps` module functions for record-style usage
2. The `:=` operator is slightly more efficient than `=>` for small maps because it knows the key already exists
3. The `:=` operator also catches misspelled keys at runtime (raises an error if key is missing)
4. Creating maps with all keys upfront enables the key tuple to be shared as a global literal
5. Matching or updating multiple literal keys at once is essentially constant-time for small maps
6. Default values reduce key-sharing effectiveness and prevent multi-element matching
7. `maps:merge/2` can efficiently apply multiple default values at once

# Construction / Recognition

## Setting Up a Map as a Record Replacement

1. Define a constructor function that returns a map with all possible keys:
   ```erlang
   new() ->
       #{a => default, b => default, c => default}.
   ```
2. Always create instances by calling the constructor and updating:
   ```erlang
   (my_module:new())#{a := 42}.
   ```
3. Always update existing maps with `:=`:
   ```erlang
   Map#{field1 := Value1, field2 := Value2}.
   ```
4. When defaults are needed, use `maps:merge/2`:
   ```erlang
   DefaultMap = #{shoe_size => 42, editor => emacs},
   MapWithDefaults = maps:merge(DefaultMap, OtherMap).
   ```

# Context & Application

This pattern is the recommended approach when maps are chosen over records (e.g., for API boundaries or cross-application data). Following these rules keeps maps in the efficient small/flat map representation where key tuples can be shared across instances, mimicking the memory efficiency of records.

**Key insight**: The constructor function approach ensures the key tuple `{a,b,c}` becomes a global literal, shared across all instances. This is the most important optimization for memory efficiency.

# Examples

**DO -- Use `:=` for updates** (Maps chapter):
```erlang
Map = Map1#{x := X, y := Y, z := Z}
```

**DO NOT -- Use maps:update/3 sequentially** (Maps chapter):
```erlang
Map2 = maps:update(x, X, Map1),
Map3 = maps:update(y, Y, Map2),
Map = maps:update(z, Z, Map3)
```

The first example runs roughly three times as fast for small maps.

**Applying defaults with maps:merge/2** (Maps chapter):
```erlang
DefaultMap = #{shoe_size => 42, editor => emacs},
MapWithDefaultsApplied = maps:merge(DefaultMap, OtherMap)
```

# Relationships

## Builds Upon

- **maps-vs-records** -- This card provides the practical "how" after the "whether" decision
- **small-map-implementation** -- The 32-element limit and key sharing come from how flat maps work

## Related

- **map-syntax-efficiency** -- Detailed analysis of why map syntax is more efficient
- **maps-module-functions** -- When maps module functions are acceptable alternatives

# Common Errors

- **Error**: Creating a map without all keys upfront, then adding keys later with `=>`
  **Correction**: Always define all keys in the constructor function so the key tuple can be a shared global literal

- **Error**: Using `=>` when the key is known to exist
  **Correction**: Use `:=` for existing keys; it is slightly more efficient and catches misspelled keys

- **Error**: Using `maps:get/3` with defaults instead of storing all values in the map
  **Correction**: Store all values explicitly; use `maps:merge/2` if defaults are truly needed

# Common Confusions

- **Confusion**: Thinking the 32-element limit is a hard limit that causes errors
  **Clarification**: Maps with more than 32 elements still work but switch to the less efficient HAMT representation, losing key sharing and compact storage

- **Confusion**: Believing `maps:merge/2` is just syntactic sugar
  **Clarification**: `maps:merge/2` (implemented in C) can share key tuples with argument maps, making it an efficient way to apply defaults

# Source Reference

Maps chapter, "Using Maps as an Alternative to Records" section. Includes code examples for constructor pattern, `:=` usage, and `maps:merge/2` for defaults.

# Verification Notes

- Definition: All rules directly extracted from the bulleted list in the source section
- Key Properties: Items directly stated in source; property about `:=` efficiency from "Using the Map Syntax" section
- Examples: Directly from source DO/DO NOT patterns
- Confidence: HIGH -- explicit numbered/bulleted guidance in official documentation
