---
concept: Maps as Sets
slug: maps-as-sets
category: data-structures
subcategory: maps
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Maps"
chapter_number: null
pdf_page: null
section: "Using Maps as Sets"
extraction_confidence: high
aliases:
  - "map-backed sets"
  - "sets version 2"
prerequisites:
  - maps-vs-records
extends: []
related:
  - maps-as-dictionaries
contrasts_with: []
answers_questions:
  - "How can maps be used to implement sets in Erlang?"
  - "When are map-backed sets not the best choice?"
---

# Quick Definition

Starting in OTP 24, the `sets` module can represent sets as maps (version 2). Map-backed sets are generally the most efficient set representation, with exceptions for intersection-heavy workloads where `ordsets` or `gb_sets` may be better.

# Core Definition

The Efficiency Guide describes map-backed sets (Maps chapter, "Using Maps as Sets" section): "Starting in OTP 24, the `sets` module has an option to represent sets as maps." Sets are created with `sets:new([{version,2}])` or `sets:from_list(List, [{version,2}])`, producing maps where elements are keys mapped to empty lists.

Map-backed `sets` is "generally the most efficient set representation," with three exceptions:

1. `ordsets:intersection/2` can be more efficient than `sets:intersection/2` when intersection is frequent and single-element operations are avoided
2. `gb_sets` can be better when both intersection and single-element operations must be efficient
3. Integer sets in a compact range can use bitwise operations (`bor` for union, `band` for intersection) on an integer representation

# Prerequisites

- **maps-vs-records** -- Understanding the map data structure underpinning this set representation

# Key Properties

1. Introduced in OTP 24 with `{version, 2}` option
2. Elements stored as map keys with empty list `[]` as values
3. Generally the most efficient set representation in Erlang
4. Intersection operations are the weak point compared to `ordsets` and `gb_sets`
5. `ordsets` intersection is more efficient when single-element operations (like `is_element/2`) are not needed
6. `gb_sets` is a compromise when both intersection and single-element operations matter
7. Bit-integer representation is optimal for compact integer ranges

# Construction / Recognition

## Creating Map-Backed Sets

1. Empty set: `sets:new([{version,2}])` produces `#{}`
2. From list: `sets:from_list([x,y,z], [{version,2}])` produces `#{x => [],y => [],z => []}`

## Recognizing When Alternatives Are Better

1. If intersection is the dominant operation and `is_element/2` is not needed: use `ordsets`
2. If both intersection and single-element operations are needed: consider `gb_sets`
3. If elements are integers in a compact range: use bitwise integer representation

# Context & Application

The `sets` module's version 2 representation replaced the older internal representation with maps, leveraging the efficient map implementation. This is significant because set operations are common in Erlang applications (e.g., tracking process groups, permission sets, feature flags).

The guidance highlights that while maps are excellent for most set operations, the intersection operation is a specific weakness. This is consistent with the note in the `maps:intersect/2` section that `ordsets:intersection/2` can outperform `maps:intersect/2`.

# Examples

**Creating map-backed sets** (Maps chapter):
```erlang
1> sets:new([{version,2}]).
#{}
2> sets:from_list([x,y,z], [{version,2}]).
#{x => [],y => [],z => []}
```

**Bitwise integer set** (Maps chapter): For integer elements in a compact range, union is `bor` and intersection is `band`.

# Relationships

## Related

- **maps-as-dictionaries** -- Sets and dictionaries are both map-based collections but with different usage patterns

# Common Errors

- **Error**: Using map-backed sets for intersection-heavy workloads without benchmarking
  **Correction**: Consider `ordsets` or `gb_sets` when intersection is the dominant operation

- **Error**: Forgetting the `{version, 2}` option and getting the old (less efficient) set representation
  **Correction**: Always pass `[{version,2}]` to `sets:new/1` or `sets:from_list/2` for map-backed sets

# Common Confusions

- **Confusion**: Thinking map-backed sets are always the best choice
  **Clarification**: They are generally best, but intersection-heavy workloads are a known exception

- **Confusion**: Believing the values in the map representation matter
  **Clarification**: The empty list `[]` values are implementation details; only the keys (set elements) are semantically significant

# Source Reference

Maps chapter, "Using Maps as Sets" section. Includes examples of set creation and discussion of when alternatives (`ordsets`, `gb_sets`, bitwise integers) are more efficient.

# Verification Notes

- Definition: Directly extracted from source section text
- Key Properties: All exception cases explicitly listed in source
- Examples: Directly from source code examples
- Confidence: HIGH -- explicit, well-structured guidance in official documentation
