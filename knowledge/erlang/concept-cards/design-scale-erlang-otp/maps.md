---
# === CORE IDENTIFICATION ===
concept: Maps
slug: maps

# === CLASSIFICATION ===
category: data-types
subcategory: maps
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Maps"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - map
  - key-value collection

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related: []
contrasts_with:
  - records

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a map in Erlang?"
  - "When should I use a map instead of a record?"
  - "What is the difference between the => and := map operators?"
---

# Quick Definition

A map is a built-in key-value collection type whose keys may be any Erlang term and whose number of entries is not fixed at compile time. It resembles dictionaries or hashes in other languages.

# Core Definition

"A map in Erlang is a key-value collection type that resembles the dictionary and hash types found in other programming languages. Maps differ from records in several ways: map is a built-in type, the number of its fields or key-value pairs is not fixed at compile time, and its keys can be any Erlang term rather than just atoms" (Cesarini & Vinoski, p. 43). "Records are fast, so use them when you have a fixed number of fields known at compile time, while maps should be used when you have a need to add fields at runtime." The `=>` operator associates (adds or updates) a key; the `:=` operator updates a key, but "ensures that the key being updated already exists in the map" (p. 44).

# Prerequisites

- **Pattern matching** — A map can be used in a pattern to capture associated values; the `:=` operator is required for map pattern matching.

# Key Properties

1. `map` is a built-in type; literal syntax is `#{}`.
2. The number of key-value pairs is not fixed at compile time.
3. Keys may be any Erlang term, not just atoms.
4. `=>` adds a new association or updates an existing one.
5. `:=` updates only an existing key, preventing accidental key creation from typos.
6. `erlang:map_size/1` returns the number of pairs.
7. In a map pattern, `:=` is required to match and capture a value.

# Construction / Recognition

## To Construct:
1. Create an empty map with `#{}` or a populated one with `#{K1 => V1, ...}`.
2. Add/update with `Map#{K => V}`.
3. Update an existing key with `Map#{K := V}`.

## To Recognize:
1. Look for `#{...}` syntax and the `=>` / `:=` operators.

# Context & Application

- **Typical contexts**: Data whose set of fields varies or grows at runtime.
- **Common applications**: Lookup tables, configuration with dynamic keys.
- **Historical/stylistic notes**: The book deliberately positions maps and records as complementary, not as replacements for one another.

# Examples

**Example 1** (p. 43): Building and updating a map of release dates:

```erlang
3> RelDates = #{ "R15B03-1" => {2012, 11, 28}, "R16B03" => {2013, 12, 11} }.
4> RelDates2 = RelDates#{ "17.0" => {2014, 4, 2}}.
5> RelDates3 = RelDates2#{"17.0" := {2014, 4, 9}}.
```

Command 4 adds a key with `=>`; command 5 updates an existing key with `:=`.

**Example 2** (p. 44): Pattern matching a map to capture a value:

```erlang
6> #{ "R15B03-1" := Date } = RelDates3.
```

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- *(none specific in scope)*

## Related
- *(none additional)*

## Contrasts With
- **Records** — Records have a compile-time-fixed set of atom-keyed fields and are faster; maps allow runtime-variable any-term keys.

# Common Errors

- **Error**: Using `=>` to "update" a key and silently creating a new one after a typo.
  **Correction**: Use `:=` when updating; it fails if the key does not already exist.

# Common Confusions

- **Confusion**: Thinking maps fully replace records.
  **Clarification**: They serve different needs — records for fixed compile-time fields, maps for runtime-variable fields.

# Source Reference

Chapter 1: Introducing Erlang, Section "Maps," pages 43-44.

# Verification Notes

- Definition source: Direct quotes from pp. 43-44.
- Confidence rationale: HIGH — explicit definition with a shell example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
