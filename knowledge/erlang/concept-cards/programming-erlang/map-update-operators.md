---
# === CORE IDENTIFICATION ===
concept: Map Update Operators
slug: map-update-operators

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
  - "=>"
  - ":="
  - map update
  - map extend

# === TYPED RELATIONSHIPS ===
prerequisites:
  - map
extends:
  - map
related:
  - map-pattern-matching
contrasts_with:
  - record

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I update a map?"
  - "What is the difference between => and := in a map update?"
  - "Why would I use := instead of =>?"
---

# Quick Definition

The map update syntax `NewMap = OldMap#{K1 Op V1, ...}` creates a copy of a map with keys added or changed, using `=>` to add-or-update and `:=` to update an existing key only.

# Core Definition

To update a map based on an existing map, Erlang uses `NewMap = OldMap#{ K1 Op V1, ..., Kn Op Vn }`, where `Op` is `=>` or `:=`. The expression `K => V` either updates the value of an existing key `K` or adds a completely new `K-V` pair; this operation always succeeds. The expression `K := V` updates the value of an existing key only — "This operation fails if the map being updated does not contain the key `K`" ("Records and Maps", *The Semantics of Maps*). The book's recommended idiom: "always use `Key => Val` the first time a key is defined and use `Key := Val` each time the value of a specific key is changed."

# Prerequisites

- **Map** — The update operators act on an existing map value.

# Key Properties

1. `=>` adds a new key or updates an existing one; it always succeeds.
2. `:=` updates an existing key only; it raises a `bad argument` exception if the key is absent.
3. Update produces a new map; the original map is never mutated.
4. `:=` catches misspelled key names — updating a key that should exist but does not fails loudly.
5. `:=`-only updates let the old and new maps share the same key descriptor, saving space when many maps have identical key sets.

# Construction / Recognition

## To Construct/Create:
1. To add a key: `F3 = F1#{ c => xx }`.
2. To change an existing key's value: `F1#{ a := 2 }`.
3. Combine in one update expression: `OldMap#{k1 => v1, k2 := v2}`.

## To Identify/Recognize:
1. `=>` in an update means "set or insert"; `:=` means "must already exist".

# Context & Application

- **Typical contexts**: incrementally building or modifying map-based data.
- **Common applications**: the character-count function uses `X#{ H => 1 }` to add a new key and `X#{ H := N+1 }` to bump an existing count.
- **Historical/stylistic notes**: the `:=`-only-update space-sharing benefit matters most for lists of millions of same-keyed maps.

# Examples

**Example 1** (*The Semantics of Maps*): adding a key with `=>` succeeds:

```erlang
5> F3 = F1#{ c => xx }.
#{ a => 1, b => 2 , c => xx}
```

**Example 2** (*The Semantics of Maps*): updating a nonexistent key with `:=` fails:

```erlang
6> F4 = F1#{ c := 3}
** exception error: bad argument
key c does not exist in old map
```

# Relationships

## Builds Upon
- **Map** — Update operators elaborate on the basic map type.

## Enables
- **Map pattern matching** — `:=` is also the operator used inside map patterns.

## Related
- **Map pattern matching** — Updates and patterns share the `:=` operator.

## Contrasts With
- **Record** — Record update (`R#rec{field=V}`) requires the field to be declared at compile time; map `=>` can add brand-new keys at runtime.

# Common Errors

- **Error**: Using `:=` to add a new key to a map.
  **Correction**: `:=` requires the key to already exist; use `=>` to add a key.

- **Error**: Misspelling a key in a `=>` update, silently creating an unwanted key.
  **Correction**: Use `:=` for updates so a misspelled key raises an error instead of being inserted.

# Common Confusions

- **Confusion**: Believing map update mutates the original map.
  **Clarification**: Update returns a new map; the old map is unchanged.

- **Confusion**: Thinking `=>` and `:=` are interchangeable.
  **Clarification**: `=>` always succeeds (insert-or-update); `:=` succeeds only when the key exists.

# Source Reference

Chapter 5: "Records and Maps", section "The Semantics of Maps".

# Verification Notes

- Definition source: Direct adaptation of *The Semantics of Maps* update-operator discussion.
- Confidence rationale: HIGH — the source explicitly contrasts `=>` and `:=` with worked examples and rationale.
- Uncertainties: None.
- Cross-reference status: Slug `map` extracted in this chapter; `record` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card content merged.
