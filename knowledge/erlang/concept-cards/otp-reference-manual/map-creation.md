---
# === CORE IDENTIFICATION ===
concept: Map Creation
slug: map-creation

# === CLASSIFICATION ===
category: data-types
subcategory: maps
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Creating Maps"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "map construction"
  - "map literal"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - map-update
  - map-pattern-matching
  - map-in-guards
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I construct and use a map in Erlang?"
  - "How do I create a new map?"
---

# Quick Definition

Maps are constructed using the `#{}` syntax with `=>` arrows separating keys and values. Any Erlang term can be used as a key or value, and keys are evaluated expressions.

# Core Definition

Constructing a new map is done by associating an expression `K` with another expression `V` using the syntax `#{K => V}`. Multiple associations are listed as `#{K1 => V1, ..., Kn => Vn}`. An empty map is `#{}`. All keys and values are terms; any expression is first evaluated and then the resulting terms are used as key and value respectively. Keys and values are separated by the `=>` arrow and associations are separated by a comma. If two matching keys are declared, the latter key takes precedence. The order in which key-value expressions are evaluated is not defined (Erlang Reference Manual, "Creating Maps" section).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Syntax: `#{K1 => V1, ..., Kn => Vn}`.
2. Empty map: `#{}`.
3. Any expression can be a key or value (expressions are evaluated first).
4. Keys and values are separated by `=>`.
5. If two matching keys are declared, the latter takes precedence.
6. The evaluation order of key-value expressions is undefined.
7. The syntactic order of key-value pairs is irrelevant, except when two keys match.

# Construction / Recognition

## To Construct:
1. Start with `#{`.
2. Add key-value pairs separated by `=>`: `Key => Value`.
3. Separate multiple pairs with commas.
4. End with `}`.

## To Recognize:
1. Look for the `#{...}` syntax with `=>` arrows.

# Context & Application

Maps are the primary key-value data structure in Erlang (introduced in OTP 17). They serve as dictionaries, records with dynamic fields, and configuration containers. Maps support any term as a key, including compound terms. They are preferred over process dictionaries and `dict` module for most key-value use cases.

# Examples

**Example 1** (Creating Maps section): Various map constructions:

```erlang
M0 = #{},                 % empty map
M1 = #{a => <<"hello">>}, % single association with literals
M2 = #{1 => 2, b => b},   % multiple associations with literals
M3 = #{k => {A,B}},       % single association with variables
M4 = #{{"w", 1} => f()}.  % compound key associated with an evaluated expression
```

**Example 2** (Creating Maps section): Duplicate keys — latter wins:

```erlang
1> #{1 => a, 1 => b}.
#{1 => b}
2> #{1.0 => a, 1 => b}.
#{1 => b, 1.0 => a}
```

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- **map-update** — Once created, maps can be updated with new or modified associations.
- **map-pattern-matching** — Maps can be deconstructed using pattern matching.
- **map-in-guards** — Maps and map BIFs can be used in guard expressions.

## Related
- No additional related concepts.

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Expecting map keys to maintain insertion order.
  **Correction**: Map key order is determined by term ordering, not insertion order.

- **Error**: Using `:=` instead of `=>` when constructing a new map.
  **Correction**: Use `=>` for construction (allows new keys); `:=` is for update-only and pattern matching.

# Common Confusions

- **Confusion**: Thinking `1` and `1.0` are the same key.
  **Clarification**: `1` (integer) and `1.0` (float) are different keys in a map; they only match under `==`, not `=:=`. Both can coexist as separate keys.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Map Expressions" section, "Creating Maps" subsection.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit syntax and semantics with examples
- Uncertainties: None
- Cross-reference status: Related map concepts verified against planned extractions
