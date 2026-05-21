---
# === CORE IDENTIFICATION ===
concept: Map Update
slug: map-update

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
section: "Updating Maps"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "map modification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - map-creation
extends:
  - map-creation
related:
  - map-pattern-matching
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I construct and use a map in Erlang?"
  - "How do I update an existing map?"
  - "What is the difference between => and := in map expressions?"
---

# Quick Definition

Map update creates a new map from an existing one by adding or replacing key-value associations. The `=>` operator adds or replaces keys, while `:=` only updates existing keys and raises an error if the key is missing.

# Core Definition

Updating a map uses the syntax `M#{K => V}` where `M` is a term of type map. If key `K` does not match any existing key, a new association is created; if it matches, the value is replaced. The expression returns a new map. For update-only semantics, the syntax `M#{K := V}` is used, where `K` must match an existing key in `M`; if it does not, a `badkey` exception is raised. If `M` is not a map, a `badmap` exception is raised in both cases. The evaluation order of key-value expressions is undefined, and when two keys match in the update, the latter value is used (Erlang Reference Manual, "Updating Maps" section).

# Prerequisites

- **map-creation** — Must understand map construction syntax before learning update syntax.

# Key Properties

1. `M#{K => V}` — adds a new key or replaces an existing one (upsert).
2. `M#{K := V}` — updates only an existing key; raises `badkey` if not present.
3. If `M` is not a map, `badmap` is raised.
4. The result is always a new map (maps are immutable).
5. Multiple updates can be combined: `M#{K1 => V1, K2 := V2}`.
6. Evaluation order of key-value expressions is undefined.
7. When two keys match in an update, the latter value wins.

# Construction / Recognition

## To Update:
1. Start with an existing map expression `M`.
2. Use `M#{K => V}` to add or replace.
3. Use `M#{K := V}` to update existing keys only.
4. Combine multiple updates: `M#{K1 => V1, K2 => V2}`.

## To Recognize:
1. Look for `MapExpr#{...}` — a map expression followed by `#{}`.
2. Distinguish between `=>` (upsert) and `:=` (update-only) arrows.

# Context & Application

Map update is central to working with maps in Erlang, since maps are immutable and all modifications create new maps. The `:=` operator provides a safety check that prevents accidentally creating new keys when only an update is intended, which is useful for maintaining map schemas.

# Examples

**Example 1** (Updating Maps section): Successive updates:

```erlang
M0 = #{},
M1 = M0#{a => 0},
M2 = M1#{a => 1, b => 2},
M3 = M2#{"function" => fun() -> f() end},
M4 = M3#{a := 2, b := 3}.  % 'a' and 'b' were added in M1 and M2.
```

**Example 2** (Updating Maps section): Distinction between `=>` and `:=`:

```erlang
1> M = #{1 => a}.
#{1 => a}
2> M#{1.0 => b}.
#{1 => a, 1.0 => b}.
3> M#{1 := b}.
#{1 => b}
4> M#{1.0 := b}.
** exception error: bad argument
```

# Relationships

## Builds Upon
- **map-creation** — Update syntax extends creation syntax.

## Enables
- **map-pattern-matching** — Understanding update operators helps understand the `:=` operator in patterns.

## Related
- No additional related concepts.

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Using `:=` to add a new key to a map.
  **Correction**: `:=` raises `badkey` if the key does not exist. Use `=>` to add new keys.

- **Error**: Expecting `M#{1.0 := b}` to update the key `1` when only integer `1` exists.
  **Correction**: `1.0` and `1` are different keys. Use the exact key type that exists in the map.

# Common Confusions

- **Confusion**: Thinking map update modifies the existing map in place.
  **Clarification**: Maps are immutable in Erlang. Update expressions return a new map; the original is unchanged.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Map Expressions" section, "Updating Maps" subsection.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit syntax, semantics, and error cases with examples
- Uncertainties: None
- Cross-reference status: Related map concepts verified
