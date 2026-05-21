---
# === CORE IDENTIFICATION ===
concept: Maps in Guards
slug: map-in-guards

# === CLASSIFICATION ===
category: data-types
subcategory: maps
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Maps in Guards"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - map-creation
  - guard-expressions
extends:
  - map-creation
related:
  - map-pattern-matching
  - guard-sequences
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I construct and use a map in Erlang?"
  - "Can I use maps in guard expressions?"
---

# Quick Definition

Maps are allowed in guard expressions as long as all subexpressions are valid guard expressions. Four guard BIFs are provided for working with maps: `is_map/1`, `is_map_key/2`, `map_get/2`, and `map_size/1`.

# Core Definition

Maps are allowed in guards as long as all subexpressions are valid guard expressions. The following guard BIFs handle maps: `is_map/1` (tests if a term is a map), `is_map_key/2` (tests if a key exists in a map), `map_get/2` (retrieves the value for a key), and `map_size/1` (returns the number of associations). All are in the `erlang` module (Erlang Reference Manual, "Maps in Guards" section).

# Prerequisites

- **map-creation** — Must understand map data type before using maps in guards.
- **guard-expressions** — Must understand what constitutes a valid guard expression.

# Key Properties

1. Map expressions are valid in guards if all subexpressions are valid guard expressions.
2. `is_map/1` — tests whether a term is a map.
3. `is_map_key/2` — tests whether a key exists in a map.
4. `map_get/2` — retrieves the value associated with a key (fails if key absent).
5. `map_size/1` — returns the number of key-value associations.
6. All four BIFs are auto-imported from the `erlang` module.

# Construction / Recognition

## To Use Maps in Guards:
1. Use `is_map(X)` to test if `X` is a map.
2. Use `is_map_key(Key, Map)` to check for key existence.
3. Use `map_get(Key, Map)` to retrieve a value within a guard.
4. Use `map_size(Map)` to check map size.

## To Recognize:
1. Look for map-related BIFs in `when` clauses.

# Context & Application

Map guard BIFs enable function clauses to dispatch based on map properties without full pattern matching. `map_get/2` in guards is particularly useful when the key is computed or when the value must participate in further guard comparisons.

# Examples

**Example 1** (Maps in Guards section): Using map guard BIFs:

```erlang
process(M) when is_map(M), map_size(M) > 0 ->
    handle(M);
process(_) ->
    empty.
```

**Example 2**: Combining `map_get/2` with comparison in a guard:

```erlang
check(M) when is_map_key(status, M), map_get(status, M) =:= active ->
    ok.
```

# Relationships

## Builds Upon
- **map-creation** — Guards operate on map values.
- **guard-expressions** — Map guard BIFs are a subset of valid guard expressions.

## Enables
- No directly dependent concepts in this extraction.

## Related
- **map-pattern-matching** — Pattern matching and guard BIFs are complementary ways to inspect maps.
- **guard-sequences** — Map guard BIFs can be part of guard sequences.

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Using `map_get/2` in a guard without first checking that the key exists.
  **Correction**: If the key might be absent, use `is_map_key/2` first, or the guard will simply fail (which may be acceptable in a guard sequence).

# Common Confusions

- **Confusion**: Thinking arbitrary map operations (like `maps:fold/3`) are allowed in guards.
  **Clarification**: Only the four listed BIFs (`is_map/1`, `is_map_key/2`, `map_get/2`, `map_size/1`) are allowed in guards. General `maps` module functions are not guard-safe.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Map Expressions" section, "Maps in Guards" subsection.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit list of guard BIFs provided
- Uncertainties: None
- Cross-reference status: Related concepts verified
