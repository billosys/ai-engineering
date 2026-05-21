---
# === CORE IDENTIFICATION ===
concept: Map Comprehension
slug: map-comprehension

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: comprehensions
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Comprehensions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "map comprehension expression"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - map-creation
  - list-comprehension
extends:
  - list-comprehension
related:
  - binary-comprehension
  - map-update
  - map-pattern-matching
contrasts_with:
  - list-comprehension

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use map comprehensions in Erlang?"
  - "How do I transform a map using a comprehension?"
  - "How do I create a map from a list using a comprehension?"
  - "What is a map generator?"
---

# Quick Definition

A map comprehension `#{KeyExpr => ValueExpr || Qualifier1, ..., QualifierN}` constructs a map by evaluating `KeyExpr` and `ValueExpr` for each combination of generator elements for which all filters are true. Introduced in OTP 26.

# Core Definition

Map comprehensions have the syntax `#{KeyExpr => ValueExpr || Qualifier1, ..., QualifierN}` where `KeyExpr` and `ValueExpr` are arbitrary expressions and each `Qualifier` is a generator or filter. A map generator `KeyPattern := ValuePattern <- MapExpression` (relaxed) or `KeyPattern := ValuePattern <:- MapExpression` (strict) iterates over key-value pairs of a map or map iterator. If key expressions produce duplicate keys, the last occurrence is stored. All generator types and filter semantics are shared with list comprehensions. When there are no generators, the result is `#{KeyExpr => ValueExpr}` if all filters are true, or `#{}` otherwise. Map comprehensions and map generators were introduced in Erlang/OTP 26 (Erlang Reference Manual, "Comprehensions" section).

# Prerequisites

- **map-creation** — Understanding map syntax and semantics.
- **list-comprehension** — Map comprehensions share generator and filter syntax.

# Key Properties

1. Syntax: `#{KeyExpr => ValueExpr || Qualifier1, ..., QualifierN}`.
2. Introduced in OTP 26.
3. Map generators: `K := V <- MapExpr` (relaxed) or `K := V <:- MapExpr` (strict).
4. Map generators can iterate over maps or map iterators (`maps:iterator/1,2`).
5. Duplicate keys: the last occurrence wins.
6. Can use any generator type (list, bit string, map, zip) as source.

# Construction / Recognition

## To Construct:
```erlang
#{X => X*X || X <:- [1,2,3]}
#{K => 2*V || K := V <:- Map}
```

## To Recognize:
1. Look for `#{ ... || ... }` syntax.
2. The expression before `||` has the form `KeyExpr => ValueExpr`.

# Context & Application

Map comprehensions provide a declarative way to construct and transform maps. They are particularly useful for transforming all values in a map, creating maps from lists, and filtering map entries. Before OTP 26, similar transformations required `maps:map/2`, `maps:filter/2`, or `maps:fold/3`.

# Examples

**Example 1** (Comprehensions section): Creating a mapping from integer to square:

```erlang
1> #{X => X*X || X <:- [1,2,3]}.
#{1 => 1,2 => 4,3 => 9}
```

**Example 2** (Comprehensions section): Doubling values in a map:

```erlang
1> #{K => 2*V || K := V <:- #{a => 1,b => 2,c => 3}}.
#{a => 2,b => 4,c => 6}
```

# Relationships

## Builds Upon
- **map-creation** — Produces maps using map construction syntax.
- **list-comprehension** — Shares generator and filter mechanics.

## Related
- **binary-comprehension** — Another comprehension variant.
- **map-update** — Map comprehensions create new maps rather than updating existing ones.
- **map-pattern-matching** — Map generators use `:=` pattern syntax.

## Contrasts With
- **list-comprehension** — Uses `#{ ... || ... }` vs `[ ... || ... ]` and produces maps vs lists.

# Common Errors

- **Error**: Using `=>` instead of `:=` in a map generator pattern.
  **Correction**: Map generators use the pattern syntax `K := V <- MapExpr`, not `K => V`.

- **Error**: Expecting insertion order in the resulting map.
  **Correction**: Maps in Erlang do not guarantee any particular key order.

# Common Confusions

- **Confusion**: Thinking map comprehensions are available in all OTP versions.
  **Clarification**: Map comprehensions and map generators were introduced in OTP 26.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Comprehensions" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — clear syntax and examples from source
- Uncertainties: None
- Cross-reference status: OTP 26 introduction date verified in source
