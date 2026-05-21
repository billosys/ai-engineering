---
concept: Maps as Dictionaries
slug: maps-as-dictionaries
category: data-types
subcategory: maps
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Maps"
chapter_number: null
pdf_page: null
section: "Using Maps as Dictionaries"
extraction_confidence: high
aliases:
  - "map dictionary"
  - "dictionary maps"
prerequisites:
  - maps-vs-records
extends: []
related:
  - maps-as-alternative-to-records
  - maps-as-sets
  - large-map-implementation
contrasts_with:
  - maps-as-alternative-to-records
answers_questions:
  - "When should I use maps as dictionaries versus as record replacements?"
  - "What are the alternatives to maps for dictionary usage?"
---

# Quick Definition

Maps used as dictionaries have runtime-determined keys, arbitrary element counts, and typically single-element access patterns. In this usage, the performance difference between map syntax and the maps module is small, making the choice mostly a matter of taste.

# Core Definition

The Efficiency Guide defines the dictionary usage pattern for maps (Maps chapter, "Using Maps as Dictionaries" section):

- Keys are usually variables not known at compile-time
- There can be any number of elements in the map
- Usually, no more than one element is looked up or updated at once

Given this usage pattern, "the difference in performance between using the map syntax and the maps module is usually small." Maps are "usually the most efficient dictionary data structure," with two exceptions: `gb_trees` when frequent conversion to/from sorted lists is needed, and the `array` module when all keys are non-negative integers.

# Prerequisites

- **maps-vs-records** -- Understanding the basic map data structure and its comparison to records

# Key Properties

1. Keys are typically variables, not compile-time constants
2. Element count is unbounded (maps may be small or large)
3. Single-element lookups and updates are the common access pattern
4. Map syntax vs. maps module performance difference is negligible for this use case
5. Maps are the most efficient general-purpose dictionary in most cases
6. `gb_trees` is better when frequent sorted list conversions are needed
7. `array` module is better when all keys are non-negative integers

# Construction / Recognition

## Recognizing Dictionary Usage

1. Keys come from runtime data (user input, database, etc.), not hardcoded atoms
2. The number of entries varies and is not fixed at design time
3. Operations are typically: insert a key-value pair, look up a value by key, delete a key

## Choosing the Right Dictionary

1. Default choice: maps
2. If frequent sorted list conversion is needed: consider `gb_trees`
3. If all keys are non-negative integers: consider `array`

# Context & Application

Dictionary usage is the most common use of maps in Erlang applications. Unlike record-replacement usage (where strict rules about key sharing and `:=` apply), dictionary usage is more relaxed because the keys are not known at compile time and the compiler cannot perform the same optimizations.

The advice to prefer map syntax over the maps module (critical for record-style usage) is relaxed here to "mostly a matter of taste."

# Examples

**Alternative data structures** (Maps chapter):

- If frequent conversion to/from sorted lists is needed, `gb_trees` can be a better choice
- If all keys are non-negative integers, the `array` module can be a better choice

# Relationships

## Related

- **maps-as-alternative-to-records** -- Contrasting usage pattern where strict rules apply
- **maps-as-sets** -- Another specialized usage pattern for maps
- **large-map-implementation** -- Dictionary maps often grow beyond 32 elements, using the HAMT representation

## Contrasts With

- **maps-as-alternative-to-records** -- Record-replacement usage has compile-time keys and strict efficiency rules; dictionary usage has runtime keys and relaxed rules

# Common Errors

- **Error**: Applying the strict record-replacement rules (always use `:=`, avoid the maps module) to dictionary usage
  **Correction**: For dictionary usage with runtime keys, the performance difference between syntax and module is small; use whichever is clearest

- **Error**: Using maps when all keys are sequential non-negative integers
  **Correction**: The `array` module is a better choice for this specific case

# Common Confusions

- **Confusion**: Thinking maps are always the fastest dictionary structure
  **Clarification**: Maps are usually most efficient, but `gb_trees` beats maps when sorted list conversion is frequent, and `array` beats maps for non-negative integer keys

- **Confusion**: Assuming dictionary-use maps need the same optimization care as record-use maps
  **Clarification**: Dictionary maps have runtime keys so compiler optimizations for literal keys do not apply; the rules are more relaxed

# Source Reference

Maps chapter, "Using Maps as Dictionaries" section. Brief section describing the usage pattern and exceptions where other data structures are more efficient.

# Verification Notes

- Definition: Directly extracted from the three-bullet usage pattern and subsequent discussion
- Key Properties: All items directly stated in source
- Exceptions (gb_trees, array): Explicitly listed in source text
- Confidence: HIGH -- concise, explicit guidance in official documentation
