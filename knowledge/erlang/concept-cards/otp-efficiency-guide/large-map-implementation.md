---
concept: Large Map Implementation
slug: large-map-implementation
category: data-structures
subcategory: maps
tier: advanced
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Maps"
chapter_number: null
pdf_page: null
section: "How Large Maps are Implemented"
extraction_confidence: high
aliases:
  - "HAMT"
  - "Hash array mapped trie"
  - "large map"
prerequisites:
  - small-map-implementation
extends:
  - small-map-implementation
related:
  - maps-as-dictionaries
  - map-syntax-efficiency
contrasts_with:
  - small-map-implementation
answers_questions:
  - "What is the HAMT data structure used for large maps?"
  - "What is a small map vs. a large map?"
  - "What distinguishes a small map (flatmap) from a large map (HAMT)?"
---

# Quick Definition

A large map (more than 32 elements) is implemented as a Hash Array Mapped Trie (HAMT), a tree structure that provides efficient search and update regardless of map size. It has higher memory overhead than small maps and less effective key sharing.

# Core Definition

The Efficiency Guide states (Maps chapter, "How Large Maps are Implemented" section): "A map with more than 32 elements is implemented as a Hash array mapped trie (HAMT). A large map can be efficiently searched and updated regardless of the number of elements in the map."

Key differences from small maps:

- There is less performance gain from matching or updating multiple elements using map syntax; execution time is "roughly proportional to the number of elements matched or updated"
- Storage overhead is higher: "the extra number of words besides the keys and values is roughly proportional to the number of elements"
- A map with 33 elements has at least 53 heap words of overhead (compared to 5 for a small map)
- Updated maps share common parts of the HAMT with the original, but sharing is "never as effective as the best possible sharing of the key tuple for small maps"

# Prerequisites

- **small-map-implementation** -- Understanding the flatmap representation that large maps transition from

# Key Properties

1. Triggered when map grows beyond 32 elements
2. Implemented as a Hash Array Mapped Trie (HAMT)
3. Search and update are efficient regardless of element count (O(log N))
4. Multi-element matching/updating has execution time proportional to the number of elements (unlike constant-time for small maps)
5. Memory overhead is proportional to element count (not constant like small maps)
6. A 33-element map has at least 53 words of overhead (vs. 5 for a small map)
7. Updated maps share common HAMT subtrees with the original map
8. HAMT sharing is never as effective as key tuple sharing in small maps
9. Representation reverts to flatmap when map shrinks to 32 or fewer elements

# Construction / Recognition

## Avoiding Large Maps as Record Replacements

1. If many instances of a map will be created (record-like usage), keep element count at most 32
2. Group related elements into sub-maps to reduce the top-level element count
3. Example: Instead of a 40-element map, split into a map with sub-maps for logical groupings

## Recognizing Large Map Overhead

1. Count the elements; more than 32 means HAMT
2. Calculate overhead: roughly proportional to element count (use the formula from the Memory chapter)
3. Compare: 33 elements = at least 53 extra words; 32 elements = exactly 5 extra words

# Context & Application

The HAMT representation is optimized for the dictionary use case where maps may grow to arbitrary sizes. It provides O(log N) access, which is sufficient for general-purpose dictionary operations. However, the transition from flatmap to HAMT at 33 elements has significant implications for memory and performance.

The Efficiency Guide recommends that if maps are used as record replacements with many instances, developers should structure their data to stay within the 32-element threshold. Grouping related fields into sub-maps is the suggested approach.

The HAMT data structure is well-known in functional programming (used in Clojure, Scala, Haskell). It provides structural sharing -- updated trees share subtrees with the original -- but this sharing is inherently less space-efficient than the simple key tuple sharing of flatmaps.

# Examples

**Memory comparison** (Maps chapter):

- Small map (32 elements): 5 words overhead (constant)
- Large map (33 elements): at least 53 words overhead (proportional)

**Structural sharing** (Maps chapter): When a large map is updated, the updated map and the original share common parts of the HAMT. However, sharing "will never be as effective as the best possible sharing of the key tuple for small maps."

**Mitigation strategy** (Maps chapter): "if maps are used instead of records and it is expected that many instances of the map will be created, it is more efficient from a memory standpoint to avoid using large maps (for example, by grouping related map elements into sub maps to reduce the number of elements)."

# Relationships

## Builds Upon

- **small-map-implementation** -- Large maps are what small maps become when they exceed 32 elements

## Related

- **maps-as-dictionaries** -- Dictionary usage is the primary use case for large maps
- **map-syntax-efficiency** -- Map syntax optimizations are less impactful for large maps

## Contrasts With

- **small-map-implementation** -- Small maps have constant overhead, full key sharing, and constant-time multi-element operations; large maps have proportional overhead, partial structural sharing, and proportional-time operations

# Common Errors

- **Error**: Using a map with 33+ elements as a record replacement without considering the memory impact
  **Correction**: Restructure into a map with sub-maps, keeping the top-level map at most 32 elements

- **Error**: Assuming multi-element update syntax provides the same speedup for large maps as for small maps
  **Correction**: For large maps, multi-element operations take time proportional to the number of elements, not constant time

# Common Confusions

- **Confusion**: Thinking HAMT is inefficient because it uses more memory than flatmaps
  **Clarification**: HAMT is efficient for its purpose (arbitrary-size dictionaries with structural sharing); it is only less efficient than flatmaps for the specific use case of record replacement with many instances

- **Confusion**: Believing the transition from small to large map is gradual
  **Clarification**: The transition is abrupt at the 32-element threshold; a 32-element map is a flatmap, a 33-element map is a HAMT

- **Confusion**: Thinking large maps do not share any memory when updated
  **Clarification**: Updated HAMTs share common subtrees with the original; sharing is just less effective than flatmap key tuple sharing

# Source Reference

Maps chapter, "How Large Maps are Implemented" section. References the Memory chapter for the overhead formula. Links to the Wikipedia article on Hash Array Mapped Tries.

# Verification Notes

- Definition: Directly extracted from source section text
- Memory numbers (53 words for 33 elements, 5 words for small maps): Directly stated in source
- HAMT reference: Source links to Wikipedia article
- Structural sharing: Explicitly described in source
- Confidence: HIGH -- detailed implementation description in official documentation
