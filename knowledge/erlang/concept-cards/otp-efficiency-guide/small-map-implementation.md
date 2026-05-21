---
concept: Small Map Implementation
slug: small-map-implementation
category: performance
subcategory: maps
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Maps"
chapter_number: null
pdf_page: null
section: "How Small Maps are Implemented"
extraction_confidence: high
aliases:
  - "flatmap"
  - "flat map"
  - "small map"
  - "compact map representation"
prerequisites:
  - maps-vs-records
extends: []
related:
  - maps-as-alternative-to-records
  - map-syntax-efficiency
contrasts_with:
  - large-map-implementation
answers_questions:
  - "What is a small map vs. a large map?"
  - "What distinguishes a small map (flatmap) from a large map (HAMT)?"
  - "How does the small map key tuple sharing work?"
---

# Quick Definition

A small map (at most 32 elements) is internally represented as a "flatmap" -- a compact structure with a shared key tuple and a flat array of values. This representation enables key tuple sharing between map instances, making it memory-efficient and suitable as a record alternative.

# Core Definition

The Efficiency Guide describes the small map representation (Maps chapter, "How Small Maps are Implemented" section):

A small map is stored as: `[FLATMAP | N | Keys | Value1 | ... | ValueN]`

- **FLATMAP**: Tag identifying a small map (called "flat map" in the runtime system source code)
- **N**: Number of elements
- **Keys**: A tuple `{Key1,...,KeyN}` with keys sorted
- **Value1...ValueN**: Values corresponding to each key in the key tuple

The critical property is that the key tuple can be shared between multiple map instances that have the same keys. When a value is updated with `:=`, the key tuple is not copied -- only the values change. If maps are created via a constructor function, the key tuple becomes a global literal shared across all instances.

Memory size: keys + values + 5 words overhead (regardless of element count, up to 32).

# Prerequisites

- **maps-vs-records** -- Understanding why small maps are compared to records

# Key Properties

1. Maximum 32 elements; exceeding 32 triggers conversion to HAMT (large map)
2. Keys are stored in a sorted tuple, separate from values
3. Key tuple can be shared across all map instances with the same keys
4. Value updates via `:=` do not copy the key tuple
5. Constructor functions produce global literal key tuples, maximizing sharing
6. Matching or updating multiple literal keys is essentially constant-time (one operation)
7. With variable keys, operations must be performed sequentially (keys could be identical)
8. Memory overhead is exactly 5 words plus the size of all keys and values
9. The 5-word overhead is constant regardless of element count (up to 32)

# Construction / Recognition

## Creating Maps That Maximize Key Sharing

1. Define a constructor function:
   ```erlang
   new() ->
       #{a => default, b => default, c => default}.
   ```
2. The key tuple `{a,b,c}` becomes a global literal
3. Create instances by calling the constructor and updating:
   ```erlang
   (my_module:new())#{a := 42}.
   ```
4. The key tuple is shared, not copied

## Recognizing Small vs. Large Maps

1. Count the elements: at most 32 means small map
2. More than 32 means conversion to HAMT (large map)
3. The transition also occurs in reverse: shrinking to 32 or fewer converts back to flatmap

# Context & Application

The flatmap representation is what makes maps a viable alternative to records. The key tuple sharing means that thousands of map instances with the same keys (e.g., representing the same record type) share a single key tuple in memory, similar to how record definitions share their structure at compile time.

The 32-element threshold is a design choice in the BEAM runtime. Below this threshold, the flat representation with sorted keys allows efficient sequential search. Above it, the HAMT tree structure provides O(log N) access.

# Examples

**Map representation** (Maps chapter):

`#{a => foo, z => bar}` is represented as:

| FLATMAP | 2 | `{a,z}` | `foo` | `bar` |

After `M#{q => baz}`:

| FLATMAP | 3 | `{a,q,z}` | `foo` | `baz` | `bar` |

After `M#{z := bird}` -- note the key tuple `{a,q,z}` is unchanged:

| FLATMAP | 3 | `{a,q,z}` | `foo` | `baz` | `bird` |

**Key sharing via constructor** (Maps chapter):
```erlang
new() ->
    #{a => default, b => default, c => default}.

%% Key tuple {a,b,c} is a global literal, shared by all instances:
(SOME_MODULE:new())#{a := 42}.
```

# Relationships

## Related

- **maps-as-alternative-to-records** -- Relies on small map properties for efficient record replacement
- **map-syntax-efficiency** -- Map syntax optimizations are most impactful for small maps

## Contrasts With

- **large-map-implementation** -- HAMT representation used when maps exceed 32 elements; different memory and performance characteristics

# Common Errors

- **Error**: Creating maps with more than 32 elements when using them as record replacements
  **Correction**: Keep maps at most 32 elements; group related elements into sub-maps if needed

- **Error**: Creating map instances without a shared constructor function
  **Correction**: Define a single constructor function so the key tuple becomes a global literal

# Common Confusions

- **Confusion**: Thinking the 32-element limit is configurable or a soft guideline
  **Clarification**: The threshold of 32 is hardcoded in the runtime system; exceeding it changes the internal representation

- **Confusion**: Believing that `:=` and `=>` updates have the same effect on key sharing
  **Clarification**: `:=` guarantees the key exists, so the key tuple is never modified; `=>` may add a new key, creating a new key tuple

- **Confusion**: Thinking all small maps with the same keys automatically share key tuples
  **Clarification**: Sharing requires that the maps be created from the same literal or constructor; independently constructed maps may have separate (but equal) key tuples

# Source Reference

Maps chapter, "How Small Maps are Implemented" section. Includes table diagrams of the flatmap layout, constructor pattern examples, and memory size formula. Cross-references the Memory chapter for detailed memory calculations.

# Verification Notes

- Definition: Directly extracted from the table and text in the "How Small Maps are Implemented" section
- Key tuple sharing: Explicitly described with code examples in source
- Memory formula (5 words overhead): Stated directly in source
- 32-element threshold: Defined in the terminology section at the chapter's start
- Confidence: HIGH -- detailed implementation description with diagrams in official documentation
