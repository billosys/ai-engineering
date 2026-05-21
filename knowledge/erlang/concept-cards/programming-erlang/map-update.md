---
# === CORE IDENTIFICATION ===
concept: Map Update
slug: map-update

# === CLASSIFICATION ===
category: data-types
subcategory: compound-data
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Records and Maps"
chapter_number: 5
pdf_page: null
section: "The Semantics of Maps"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "=> operator"
  - ":= operator"
  - map update operator

# === TYPED RELATIONSHIPS ===
prerequisites:
  - map
extends:
  - map
related:
  - map-pattern-matching
  - record-update
contrasts_with:
  - record-update

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I update a map?"
  - "What is the difference between => and := in a map?"
---

# Quick Definition

Map update creates a new map from an old one, using `=>` to add or change a key and `:=` to update only an existing key. The `:=` operator fails if the key does not already exist.

# Core Definition

To update a map based on an existing map, the syntax is `NewMap = OldMap#{ K1 Op V1, ..., Kn Op Vn }`, where `Op` is `=>` or `:=`. The expression `K => V` is used either to update the value of an existing key `K` or to add a completely new `K-V` pair to the map — this operation always succeeds. The expression `K := V` is used only to update the value of an existing key; this operation fails if the map being updated does not contain the key `K`. The recommended practice is to always use `Key => Val` the first time a key is defined and `Key := Val` each time the value of an existing key is changed ("Records and Maps," *The Semantics of Maps*).

# Prerequisites

- **Map** — Map update operates on existing map values.

# Key Properties

1. `OldMap#{ K => V }` adds a new key or changes an existing one; always succeeds.
2. `OldMap#{ K := V }` updates only an existing key; raises a `bad argument` exception if the key is absent.
3. The original map is never modified; a new map is produced.
4. `:=` catches misspelled key names — updating a key that should exist but doesn't fails loudly.
5. Using only `:=` in an update lets the system know old and new maps share an identical key set, allowing them to share the same key descriptor (a space saving across many maps).

# Construction / Recognition

## To Construct/Create:
1. Start with an existing map, e.g. `F1 = #{ a => 1, b => 2 }`.
2. Add a new key with `F3 = F1#{ c => xx }`.
3. Update an existing key with `D2 = D1#{status := done}`.

## To Identify/Recognize:
1. An update using `:=` on an absent key raises `** exception error: bad argument`.

# Context & Application

- **Typical contexts**: Functional updates to associative data while preserving immutability.
- **Common applications**: Maintaining a running count, e.g. `X#{ H := N+1 }` in `count_characters/2`.
- **Historical/stylistic notes**: The `:=`-only pattern matters for large lists of maps with identical keys, where shared key descriptors save significant space.

# Examples

**Example 1** (*The Semantics of Maps*): Adding a new key with `=>`.

```erlang
F3 = F1#{ c => xx }.
%% => #{ a => 1, b => 2, c => xx }
```

**Example 2** (*The Semantics of Maps*): `:=` on a key that does not exist fails.

```erlang
F4 = F1#{ c := 3 }.
%% ** exception error: bad argument
%% key c does not exist in old map
```

**Example 3** (*Maps in Other Languages* sidebar): `:=` update produces an independent new map.

```erlang
D1 = #{status=>old, task=>'feed cats'},
D2 = D1#{status := done}.
%% D1 is unchanged; D2 behaves as a deep copy of D1
```

# Relationships

## Builds Upon
- **Map** — Update produces a new map from an existing one.

## Enables
- **Map pattern matching** — The `:=` operator is also used in map patterns.

## Related
- **Record update** — The analogous copy-with-change operation for records.

## Contrasts With
- **Record update** — Record update cannot add new fields; `=>` in a map update can add new keys.

# Common Errors

- **Error**: Using `:=` to add a brand-new key to a map.
  **Correction**: Use `=>` to add a new key; `:=` only updates existing keys.

- **Error**: Misspelling a key name during an update and silently creating a new key.
  **Correction**: Use `:=` for updates so a misspelled key raises an error instead of being added.

# Common Confusions

- **Confusion**: Thinking `=>` and `:=` are interchangeable.
  **Clarification**: `=>` always succeeds (add or update); `:=` only updates and fails on a missing key. The recommended idiom is `=>` for first definition, `:=` for subsequent changes.

# Source Reference

Chapter 5: Records and Maps, section "The Semantics of Maps," including the "Maps in Other Languages" sidebar. EPUB-origin source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the update-syntax description and the two reasons for `:=`.
- Confidence rationale: HIGH — explicit syntax, semantics, and worked shell examples in the source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
