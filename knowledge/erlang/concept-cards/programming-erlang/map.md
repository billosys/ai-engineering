---
# === CORE IDENTIFICATION ===
concept: Map
slug: map

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
section: "Maps: Associative Key-Value Stores"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - associative array
  - hash
  - hashmap
  - dictionary
  - "#{}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tuple
  - pattern-matching
related:
  - map-update
  - map-pattern-matching
  - record
contrasts_with:
  - record

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a map?"
  - "When should I use a map instead of a record?"
  - "What can be used as a key in a map?"
---

# Quick Definition

A map is an associative collection of key-value pairs where the key can be any fully ground Erlang term. Maps are written with the `#{ ... }` syntax and are ordered by their keys.

# Core Definition

Maps are associative collections of key-value pairs, made available from version R17 of Erlang. The keys in a map can be any *fully ground* Erlang term — meaning there are no unbound variables in the term. Map literals are written `#{ Key1 Op Val1, Key2 Op Val2, ..., KeyN Op ValN }`, where `Op` is `=>` or `:=`. The elements in a map are ordered by their keys, and a map is always printed using the sort order of the keys, irrespective of how it was created. Updating a map where the keys are not changed is space-efficient, and looking up the value of a key is efficient. In other languages this structure is called a hash (Perl, Ruby), map (C++, Java), table (Lua), or dictionary (Python) ("Records and Maps," *Maps: Associative Key-Value Stores*; *The Semantics of Maps*).

# Prerequisites

- **Tuple** — Maps are introduced as a more flexible alternative to tuples and records for storing data.
- **Pattern matching** — Map values are extracted by pattern matching against map patterns.

# Key Properties

1. Syntax `#{ K1 => V1, ... }`; similar to records but with no record name after `#`.
2. Keys may be any fully ground Erlang term (no unbound variables).
3. Elements are ordered by their keys; printing always uses key sort order.
4. Updating a map without changing its key set is space-efficient.
5. Key lookup is an efficient operation.
6. Maps have a well-defined total order and are considered "more complex" than lists or tuples in term comparison.
7. Maps were introduced in Erlang/OTP R17.

# Construction / Recognition

## To Construct/Create:
1. Write a map literal `#{ a => 1, b => 2 }` using `=>` for each key the first time it is defined.
2. Keys and values may be any valid Erlang terms, including tuples as keys.

## To Identify/Recognize:
1. Use the guard test `is_map(M)` to check whether a term is a map.
2. The shell prints maps in key sort order, e.g. `#{ a => 1, b => 2 }`.

# Context & Application

Maps are appropriate when keys are not known in advance, when there are large numbers of different keys, as a ubiquitous structure where convenience matters more than efficiency, for self-documenting data structures, for key-value parse trees such as XML or configuration files, and for communication with other languages using JSON.

- **Typical contexts**: Configuration data, parse trees, JSON-like data exchange.
- **Common applications**: `count_characters/1`, which builds a map of character counts in a string.
- **Historical/stylistic notes**: Maps work very differently from JavaScript objects — assigning through an aliased variable in Erlang never changes the original.

# Examples

**Example 1** (*The Semantics of Maps*): A map with two atom keys.

```erlang
F1 = #{ a => 1, b => 2 }.
%% => #{ a => 1, b => 2 }
```

**Example 2** (*The Semantics of Maps*): A map with non-atomic (tuple) keys.

```erlang
Facts = #{ {wife,fred} => "Sue", {age, fred} => 45,
           {daughter,fred} => "Mary",
           {likes, jim} => [...]}.
```

**Example 3** (*The Semantics of Maps*): Maps with the same contents created in different key orders compare equal.

```erlang
F2 = #{ b => 2, a => 1 }.   %% prints as #{ a => 1, b => 2 }
F1 = F2.                    %% succeeds
```

# Relationships

## Builds Upon
- **Tuple** — Maps are presented alongside tuples and records as a way to create compound data structures.

## Enables
- **Map update** — Maps support `=>`/`:=` update operations.
- **Map pattern matching** — Map patterns extract values by key.

## Related
- **Record** — Both add names to data; records are fixed and tuple-backed, maps are dynamic.

## Contrasts With
- **Record** — Records use a fixed, predefined set of names with tuple storage and faster lookup; maps allow dynamically added keys but use more storage and have slower lookup.

# Common Errors

- **Error**: Using an unbound variable as a map key.
  **Correction**: Keys must be fully ground terms; bind the variable first.

- **Error**: Assuming maps preserve insertion order.
  **Correction**: Maps are always ordered and printed by key sort order.

# Common Confusions

- **Confusion**: Thinking Erlang maps behave like mutable JavaScript objects, where aliasing one variable changes another.
  **Clarification**: Erlang maps are immutable; `D2 = D1#{status := done}` leaves `D1` unchanged — `D2` behaves like a deep copy.

- **Confusion**: Believing maps are always the best choice over records.
  **Clarification**: Maps use more storage and have slower lookup than tuples/records; choose based on whether the key set is fixed or dynamic.

# Source Reference

Chapter 5: Records and Maps, sections "When to Use Maps or Records," "Maps: Associative Key-Value Stores," and "The Semantics of Maps," including the "Maps in Other Languages" sidebar. EPUB-origin source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the maps properties list and "The Semantics of Maps."
- Confidence rationale: HIGH — the source explicitly defines maps, their properties, and syntax with worked examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
